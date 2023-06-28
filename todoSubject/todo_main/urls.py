from django.conf import settings
from django.conf.urls.static import static
# from django.template.defaulttags import
from django.urls import re_path

from . import views

app_name="todo_main"

urlpatterns = [
    re_path(r'^$', views.Todo_main.as_view(), name="todo_main")
]

urlpatterns += static(settings.MEDIA_URL, document_roof=settings.MEDIA_URL)