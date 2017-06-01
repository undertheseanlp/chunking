from os.path import join, dirname
from data_preparation.tagged_corpus import TaggedCorpus

if __name__ == '__main__':
    corpus_file = join(dirname(dirname(__file__)), "data", "vi-chunk.train")
    corpus = TaggedCorpus()
    corpus.load(corpus_file)
    corpus.analyze()
