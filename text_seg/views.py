
from django.views.decorators.http import require_http_methods
import json
from text_seg.service import tokenize_service
from text_seg.service import part_of_speech_service


# 分词API
@require_http_methods(['POST'])
def tokenize(request):
    parameters = json.loads(request.body.decode())
    return tokenize_service(parameters)


# 词性标注
@require_http_methods(['POST'])
def part_of_speech(request):
    parameters = json.loads(request.body.decode())
    return part_of_speech_service(parameters)
