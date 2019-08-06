#!/usr/bin/env python
import requests 
import sys 
import unicodedata
import imdb
import re
import numpy as np
from bs4 import BeautifulSoup

class0 = 'ipl-status-pill '
class1 = 'ipl-status-pill ipl-status-pill--ok'
class2 = 'ipl-status-pill ipl-status-pill--warning'
class3 = 'ipl-status-pill ipl-status-pill--critical'


sex_and_nudity_level = ""
violence_and_gore_level =""
profanity_level = ""
alcohol_drugs_and_smoking_level = ""
frightening_and_intense_level = ""

sex_and_nudity_scenes = []
violence_and_gore_scenes =[]
profanity_scenes = []
alcohol_drugs_and_smoking_scenes = []
frightening_and_intense_scenes = []

def count(list):
  item_count = 0
  for item in list[:]:
    item_count += 1
  return item_count


ia = imdb.IMDb()
movie = str(sys.argv[1])
m = ia.search_movie(movie)


website = "https://www.imdb.com/title/tt"+str(m[0].movieID)+"/parentalguide"
page = requests.get(website)
soup = BeautifulSoup(page.content,'html.parser')


#------ SEX AND NUDITY -----------------

for l in soup.find_all(id='advisory-nudity'):
    if(str(soup.find('span',class_=class0).get_text()) == 'None'):
    	sex_and_nudity_level = "None"
    for o in l.find_all('span',{'class': [class1,class2,class3]}):
        sex_and_nudity_level = str(o.text) 

for ultag in soup.find_all(id='advisory-nudity'):
    for litag in ultag.find_all('li',class_='ipl-zebra-list__item'):
        sex_and_nudity_scenes.append(str(litag.text))

for lol in range(0,count(sex_and_nudity_scenes)):
    sex_and_nudity_scenes[lol].strip()
    sex_and_nudity_scenes[lol] = " ".join(sex_and_nudity_scenes[lol].split())
    sex_and_nudity_scenes[lol] = sex_and_nudity_scenes[lol].replace('Edit','')

# ---------- VIOLENCE AND GORE -------------------

for q in soup.find_all(id='advisory-violence'):
    if(str(soup.find('span',class_=class0).get_text()) == 'None'):
    	violence_and_gore_level = "None"
    for w in q.find_all('span',{'class': [class1,class2,class3]}):
        violence_and_gore_level = str(w.text) 

for ultag_v in soup.find_all(id='advisory-violence'):
    for litag_v in ultag_v.find_all('li',class_='ipl-zebra-list__item'):
        violence_and_gore_scenes.append(str(litag_v.text))

for lol_v in range(0,count(violence_and_gore_scenes)):
    violence_and_gore_scenes[lol_v].strip()
    violence_and_gore_scenes[lol_v] = " ".join(violence_and_gore_scenes[lol_v].split())
    violence_and_gore_scenes[lol_v] = violence_and_gore_scenes[lol_v].replace('Edit','')

#------PROFANITY--------

for q_p in soup.find_all(id='advisory-profanity'):
    if(str(soup.find('span',class_=class0).get_text()) == 'None'):
    	profanity_level = "None"
    for w_p in q_p.find_all('span',{'class': [class1,class2,class3]}):
        profanity_level = str(w_p.text) 

for ultag_p in soup.find_all(id='advisory-profanity'):
    for litag_p in ultag_p.find_all('li',class_='ipl-zebra-list__item'):
        profanity_scenes.append(str(litag_p.text))

for lol_p in range(0,count(profanity_scenes)):
    profanity_scenes[lol_p].strip()
    profanity_scenes[lol_p] = " ".join(profanity_scenes[lol_p].split())
    profanity_scenes[lol_p] = profanity_scenes[lol_p].replace('Edit','')

#-----ALCOHOL DRUGS AND SMOKE-------

for q_a in soup.find_all(id='advisory-alcohol'):
    if(str(soup.find('span',class_=class0).get_text()) == 'None'):
    	alcohol_drugs_and_smoking_level = "None"
    for w_a in q_a.find_all('span',{'class': [class1,class2,class3]}):
        alcohol_drugs_and_smoking_level = str(w_a.text) 

for ultag_a in soup.find_all(id='advisory-alcohol'):
    for litag_a in ultag_a.find_all('li',class_='ipl-zebra-list__item'):
        alcohol_drugs_and_smoking_scenes.append(str(litag_a.text))

for lol_a in range(0,count(alcohol_drugs_and_smoking_scenes)):
    alcohol_drugs_and_smoking_scenes[lol_a].strip()
    alcohol_drugs_and_smoking_scenes[lol_a] = " ".join(alcohol_drugs_and_smoking_scenes[lol_a].split())
    alcohol_drugs_and_smoking_scenes[lol_a] = alcohol_drugs_and_smoking_scenes[lol_a].replace('Edit','')







print "Movie is: "+ m[0]['title']+"\n"

print "Sex and Nudity Level: "+str(sex_and_nudity_level) + "\n" 
print sex_and_nudity_scenes 

print "\n"

print "Violence and Gore Level: "+str(violence_and_gore_level) + "\n" 
print violence_and_gore_scenes

print "\n"

print "Profanity Level: "+str(profanity_level) + "\n" 
print profanity_scenes

print "\n"

print "Alcohol, Drugs and Smoking Level: "+str(alcohol_drugs_and_smoking_level) + "\n" 
print alcohol_drugs_and_smoking_scenes











