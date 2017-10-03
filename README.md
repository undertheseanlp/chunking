# Chunking Experiments

This repository contains experiments in Vietnamese Chunking problems. It is a part of [underthesea](https://github.com/magizbox/underthesea) project.

## Corpus Summary 

```
Sentences    : 7855
Unique words : 14245
Top words    : ,, ., ", của, là, và, có, một, người, được, không, đã, những, cho, :, ..., ở, trong, với, đến
POS Tags     : 28
List tags    : A, Ab, C, CH, Cb, Cc, E, Eb, I, L, M, Mb, N, Nb, Nc, Np, Nu, Ny, P, Pb, R, T, V, Vb, Vy, X, Y, Z
Chunking Tags: 21
List tags    : B-AP, B-MP, B-NP, B-PP, B-QP, B-TP, B-VP, B-WH, B-WP, B-XP, I-AP, I-MP, I-NP, I-PP, I-QP, I-VP,
               I-WH , I-WP, I-XP, N-NP, O
```

## Reports

![](https://img.shields.io/badge/F1-85.1%25-red.svg)

* Detail Reports, [link](https://docs.google.com/spreadsheets/d/17atXtvgstvqWZStr9WxDziL5zvQjiBnYH1qXYFb8L5g/pubhtml?gid=0&single=true)
* Related Works: [Other Tools](https://github.com/magizbox/underthesea/wiki/Vietnamese-NLP-Tools#chunking), [Publications](https://github.com/magizbox/underthesea/wiki/Vietnamese-NLP-Publications#chunking), [State of The Art](https://github.com/magizbox/underthesea/wiki/Vietnamese-NLP-SOTA#chunking), [Service](https://github.com/magizbox/underthesea/wiki/Vietnamese-NLP-Services#chunking)

## How to usage

```
# clone project
$ git clone git@github.com:magizbox/underthesea.chunking.git
$ cd underthesea.chunking

# create environment
$ conda env create -f environment.yml
$ source activate underthesea.chunking
```

Last update: October 2017
