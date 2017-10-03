from os.path import dirname, join
from underthesea_flow.reader.tagged_corpus import TaggedCorpus


def load_data(file):
    tagged_corpus = TaggedCorpus()
    tagged_corpus.load(file)
    sentences = tagged_corpus.sentences
    return sentences


def sample_data(n=200):
    tagged_corpus = TaggedCorpus()
    file = join(dirname(__file__), "corpus", "vlsp_chunk", "train.txt")
    tagged_corpus.load(file)
    sentences = tagged_corpus.sentences[:n]
    sample_corpus = TaggedCorpus(sentences)
    file = join(dirname(__file__), "corpus", "vlsp_chunk_sample", "train.txt")
    sample_corpus.save(file)


if __name__ == '__main__':
    sample_data()
    # file = join(dirname(__file__), "corpus", "vlsp_chunk", "train.txt")
    # load_data(file)
