from django.contrib import admin
from map_traffic.models import Camera, Problem


class CameraAdmin(admin.ModelAdmin):
    list_display = ('id', 'direction_text', 'problem_place', 'local_video')


admin.site.register(Camera, CameraAdmin)


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Problem, ProblemAdmin)
