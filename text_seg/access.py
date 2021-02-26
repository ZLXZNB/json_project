from bson import ObjectId

from text_seg.models import RsSegConfig


def get_seg_dictionary(dictionary_id):
    return RsSegConfig.objects.filter(_id=dictionary_id)
