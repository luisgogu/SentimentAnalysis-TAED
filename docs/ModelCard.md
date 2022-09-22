# Model Card for Sentiment Analysis Project. TAED2. HeartTeam

## Persons and Organization
Joel Castaño, Luis Gonzalez, Alex Muñoz, Mireia Andres


Heart Team. Subject: TAED2. UPC.

## Contact

Please, you are welcome to adress questions and comments about the model to mireia.andres@estudiantat.upc.edu

## Table of Contents
- [Model Date and Version](#model-date-and-version)
- [Model Type](#model-type)
- [Intended Use](#intended-use)
  - [Intended Primary Users](#intended-primary-users)


## Model Date and Version

- October 2022
- Version 1.0

## Model Type

Text analysis model for sentiment recognition.

Fine-tuning of BERT Model.

**Aquí hauríem d'explicar més detalladament les etapes del model**

## Intended Use

### Intended Primary Users

### Intend Primary Uses

## Out-of-Scope Uses

## Limitations

The quality of user's input may impact the accuracy of the results. The factors that may detriment accuracy are:

- Not natural language (e.g emojis, numbers, internet slangs...)
- Language ambiguity
- Monolingual language (only in english)
- ...


## Ethical Considerations

Sentiment analysis tools are increasingly used everywhere. As sentiments and emotions are nuclear issues in people's lives, they are full of ethical concerns. Indentifying sentiments can be used to improve people's lives but it also carries the option of abusing of this information in order to manipulate or harm people in many ways (think about using this to discard people from job selection processes, to assist the police or judges, to impact on the intention of vote in democratic elections an so far). 


## Carbon Footprint Evaluation

In order to fight climate change and to protect the planet health it is mandatory to develop green technology. One side of this green technology is about spending as less energy as possible in the development of ML models. So it is necessary to provide transparency regarding the energy burden of each model. In this project the estimation of energy consumption has been done through the Code Carbon profiler (https://codecarbon.io) and computing the FLOPs required to train the model using the keras-flops4 package for TensorFlow (https://github.com/tokusumi/keras-flops).

## Metrics

The metrics used to evaluate the performance of the model have been **accuracy** and **F1 score**.

F1 Score is dedicated to solve the problem of imbalanced training data and is builded on Precision and Recall metrics.

$$Accuracy = \frac{CorrectPredictions}{TotalPredictions}$$

$$F1  Score = 2*\frac{Precision * Recall}{Precision + Recall}$$

## Training en Evaluation Data

## Quantitative Analysis

## Suported Inputs

**Posar quin format d'entrada de text accepta**

## Table Summary

| Language | license   | library_name | tags                       | datasets | metrics |
| :------: | :-----:   | :-----:      | :------:                   |:--------:|:------: |
| eng      | cc-by-4.0 | PyTorch      | text-sentiment-analysis    |  imdb    |accuracy |
|          |           |              |natural-language-processing |          |f1       |


- language:
eng
- license: 
cc-by-4.0
- library_name: 
PyTorch  # Optional. Example: keras or any library from https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Libraries.ts
- tags:
text-sentiment-analysis
natural-language-processing
- datasets:
imdb
- metrics:
accuracy
f1
