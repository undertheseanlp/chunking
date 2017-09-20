from os.path import join

from underthesea_flow.reader.tagged_corpus import TaggedCorpus

# input = "chunk_train.txt"
# output = "train"

# input = "chunk_dev.txt"
# output = "dev"

# input = "chunk_test.txt"
# output = "test"
#
# input_file = join("corpus", "vlsp_chunk", input)
# output_folder = join("eda", "vlsp_chunk", output)

input_file = join("corpus", "vi_chunk", "train.txt")
output_folder = join("eda", "vi_chunk")

corpus = TaggedCorpus()
corpus.load(input_file)

corpus.analyze(output_folder=output_folder)
