import mongoengine
from ..twitter_collector.settings import DATABASE


mongoengine.connect(db=DATABASE["NAME"], host=DATABASE["HOST"])

# Create your models here


class Tweet(mongoengine.Document):
    content     = mongoengine.StringField()
    language    = mongoengine.StringField()
    toxicity    = mongoengine.FloatField()

