from analysis_project.access import get_project_details
from api import ERROR_CODE_INEXISTENCE, ERROR_CODE_UNSATISFIED
from text_library.access import get_text_library_data_field
import jieba.posseg as pseg
from api import SUCCESS_CODE_COMPLETE
from analysis_project.access import *
from django.core.exceptions import ObjectDoesNotExist
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from analysis_project.access import get_project_details
from api import ERROR_CODE_INEXISTENCE, ERROR_CODE_UNSATISFIED
from text_library.access import get_text_library_data_field
from text_seg import access
from ansj_utils.http_utils import response_error_msg
from analysis_project import ANALYSIS_TYPE_TEXT_SEG
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import jieba
import numpy as np
from text_seg.tokenizer import ansj_tokenize
from ansj_utils.http_utils import response_error_msg
import json


# 数据类型转换函数
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(self, obj):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.array):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)


# 分词
def tokenize_service(parameters):
    project_id = parameters["projectId"]
    dictionary_id = parameters["dictionary_id"]
    try:
        project = get_project_details(project_id)
    except ObjectDoesNotExist:
        return JsonResponse(response_error_msg(ERROR_CODE_INEXISTENCE, "待分析的项目不存在。"))

    # 获取待分析文本数据
    text_library_id = project.textlibrary_id
    try:
        text_library_data = get_text_library_data_field(text_library_id, project.analysis_fields)
    except ObjectDoesNotExist:
        return JsonResponse(response_error_msg(ERROR_CODE_UNSATISFIED, "待分析的项目的文本库或其父文本库不存在。"))

    text_list = [row[project.analysis_fields] for row in text_library_data]
    seg_dictionary = access.get_seg_dictionary(dictionary_id)[0]
    custom_words = seg_dictionary.custom_words
    stop_words = seg_dictionary.stop_words
    stop_natures = seg_dictionary.stop_natures
    min_word_length = seg_dictionary.min_word_length

    seg_list = ansj_tokenize(text_list,
                             stop_words=stop_words,
                             stop_natures=stop_natures,
                             custom_words=custom_words,
                             min_word_length=min_word_length, use_nature=False)
    save_analysis_result(project_id, ANALYSIS_TYPE_TEXT_SEG, seg_list)
    return JsonResponse({"code": SUCCESS_CODE_COMPLETE, "message": "分析完成"})


# 词性标注
def part_of_speech_service(parameters):
    project_id = parameters["projectId"]
    try:
        project = get_project_details(project_id)
    except ObjectDoesNotExist:
        return JsonResponse(response_error_msg(ERROR_CODE_INEXISTENCE, "待分析的项目不存在。"))

    # 获取待分析文本数据
    text_library_id = project.textlibrary_id
    try:
        text_library_data = get_text_library_data_field(text_library_id, project.analysis_fields)
    except ObjectDoesNotExist:
        return JsonResponse(response_error_msg(ERROR_CODE_UNSATISFIED, "待分析的项目的文本库或其父文本库不存在。"))

    text_list = [row[project.analysis_fields] for row in text_library_data]
    seg_list = ansj_tokenize(text_list,
                             stop_words=parameters["stopWords"],
                             stop_natures=parameters["stopNatures"],
                             custom_words=parameters["customWords"],
                             min_word_length=parameters["minWordLength"], use_nature=True)
    save_analysis_result(project_id, ANALYSIS_TYPE_TEXT_SEG, seg_list)
    return JsonResponse({"code": SUCCESS_CODE_COMPLETE, "message": "分析完成"})
