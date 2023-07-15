import csv
import pandas as pd
import random
import osmnx as ox
from geopy.distance import geodesic
from graph1 import *
from graph2 import *
from graph3 import *
from datetime import time,date
class login_main:

    def __init__(self):
        print('\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE} Welcome To Ride Of Comfort\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}')
        print('1] For a Driver')
        print('2] For a User')
        self.op=int(input('1 or 2 or Any other key For Exit:'))
        if self.op==1:
            driver.__init__(self)
        elif self.op==2:
            user.__init__(self)
        else:
            exit(0)

class driver:

    def __init__(self):
        print('\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE} Welcome To Driver Session\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}')
        print('1]Please Press 1 for Sign in or Anything for Exit:')
        self.ch=int(input('Your choice:'))
        if self.ch==1:
            driver.creatdriver(self)
        else:
            exit(0)

    def creatdriver(self):

       print(
            '\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE} Here We Go...\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}')
       self.price=0
       self.d_name=input('Enter your name(driver):')
       self.d_phone_no=int(input('Enter Your Phonenumber(driver):'))
       self.uf = open('driver.csv', 'r')
       self.cl = csv.DictReader(self.uf)
       check=0
       for i in self.cl:
           if(i['Drivername']==self.d_name):
               check=1
       if(check==1):
            print('Already Exists')
            login_main.__init__(self)
       else:
           if(len(str(self.d_phone_no))==10):
               self.ua = open('driver.csv', 'a', newline='')
               self.cv=csv.writer(self.ua)
               self.cv.writerow([self.d_name,self.d_phone_no,self.price])
               self.ua.close()
               self.uf.close()
               #driver.__init__(self)
               login_main.__init__(self)
           else:
               print('You Enter Invaild Phonenumber')
               driver.creatdriver(self)

class user:
    dict_data = {}
    u_name=''
    #l=[1234,4567,8906]
    def __init__(self):
        print('\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE} Welcome To User Session\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}')
        self.option=int(input("1]if you are new user\n2]For Login\n3]Any other key for exit\nEnter option:"))
        if (self.option==1):
            user.creatuser(self)
        elif(self.option==2):
            user.login(self)
        else:
            exit(0)

    def login(self):
        print(
            '\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE} Here We Go...\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}')
        self.username = input("Enter Your Username:")
        user.u_name=self.username
        self.phonenumber=int(input("Enter Your Phonenumber(Please Enter 10 digit Phonenumber):"))
        self.uf = open('user.csv', 'r')
        self.cl = csv.DictReader(self.uf)
        self.check = 0
        for i in self.cl:
            if (i['username'] == self.username):
                self.check+=1
                if i['phonenumber'] == str(self.phonenumber):
                    self.check+=1
        if(self.check==0):
            print('username not found')
            user.__init__(self)
        if(self.check==1):
            print('phonenumber is invaild')
            user.login(self)
        elif(self.check==2):
            user.otpcheck(self)

    def creatuser(self):

       print('\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE} Profile Making\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}')
       self.username=input('Username:')
       self.phonenumber=int(input('Enter Your Phonenumber:'))
       self.uf = open('user.csv', 'r')
       self.cl = csv.DictReader(self.uf)
       check=0
       for i in self.cl:
           if(i['username']==self.username):
               check=1
       if(check==1):
            print('Already Exists')
            user.__init__(self)
       else:
           if(len(str(self.phonenumber))==10):
               self.ua = open('user.csv', 'a', newline='')
               self.cv=csv.writer(self.ua)
               self.cv.writerow([self.username,self.phonenumber])
               self.ua.close()
               self.uf.close()
               user.__init__(self)
           else:
               print('You Enter Invaild Phonenumber')
               user.creatuser(self)

    def otpcheck(self):
            self.a = random.randint(1000, 9999)
            #print("Your otp:", self.a)
            print(
                '\N{LARGE RED CIRCLE}\N{LARGE RED CIRCLE}\N{LARGE RED CIRCLE}Your OTP \U0001F447 \N{LARGE RED CIRCLE}\N{LARGE RED CIRCLE}\N{LARGE RED CIRCLE}')
            print("OTP:",self.a)
            self.otp = int(input("Enter your otp:"))
            if self.otp == self.a:
                print("LOGGIN SUCCESSFULLY....")
                self.loc=location()
                self.ans=permission()
            else:
                print("You enter wrong otp,Please Try again")
                user.otpcheck(self)

class location:
    pick=''
    drop=''
    cost_=0
    dist_=0
    time=''
    date=''
    def __init__(self):
        try:
            self.location1 = input('Enter pickup location like:"Vastrapur, Ahmedabad"')
            self.location2 = input('Enter destination location like:"Gandhinagar"')
            t_h=int(input('Enter hours in 24 hours format'))
            t_m=int(input('Enter Minutes'))
            location.time=time(t_h,t_m)
            d_m=int(input('Enter Month of Date When you Want to Schedule your trip:'))
            d_d=int(input('Enter The Date When you Want to Schedule your trip:'))
            location.date=date(2023,d_m,d_d)
            location.pick=self.location1
            location.drop=self.location2

            # Get the latitude and longitude of the locations
            point1 = ox.geocode(self.location1)
            point2 = ox.geocode(self.location2)

            # Calculate the distance between the two points
            self.distance = geodesic(point1, point2).km

            # Print the distance
            #print(f"The distance between {self.location1} and {self.location2} is {self.distance:.2f} kilometers.")
            self.dist = round(self.distance, 2)
            self.cost = round(20 + (self.distance - 1) * 20, 2)
            location.cost_=self.cost
            location.dist_=self.dist
            print(f"distance between {self.location1} and {self.location2} is {self.dist} and cost {self.cost}")
        except:
            print('Location Not Found Please Try Again...')
            location.__init__(self)

class permission:

    def __init__(self):
        print('if You are Comfortable with this price then please enter Yes otherwise No:')
        location.option = input('Yes or No:')
        if (location.option).lower() == 'yes':
                self.random_driver= drive()
                self.random_driver.database()
        else:
            exit(0)



class drive(location,driver,user):

    def __init__(self):
        self.temp_name=[]
        self.temp_no=[]
        self.df = open('driver.csv', 'r')
        self.cl = csv.DictReader(self.df)
        for i in self.cl:
            self.temp_name.append(i['Drivername'])
            self.temp_no.append(i['phone_no'])
            self.dic={k:l for k,l in zip(self.temp_name,self.temp_no)}
        self.name_d=random.choice(self.temp_name)
        self.no_d=self.dic[self.name_d]


    def database(self):

        with open('database.csv', 'a', newline='') as csvfile:
            # Create a CSV writer object
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([user.u_name, self.name_d, location.pick, location.drop, location.cost_, location.dist_,location.date,location.time])

        csvread = pd.read_csv('driver.csv')
        rowindex = csvread.loc[csvread['Drivername'] == self.name_d].index[0]
        csvread.loc[rowindex, 'price'] += location.cost_
        csvread.to_csv('driver.csv', index=False)

        print(
            '\N{LARGE GREEN CIRCLE}\N{LARGE GREEN CIRCLE}\N{LARGE GREEN CIRCLE}Here Your Trip Details \N{LARGE GREEN CIRCLE}\N{LARGE GREEN CIRCLE}\N{LARGE GREEN CIRCLE}')
        print('your Driver name is:',self.name_d)
        print('Your Driver Number is:',self.no_d)
        print('Your Cost for Trip is:',location.cost_)
        print('Your Traveling Distances:',location.dist_)
        print('Your Pick-up time is:',location.time)
        print('Your Trip Date is:',location.date)
        print('Feel Free to Call Driver If you Have to Conform Your Trip Details')


def random_genrate():
    user_list=[]
    driver_list=[]
    with open('user.csv','r') as csvfile:
        csvreader=csv.DictReader(csvfile)
        for i in csvreader:
            user_list.append(i['username'])
            #driver_list.append(i['Driver'])

    with open('driver.csv','r') as csvfile:
        csvreader=csv.DictReader(csvfile)
        for i in csvreader:
            driver_list.append(i['Drivername'])
            #driver_list.append(i['Driver'])
    #driver_list=['Tanvi','Maheshbhai','pradeepbhai','Sanjaybhai','Elon','Kunal','Tanmay','Tanasha','Sitara','Agasthya']
    loc_list = ['Manek Chowk, Ahmedabad', 'Sabarmati Ashram, Ahmedabad', 'Kankaria Lake, Ahmedabad',  'Stanza, Ahmedabad',         'courtyard marriott, Ahmedabad', 'Taj Skyline, ahmedabad', 'lal darwaja, ahmedabad', 'Jama Masjid, Ahmedabad',             'LD, Ahmedabad', 'Akshardham Temple, Gandhinagar', 'Vastrapur Lake, Ahmedabad', 'Iskcon Temple, Ahmedabad',             'Science City, Ahmedabad', 'Law Garden, Ahmedabad', 'Sarkhej Roza, Ahmedabad', 'Nehru Bridge, Ahmedabad',    "nirma university, Ahmedabad", 'Iskcon Temple, Ahmedabad', 'PrahladNagar Garden, Ahmedabad', 'shott, Ahmedabad']
    for i in range(100):
        pick,drop=random.sample(loc_list,2)
        point1 = ox.geocode(pick)
        point2 = ox.geocode(drop)
        user=random.choice(user_list)
        driver_var=random.choice(driver_list)
        dist=geodesic(point1, point2).km
        dist=round(dist,2)
        cost=round(20+(dist-1)*20,2)

        t_hl=random.randint(0,23)
        t_ml=random.randint(0,59)
        d_dl=random.randint(1,28)
        d_ml=random.randint(1,11)
        pickup_time=time(t_hl,t_ml)
        trip_date=date(2023,d_ml,d_dl)
        #print(f"distance between {pick} and {drop} is {dist} and cost {cost}")
        with open('database.csv', 'a', newline='') as csvfile:
            # Create a CSV writer object
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([user, driver_var, pick,drop,cost,dist,trip_date,pickup_time])
        csvread = pd.read_csv('driver.csv')
        rowindex = csvread.loc[csvread['Drivername'] == driver_var].index[0]
        csvread.loc[rowindex, 'price'] += cost
        csvread.to_csv('driver.csv', index=False)

obj1=login_main()


class graph:
    def __init__(self):
        print(
            '\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE} Here We have 3 Types Of Graphs\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}')
        #print('Here We have 3 Types Of Graphs:')
        print('1] Scatter Graph Showing Locations v/s their Count of Occuerence:')
        print('2] Pie Chart Showing The Total Count Of Trips Made By Each Driver:')
        print('3] Hist Graph Showing Frequency for Distance Range:')
        self.inu_t = int(input('Enter 1 or 2 or 3 or other key for Exit:'))
        self.dispaly(self.inu_t)

    def dispaly(self,inu_t):
        if inu_t==1:
            random_genrate()
            graph1()
            print('\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE} If you want to show other graphs then click yes Otherwise No:\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}')
            #print('If you want to show other graphs then click yes Otherwise No:')
            self.choice=input('Enter your Choice:')
            if self.choice.lower()=='yes':
                graph.__init__(self)
            else:
                exit(0)
        elif inu_t==2:
            random_genrate()
            graph2()
            print('\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE} If you want to show other graphs then click yes Otherwise No:\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}')
            self.choice = input('Enter your Choice:')
            if self.choice.lower() == 'yes':
                graph.__init__(self)
            else:
                exit(0)
        elif inu_t==3:
            random_genrate()
            graph3()
            print('\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE} If you want to show other graphs then click yes Otherwise No:\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}\N{LARGE BLUE CIRCLE}')
            self.choice = input('Enter your Choice:')
            if self.choice.lower() == 'yes':
                graph.__init__(self)
            else:
                exit(0)
        else:
            exit(0)
g=graph()