# Model Card for Sentiment Analysis Project. TAED2. HeartTeam

## Persons and Organization
Joel Castaño, Luis Gonzalez, Alex Muñoz, Mireia Andres


Heart Team. Subject: TAED2. UPC.

## Contact

Please, you are welcome to adress questions and comments about the model to mireia.andres@estudiantat.upc.edu

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

- Too short text
- not natural language

**- pensar altres exemples**

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

# Optional. Add this if you want to encode your eval results in a structured way.
model-index:
- name: {model_id}
  results:
  - task:
      type: {task_type}             # Required. Example: automatic-speech-recognition
      name: {task_name}             # Optional. Example: Speech Recognition
    dataset:
      type: {dataset_type}          # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: {dataset_name}          # Required. A pretty name for the dataset. Example: Common Voice (French)
      config: {dataset_config}      # Optional. The name of the dataset configuration used in `load_dataset()`. Example: fr in `load_dataset("common_voice", "fr")`. See the `datasets` docs for more info: https://huggingface.co/docs/datasets/package_reference/loading_methods#datasets.load_dataset.name
      split: {dataset_split}        # Optional. Example: test
      revision: {dataset_revision}  # Optional. Example: 5503434ddd753f426f4b38109466949a1217c2bb
      args:
        {arg_0}: {value_0}          # Optional. Additional arguments to `load_dataset()`. Example for wikipedia: language: en
        {arg_1}: {value_1}          # Optional. Example for wikipedia: date: 20220301
    metrics:
        type: {metric_type}         # Required. Example: wer. Use metric id from https://hf.co/metrics
        value: {metric_value}       # Required. Example: 20.90
        name: {metric_name}         # Optional. Example: Test WER
        config: {metric_config}     # Optional. The name of the metric configuration used in `load_metric()`. Example: bleurt-large-512 in `load_metric("bleurt", "bleurt-large-512")`. See the `datasets` docs for more info: https://huggingface.co/docs/datasets/v2.1.0/en/loading#load-configurations
        args:
          {arg_0}: {value_0}        # Optional. The arguments passed during `Metric.compute()`. Example for `bleu`: max_order: 4
        verified: true              # Optional. If true, indicates that evaluation was generated by Hugging Face (vs. self-reported).
---
