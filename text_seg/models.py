from django.db import models
# import djongo.models as mongo_models
import mongoengine
from django.contrib.postgres.fields import ArrayField


class RsSegConfig(mongoengine.Document):
    _id = mongoengine.ObjectIdField(primary_key=True, auto_created=True)
    custom_words = mongoengine.ListField()
    stop_words = mongoengine.ListField()
    stop_natures = mongoengine.ListField()
    min_word_length = mongoengine.FloatField()

    def set_all_value(self, custom_words, stop_words, stop_natures, min_word_length):
        self.custom_words = custom_words
        self.stop_words = stop_words
        self.stop_natures = stop_natures
        self.min_word_length = min_word_length

    meta = {
        "collection": 'rs_seg_config',
        'strict': False
    }
