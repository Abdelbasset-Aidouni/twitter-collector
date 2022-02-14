from time import sleep, time
from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
# Create your views here.
from .utils import crawl_page
from textblob import TextBlob
from .models import Tweet

from django.views.generic import ListView


class TestView(TemplateView):
    template_name = "test.html"


class CrawlTweetsView(View):

    def get(self,request,*args,**kwargs):


        q =request.GET["q"]
        url = f"https://twitter.com/search?q={q}&src=typed_query"
        tweets = crawl_page(url)
        
        for tweet in tweets:
            sentiment = TextBlob(tweet).sentiment
            _tweet = Tweet(
                content = tweet,
                polarity = sentiment.polarity,
                subjectivity = sentiment.subjectivity,
                subject=q
            )
            _tweet.save()
        
        documents = Tweet.objects(subject=q)
        
        return HttpResponse(render(request,"tweet_list.html",{"tweets":documents}))
