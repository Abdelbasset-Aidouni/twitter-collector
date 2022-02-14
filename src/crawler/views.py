from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
from .utils import crawl_page
from detoxify import Detoxify


class CrawlTweetsView(View):

    def get(request,*args,**kwargs):

        url = "https://twitter.com/search?q=covid&src=typed_query"
        # tweets = crawl_page(url)
        tweets = ["hhh","good","baad"]
        toxicity = []
        for tweet in tweets:
            toxicity.append(Detoxify('original').predict(tweet))

        return HttpResponse(toxicity)
