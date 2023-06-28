from django.conf import settings
from django.conf.urls.static import static
# from django.template.defaulttags import url
from django.urls import re_path

from . import views

app_name="todo_board"

urlpatterns = [
    re_path(r'^$', views.Todo_main.as_view(), name="todo_board")
]

urlpatterns += static(settings.MEDIA_URL, document_roof=settings.MEDIA_URL)