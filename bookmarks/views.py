from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from .models import Bookmark
from .forms import BookmarkForm, DeleteForm


def create_bookmark(request):
    if request.method == "POST":
        form = BookmarkForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            bookmark = Bookmark(name=data['name'],
                                url=data['url'],
                                description=data['description'],
                                folder_id=data['folder'].id)
            bookmark.save()
        return render(request, 'create_bookmark.html', {'form': BookmarkForm})
    else:
        return render(request, 'create_bookmark.html', {'form': BookmarkForm})


def list_bookmarks(request):
    bookmarks = Bookmark.objects.all()
    return render(request, 'list_bookmarks.html', {'bookmarks': bookmarks})


def edit_bookmark(request, bookmark_id):
    bookmark = Bookmark.objects.get(pk=bookmark_id)
    if request.method == "POST":
        form = BookmarkForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            bookmark.name = data['name']
            bookmark.url = data['url']
            bookmark.description = data['description']
            bookmark.folder_id = data['folder']
            bookmark.save()
            return redirect(reverse('list_bookmarks'))
    else:
        form = BookmarkForm(initial={'name': bookmark.name,
                                     'url': bookmark.url,
                                     'description': bookmark.description})
        return render(request, 'create_bookmark.html',
                      {'form': form, 'bookmark': bookmark})


def delete_bookmark(request, bookmark_id):
    bookmark = Bookmark.objects.get(pk=bookmark_id)
    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.is_valid():
            bookmark.delete()
            return redirect(reverse('list_bookmarks'))
        return render(request, 'new_contact.html', {'form': form})
    else:
        return render(request, 'delete_contact.html', {'bookmark': bookmark})
