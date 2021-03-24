from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Yield
from sklearn.preprocessing import LabelEncoder
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from .models import CropData

# Create your views here.

"""def home(request):
   #return HttpResponse("jhudele traders")
    return render(request,"home.html")"""

"""def register(request):
    return render(request,"register.html")"""

def home(request):
    return render(request,"home.html")

def login(request):
    pr = Yield.objects.all()
    if request.method == 'POST':
        uname = request.POST['username']
        passw = request.POST['password']

        user = auth.authenticate(username=uname, password=passw)

        if user is not None:
            auth.login(request, user)
            return render(request,'prediction.html')
        else:
            messages.info(request, 'invalid credentials')
            return render(request,'home.html')
    else:
        return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return render(request,"register.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return render(request,"register.html")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return render(request,'home.html')

        else:
            messages.info(request, 'Password not matching')
            return render(request,"register.html")
        return redirect('home')
    else:
        return render(request, 'register.html')


def prediction(request):
    return render(request,"prediction.html")

def predict_crop(request):
    if (request.method == 'POST'):
        area = request.POST['area']
        ha_yield = request.POST['ha_yield']
        avg_rainfall_mm = request.POST['avg_rainfall_mm']
        pesticides_tonnes = request.POST['pesticides_tonnes']
        avg_tem = request.POST['avg_tem']

        df = pd.read_csv(r"static/dataset/yield_df.csv")
        df.dropna(inplace=True)

        l = LabelEncoder()
        Area = l.fit_transform(df['Area'])
        new_data = df.drop(['Area'], axis=1)
        new_data['Area'] = Area

        X_train = new_data[['Area', 'hg/ha_yield', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp']]

        Y_train = new_data[['Item']]

        classify = DecisionTreeClassifier()
        classify.fit(X_train, Y_train)

        predicted_data = classify.predict([[area, ha_yield, avg_rainfall_mm, pesticides_tonnes, avg_tem]])

        pred_store = CropData.objects.create(area=area, ha_yield=ha_yield, avg_rainfall_mm=avg_rainfall_mm,
                                             pesticides_tonnes=pesticides_tonnes, avg_tem=avg_tem)
        pred_store.save()

        print("predicted yield of crop:", predicted_data)

        """from sklearn.naive_bayes import GaussianNB
        g = GaussianNB()
        g.fit(X_train, Y_train)
       predic = g.predict([[area, ha_yield, avg_rainfall_mm, pesticides_tonnes, avg_tem]])
        print("predicted yield of crop by GaussianNB:", predic)"""
        """from sklearn.linear_model import LinearRegression
        from sklearn.metrics import accuracy_score, r2_score
        reg = LinearRegression()
        reg.fit(X_train, Y_train)
        r=reg.predict([['area','ha_yield','avg_rainfall_mm','pesticides_tonnes','avg_tem']])
        print("prediction from linear regression algo:"r)
        print("Coefficient: ", reg.coef_)
        print("Intercept: ", reg.intercept_)"""

        return render(request, 'predicted_crop.html', {"data": predicted_data, 'area': area, 'ha_yield': ha_yield,
                                                       'avg_rainfall_mm': avg_rainfall_mm,
                                                       'pesticides_tonnes': pesticides_tonnes,
                                                       'avg_tem': avg_tem})
    else:
        return render(request,"prediction.html")



def logout(request):
    return render(request,"home.html")