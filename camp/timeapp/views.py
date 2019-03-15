from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
import datetime
# Create your views here.


def hello(request):
    """A view to display Hello World"""
    text = HttpResponse()
    text.write("<htm><head>")
    text.write("<title>Sample</title></head>")
    text.write("<body><p>Hello friends,<p>")
    text.write("<p>Welcome to Winter camp..</p></body>")
    return text


def time(request):
    time = datetime.datetime.now()
    return HttpResponse(time)


def time_diff(request, offset):
    hours = int(offset)
    time = datetime.datetime.now()
    new_time = datetime.timedelta(hours=hours)+time
    return HttpResponse(new_time)


def time_diff2(request, offset):
    res = HttpResponse()
    hours = int(offset)
    time = datetime.datetime.now()
    res.write("<p>The present time is %s"%time)
    new_time = datetime.timedelta(hours=hours)+time
    res.write("<p>The time after %s hours is %s"%(hours, new_time))
    return res


# def ttime(request):
#     time = datetime.datetime.now()
#     template = get_template("c_time.html")
#     res = template.render({'c_time': time})
#     return HttpResponse(res)

def ttime(request):
    time = datetime.datetime.now()
    return render(request, "c_time.html",{'c_time': time})


def ttime_diff(request, offset):
    hours = int(offset)
    time = datetime.datetime.now()
    new_time = datetime.timedelta(hours=hours)+time
    return render(request, "f_time.html", {'c_time': time, 'hours': hours, 'f_time': new_time})






