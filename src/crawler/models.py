import mongoengine
from django.conf import settings


mongoengine.connect(host="mongodb://root:root@db:27017/tweet_db?authSource=admin")

# Create your models here


class Tweet(mongoengine.Document):
    content         = mongoengine.StringField()
    polarity        = mongoengine.FloatField()
    subjectivity    = mongoengine.FloatField()
    subject         = mongoengine.StringField()

