from django.urls import path
from celebrityRankingApp.views import getAndRankCelebrities # importing the method from the views 

app_name = 'celebrityRankingApp' 

urlpatterns = [
    path('', getAndRankCelebrities, name = 'getAndRankCelebrities')
]   

