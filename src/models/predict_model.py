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

