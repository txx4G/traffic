import json
import time

from django.conf import settings
from django.views import View
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from django.http import HttpResponse



class SaveClaimView(View):
    def post(self, request):
        print(request.FILES)
        input_image_file = request.FILES.get('image')
        time_mark = time.time()
        json_data = {
            'phone': request.POST['phone'],
            'description': request.POST['description'],
            'point': request.POST['point'],
        }

        path_dir = settings.MEDIA_ROOT / 'claim_files'
        if not path_dir.exists():
            path_dir.mkdir()

        with open(path_dir / f'{time_mark}.jpg', 'wb') as image_file:
            image_file.write(input_image_file.read())

        with open(path_dir / f'{time_mark}.json', 'w') as json_file:
            json.dump(json_data, json_file)

        # return Response(status=status.HTTP_201_CREATED)
        return HttpResponse('', 'plain/text', 201)
