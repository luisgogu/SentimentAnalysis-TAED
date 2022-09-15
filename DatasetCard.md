---
annotations_creators:
- found
language:
- en
language_creators:
- found
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: IMDB Movie Reviews
size_categories:
- 10K<n<100K
source_datasets:
- original
tags: []
task_categories:
- text-classification
task_ids:
- sentiment-analysis
---

# Dataset Card for IMDB Large Movie Review Dataset

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://ai.stanford.edu/~amaas/data/sentiment/
- **Repository:** https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
- **Paper:** http://www.aclweb.org/anthology/P11-1015
- **Leaderboard:** None
- **Point of Contact:** http://www.andrew-maas.net/

### Dataset Summary

Large Movie Review Dataset. This is a dataset for binary sentiment classification
containing substantially more data than previous benchmark datasets. We provide
a set of 25,000 highly polar movie reviews for training, and 25,000 for testing.
There is additional unlabeled data for use as well.

### Supported Tasks and Leaderboards

Supported Tasks: Sentiment Analysis, Sentiment Classification

### Languages

Monolingual - English

## Dataset Structure

### Data Instances

#### plain_text
- **Size of downloaded dataset files:** 80.23 MB
- **Size of the generated dataset:** 127.06 MB
- **Total amount of disk used:** 207.28 MB
An example of 'train' looks as follows.
```
{
    "label": 0,
    "text": "Goodbye world2\n"
}
```
In addition to the review text files, two more files can be found:
- An already-tokenized bag of words (BoW) features.
- A txt file that contains the expected rating for each token as computed by (Potts, 2011).

### Data Fields

The data fields are the same among all splits.
#### plain_text
- `text`: a `string` feature.
- `label`: a classification label, with possible values including `neg` (0), `pos` (1).

### Data Splits

The core dataset contains 50,000 reviews split evenly into 25k train
and 25k test sets. The overall distribution of labels is balanced (25k
pos and 25k neg). We also include an additional 50,000 unlabeled
documents for unsupervised learning.

## Dataset Creation

### Curation Rationale

IMDB Movie Review dataset was built to provide a test-bed for machines to learn
how to analyze and understand natural language as to identify the sentiment behind
the phrase/review. The dataset was built by gathering movie ratings through the
IMDB webpage, along with the reviews that were provided by the users. Given the
nature of movie ratings, one can easily interpret that a bad rating will probably
lead to a negative review (and vice versa), which serves as an easy start-point
for automated sentiment analysis and a base for more complex sentiment analysis tasks.

### Source Data

#### Initial Data Collection and Normalization

In the entire collection, no more than 30 reviews are allowed for any
given movie because reviews for the same movie tend to have correlated
ratings. Further, the train and test sets contain a disjoint set of
movies, so no significant performance is obtained by memorizing
movie-unique terms and their associated with observed labels.  In the
labeled train/test sets, a negative review has a score <= 4 out of 10,
and a positive review has a score >= 7 out of 10. Thus reviews with
more neutral ratings are not included in the train/test sets. In the
unsupervised set, reviews of any rating are included and there are an
even number of reviews > 5 and <= 5.

#### Who are the source language producers?

The language producers are users of the IMDB webpage.

### Annotations

The dataset does not contain any additional annotations.

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

The user ID's were removed from the train/test text files and only the plain plain text is saved.
However, we have access to the movie URL from IMDB (not the actual review), but one could
achieve user tracking by using the text value from the train/test files.

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of this dataset is to help develop better sentiment analysis systems.

A system that succeeds at the supported task would be able to provide a state of the art system that
serves as the basis for sentiment analysis systems. Moreover, it could be used as a basis for more complex
systems via knowledge transfer strategies.

### Discussion of Biases

It is widely known that all NLP tasks/systems include certain biases (both explicit and implicit) transmitted
through language. However, given the task we are trying to solve, the impact of those biases are not as heavy
as for other NLP tasks. Furthermore, movie reviews are a limited environment (in terms of language use and possible
biases) and IMDb reviews and moderates user reviews, meaning that the dataset is safer than other alternatives such
as extracting data from social networks or other sources.

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

The dataset was created by Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher}
during work done for the Learning Word vectors for Sentiment Analysis (Proceedings of
the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies) paper.

### Licensing Information

When using the dataset it is mandatory to cite the original paper made by the authors.
It can be found on the Citation Information section.

### Citation Information

```
@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
  url       = {http://www.aclweb.org/anthology/P11-1015}
}
```


### Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.
