from django.urls import path

from front_app.views import (
    IndexView,
)

app_name = 'front_app'

urlpatterns = [
    path(
        '',
        IndexView.as_view(),
        name='index',
    ),
]
