from django.conf import settings
from django.views import View
from django.shortcuts import render, get_object_or_404, resolve_url

from map_traffic.models import Problem


class IndexView(View):
    def get(self, request):
        problems = list(Problem.objects.values('id', 'name'))
        problems = [{'link': resolve_url('problem', problem['id']), **problem} for problem in problems]
        problems[0]['coords'] = [45.03585, 38.97408]
        problems[1]['coords'] = [45.05284, 38.97688]
        problems[2]['coords'] = [45.0435, 39.0007]
        problems[3]['coords'] = [45.055200, 39.002765]
        problems[4]['coords'] = [45.037441, 38.954626]
        problems[5]['coords'] = [45.070221, 38.972861]
        context = {
            'problem_places': problems
            # [
            #     { 'coords': [45.03585, 38.97408], 'name': "Галерея", 'link': "details.html?map=gallery", 'id': "gallery"},  # TODO: удалить поле link (его заменит id)
            #     { 'coords': [45.05284, 38.97688], 'name': "Баскет-Холл", 'link': "details.html?map=basket-hall", 'id': "basket-hall" },
            #     { 'coords': [45.0435, 39.0007], 'name': "Красная-Ростовское", 'link': "details.html?map=red-rostov", 'id': 'red-rostov'},
            # ]
        }
        print(context)
        return render(request, 'pages/index.html', context)


class ProblemView(View):
    def get(self, request, problem_id):
        problem = get_object_or_404(Problem, pk=problem_id)
        context = {
            'name': problem.name,
            'map_link': problem.map_link,
            'cameras': [{'local_video': f'{settings.MEDIA_URL}{camera.local_video}'} for camera in problem.cameras.all()],
        }
        return render(request, 'pages/problem.html', context)


class ClaimView(View):
    def get(self, request):
        context = {
            'claims': [
                {'phone': '+735467586', 'coords': [3456, 5785], 'dt': '23.12.45 20:12', 'description': 'Sed ut perspiciatis, unde omnis iste natus error sit volupta hitecto'},
                {'phone': '+754678654', 'coords': [3456, 5785], 'dt': '23.12.45 20:12', 'description': 'perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremquperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto'},
                {'phone': '+743564784', 'coords': [5436, 5464], 'dt': '23.12.45 20:12', 'description': 'iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto'},
                {'phone': '+702938484', 'coords': [3456, 5785], 'dt': '23.12.45 20:12', 'description': ' natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam etis et quasi architecto'},
                {'phone': '+743564543', 'coords': [3456, 5785], 'dt': '23.12.45 20:12', 'description': 'Sed unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto'},
                {'phone': '+734567535', 'coords': [9808, 5785], 'dt': '23.12.45 20:12', 'description': 'perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto'},
                {'phone': '+732454674', 'coords': [3456, 5785], 'dt': '23.12.45 20:12', 'description': ' iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto'},
                {'phone': '+732454675', 'coords': [3456, 5785], 'dt': '23.12.45 20:12', 'description': 'Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantiuo'},
            ]
        }
        return render(request, 'pages/claim.html', context)


class EffectiveView(View):
    def get(self, request):
        context = {
        }
        return render(request, 'pages/effective.html', context)



class PredictView(View):
    def get(self, request):
        context = {
        }
        return render(request, 'pages/predict.html', context)