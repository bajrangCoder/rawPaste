from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from .forms import PasteForm
from .models import Paste
from django.utils import timezone
from django.apps import apps
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


config = apps.get_app_config("pastes")
def get_expiry_datetime(expiration):
    exp_datetime = timezone.now()
    if expiration == config.FIFTEEN_MINUTES:
        exp_datetime += timezone.timedelta(minutes=15)
    elif expiration == config.ONE_HOUR:
        exp_datetime += timezone.timedelta(hours=1)
    elif expiration == config.ONE_DAY:
        exp_datetime += timezone.timedelta(hours=24)
    elif expiration == config.ONE_WEEK:
        exp_datetime += timezone.timedelta(weeks=1)
    elif expiration == config.ONE_MONTH:
        exp_datetime += timezone.timedelta(hours=24*31) # Assuming 1 month=31days
    elif expiration == config.SIX_MONTH:
        exp_datetime += timezone.timedelta(hours=24*31*6)
    elif expiration == config.ONE_YEAR:
        exp_datetime += timezone.timedelta(hours=24*31*12)
    return exp_datetime

def index(request):
    form = PasteForm(request.POST or None, request=request)
    if form.is_valid():
        data = form.cleaned_data
        expiry_datetime = get_expiry_datetime(data["expiration"])
        paste = Paste(title=data["title"],content=data["content"],lang=data["lang"], expired_on=expiry_datetime)
        paste.save(session=request.session)
        return HttpResponseRedirect(paste.get_absolute_url())
    return render(request, 'new.html',{"form":form})


def paste_detail(request,slug_key):
    paste = Paste.objects.filter(secret_key=slug_key).first()
    if paste.is_expired():
        raise Http404("This paste is expired.")
    paste.view_count += 1
    paste.save(session=request.session)
    lexer = get_lexer_by_name(paste.lang)
    formatter = HtmlFormatter(linenos=True,style="github-dark")
    result = highlight(paste.content, lexer, formatter)
    stylying_code = formatter.get_style_defs('.highlight')
    
    return render(request, 'paste.html', {"paste":paste,"html_code":result,"stylying_code":stylying_code})
    

def raw_paste(request, slug_key):
    try:
        paste = Paste.objects.filter(secret_key=slug_key).first()
        if paste.is_expired():
            raise Http404("This paste is expired.")
        #response = render(request, 'raw_paste.html', {"paste":paste})
        response = HttpResponse(paste.content)
        response["Content-Type"] = "text/plain;charset=UTF-8"
    except:
        Http404("Something went wrong.")
    return response

def paste_history(request):
    try:
        user_key = request.session["user_key"]
        data = Paste.objects.filter(user_key=user_key).order_by("-created_on")
        context = {"data":data}
    except KeyError:
        context = {"status":"no_data"}
    return render(request, 'history.html', context)

