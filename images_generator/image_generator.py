import json
from PIL import Image, ImageDraw, ImageFont, ImageOps

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

    place = len(series["series"])
    count = 1
    
    # FONTES / FONTES-SIZE
    font = RALEWAY_LIGHT_PATH
    font2 = RALEWAY_SEMI_PATH
    font36 = ImageFont.truetype(font, 36)
    font60 = ImageFont.truetype(font, 60)
    font242 = ImageFont.truetype(font2, 24)
    font362 = ImageFont.truetype(font2, 36)
    font482 = ImageFont.truetype(font2, 48)
    # / FONTES / FONTES-SIZE
    
    clear_null = list(filter(None, series['participants'])) # removendo participantes null
    clear_null = len(set(clear_null)) # numero de participantes nao-null
    
    for song in series["series"]:
        image = Image.new('RGBA', (1920,1080), color ='#00000000')
        text = ImageDraw.Draw(image)
        print(str(series["series"][song]["song"].encode('utf-8')))

        text.text((195,1029),series['series'][song]['anime'], fill=(255,255,255), font=font482, anchor='lm') #anime name
        text.text((195,960),series["series"][song]["song"], fill=(255,244,79), font=font482, anchor='lm') # song name
        text.text((195,891),series["series"][song]["type"], fill=(255,244,79), font=font362, anchor='lm') # type
        text.text((51,80),title, fill=(255,255,255), font=font242, anchor='ld')

        text.text((113,839),str(count), fill=(255,255,255), font=font60, anchor='mm')
        colors = [(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255)]
        colors_note = [(255,255,255),(255,0,0),(0,255,0)]
        average_note = (24,249,248)

        random_number = -30
        random_number2 = 51
        border = (2, 2, 2, 2)

        PIXELS_POSITION_NICK = {
            0: (1661+random_number2,70+190+random_number),
            1: (1661+random_number2,70+190+190+random_number),
            2: (1661+random_number2,70+190+190+190+random_number),
            3: (1661+random_number2,70+190+190+190+190+random_number),
            4: (1503+random_number2,70+190+random_number),
            5: (1503+random_number2,70+190+190+random_number),
            6: (1503+random_number2,70+190+190+190+random_number),
            7: (1503+random_number2,70+190+190+190+190+random_number)
        }
        PIXELS_POSITION_NOTE = {
            0: (1661+random_number2,70+25+190+random_number),
            1: (1661+random_number2,70+25+190+190+random_number),
            2: (1661+random_number2,70+25+190+190+190+random_number),
            3: (1661+random_number2,70+25+190+190+190+190+random_number),
            4: (1503+random_number2,70+25+190+random_number),
            5: (1503+random_number2,70+25+190+190+random_number),
            6: (1503+random_number2,70+25+190+190+190+random_number),
            7: (1503+random_number2,70+25+190+190+190+190+random_number)
        }
        PIXELS_POSITION_IMAGE = {
            0: (1661-14,70+190+random_number-142),
            1: (1661-14,70+190+190+random_number-142),
            2: (1661-14,70+190+190+190+random_number-142),
            3: (1661-14,70+190+190+190+190+random_number-142),
            4: (1503-14, 70+190+random_number-142),
            5: (1503-14, 70+190+190+random_number-142),
            6: (1503-14, 70+190+190+190+random_number-142),
            7: (1503-14, 70+190+190+190+190+random_number-142)
        }
        
        text.rectangle(((49, 87), (1330, 808)), outline ="white") # el retangulo

        menor = -1
        maior = -1
        m = -1
        mn = 999
        soma = 0
        for h in range(clear_null): # ENCONTRA MENOR E MAIOR NOTA
            nota = float(series["series"][song]["notes"][h])
            soma += nota
            if(nota > m):
                maior = h
                m = nota
            if(nota < mn):
                menor = h
                mn = nota
        text.text((1600,62),"Average: {}".format(round(soma/clear_null, 2)), fill=average_note, font=font36, anchor='mm')
        for h in range(clear_null):
            nota = series["series"][song]["notes"][h]
            participante = series["participants"][h]
            cor = 0
            if h == menor:
                cor = 1
            elif h == maior:
                cor = 2
            text.text(PIXELS_POSITION_NICK[h], participante, fill=colors[h], font=font242, anchor='mm')
            text.text(PIXELS_POSITION_NOTE[h], nota, fill=colors_note[cor], font=font242, anchor='mm')
            parImg = Image.open(PARTICIPANTS_PATH+"/{}.png".format(participante))
            parImg = parImg.convert('RGB')
            parImg = parImg.resize((128,128), Image.Resampling.LANCZOS)
            parImg = ImageOps.expand(parImg, border=border, fill="#ffffff")
            image.paste(parImg, PIXELS_POSITION_IMAGE[h])

        cover = Image.open(THUMBNAIL_PATH+"/{}".format(series["series"][song]["cover"])).convert('RGB').resize((131,184), Image.Resampling.LANCZOS)
        image.paste(cover,(50,873))
        image.save(f"{SAVE_PATH}/{place}.png")
        place -= 1
        count += 1