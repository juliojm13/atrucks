from django.urls import path

from main_api.views import (
    process_cellphone,
)

app_name = 'main_api'

urlpatterns = [
    path(
        'process_cellphone/',
        process_cellphone,
        name='process_cellphone',
    ),
]
