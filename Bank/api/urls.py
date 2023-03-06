from django.urls import path
from .views import autocomplete_branch, allpossible_branch

urlpatterns = [
    path('autocomplete/', autocomplete_branch),
    path('', allpossible_branch),
]