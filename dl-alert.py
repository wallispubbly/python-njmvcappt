import requests
import re
import time
from bs4 import BeautifulSoup
from datetime import datetime
import sys
import os
import random

location_arr = ['203', '202', '204', '198', '201', '207', '187', '206', '193', '194', '195', '192', '197', '186']
locationname_arr = ['Oakland', 'Wayne', 'Paterson', 'Lodi', 'North Bergen', 'Randolph', 'Bayonne', 'Rahway', 'South Plainfield', 'Edison', 'Flemginton', 'Eatontown', 'Freehold', 'Bakers Basin']
base_url_link='https://telegov.njportal.com/njmvc/AppointmentWizard/15/'
required_months = ['March','April','May','June']

def beep():
    sys.stdout.write('\a')
    sys.stdout.write('\a')
    sys.stdout.write('\a')
    sys.stdout.write('\a')
    sys.stdout.write('\a')
    sys.stdout.write('\a')

def announce():
    os.system('say "Found MVC appointment"')
    os.system('say "Found MVC appointment"')
    os.system('say "Found MVC appointment"')


def job():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\n\n\nDate Time: ", dt_string, "\n\n")
    i=0
    found=0
    
    
    for location in location_arr:
        print(location)

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        page_html = requests.get(base_url_link+location, headers=headers)
        soup = BeautifulSoup(page_html.text, features="html.parser")
        unavailable=soup.find('div',attrs={'class': 'alert-danger'})
        if unavailable is not None :
            #print('No appointments are available in '+locationname_arr[i])
            dt_string=""
        else:
            dates_html = soup.find('div',attrs={'class': 'col-md-8'})
            date_string = dates_html.find('label',attrs={'class': 'control-label'})
            if set(required_months) & set(date_string.text.split()):
                #print("Matching required months")
                date_string=re.sub('Time of Appointment for ', '', date_string.text)
                date_string=re.sub(':', '', date_string)
                message = 'DL Renew Dates: '+locationname_arr[i]+' / ('+location+') : '+date_string
                print(message)
                print(base_url_link+location)
                announce()
                beep()
                found=1
        i=i+1
        
if __name__ == "__main__": 
    while True:
        time_to_wait = random.randint(5, 54)
        try:
            job()
        except:
            print("Something went wrong")
            time.sleep(time_to_wait)
        else:
            time.sleep(time_to_wait)


    
