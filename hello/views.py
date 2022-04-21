from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("my name is Ilyas")

def hello(request):
    return HttpResponse("hello world")

def goodbye(request):
    return HttpResponse("I live in Bishkek")

def city(request):
    return HttpResponse("My home town is famous for its architecture")

def country(request):
    return HttpResponse("Essay on the topic my homeland Kyrgyzstan in EnglishKyrgyzstan is a beautiful country."
                        " in Kyrgyzstan, many mountains, nut wood. at the mountains, fresh air and very beautiful."
                        " In my country is home to more than 6 million people in Bishkek, capital of Kyrgyzstan in Kyrgyzstan "
                        "there are 7 regions of Jalal-Abad, OSH, Batken, Naryn, Talas, Chui and Yssyk-Kul."
                        " Fundamental Republic has its own flag, anthem and coat of arms of Kyrgyzstan live many nationalities such as:"
                        " Uzbeks, Tajiks, Russians, Cossacks, etc")
# Create your views here.
