from django.shortcuts import render
from celebrityRankingApp.forms import InputCelebrityNames
import requests
from time import sleep
import os 
from operator import itemgetter
from django.contrib import messages

# Create your views here.

def extractCelebrityData(celebDataDict):
    celebrityInfoList = []
    celebrityInfoList.append(celebDataDict.get('name'))           
    celebrityInfoList.append(celebDataDict.get('age'))           
    celebrityInfoList.append(celebDataDict.get('height'))           
    celebrityInfoList.append(celebDataDict.get('net_worth'))
    return(celebrityInfoList)

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
    allCelebrityList = []

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

        apiErrorFlag = False

        if firstCelebrityTicked == 'on':
            celebrityData = getCelebrityStats("Benedict Cumberbatch")
            if celebrityData != "Error":     
                allCelebrityList.append(extractCelebrityData(celebrityData[0]))      
            else:
                apiErrorFlag = True
                
        if secondCelebrityTicked == 'on':
            celebrityData = getCelebrityStats("Tom Hiddleston")
            if celebrityData != "Error":     
                allCelebrityList.append(extractCelebrityData(celebrityData[0]))      
            else:
                apiErrorFlag = True 

        if thirdCelebrityTicked == 'on':
            celebrityData = getCelebrityStats("Scarlett Johansson")
            if celebrityData != "Error":     
                allCelebrityList.append(extractCelebrityData(celebrityData[0]))      
            else:
                apiErrorFlag = True

        if fourthCelebrityTicked == 'on':
            celebrityData = getCelebrityStats("Elizabeth Olsen")
            if celebrityData != "Error":     
                allCelebrityList.append(extractCelebrityData(celebrityData[0]))      
            else:
                apiErrorFlag = True

        if fifthCelebrityTicked == 'on':
            celebrityData = getCelebrityStats("Chris Hemsworth")
            if celebrityData != "Error":     
                allCelebrityList.append(extractCelebrityData(celebrityData[0]))      
            else:
                apiErrorFlag = True

        #allCelebrityList = [['Scarlett Johansson', 37, 1.6, 165000000.0], ['Chris Hemsworth', 39, 1.9, 130000000.0], ['Tom Hiddleston', 41, 1.87, 25000000.0]]
        #allCelebrityList = [['Scarlett Johansson', 37, 1.6, 165000000.0]]
        if len(allCelebrityList) <= 1:
            if apiErrorFlag:
                context['message'] = "Error in API try again later."
            else : 
                context['message'] = "Please select two or more celebrities."
        else:
            sortedList = sorted(allCelebrityList, key=itemgetter(3), reverse=True)
            context['inputs'] = sortedList 

    return render(request, 'celebrity-ranking.html', context)

def getCelebrityStats(name):
    try : 
        apiKey = os.getenv('X-RapidAPI-Key')
        sleep(1)
        url = "https://celebrityninjas.p.rapidapi.com/v1/searchu"

        querystring = {"name":name,"limit":"10"}

        headers = {
            "X-RapidAPI-Key": apiKey,
            "X-RapidAPI-Host": "celebrityninjas.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        response.raise_for_status() # Goes straight to the except without executing anything below it if something goes wrong.
        print(f"PRINTING : {response.text}")
        return(response.json())

    except Exception as error :
        print(f"{error}")
        return("Error")


