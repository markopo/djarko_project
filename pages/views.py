from django.shortcuts import render
from .models import Page


def index(request, pagename):
    pagename = '/' + pagename
    page = Page.objects.get(permalink=pagename)

    photo_url = ''
    photo_width = 0
    print('photo: ' + repr(page.photo))
    if page.photo:
        photo_url = page.photo.url
        photo_width = page.photo.width

    context = {
        'title': page.title,
        'content': page.bodytext,
        'last_update': page.update_date,
        'photo_url': photo_url,
        'photo_width': photo_width
    }
    return render(request, 'pages/page.html', context)


