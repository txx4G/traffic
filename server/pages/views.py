from django.views import View
from django.shortcuts import render, get_object_or_404


class IndexView(View):
    def get(self, request):
        context = {
            'problem_points': [
                { 'coords': [45.03585, 38.97408], 'name': "Галерея", 'link': "details.html?map=gallery", 'id': "gallery"},  # TODO: удалить поле link (его заменит id)
                { 'coords': [45.05284, 38.97688], 'name': "Баскет-Холл", 'link': "details.html?map=basket-hall", 'id': "basket-hall" },
                { 'coords': [45.0435, 39.0007], 'name': "Красная-Ростовское", 'link': "details.html?map=red-rostov", 'id': 'red-rostov'},
            ]
        }
        return render(request, 'pages/index.html', context)


class ProblemView(View):
    def get(self, request, coords):
        context = {
        }
        return render(request, 'pages/problem.html', context)
