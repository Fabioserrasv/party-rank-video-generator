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

google = True

THUMBNAIL_PATH = "./images_generator/thumbnails"
JSON_PATH = "./images_generator/series2.json"
RALEWAY_LIGHT_PATH = "./images_generator/Raleway-Light.ttf"
RALEWAY_SEMI_PATH = "./images_generator/Raleway-SemiBold.ttf"
PARTICIPANTS_PATH = "./images_generator/participants_images"
SAVE_PATH = "images"
if(google == True):
  THUMBNAIL_PATH = "/content/party-rank-video-generator/images_generator/thumbnails"
  JSON_PATH = "/content/party-rank-video-generator/images_generator/series2.json"
  RALEWAY_LIGHT_PATH = "/content/party-rank-video-generator/images_generator/Raleway-Light.ttf"
  RALEWAY_SEMI_PATH = "/content/party-rank-video-generator/images_generator/Raleway-SemiBold.ttf"
  PARTICIPANTS_PATH = "/content/party-rank-video-generator/images_generator/participants_images"
  SAVE_PATH = "/content/drive/MyDrive/images_party_rank"

def generate_images():
    with open(JSON_PATH,'r') as f:
        series = json.load(f)

    sorted_series_names = sorted(series['series'], key=lambda x:(series['series'][x]['anime']), reverse=False)
    sorted_series = series
    title = series["title"]
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
    place = len(series["series"])
    count = 1
    font = RALEWAY_LIGHT_PATH
    font2 = RALEWAY_SEMI_PATH
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
        
        print(str(series["series"][song]["song"].encode('utf-8')))

        text.text((195,1029),series['series'][song]['anime'], fill=(255,255,255), font=font482, anchor='lm') #anime name
        text.text((195,960),series["series"][song]["song"], fill=(255,244,79), font=font482, anchor='lm') # song name
        text.text((51,80),title, fill=(255,255,255), font=font242, anchor='ld')

        text.text((113,839),str(count), fill=(255,255,255), font=font60, anchor='mm')
        colors = [(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255)]
        colors_note = [(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255)]
        average_note = (24,249,248)

        soma2 = float(series['series'][song]['note1'])+float(series['series'][song]['note2'])+float(series['series'][song]['note3'])+float(series['series'][song]['note4'])+float(series['series'][song]['note5'])+float(series['series'][song]['note6'])+float(series['series'][song]['note7'])+float(series['series'][song]['note8'])
        random_number = -30
        random_number2 = 51
        border = (2, 2, 2, 2)
        
        text.text((1600,62),"Average: {}".format(round(soma2/8, 2)), fill=average_note, font=font36, anchor='mm')
        #1
        text.text((1661+random_number2,70+190+random_number),series["participants"][0], fill=colors[0], font=font242, anchor='mm')
        text.text((1661+random_number2,70+25+190+random_number),series["series"][song]["note1"], fill=colors_note[0], font=font242, anchor='mm')

        par1Img = Image.open(PARTICIPANTS_PATH+"/{}.png".format(series["participants"][0]))
        par1Img = par1Img.convert('RGB')
        par1Img = par1Img.resize((128,128), Image.Resampling.LANCZOS)
        par1Img = ImageOps.expand(par1Img, border=border, fill="#ffffff")
        image.paste(par1Img, (1661-14,70+190+random_number-142))
        
        #2
        text.text((1661+random_number2,70+190+190+random_number),series["participants"][1], fill=colors[1], font=font242, anchor='mm')
        text.text((1661+random_number2,70+25+190+190+random_number),series["series"][song]["note2"], fill=colors_note[1], font=font242, anchor='mm')
        
        par2Img = Image.open(PARTICIPANTS_PATH+"/{}.png".format(series["participants"][1]))
        par2Img = par2Img.convert('RGB')
        par2Img = par2Img.resize((128,128), Image.Resampling.LANCZOS)
        par2Img = ImageOps.expand(par2Img, border=border, fill="#ffffff")
        image.paste(par2Img, (1661-14,70+190+190+random_number-142))
        #3
        text.text((1661+random_number2,70+190+190+190+random_number),series["participants"][2], fill=colors[2], font=font242, anchor='mm')
        text.text((1661+random_number2,70+25+190+190+190+random_number),series["series"][song]["note3"], fill=colors_note[2], font=font242, anchor='mm')
        
        par3Img = Image.open(PARTICIPANTS_PATH+"/{}.png".format(series["participants"][2]))
        par3Img = par3Img.convert('RGB')
        par3Img = par3Img.resize((128,128), Image.Resampling.LANCZOS)
        par3Img = ImageOps.expand(par3Img, border=border, fill="#ffffff")
        image.paste(par3Img, (1661-14,70+190+190+190+random_number-142))
        #4
        text.text((1661+random_number2,70+190+190+190+190+random_number),series["participants"][3], fill=colors[3], font=font242, anchor='mm')
        text.text((1661+random_number2,70+25+190+190+190+190+random_number),series["series"][song]["note4"], fill=colors_note[3], font=font242, anchor='mm')
        
        par4Img = Image.open(PARTICIPANTS_PATH+"/{}.png".format(series["participants"][3]))
        par4Img = par4Img.convert('RGB')
        par4Img = par4Img.resize((128,128), Image.Resampling.LANCZOS)
        par4Img = ImageOps.expand(par4Img, border=border, fill="#ffffff")
        image.paste(par4Img, (1661-14,70+190+190+190+190+random_number-142))
        #5
        text.text((1503+random_number2,70+190+random_number),series["participants"][4], fill=colors[4], font=font242, anchor='mm')
        text.text((1503+random_number2,70+25+190+random_number),series["series"][song]["note5"], fill=colors_note[4], font=font242, anchor='mm')
        
        par5Img = Image.open(PARTICIPANTS_PATH+"/{}.png".format(series["participants"][4]))
        par5Img = par5Img.convert('RGB')
        par5Img = par5Img.resize((128,128), Image.Resampling.LANCZOS)
        par5Img = ImageOps.expand(par5Img, border=border, fill="#ffffff")
        image.paste(par5Img, (1503-14, 70+190+random_number-142))
        #6
        text.text((1503+random_number2,70+190+190+random_number),series["participants"][5], fill=colors[5], font=font242, anchor='mm')
        text.text((1503+random_number2,70+25+190+190+random_number),series["series"][song]["note6"], fill=colors_note[5], font=font242, anchor='mm')
        
        par6Img = Image.open(PARTICIPANTS_PATH+"/{}.png".format(series["participants"][5]))
        par6Img = par6Img.convert('RGB')
        par6Img = par6Img.resize((128,128), Image.Resampling.LANCZOS)
        par6Img = ImageOps.expand(par6Img, border=border, fill="#ffffff")
        image.paste(par6Img, (1503-14, 70+190+190+random_number-142))
        
        #7
        text.text((1503+random_number2,70+190+190+190+random_number),series["participants"][6], fill=colors[6], font=font242, anchor='mm')
        text.text((1503+random_number2,70+25+190+190+190+random_number),series["series"][song]["note7"], fill=colors_note[6], font=font242, anchor='mm')
        
        par7Img = Image.open(PARTICIPANTS_PATH+"/{}.png".format(series["participants"][6]))
        par7Img = par7Img.convert('RGB')
        par7Img = par7Img.resize((128,128), Image.Resampling.LANCZOS)
        par7Img = ImageOps.expand(par7Img, border=border, fill="#ffffff")
        image.paste(par7Img, (1503-14, 70+190+190+190+random_number-142))
        #8
        text.text((1503+random_number2,70+190+190+190+190+random_number),series["participants"][7], fill=colors[7], font=font242, anchor='mm')
        text.text((1503+random_number2,70+25+190+190+190+190+random_number),series["series"][song]["note8"], fill=colors_note[7], font=font242, anchor='mm')

        par8Img = Image.open(PARTICIPANTS_PATH+"/{}.png".format(series["participants"][7]))
        par8Img = par8Img.convert('RGB')
        par8Img = par8Img.resize((128,128), Image.Resampling.LANCZOS)
        par8Img = ImageOps.expand(par8Img, border=border, fill="#ffffff")
        image.paste(par8Img, (1503-14, 70+190+190+190+190+random_number-142))

        cover = Image.open(THUMBNAIL_PATH+"/{}".format(series["series"][song]["cover"]))
        cover = cover.convert('RGB')
        cover = cover.resize((131,184), Image.Resampling.LANCZOS)
        image.paste(cover,(50,873))
        image.save(f"{SAVE_PATH}/{place}.png")
        place -= 1
        count += 1