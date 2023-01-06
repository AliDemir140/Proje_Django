from django.urls import path
from . import views
urlpatterns = [
    path('<int:pinterest_id>', views.detail, name='detail'),
]
