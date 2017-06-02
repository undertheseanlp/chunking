from os.path import join, dirname
from data_preparation.tagged_corpus import TaggedCorpus

if __name__ == '__main__':
    corpus_file = join(dirname(dirname(__file__)), "data", "corpus_v1.txt")
    corpus = TaggedCorpus()
    corpus.load(corpus_file)
    corpus.analyze()
