from PIL import Image, ImageDraw, ImageOps
from pathlib import Path
from io import BytesIO
from config import Config
from entities.colors import Colors
from entities.fonts import Fonts
from entities.song import Song
from entities.participant import Participant
from .pixels_position import getPixels
import requests

class ImageGenerator:
  def __init__(self, data : str):
    self._title = data["title"]
    self.songs = []
    self.participants_name = data['participants']
    self.pixels = getPixels(len(self.participants_name))
    self.__check_images(self.participants_name)
    series = data['series']
    for serie in series:
      participants = []
      for index, p in enumerate(series[serie]['notes']):
        participant = Participant(self.participants_name[index], p)
        participants.append(participant)
      participants.sort(key=lambda x: x.get_grade(), reverse=False)
      song = Song(serie, series[serie]['type'], series[serie]['song'], participants, series[serie]['average'], series[serie]['cover'])
      self.songs.append(song)

  def generate_images(self) -> bool:
    for index, song in enumerate(self.songs):
      self.__generate_image(song, f'{str(index)}.png')
    return True
  
  def __generate_image(self, song: Song, file_name: str):
    (song.get_participants_name())
    image = Image.new('RGBA', (1920, 1080), color='#00000000')
    self.__place_info_text_in_image(song.get_name(), song.get_song(), song.get_type(), self._title, image)
    self.__place_white_rectangle_as_border(image)
    self.__place_average_grade(song.get_average(), image)
    self.__place_participants_images(song.get_participants(), image)
    image.save(f"{Config.SAVE_PATH}/{file_name}")

  def __place_participants_images(self, particpants: list, image: Image) -> ImageDraw:
    draw = ImageDraw.Draw(image)
    for i, participant in enumerate(particpants):
      draw.text(self.pixels[0][self.participants_name.index(participant.get_name())], participant.get_name(),fill=(255, 255, 255), font=Fonts.font242, anchor='mm')
      draw.text(self.pixels[1][self.participants_name.index(participant.get_name())], participant.get_grade(), fill=Colors.colors_note[1 if i == 0 else 2 if i == len(particpants) else 0], font=Fonts.font242, anchor='mm')
      parImg = Image.open(Config.PARTICIPANTS_PATH + "/{}.png".format(participant.get_name()))
      parImg = parImg.convert('RGB')
      parImg = parImg.resize((128, 128), Image.Resampling.LANCZOS)
      parImg = ImageOps.expand(parImg, border=(2, 2, 2, 2), fill="#ffffff")
      image.paste(parImg, self.pixels[2][self.participants_name.index(participant.get_name())])
    return draw
  
  def __check_images(self, participants: list):
    for participant in participants:
      if not Path(f'{Config.PARTICIPANTS_PATH}/{participant}.png').is_file():
        self.__get_images_from_web_server(participants)
        return
  
  def __place_average_grade(self, average:float, image: Image) -> ImageDraw:
    draw = ImageDraw.Draw(image)
    draw.text((1600, 62), "Average: {}".format(round(average, 2)), fill=Colors.average_note, font=Fonts.font36, anchor='mm')
  
  def __place_white_rectangle_as_border(self, image: Image) -> ImageDraw:
    text = ImageDraw.Draw(image)
    text.rectangle(((49, 87), (1330, 808)),outline="white")
    return text 
  
  def __place_info_text_in_image(self, anime: str, song: str, type:str, title: str, image) -> ImageDraw:
    text = ImageDraw.Draw(image)
    text.text((195, 1029), anime, fill=(255, 255, 255), font=Fonts.font482, anchor='lm')
    text.text((195, 960), song, fill=(255, 244, 79), font=Fonts.font482, anchor='lm')
    text.text((195, 891), type, fill=(255, 244, 79), font=Fonts.font362, anchor='lm')
    text.text((51, 80), title, fill=(255, 255, 255),font=Fonts.font242, anchor='ld')
    text.text((113, 839), str('REMEMBER NUMBER'), fill=(255, 255, 255), font=Fonts.font60, anchor='mm')
    return text

  def get_participants_name(self):
    return ' '.join(self.participants_name)

  
  def __get_images_from_web_server(self, participants: list):
    for participant in participants:
        print('-------------')
        print(participant)
        response = requests.get(Config.WEBURL + "/{}.png".format(participant))
        if(response.status_code == 200):
          img = Image.open(BytesIO(response.content))
          img = img.resize((640,640), Image.Resampling.LANCZOS)
          img.save(Config.PARTICIPANTS_PATH + "/{}.png".format(participant))
        else:
          print(f'NÃO ACHOU IMAGEM: {participant}') 