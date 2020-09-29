from django.shortcuts import render, get_object_or_404
from .models import Page


def index(request, slug='', is_front_page=False):

    if is_front_page:
        page = get_object_or_404(Page, is_front_page=is_front_page)
    else:
        page = get_object_or_404(Page, slug=slug)

    pages = Page.objects.all().order_by('-is_front_page', '-title').values('slug', 'title')

    photo_url = ''
    photo_width = 0
    if page.photo:
        photo_url = page.photo.url
        photo_width = page.photo.width

    context = {
        'title': page.title,
        'content': page.bodytext,
        'last_update': page.update_date,
        'photo_url': photo_url,
        'photo_width': photo_width,
        'pages': pages
    }
    return render(request, 'pages/page.html', context)


