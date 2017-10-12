from os.path import dirname, join
from underthesea_flow.reader.tagged_corpus import TaggedCorpus


def pos_tag_normalize(tag):
    tags_map = {
        "Ab": "A",
        "B": "FW",
        "Cc": "C",
        "Fw": "FW",
        "Nb": "FW",
        "Ne": "Nc",
        "Ni": "Np",
        "NNP": "Np",
        "Ns": "Nc",
        "S": "Z",
        "Vb": "V",
        "Y": "Np"
    }
    if tag in tags_map:
        return tags_map[tag]
    else:
        return tag


def chunk_tag_normalize(tag):
    tags_map = {
        "B-IP": "O",
        "B-MP": "O",
        "B-NPb": "B-NP",
        "B-QP": "B-NP",
        "B-RP": "O",
        "B-VPb": "B-VP",
        "I-PP": "B-PP",
        "I-QP": "I-NP",
        "I-RP": "O"
    }
    if tag in tags_map:
        return tags_map[tag]
    else:
        return tag


def preprocess(sentences):
    def process_token(t):
        output = t
        output[0] = t[0].replace("_", " ")
        output[1] = pos_tag_normalize(t[1])
        output[2] = chunk_tag_normalize(t[2])
        return output

    def process_sentence(s):
        return [process_token(t) for t in s]

    return [process_sentence(s) for s in sentences]


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


def raw_to_corpus():
    for f1, f2 in [("chunk_train.txt", "train.txt"),
                   ("chunk_dev.txt", "dev.txt"),
                   ("chunk_test.txt", "test.txt")]:
        tagged_corpus = TaggedCorpus()
        input = join(dirname(dirname(__file__)), "raw", "vlsp_chunk", f1)
        tagged_corpus.load(input)
        tagged_corpus.sentences = preprocess(tagged_corpus.sentences)
        output = join(dirname(dirname(__file__)), "corpus", "vlsp_chunk", f2)
        tagged_corpus.save(output)


if __name__ == '__main__':
    raw_to_corpus()
    # file = join(dirname(__file__), "corpus", "vlsp_chunk", "train.txt")
    # load_data(file)
