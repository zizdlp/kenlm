import kenlm  # type: ignore
from cachetools import cached  ### model 缓存
@cached(cache={})
def load_model(lang):
    lm_config = kenlm.Config()
    lm_config.load_method = 2
    model_path="/metadata0/wxl_data/lm_sp/{lang}.arpa.bin"
    lm = kenlm.Model(model_path, lm_config)
    return lm
def process_line(model,line):
    log_score = model.score(line)
    return log_score
