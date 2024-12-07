from django.views import View
from django.shortcuts import render, get_object_or_404


class IndexView(View):
    def get(self, request):
        context = {
        }
        return render(request, 'pages/index.html', context)


class ProblemView(View):
    def get(self, request):
        context = {}
        return render(request, 'pages/problem.html', context)
