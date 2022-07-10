from django.urls import path
from .views import ResultsView

app_name = 'app'

urlpatterns = [
    path('result/<str:pk>/', ResultsView.as_view(), name="result"),
]