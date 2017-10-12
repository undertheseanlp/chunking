from underthesea import pos_tag

from .model_crf import CRFChunkingPredictor


def chunk(sentence):
    sentence = pos_tag(sentence)
    crf_model = CRFChunkingPredictor.Instance()
    result = crf_model.predict(sentence, format)
    return result

