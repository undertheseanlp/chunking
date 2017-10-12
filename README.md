# Underthesea Chunking

![](https://img.shields.io/badge/build-passing-brightgreen.svg) ![](https://img.shields.io/badge/F1-77%25-red.svg)

This repository contains experiments in Vietnamese Chunking problems. It is a part of [underthesea](https://github.com/magizbox/underthesea) project.

* [Demo](http://magizbox.com:9386)
* [Detail Report](https://docs.google.com/spreadsheets/d/17atXtvgstvqWZStr9WxDziL5zvQjiBnYH1qXYFb8L5g/edit?usp=sharing)

## Corpus Summary 

```
Sentences    : 7855
Unique words : 14245
Top words    : ,, ., ", của, là, và, có, một, người, được, không, đã, những, cho, :, ..., ở, trong, với, đến
POS Tags (28): A, Ab, C, CH, Cb, Cc, E, Eb, I, L, M, Mb, N, Nb, Nc, Np, Nu, Ny, P, Pb, R, T, V, Vb, Vy, X, Y, Z
Chunking Tags (21): B-AP, B-MP, B-NP, B-PP, B-QP, B-TP, B-VP, B-WH, B-WP, B-XP, I-AP, I-MP, I-NP, I-PP, I-QP, I-VP, I-WH , I-WP, I-XP, N-NP, O
```

## Usage

**Setup Environment**

```
# clone project
$ git clone git@github.com:magizbox/underthesea.chunking.git

# create environment
$ cd underthesea.chunking
$ conda create -n uts.chunking python=3.4
$ pip install -r requirement.txt
```

**Run Experiments**

```
$ cd underthesea.chunking
$ source activate uts.chunking
$ python main.py
```

## Related Works

* [Vietnamese Chunking Tools](https://github.com/magizbox/underthesea/wiki/Vietnamese-NLP-Tools#chunking)
* [Vietnamese Chunking Publications](https://github.com/magizbox/underthesea/wiki/Vietnamese-NLP-Publications#chunking)
* [Vietnamese Chunking State of The Art](https://github.com/magizbox/underthesea/wiki/Vietnamese-NLP-SOTA#chunking)
* [Vietnamese Chunking Service](https://github.com/magizbox/underthesea/wiki/Vietnamese-NLP-Services#chunking)

Last update: October 2017
