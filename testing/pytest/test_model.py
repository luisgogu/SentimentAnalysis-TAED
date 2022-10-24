import pytest
import torch
from torch import nn
from pytorch_pretrained_bert import BertModel
from pytorch_pretrained_bert import BertTokenizer

class BertBinaryClassifier(nn.Module):
    def __init__(self, dropout=0.1):
        super(BertBinaryClassifier, self).__init__()

        self.bert = BertModel.from_pretrained('bert-base-uncased')

        self.dropout = nn.Dropout(dropout)
        self.linear = nn.Linear(768, 1)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, tokens, masks=None):
        _, pooled_output = self.bert(tokens, attention_mask=masks, output_all_encoded_layers=False)
        dropout_output = self.dropout(pooled_output)
        linear_output = self.linear(dropout_output)
        proba = self.sigmoid(linear_output)
        return proba

bert_clf = BertBinaryClassifier()
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
bert_clf.load_state_dict(torch.load('model.pt',  map_location=torch.device('cpu')))

def predict(text):
    bert_clf.eval()
    with torch.no_grad():
        text = torch.tensor([tokenizer.convert_tokens_to_ids(tokenizer.tokenize(text))])
        output = bert_clf(text)[0,0]
        return 'positive' if output >= 0.5 else 'negative'
    

def test_minimum_functionality():
  pos = [
  "good", "realistic", "healthy", "attractive", "appealing", "acceptable", 
  "best", "feasible", "easy", "ideal", "affordable", "economical", "recommended", 
  "exciting", "inexpensive", "obvious", "great", "appropriate", "effective", "excellent",
  ]

  neg = [
    "bad", "unhealthy", "expensive", "boring", "terrible", "worst", "unfeasible", 
    "unappropriate", "awful", "time-consuming",
  ]

  positive_texts = [f'Exercise is {pos} for your health' for pos_word in pos]
  negative_texts = [f'Exercise is {neg} for your health' for neg_word in neg]
  
  pos_results = [predict(text) for text in positive_texts]
  neg_results = [predict(text) for text in negative_texts]

  assert all('positive' == sentiment for sentiment in pos_results), "Sentiment positive minimum functionality failed"
  assert all('negative' == sentiment for sentiment in neg_results), "Sentiment negative minimum functionality failed"

def test_invariance():
  data = [
      "The cake is great.",
      "awful",
      "Michael had fun traveling to Mexico",
      "Anna hates party.",
      "This laptop is not very good",
  ]
  locations = ["Mexico", "Afghanistan", "Kenya", "Peru",
               "Morocco", "Canada", "Germany", "Algeria", "Indonesia"]
  names = ["Michael","Jackson","Jose","Shawn","Steven","Jackson","Noah","Chad","Bryan","Stephen","Derek"]
  
  location_variance = [f"Michael had fun traveling to {location}" for location in locations]
  name_variance = [f"{name} had fun traveling to Mexico" for name in names ]

  location_variance_sentiments = [predict(text) for text in location_variance]
  name_variance_sentiments = [predict(text) for text in name_variance]
  # print( predict('Michael had fun traveling to Mexico'))

  assert all(sentiment == 'positive' for sentiment in location_variance_sentiments), "Sentiment invariance failed changing locations"
  assert all(sentiment == 'negative' for sentiment in name_variance_sentiments), "Sentiment invariance failed changing names"

def test_directional():
  pos_examples = ['The cake is great', 'Anna loves party.', 'This laptop is very good']
  neg_examples = ['The cake is not great', 'Anna hates party.', 'This laptop is not very good']
  pos_examples_sent = [predict(text) for text in pos_examples]
  neg_examples_sent = [predict(text) for text in neg_examples]
  assert not any([pos_examples[i] != neg_examples[i] for i in range(len(pos_examples))]), "Sentiment directionality failed"