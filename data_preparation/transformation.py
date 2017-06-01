"""
transform vi-chunk.train to corpus-v1.txt
"""
from os.path import join, dirname

from data_preparation.tagged_corpus import TaggedCorpus


def transform_word(word):
    word = word.decode("utf-8")
    word = word.replace("_", " ")
    return word


def transform_token(t):
    tokens = t.split()
    tokens[0] = transform_word(tokens[0])
    return tokens


def transform_sentence(s):
    s = [transform_token(t) for t in s]
    return s


if __name__ == '__main__':
    data_folder = join(dirname(dirname(__file__)), "data")
    file = join(data_folder, "vi-chunk.train")
    sentences = open(file, "r").read().strip().split("\n\n")
    sentences = [s.split("\n") for s in sentences]
    sentences = [transform_sentence(s) for s in sentences]
    corpus = TaggedCorpus(sentences)
    output_file = join(data_folder, "corpus_v1.txt")
    corpus.save(output_file)
    corpus.analyze()
    print(0)
