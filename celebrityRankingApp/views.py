from django.shortcuts import render
from celebrityRankingApp.forms import InputCelebrityNames
import requests
from time import sleep
import os 

# Create your views here.

def getAndRankCelebrities(request):
    # creating empty strings for the details of each celebiry to load into. It will be a string.
    celebrityOneDetails = ""
    celebrityTwoDetails = ""
    celebrityThreeDetails = ""
    celebrityFourDetails = ""
    celebrityFiveDetails = ""
    
    # creating lists for each celebrity tp ut the wanted information in
    celebrityOneInfoList = []
    celebrityTwoInfoList = []
    celebrityThreeInfoList = []
    celebrityFourInfoList = []
    celebrityFiveInfoList = []

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
            celebrityOneDetailsDict = getCelebrityStats("Benedict Cumberbatch")[0] 
            celebrityOneInfoList.append(celebrityOneDetailsDict.get('name'))           
            celebrityOneInfoList.append(celebrityOneDetailsDict.get('age'))           
            celebrityOneInfoList.append(celebrityOneDetailsDict.get('height'))           
            celebrityOneInfoList.append(celebrityOneDetailsDict.get('net_worth'))           

        if secondCelebrityTicked == 'on':
            celebrityTwoDetails = getCelebrityStats("Tom Hiddleston")[0]
            celebrityTwoInfoList.append(celebrityTwoDetails.get('name'))           
            celebrityTwoInfoList.append(celebrityTwoDetails.get('age'))           
            celebrityTwoInfoList.append(celebrityTwoDetails.get('height'))           
            celebrityTwoInfoList.append(celebrityTwoDetails.get('net_worth'))

        if thirdCelebrityTicked == 'on':
            celebrityThreeDetails = getCelebrityStats("Scarlett Johansson")[0]
            celebrityThreeInfoList.append(celebrityThreeDetails.get('name'))           
            celebrityThreeInfoList.append(celebrityThreeDetails.get('age'))           
            celebrityThreeInfoList.append(celebrityThreeDetails.get('height'))           
            celebrityThreeInfoList.append(celebrityThreeDetails.get('net_worth'))

        if fourthCelebrityTicked == 'on':
            celebrityFourDetails = getCelebrityStats("Elizabeth Olsen")[0]
            celebrityFourInfoList.append(celebrityFourDetails.get('name'))           
            celebrityFourInfoList.append(celebrityFourDetails.get('age'))           
            celebrityFourInfoList.append(celebrityFourDetails.get('height'))           
            celebrityFourInfoList.append(celebrityFourDetails.get('net_worth'))

        if fifthCelebrityTicked == 'on':
            celebrityFiveDetails = getCelebrityStats("Chris Hemsworth")[0]
            celebrityFiveInfoList.append(celebrityFiveDetails.get('name'))           
            celebrityFiveInfoList.append(celebrityFiveDetails.get('age'))           
            celebrityFiveInfoList.append(celebrityFiveDetails.get('height'))           
            celebrityFiveInfoList.append(celebrityFiveDetails.get('net_worth'))

        context['inputs'] = f"{celebrityOneInfoList}, {celebrityTwoInfoList}, {celebrityThreeInfoList}, {celebrityFourInfoList}, {celebrityFiveInfoList}"  


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
    return(response.json())


