from django.urls import path
from core.views import upload_file,edit_time,process_additional_file
urlpatterns = [
    path("", upload_file, name="upload_file"),
    path('edit-time/', edit_time, name='edit_time'),
    path("process-additional-file/", process_additional_file, name="process_additional_file"),
]