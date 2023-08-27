import json
from tkinter import PhotoImage, font
from tkinter.constants import RADIOBUTTON
from typing import Text
import requests
import tkinter as tk
from configparser import ConfigParser, DuplicateOptionError, MissingSectionHeaderError
from tkinter import Label, StringVar, messagebox
from datetime import datetime
from PIL import Image,ImageTk
from urllib import request as urlreq
from io import BytesIO

date_today = datetime.now().date()
date_today_ls = str(date_today).split('-')
date_2 = str(date_today).split('-')[2]
date_2i = int(date_2)+1
date_2_f = str(date_today).replace(date_today_ls[2], str(date_2i))

date_3 = str(date_today).split('-')[2]
date_3i = int(date_3)+2
date_3_f = str(date_today).replace(date_today_ls[2], str(date_3i))

date_4 = str(date_today).split('-')[2]
date_4i = int(date_4)+3
date_4_f = str(date_today).replace(date_today_ls[2], str(date_4i))

date_5 = str(date_today).split('-')[2]
date_5i = int(date_5)+4
date_5_f = str(date_today).replace(date_today_ls[2], str(date_5i))


#config
config_file = ''##mention the path to a config.ini file which contains your api credentials
config = ConfigParser()
config.read(config_file)
api_key = config['owa']['owmapi'] ##replace owa and owmapi with the api key you received from openweathermap.org
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

# weather details
lat =''
long = ''

def generate_tk_image(icon):
    URL = "https://openweathermap.org/img/wn/" + icon +".png"
    u = urlreq.urlopen(URL)
    raw_data = u.read()
    u.close()

    im = Image.open(BytesIO(raw_data))
    im = im.resize((32, 32))
    return ImageTk.PhotoImage(im)

def getweather(city):
    result = requests.get(url.format(city, api_key))
      
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin-273.15  
        weather1 = json['weather'][0]['main']
        icon1 = json['weather'][0]['icon']
        humidity = json['main']['humidity']
        windspd = json['wind']['speed']
        final = [city, country, temp_kelvin, 
                 temp_celsius, weather1,humidity,windspd, icon1]
        global lat,long
        lat = json['coord']['lat']
        long = json['coord']['lon']
        
        return final
        

    else:
        print("NO Content Found")

# search city
weatherlabels=[]
def search():
    city = city_text.get()
    weather = getweather(city)
      
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0].split(',')[0], weather[1]['country'])
        temperature_label['text'] = str(format(weather[3],".1f"))+"   ° Celsius"
        
        humidity_l['text']=str(weather[5])+"%"
        wind_spd['text']=weather[6]
        icon1 = weather[7]

        img = generate_tk_image(icon1)
        weather_l.config(text=weather[4], image = img)
        weather_l["compound"] = tk.LEFT
        weather_l.image = img

        url2="https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=hourly&appid={}"
        dailyreq = requests.get(url2.format(lat,long,api_key))
        dailyreqj=dailyreq.json()

        #day2 modifications
        location_lbl2['text'] = '{} ,{}'.format(weather[0].split(',')[0], weather[1]['country'])
        temperature_label2.config(text=str(format(dailyreqj['daily'][1]['temp']['max'] -273.15,".1f"))+ "   ° Celsius")
        humidity_l2.config(text=str(dailyreqj['daily'][1]['humidity'])+"%") 
        wind_spd2.config(text=dailyreqj['daily'][1]['wind_speed'])

        img = generate_tk_image(dailyreqj['daily'][1]['weather'][0]['icon'])
        weather_l2.config(text=dailyreqj['daily'][1]['weather'][0]['main'], image = img)
        weather_l2["compound"] = tk.LEFT
        weather_l2.image = img

        #day3 mods
        location_lbl3['text'] = '{} ,{}'.format(weather[0].split(',')[0], weather[1]['country'])
        temperature_label3.config(text=str(format(dailyreqj['daily'][2]['temp']['max'] -273.15,".1f"))+ "   ° Celsius")
        humidity_l3.config(text=str(dailyreqj['daily'][2]['humidity'])+"%") 
        wind_spd3.config(text=dailyreqj['daily'][2]['wind_speed'])

        img = generate_tk_image(dailyreqj['daily'][2]['weather'][0]['icon'])
        weather_l3.config(text=dailyreqj['daily'][2]['weather'][0]['main'], image = img)
        weather_l3["compound"] = tk.LEFT
        weather_l3.image = img

        #day4 mods
        location_lbl4['text'] = '{} ,{}'.format(weather[0].split(',')[0], weather[1]['country'])
        temperature_label4.config(text=str(format(dailyreqj['daily'][3]['temp']['max'] -273.15,".1f"))+ "   ° Celsius")
        humidity_l4.config(text=str(dailyreqj['daily'][3]['humidity'])+"%") 
        wind_spd4.config(text=dailyreqj['daily'][3]['wind_speed'])

        img = generate_tk_image(dailyreqj['daily'][3]['weather'][0]['icon'])
        weather_l4.config(text=dailyreqj['daily'][3]['weather'][0]['main'], image = img)
        weather_l4["compound"] = tk.LEFT
        weather_l4.image = img

        #day5 mods
        location_lbl5['text'] = '{} ,{}'.format(weather[0].split(',')[0], weather[1]['country'])
        temperature_label5.config(text=str(format(dailyreqj['daily'][4]['temp']['max'] -273.15,".1f"))+ "   ° Celsius")
        humidity_l5.config(text=str(dailyreqj['daily'][4]['humidity'])+"%") 
        wind_spd5.config(text=dailyreqj['daily'][4]['wind_speed'])

        img = generate_tk_image(dailyreqj['daily'][4]['weather'][0]['icon'])
        weather_l5.config(text=dailyreqj['daily'][4]['weather'][0]['main'], image = img)
        weather_l5["compound"] = tk.LEFT
        weather_l5.image = img
        # print('\n',weather)
          
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))


window = tk.Tk()
window.config(bg="#FFEDED")
window.title("Weather window")
window.geometry('1000x500')
city_text = StringVar()
cityentry = tk.Entry(window,textvariable=city_text)
cityentry.grid(row=0,column=2,padx=80,pady=20)
Search_btn = tk.Button(window, text="Search Weather",width=12, command=search)
Search_btn.grid(row=0,column=3)  
location_lbl = tk.Label(window, text="                 ", font={'bold', 20},bg='#FFF9F9')
location_lbl.grid(row=2,column=2,pady=20,padx=0)
temperature_label = tk.Label(window, text="                       ",bg='#FFF9F9')
temperature_label.grid(row=3,column=2,pady=20,padx=0)
weather_l = tk.Label(window, text="                        ",bg='#FFF9F9')
weather_l.grid(row=4,column=2,pady=20,padx=0)
humidity_l = tk.Label(window,text="                  ",font={'bold',20},bg='#FFF9F9')
humidity_l.grid(row=5,column=2,pady=20,padx=0)
wind_spd = tk.Label(window,text="                 ",font={'bold',20},bg='#FFF9F9')
wind_spd.grid(row=6,column=2,pady=20)
l_lbl = tk.Label(window, text="Location : ",bg='#FFF9F9')
l_lbl.grid(row=2,column=1,pady=20)
t_lbl = tk.Label(window, text="Temperature : ",bg='#FFF9F9')
t_lbl.grid(row=3,column=1,pady=20)
w_lbl = tk.Label(window, text="Weather Info : ",bg='#FFF9F9')
w_lbl.grid(row=4,column=1,pady=20)
h_lbl = tk.Label(window,text="Humidity : ",bg='#FFF9F9')
h_lbl.grid(row=5,column=1,pady=20,padx=0)
ws_lbl = tk.Label(window,text="Wind speed : ",bg='#FFF9F9')
ws_lbl.grid(row=6,column=1,pady=20)
#date labels
present_label = tk.Label(window,text=date_today,bg="#FFEDED")
present_label.grid(row=1,column=2)

#DAY2------------------------------------------------------
day2 = tk.Label(window,text=date_2_f,bg="#FFEDED")
day2.grid(row=1,column=3)
location_lbl2 = tk.Label(window, text="                 ", font={'bold', 20},bg='#FFF9F9')
location_lbl2.grid(row=2,column=3,pady=20,padx=0)
temperature_label2 = tk.Label(window, text="                       ",bg='#FFF9F9')
temperature_label2.grid(row=3,column=3,pady=20,padx=0)
weather_l2 = tk.Label(window, text="                        ",bg='#FFF9F9')
weather_l2.grid(row=4,column=3,pady=20,padx=0)
humidity_l2 = tk.Label(window,text="                  ",font={'bold',20},bg='#FFF9F9')
humidity_l2.grid(row=5,column=3,pady=20,padx=0)
wind_spd2 = tk.Label(window,text="                 ",font={'bold',20},bg='#FFF9F9')
wind_spd2.grid(row=6,column=3,pady=20)
#DAY3--------------------------------------------------------
day3 = tk.Label(window,text=date_3_f,bg="#FFEDED",padx=40)
day3.grid(row=1,column=4)
location_lbl3 = tk.Label(window, text="                 ", font={'bold', 20},bg='#FFF9F9')
location_lbl3.grid(row=2,column=4,pady=20,padx=0)
temperature_label3 = tk.Label(window, text="                       ",bg='#FFF9F9')
temperature_label3.grid(row=3,column=4,pady=20,padx=0)
weather_l3 = tk.Label(window, text="                        ",bg='#FFF9F9')
weather_l3.grid(row=4,column=4,pady=20,padx=0)
humidity_l3 = tk.Label(window,text="                  ",font={'bold',20},bg='#FFF9F9')
humidity_l3.grid(row=5,column=4,pady=20,padx=0)
wind_spd3 = tk.Label(window,text="                 ",font={'bold',20},bg='#FFF9F9')
wind_spd3.grid(row=6,column=4,pady=20)

#DAY4----------------------------------------------------------

day4 = tk.Label(window,text=date_4_f,bg="#FFEDED",padx=20)
day4.grid(row=1,column=5)

location_lbl4 = tk.Label(window, text="                 ", font={'bold', 20},bg='#FFF9F9')
location_lbl4.grid(row=2,column=5,pady=20,padx=0)
temperature_label4 = tk.Label(window, text="                       ",bg='#FFF9F9')
temperature_label4.grid(row=3,column=5,pady=20,padx=0)
weather_l4 = tk.Label(window, text="                        ",bg='#FFF9F9')
weather_l4.grid(row=4,column=5,pady=20,padx=0)
humidity_l4 = tk.Label(window,text="                  ",font={'bold',20},bg='#FFF9F9')
humidity_l4.grid(row=5,column=5,pady=20,padx=0)
wind_spd4 = tk.Label(window,text="                 ",font={'bold',20},bg='#FFF9F9')
wind_spd4.grid(row=6,column=5,pady=20)

#DAY5------------------------------------------------------------
day5 = tk.Label(window,text=date_5_f,bg="#FFEDED",padx=40)
day5.grid(row=1,column=6)
location_lbl5 = tk.Label(window, text="                 ", font={'bold', 20},bg='#FFF9F9')
location_lbl5.grid(row=2,column=6,pady=20,padx=0)
temperature_label5 = tk.Label(window, text="                       ",bg='#FFF9F9')
temperature_label5.grid(row=3,column=6,pady=20,padx=0)
weather_l5 = tk.Label(window, text="                        ",bg='#FFF9F9')
weather_l5.grid(row=4,column=6,pady=20,padx=0)
humidity_l5 = tk.Label(window,text="                  ",font={'bold',20},bg='#FFF9F9')
humidity_l5.grid(row=5,column=6,pady=20,padx=0)
wind_spd5 = tk.Label(window,text="                 ",font={'bold',20},bg='#FFF9F9')
wind_spd5.grid(row=6,column=6,pady=20)


img = Image.open('<Enter your logo here>') ##enter a logo of your brand of your choice
img=img.resize((590,60),Image.ANTIALIAS)
img=ImageTk.PhotoImage(img)
wforecast = tk.Label(window,image=img,bg="#FFEDED",highlightthickness=0,fg="#FFEDED")
wforecast.grid(row=7,column=2,columnspan=5)
#geometry 
window.mainloop()

