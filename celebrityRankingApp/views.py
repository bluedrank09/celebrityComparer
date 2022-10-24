# importing libraries needed for the project
from django.shortcuts import render
from celebrityRankingApp.forms import InputCelebrityNames
import requests
from time import sleep
import os 
from operator import itemgetter

# Create your views here.

def extractCelebrityData(celebDataDict):
    celebrityInfoList = [] # creating the lists with the correct info needed using the keys from the API KVPs
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
    
    # creating lists for each celebrity to put the wanted information in
    celebrityOneInfoList = []
    celebrityTwoInfoList = []
    celebrityThreeInfoList = []
    celebrityFourInfoList = []
    celebrityFiveInfoList = []
    allCelebrityList = []

    context = {}
    form = InputCelebrityNames(request.GET or None)
    context['form'] = form
    if request.method == 'GET': # checking to see which celebrities have been checked by the user (user input)
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

        apiErrorFlag = False # setting a flag to make sure that if an error occurs, it's not the faut of a bad API call.

        if firstCelebrityTicked == 'on':
            celebrityData = getCelebrityStats("Benedict Cumberbatch")
            if celebrityData != "Error": # making sure nothing will continue if there is an error. This code ONLY operates if there are NO errors.    
                allCelebrityList.append(extractCelebrityData(celebrityData[0]))      
            else:
                apiErrorFlag = True # when the flag is set to True, it means that there was an error trying to call the API.
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

        print(f"{firstCelebrityTicked}, {secondCelebrityTicked}, {thirdCelebrityTicked}, {fourthCelebrityTicked}, {fifthCelebrityTicked}")

        #allCelebrityList = [['Scarlett Johansson', 37, 1.6, 165000000.0], ['Chris Hemsworth', 39, 1.9, 130000000.0], ['Tom Hiddleston', 41, 1.87, 25000000.0]] - previously tried harcoded list to check is the API key was failing
        #allCelebrityList = [['Scarlett Johansson', 37, 1.6, 165000000.0]]
        if len(allCelebrityList) <= 1: # making sure the user hasn't inputted one or less celebrities.
            if apiErrorFlag:
                context['message'] = "Error in API. Please try again." # telling users that it's not their fault the program has crashed, it's an API call fault.
            else : 
                context['message'] = "Please select two or more celebrities." # letting the user kno that they have to choose two or more celebrities.
        else:
            sortedList = sorted(allCelebrityList, key=itemgetter(3), reverse=True)
            context['inputs'] = sortedList 

    return render(request, 'celebrity-ranking.html', context)

def getCelebrityStats(name):
    try : 
        apiKey = os.getenv('X-RapidAPI-Key') # getting the API key from the compiter system.
        sleep(1)
        url = "https://celebrityninjas.p.rapidapi.com/v1/search" # this is the website where I got the API key from.

        querystring = {"name":name,"limit":"10"}

        headers = { # creating a dictionary to hold the API key and host in KVP
            "X-RapidAPI-Key": apiKey,
            "X-RapidAPI-Host": "celebrityninjas.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        response.raise_for_status() # Goes straight to the except without executing anything below it if something goes wrong.
        #print(f"PRINTING : {response.text}")
        return(response.json())

    except Exception as error : # checking and printing errors in the console.
        print(f"{error}")
        return("Error")


