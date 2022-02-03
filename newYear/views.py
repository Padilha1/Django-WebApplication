from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "newYear/index.html", {
        "new year": now.month == 1 and now.day == 1
    })

