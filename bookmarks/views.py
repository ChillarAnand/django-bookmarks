from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import HttpResponse, HttpResponseRedirect

from .models import Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse_lazy('bookmark-list'))


class BookmarkListView(ListView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse_lazy('bookmark-list'))


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark-list')
