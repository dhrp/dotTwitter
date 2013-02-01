from django.template import Context, loader
from datetime import datetime, date
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import Tweet, Query, CleanedTweet
from main.forms import TweetForm, KeywordForm, UserProfileForm, UserForm
import time
from twilio.rest import TwilioRestClient
from django.conf import settings
from django.contrib.auth.models import User
from helpers.dottwitter import dotTwitter
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import xlwt
import simplejson
import urllib


from django.utils.log import logger

def saved_tweets(request):

    tweets = Tweet.objects.all().order_by('tweet_id').reverse()
    paginator = Paginator(tweets, 25)

    page = request.GET.get('page')
    try:
        tweets = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tweets = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tweets = paginator.page(paginator.num_pages)


    return render_to_response('saved_tweets.html', {
        'current_time': datetime.now(),
        'tweets': tweets
    }, context_instance = RequestContext(request))


def home(request):

    result = {}
    querys = Query.objects.all()

    try:
        latest_keywords = Query.objects.latest('id')
    except ObjectDoesNotExist:
        latest_keywords = "dotCloud"

    all_keywords = Query.objects.all()
    user = User.objects.get(pk=1)

    keywordform = KeywordForm (
        initial={'keywords': latest_keywords},
        prefix='keyword'
    )

    userprofileform = UserProfileForm (
        instance=user.userprofile,
        prefix='userprofile'
    )

    userform = UserForm (
        instance=user,
    )

    return render_to_response('home.html', {
        'current_time': datetime.now(),
        'keywordform': keywordform,
        'userform': userform,
        'userprofileform': userprofileform,
        'querys': querys,
        'result': result,
        'user': user,
        'all_keywords': all_keywords

    }, context_instance = RequestContext(request))

def home_submit(request):

    user = User.objects.get(pk=1)

    if request.method == 'POST':
        keywordform = KeywordForm(data=request.POST, prefix='keyword')
        userform = UserForm(data=request.POST, instance=user)
        userprofileform = UserProfileForm(data=request.POST, instance=user.userprofile, prefix='userprofile')

        if keywordform.is_valid():
            keywordform.save()

        if  userprofileform.is_valid():
            user = userform.save()
            profile = userprofileform.save()
            result = {'status': 'Update Succesfull'}

    return HttpResponseRedirect('/')



def remove_keywords(request, id):

    query = Query.objects.get(pk=id)
    query.delete()

    return HttpResponseRedirect('/')


def search(request):

    dot = dotTwitter()

    keywords = dot.keywords
    message = ""
    tweets = dot.searchTweets(keywords)
    status = dot.storeResults(tweets)
    message = dot.sendMessage(tweets)


    return render_to_response('search.html', {
        'tweets': tweets,
        'status': status,
        'message': message
    }, context_instance = RequestContext(request))


def make_filter(request, keyword=None, start=0, end=1000):

    if keyword and keyword != 'None':
        # give me the first X results using this keyword.
        results = Tweet.objects.filter(keyword=keyword)[start:end]
    else:
        # give me the first 500 results of everything.
        results = Tweet.objects.all()[start:end]

    set = {}
    doubles = {}
    keywords = {}

    for result in results:
        texthash = hash(result.text)

        try:
            item = set[texthash]
            try:
                doubles[texthash] = [doubles[texthash][0] + 1, result.text]
            except:
                # this is a duplicate so the count is two, add to duplicates
                doubles[texthash] = [2, result.text]
        except:
            set[texthash] = result.text

        keywords[result.keyword] = True

    return keywords, doubles

def filter(request, keyword=None, start=0, end=1000):

    keywords, results = make_filter(request, keyword, start, end)

    filteraddress = "{0}/{1}/{2}/".format(keyword, start, end)

    return render_to_response('filter.html', {
        'keywords': keywords,
        'results': results,
        'filteraddress': filteraddress
    }, context_instance = RequestContext(request))


def export(request, keyword=None, start=0, end=1000):
    book = xlwt.Workbook(encoding='utf8')

    sheet = book.add_sheet('untitled')

    default_style = xlwt.Style.default_style
    datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy hh:mm')
    date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')

    # get values
    keywords, results = make_filter(request, keyword, start, end)

    for row, rowdata in enumerate(results):
        for col, val in enumerate(results[rowdata]):
            sheet.write(row, col, val, style=default_style)


    response = HttpResponse(mimetype='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=example.xls'
    #    book.save("document.xls")
    book.save(response)
    return response

