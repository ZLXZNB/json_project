from text_seg import ANSJ_URL
# from ansj_utils.http_utils import post_json

import ansj_utils.http_utils as post_utils
import os
import logging
import json
logger = logging.getLogger('api_logger')


def ansj_tokenize(text_list, stop_words, stop_natures, custom_words, min_word_length,
                  use_nature):
    if stop_words is None:
        stop_words = []
    if stop_natures is None:
        stop_natures = []
    if custom_words is None:
        custom_words = []
    if min_word_length is None:
        min_word_length = 2

    parameters = {
        "texts": text_list,
        "stopWords": stop_words,
        "stopNatures": stop_natures,
        "customWords": custom_words,
        "minWordLength": min_word_length
    }

    logger.info("开始分词。使用的ansj url：" + ANSJ_URL)
    # logger.info("分词参数：" + json.dumps(parameters, ensure_ascii=False))

    if use_nature:
        return post_utils.post_json(ANSJ_URL, parameters)
    else:
        return [[word["name"] for word in seg] for seg in post_utils.post_json(ANSJ_URL, parameters)]
