from django.shortcuts import render
from .models import Page


def index(request, pagename):
    pagename = '/' + pagename
    print('page: ' + repr(pagename))
    page = Page.objects.get(permalink=pagename)

    context = {
        'title': page.title,
        'content': page.bodytext,
        'last_update': page.update_date
    }
    return render(request, 'pages/page.html', context)


