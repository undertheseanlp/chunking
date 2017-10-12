from os.path import join

from underthesea_flow.reader.tagged_corpus import TaggedCorpus


def eda_vlsp_chunk():
    total_corpus = TaggedCorpus()
    for file in ["train", "test", "dev"]:
        input_file = join("corpus", "vlsp_chunk", file + ".txt")
        output_folder = join("eda", "vlsp_chunk", file)

        corpus = TaggedCorpus()
        corpus.load(input_file)
        total_corpus.sentences += corpus.sentences

        corpus.analyze(output_folder=output_folder, auto_remove=True)
    total_corpus.analyze(output_folder=join("eda", "vlsp_chunk", "total"),
                         auto_remove=True)


def eda_vlsp2016():
    total_corpus = TaggedCorpus()
    for file in ["train", "test", "dev"]:
        input_file = join("corpus", "vlsp2016", file + ".txt")
        output_folder = join("eda", "vlsp2016", file)

        corpus = TaggedCorpus()
        corpus.load(input_file)
        total_corpus.sentences += corpus.sentences

        corpus.analyze(output_folder=output_folder, auto_remove=True)
    total_corpus.analyze(output_folder=join("eda", "vlsp2016", "total"),
                         auto_remove=True)


if __name__ == '__main__':
    # eda_vlsp_chunk()
    eda_vlsp2016()
