from os.path import dirname, join

import pycrfsuite
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, recall_score, \
    f1_score
from underscore import _
from underthesea_flow.flow import Flow
from underthesea_flow.model.crf import CRF
from underthesea_flow.reader.tagged_corpus import TaggedCorpus
from underthesea_flow.transformer.tagged import TaggedTransformer
from underthesea_flow.validation.validation import TrainTestSplitValidation

from models.crf_model.features.feature import word2features
from models.crf_model.model_profiling import ModelProfiling
from models.crf_model.transformer import Transformer
from preprocess import load_data


def convert_cm_to_log(cm, labels, line=5):
    cm = cm.tolist()
    cm = [" ".join([("%-" + str(line) + "s") % labels[index]] + map(
        lambda i: ("%" + str(line) + "d") % i, row)) for index, row in
          enumerate(cm)]
    title = " " * (line + 1) + " ".join(
        map(lambda i: ("%" + str(line) + "s") % i, labels))
    cm.insert(0, title)
    return cm


if __name__ == '__main__':
    # file = join(dirname(__file__), "corpus", "vlsp_chunk", "train.txt")
    file = join(dirname(__file__), "corpus", "vlsp_chunk_sample", "train.txt")
    sentences = load_data(file)
    flow = Flow()
    flow.data(sentences=sentences)
    template = [
        "T[0].lower", "T[-1].lower", "T[1].lower",
        "T[0].istitle", "T[-1].istitle", "T[1].istitle",
        "T[-2]", "T[-1]", "T[0]", "T[1]", "T[2]",  # unigram
        "T[-2,-1]", "T[-1,0]", "T[0,1]", "T[1,2]",  # bigram
        "T[-1][1]", "T[-2][1]", "T[-3][1]",  # dynamic feature
        "T[-3,-2][1]", "T[-2,-1][1]",
        "T[-3,-1][1]"
    ]
    transformer = TaggedTransformer(template)
    flow.transform(transformer)

    crf_params = {
        'c1': 1.0,  # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 1000,  #
        # include transitions that are possible, but not observed
        'feature.possible_transitions': True
    }
    flow.add_model(CRF(params=crf_params))

    flow.add_score('f1')
    flow.add_score('accuracy')

    flow.set_validation(TrainTestSplitValidation(test_size=0.1))

    flow.validation()

    # random_state = 10
    # profile = ModelProfiling()
    # profile.add("data", {"train": len(X_train), "test": len(X_test)})
    # profile.add("model", model_params)
    # profile.add("template", template)
    #
    # model_name = "chunking-crf-model"
    # profile.start_train()
    # trainer.train(model_name)
    # profile.end_train()
    #
    # model = pycrfsuite.Tagger()
    # model.open(model_name)
    #
    # y_test = _.flatten(y_test)
    # y_pred = [model.tag(x) for x in X_test]
    # y_pred = _.flatten(y_pred)
    # labels = list(set(y_test).union(set(y_pred)))
    #
    # cm = confusion_matrix(y_test, y_pred, labels)
    # cm = convert_cm_to_log(cm, labels)
    # score = {
    #     "accuracy": accuracy_score(y_test, y_pred),
    #     "recall": recall_score(y_test, y_pred, average='weighted'),
    #     "precision": precision_score(y_test, y_pred, average='weighted'),
    #     "f1": f1_score(y_test, y_pred, average='weighted')
    # }
    # profile.add("score", score)
    # profile.add("confusion matrix", cm)
    #
    # profile.save()
    # profile.show()
