from django.views.generic.base import View
from django.shortcuts import render_to_response


class HelloWorldView(View):
    def get(self, request):
        return render_to_response("hello.html")
