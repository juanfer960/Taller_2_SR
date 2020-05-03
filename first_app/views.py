from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .models import PREDICTION_CHART
from .models import Registry
from .models import review, business, tip, userData
from .models import Document_features,Categorie,DfReview_train,DfReview_test,Prediction
from .models import ItemItem
from . import forms
from first_app.forms import NewUserForm,FormName
from sklearn.model_selection import train_test_split
import pickle
from sklearn import svm
from sklearn.metrics import classification_report

# imports SR

import pandas as pd
import numpy as np

# Create your views here.

def index(request):
    return render(request,'index.html')


def login(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['user']
            password = form.cleaned_data['password']

            #rs()

            predictions = Prediction.objects.filter(user_id = password, mark = 'True')[:10]

            con = 1
            dataRes_1 = []
            dataRes_2 = []
            dataRes_3 = []
            dataRes_4 = []
            dataRes_5 = []
            dataRes_6 = []

            if(not predictions):
                busines_ = business.objects.filter()[:10]

                for busines in busines_:

                    if(con <= 3):
                        try:
                            dataRes_1.append(busines.name)
                            con = con+1
                        except:
                            print('error')
                    else:
                        if(con <=6):
                            try:
                                dataRes_2.append(busines.name)
                                con = con+1
                            except:
                                print('error')
                        else:
                            if(con <= 9):
                                try:
                                    dataRes_3.append(busines.name)
                                    con = con+1
                                except:
                                    print('error')
                            else:
                                break

            else:
                for prediction in predictions:
                    busines = business.objects.filter(business_id = prediction.business_id).first()

                    if(con <= 3):
                        try:
                            dataRes_1.append(busines.name)
                            con = con+1
                        except:
                            print('error')
                    else:
                        if(con <=6):
                            try:
                                dataRes_2.append(busines.name)
                                con = con+1
                            except:
                                print('error')
                        else:
                            if(con <= 9):
                                try:
                                    dataRes_3.append(busines.name)
                                    con = con+1
                                except:
                                    print('error')
                            else:
                                break

            prediction_1 = modelItemitem(password)

            conM2 = 1 

            for prediction in prediction_1:
                    busines = business.objects.filter(business_id = prediction.business_id).first()
            
                    if(conM2 <= 3):
                        try:
                            dataRes_4.append(busines.name)
                            conM2 = conM2+1
                        except:
                            print('error')
                    else:
                        if(conM2 <=6):
                            try:
                                dataRes_5.append(busines.name)
                                conM2 = conM2+1
                            except:
                                print('error')
                        else:
                            if(conM2 <= 9):
                                try:
                                    dataRes_6.append(busines.name)
                                    conM2 = conM2+1
                                except:
                                    print('error')
                            else:
                                break

            dataRes = {'user': user, 'password': password,'dataRes_uno':dataRes_1,'dataRes_dos':dataRes_2,'dataRes_tres':dataRes_3,'dataRes_cuatro':dataRes_4,'dataRes_cinco':dataRes_5,'dataRes_seis':dataRes_6}

            if userValid(user,password):
                return  render(request,'basicapp/workPage.html',context=dataRes)

            else:
                data = {'user': 'null', 'password': 'null'}
                form = NewUserForm(data)
                form.is_valid()

                return render(request,'basicapp/pageError.html')

    return render(request,'basicapp/login.html',{'form':form})


def logup(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'basicapp/successPage.html')
        else:
            print('ERROR FORM INVALID')

    return render(request,'basicapp/logup.html',{'form':form})


def userValid (user, password):
    try:
        User.objects.get(user = user, password =  password)
        print(User)
    except:
        return False

    return True


def singout(request):
    return render(request,'index.html')


def search(request,**kwargs):

    user = kwargs['user']
    password = kwargs['password']
    dataRes = {'user': user, 'password': password}

    return  render(request,'basicapp/search.html',context=dataRes)


def search(request,**kwargs):
    form = forms.FormSearch()

    user = kwargs['user']
    password = kwargs['password']
    dataRes = {'user': user, 'password': password,'form':form}

    return  render(request,'basicapp/search.html',context=dataRes)


def home(request,**kwargs):

    user = kwargs['user']
    password = kwargs['password']

    #rs()

    predictions = Prediction.objects.filter(user_id = password, mark = 'True')[:10]

    con = 1
    dataRes_1 = []
    dataRes_2 = []
    dataRes_3 = []
    dataRes_4 = []
    dataRes_5 = []
    dataRes_6 = []

    if(not predictions):
        busines_ = business.objects.filter()[:10]
  
        for busines in busines_:
            if(con <= 3):
                try:
                    dataRes_1.append(busines.name)
                    con = con+1
                except:
                    print('error')
            else:
                if(con <=6):
                    try:
                        dataRes_2.append(busines.name)
                        con = con+1
                    except:
                        print('error')
                else:
                    if(con <= 9):
                        try:
                            dataRes_3.append(busines.name)
                            con = con+1
                        except:
                            print('error')
                    else:
                        break

    else:
        for prediction in predictions:
            busines = business.objects.filter(business_id = prediction.business_id).first()

            if(con <= 3):
                try:
                    dataRes_1.append(busines.name)
                    con = con+1
                except:
                    print('error')
            else:
                if(con <=6):
                    try:
                        dataRes_2.append(busines.name)
                        con = con+1
                    except:
                        print('error')
                else:
                    if(con <= 9):
                        try:
                            dataRes_3.append(busines.name)
                            con = con+1
                        except:
                            print('error')
                    else:
                        break

    prediction_1 = modelItemitem(password)

    conM2 = 1

    for prediction in prediction_1:
            busines = business.objects.filter(business_id = prediction.business_id).first()
            print('***************************************')
            print(busines.name)
            print('***************************************')

            if(conM2 <= 3):
                try:
                    dataRes_4.append(busines.name)
                    conM2 = conM2+1
                except:
                    print('error')
            else:
                if(conM2 <=6):
                    try:
                        dataRes_5.append(busines.name)
                        conM2 = conM2+1
                    except:
                        print('error')
                else:
                    if(con <= 9):
                        try:
                            dataRes_6.append(busines.name)
                            conM2 = conM2+1
                        except:
                            print('error')
                    else:
                        break



    dataRes = {'user': user, 'password': password,'dataRes_uno':dataRes_1,'dataRes_dos':dataRes_2,'dataRes_tres':dataRes_3,'dataRes_cuatro':dataRes_4,'dataRes_cinco':dataRes_5,'dataRes_seis':dataRes_6}

    return  render(request,'basicapp/workPage.html',context=dataRes)


def modelItemitem(id_user):
    
    dataRes = []

    try:
        return ItemItem.objects.filter(user_id = id_user)[:10]
    except: 
        return dataRes


def businessA(request,**kwargs):

    user = kwargs['user']
    password = kwargs['password']

    dataRes_1 = []
    dataRes_2 = []
    dataRes_3 = []


    business_ = business.objects.all()[:10]

    for busines in business_:
        print('***********************************************')
        print(busines.name)
        print('***********************************************')

    dataRes = {'user': user, 'password': password,'dataRes_uno':dataRes_1,'dataRes_dos':dataRes_2,'dataRes_tres':dataRes_3,}

    return  render(request,'basicapp/workPage.html',context=dataRes)


def analysis(request,**kwargs):

    user=kwargs['user']
    password=kwargs['password']

    cont = 0
  
    predictions = Prediction.objects.filter(user_id = password, mark = 'True')[:10]

    dataRes_Name = []
    dataRes_city = []
    dataRes_adreesss = []
    dataRes_score = []
    
    for prediction in predictions:
        busines = business.objects.filter(business_id = prediction.business_id).first()
        try:

            if(len(busines.name) == 0 ):
                dataRes_Name.append('No adname found')
            else:
                dataRes_Name.append(busines.name)

            if(len(busines.city) == 0 ):
                dataRes_city.append('No city found')
            else:
                dataRes_city.append(busines.city)

            if(len(busines.address) == 0 ):
                dataRes_adreesss.append('No address found')
            else:
                dataRes_adreesss.append(busines.address)

            if(len(busines.stars) == 0 ):
                dataRes_score.append('No stars found')
            else:
                dataRes_score.append(busines.stars)
                
            cont = cont + 1
        except:
            print('error')

        if(cont > 8):
            break

    dataRes = {'user': user, 'password': password,'dataRes_artistName':dataRes_Name,'dataRes_city':dataRes_city,'dataRes_artistId':dataRes_adreesss,'dataRes_prediction':dataRes_score}
    return  render(request,'basicapp/analysis.html',context=dataRes)


def songSerch(request,**kwargs):
    form = forms.FormSearch()
    dataRes_  = []
    user=kwargs['user']
    password=kwargs['password']
    dataRes = {}

    if request.method == 'POST':
        form = forms.FormSearch(request.POST)

        con = 0
        if form.is_valid():
            busines = business.objects.filter(city = form.cleaned_data['search'])
            for oneBusines in busines:
                predictions = Prediction.objects.filter(business_id = oneBusines.business_id, user_id = password ,mark = 'True').first()

                try:
                    predictions.user_id
                    if(con < 10):
                        dataRes_.append(oneBusines.name)
                        con = con +1
                    else:
                        break
                except:
                    print('ERROR')
                    #dataRes = {'user': user, 'password': user}

                dataRes = {'user': user, 'password': password,'form':form, 'dataRes_':dataRes_}

        return  render(request,'basicapp/search.html',context=dataRes)

    return  render(request,'basicapp/search.html',context=dataRes)


def scoreone(request,**kwargs):
    user=kwargs['user']
    password=kwargs['password']
    artist=kwargs['dataRes']
    print('************************************ UNO'+artist)
    dataRes = {'user': user, 'password': user}
    return render(request,'basicapp/infoScorePage.html',context=dataRes)


def scoretwo(request,**kwargs):
    user=kwargs['user']
    print('************************************ DOS'+user)
    dataRes = {'user': user, 'password': user}
    return render(request,'basicapp/infoScorePage.html',context=dataRes)


def scorethree(request,**kwargs):
    user=kwargs['user']
    print('************************************ TRES'+user)
    dataRes = {'user': user, 'password': user}
    return render(request,'basicapp/infoScorePage.html',context=dataRes)


def scorefour(request,**kwargs):
    user=kwargs['user']
    print('************************************ CUATRO'+user)
    dataRes = {'user': user, 'password': user}
    return render(request,'basicapp/infoScorePage.html',context=dataRes)


def scorefive(request,**kwargs):
    user=kwargs['user']
    print('************************************ CINCO'+user)
    dataRes = {'user': user, 'password': user}
    return render(request,'basicapp/infoScorePage.html',context=dataRes)

def rs():

    print('******************************************************************************************************')

    print('******************************************************************************************************')
