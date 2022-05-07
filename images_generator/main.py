import json
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import sys
import math
import re
import random
import string
import requests
import urllib

if os.path.exists("thumbnails") == False:
    with open('series.txt','r') as f:
        thing = f.read().splitlines()
    with open('series.json','r') as f:
        series = json.load(f)
    os.mkdir("thumbnails")
    for i in range(0,math.ceil(len(thing)/20.0)):
        random_string = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(32))
        song = thing[1+20*i]
        series['series'][song] = {}
        series['series'][song]['anime'] = re.sub("\t","",thing[0+20*i])
        series['series'][song]['song'] = re.sub("\t","",thing[1+20*i])
        series['series'][song]['season'] = re.sub("\t","",thing[2+20*i])
        series['series'][song]['popularity'] = re.sub("\t","",thing[3+20*i])
        series['series'][song]['album'] = re.sub("\t","",thing[4+20*i])
        series['series'][song]['vocal'] = re.sub("\t","",thing[5+20*i])
        series['series'][song]['lyrics'] = re.sub("\t","",thing[6+20*i])
        series['series'][song]['note1'] = re.sub("\t","",thing[7+20*i])
        series['series'][song]['note2'] = re.sub("\t","",thing[8+20*i])
        series['series'][song]['note3'] = re.sub("\t","",thing[9+20*i])
        series['series'][song]['note4'] = re.sub("\t","",thing[10+20*i])
        series['series'][song]['note5'] = re.sub("\t","",thing[11+20*i])
        series['series'][song]['note6'] = re.sub("\t","",thing[12+20*i])
        series['series'][song]['note7'] = re.sub("\t","",thing[13+20*i])
        series['series'][song]['note8'] = re.sub("\t","",thing[14+20*i])
       
        soma = float(series['series'][song]['note1'])+float(series['series'][song]['note2'])+float(series['series'][song]['note3'])+float(series['series'][song]['note4'])+float(series['series'][song]['note5'])+float(series['series'][song]['note6'])+float(series['series'][song]['note7'])+float(series['series'][song]['note8'])
        series['series'][song]['average'] = soma/8
        cover = re.sub("\t","",thing[18+20*i])
        image = requests.get(cover,allow_redirects=True)
        filename = "cover_"+random_string+".png"
        open(f"thumbnails/{filename}".format("cover_"),'wb').write(image.content)
        series['series'][song]['cover'] = filename
        cover = re.sub("\t","",thing[19+20*i])
        image = requests.get(cover,allow_redirects=True)
        open(f"thumbnails/{filename}".format("cover_"),'wb').write(image.content)
        print("finished {}".format(song))

    with open('series2.json','w') as f:
        json.dump(series,f,indent=4)
else:
    with open('series2.json','r') as f:
        series = json.load(f)

sorted_series_names = sorted(series['series'], key=lambda x:(series['series'][x]['anime']), reverse=False)
sorted_series = series
series = {}
series['series'] = {}
series['participants'] = sorted_series['participants']
for song in sorted_series_names:
    series['series'][song] = sorted_series['series'][song]
sorted_series_names = sorted(series['series'], key=lambda x:(series['series'][x]['average']), reverse=True)
sorted_series = series
series = {}
series['series'] = {}
series['participants'] = sorted_series['participants']
for song in sorted_series_names:
    series['series'][song] = sorted_series['series'][song]
    
size = 1920,1080
place = 1
font = 'Raleway-Light.ttf'
font2 = 'Raleway-SemiBold.ttf'
for song in series["series"]:
    image = Image.new('RGBA', size, color ='#00000000')
    text = ImageDraw.Draw(image)
    font48 = ImageFont.truetype(font, 48)
    font60 = ImageFont.truetype(font, 60)
    font36 = ImageFont.truetype(font, 36)
    font24 = ImageFont.truetype(font, 24)
    font22 = ImageFont.truetype(font, 22)
    font482 = ImageFont.truetype(font2, 48)
    font602 = ImageFont.truetype(font2, 60)
    font362 = ImageFont.truetype(font2, 36)
    font242 = ImageFont.truetype(font2, 24)
    font222 = ImageFont.truetype(font2, 22)
    
    aa = series["series"][song]["song"]
    print(str(aa.encode('utf-8')))
    
    text.text((195,1029),series['series'][song]['anime'], fill=(255,255,255), font=font482, anchor='lm') #anime name
    text.text((195,960),series["series"][song]["song"], fill=(255,244,79), font=font482, anchor='lm') # song name
    text.text((51,50),"Winter 2022 Anime Openings", fill=(255,255,255), font=font242, anchor='ld')

    avg = round(series["series"][song]["average"],3)
    show_avg = round(series["series"][song]["average"],2)
    text.text((113,839),str(place), fill=(255,255,255), font=font60, anchor='mm')
    colors = [(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255)]
    colors_note = [(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255)]
    average_note = (255,255,255)

    soma2 = float(series['series'][song]['note1'])+float(series['series'][song]['note2'])+float(series['series'][song]['note3'])+float(series['series'][song]['note4'])+float(series['series'][song]['note5'])+float(series['series'][song]['note6'])+float(series['series'][song]['note7'])+float(series['series'][song]['note8'])
    random_number = -30
    random_number2 = 51
    border = (2, 2, 2, 2)
    
    text.text((1600,62),"Average: {}".format(round(soma2/8, 2)), fill=average_note, font=font36, anchor='mm')
    #1
    text.text((1661+random_number2,70+190+random_number),series["participants"][0], fill=colors[0], font=font242, anchor='mm')
    text.text((1661+random_number2,70+25+190+random_number),series["series"][song]["note1"], fill=colors_note[0], font=font242, anchor='mm')

    par1Img = Image.open("./participants_images/{}.png".format(series["participants"][0]))
    par1Img = par1Img.convert('RGB')
    par1Img = par1Img.resize((128,128), Image.Resampling.LANCZOS)
    par1Img = ImageOps.expand(par1Img, border=border, fill="#ffffff")
    image.paste(par1Img, (1661-14,70+190+random_number-142))
    
    #2
    text.text((1661+random_number2,70+190+190+random_number),series["participants"][1], fill=colors[1], font=font242, anchor='mm')
    text.text((1661+random_number2,70+25+190+190+random_number),series["series"][song]["note2"], fill=colors_note[1], font=font242, anchor='mm')
    
    par2Img = Image.open("./participants_images/{}.png".format(series["participants"][1]))
    par2Img = par2Img.convert('RGB')
    par2Img = par2Img.resize((128,128), Image.Resampling.LANCZOS)
    par2Img = ImageOps.expand(par2Img, border=border, fill="#ffffff")
    image.paste(par2Img, (1661-14,70+190+190+random_number-142))
    #3
    text.text((1661+random_number2,70+190+190+190+random_number),series["participants"][2], fill=colors[2], font=font242, anchor='mm')
    text.text((1661+random_number2,70+25+190+190+190+random_number),series["series"][song]["note3"], fill=colors_note[2], font=font242, anchor='mm')
    
    par3Img = Image.open("./participants_images/{}.png".format(series["participants"][2]))
    par3Img = par3Img.convert('RGB')
    par3Img = par3Img.resize((128,128), Image.Resampling.LANCZOS)
    par3Img = ImageOps.expand(par3Img, border=border, fill="#ffffff")
    image.paste(par3Img, (1661-14,70+190+190+190+random_number-142))
    #4
    text.text((1661+random_number2,70+190+190+190+190+random_number),series["participants"][3], fill=colors[3], font=font242, anchor='mm')
    text.text((1661+random_number2,70+25+190+190+190+190+random_number),series["series"][song]["note4"], fill=colors_note[3], font=font242, anchor='mm')
    
    par4Img = Image.open("./participants_images/{}.png".format(series["participants"][3]))
    par4Img = par4Img.convert('RGB')
    par4Img = par4Img.resize((128,128), Image.Resampling.LANCZOS)
    par4Img = ImageOps.expand(par4Img, border=border, fill="#ffffff")
    image.paste(par4Img, (1661-14,70+190+190+190+190+random_number-142))
    #5
    text.text((1503+random_number2,70+190+random_number),series["participants"][4], fill=colors[4], font=font242, anchor='mm')
    text.text((1503+random_number2,70+25+190+random_number),series["series"][song]["note5"], fill=colors_note[4], font=font242, anchor='mm')
    
    par5Img = Image.open("./participants_images/{}.png".format(series["participants"][4]))
    par5Img = par5Img.convert('RGB')
    par5Img = par5Img.resize((128,128), Image.Resampling.LANCZOS)
    par5Img = ImageOps.expand(par5Img, border=border, fill="#ffffff")
    image.paste(par5Img, (1503-14, 70+190+random_number-142))
    #6
    text.text((1503+random_number2,70+190+190+random_number),series["participants"][5], fill=colors[5], font=font242, anchor='mm')
    text.text((1503+random_number2,70+25+190+190+random_number),series["series"][song]["note6"], fill=colors_note[5], font=font242, anchor='mm')
    
    par6Img = Image.open("./participants_images/{}.png".format(series["participants"][5]))
    par6Img = par6Img.convert('RGB')
    par6Img = par6Img.resize((128,128), Image.Resampling.LANCZOS)
    par6Img = ImageOps.expand(par6Img, border=border, fill="#ffffff")
    image.paste(par6Img, (1503-14, 70+190+190+random_number-142))
    
    #7
    text.text((1503+random_number2,70+190+190+190+random_number),series["participants"][6], fill=colors[6], font=font242, anchor='mm')
    text.text((1503+random_number2,70+25+190+190+190+random_number),series["series"][song]["note7"], fill=colors_note[6], font=font242, anchor='mm')
    
    par7Img = Image.open("./participants_images/{}.png".format(series["participants"][5]))
    par7Img = par7Img.convert('RGB')
    par7Img = par7Img.resize((128,128), Image.Resampling.LANCZOS)
    par7Img = ImageOps.expand(par7Img, border=border, fill="#ffffff")
    image.paste(par7Img, (1503-14, 70+190+190+190+random_number-142))
    #8
    text.text((1503+random_number2,70+190+190+190+190+random_number),series["participants"][7], fill=colors[7], font=font242, anchor='mm')
    text.text((1503+random_number2,70+25+190+190+190+190+random_number),series["series"][song]["note8"], fill=colors_note[7], font=font242, anchor='mm')

    par8Img = Image.open("./participants_images/{}.png".format(series["participants"][6]))
    par8Img = par8Img.convert('RGB')
    par8Img = par8Img.resize((128,128), Image.Resampling.LANCZOS)
    par8Img = ImageOps.expand(par8Img, border=border, fill="#ffffff")
    image.paste(par8Img, (1503-14, 70+190+190+190+190+random_number-142))

    cover = Image.open("./thumbnails/{}".format(series["series"][song]["cover"]))
    cover = cover.convert('RGB')
    cover = cover.resize((131,184), Image.Resampling.LANCZOS)
    image.paste(cover,(50,873))
    image.save(f"out/{place}.png")
    place+=1
