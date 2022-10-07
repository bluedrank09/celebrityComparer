from django.shortcuts import render
from celebrityRankingApp.forms import InputCelebrityNames
import requests
from time import sleep
import os

# Create your views here.

def getAndRankCelebrities(request):
    celebrityOneDetails = ""
    celebrityTwoDetails = ""
    celebrityThreeDetails = ""
    celebrityFourDetails = ""
    celebrityFiveDetails = ""

    context = {}
    form = InputCelebrityNames(request.GET or None)
    context['form'] = form
    if request.method == 'GET':
        firstCelebrityTicked = request.GET.get('first_celebrity')
        print(f"{firstCelebrityTicked}")

        secondCelebrityTicked = request.GET.get('second_celebrity')
        print(f"{secondCelebrityTicked}")

        thirdCelebrityTicked = request.GET.get('third_celebrity')
        print(f"{thirdCelebrityTicked}")

        fourthCelebrityTicked = request.GET.get('fourth_celebrity')
        print(f"{fourthCelebrityTicked}")

        fifthCelebrityTicked = request.GET.get('fifth_celebrity')
        print(f"{fifthCelebrityTicked}")

        if firstCelebrityTicked == 'on':
            celebrityOneDetails = getCelebrityStats("Benedict Cumberbatch")

        if secondCelebrityTicked == 'on':
            celebrityTwoDetails = getCelebrityStats("Tom Hiddleston")

        if thirdCelebrityTicked == 'on':
            celebrityThreeDetails = getCelebrityStats("Scarlett Johansson")

        if fourthCelebrityTicked == 'on':
            celebrityFourDetails = getCelebrityStats("Elizabeth Olsen")

        if fifthCelebrityTicked == 'on':
            celebrityFiveDetails = getCelebrityStats("Chris Hemsworth")

        context['inputs'] = f"{celebrityOneDetails}, {celebrityTwoDetails}, {celebrityThreeDetails}, {celebrityFourDetails}, {celebrityFiveDetails}"  


    return render(request, 'celebrity-ranking.html', context)

def getCelebrityStats(name):
    apiKey = os.getenv('X-RapidAPI-Key')
    sleep(1)
    url = "https://celebrityninjas.p.rapidapi.com/v1/search"

    querystring = {"name":name,"limit":"10"}

    headers = {
        "X-RapidAPI-Key": apiKey,
        "X-RapidAPI-Host": "celebrityninjas.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    return(response.text)
