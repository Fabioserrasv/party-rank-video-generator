from entities.song import Song
from entities.participant import Participant
import json
from validators.image_json_validator import image_json_validator

class DataInitiator:
  def __init__(self, json_images, json_videos) -> None:
    self.__songs = []
    self.validate(json_images)
    self.convert_json_images_to_object(json_images)
    self.convert_json_videos_to_object(json_videos)
  
  def validate(self, json_a):
    with open(json_a, 'r') as f:
      print(f)
      valid, errors = image_json_validator.is_valid(json.load(f))
      print(errors)
    return valid

  def get_video_title(self):
    return self.__series['title']

  def get_all_participants_name_as_array(self):
    return self.__series['participants']

  def get_series(self):
    return self.__series

  def get_songs(self):
    return self.__songs

  def convert_json_images_to_object(self, json_string):
    with open(json_string, 'r') as f:
      self.__series = json.load(f)
    self.__participants_name = self.__series['participants']

    s_list = self.__series['series']

    for serie in s_list:
      participants = []
      for index, p in enumerate(s_list[serie]['notes']):
        participant = Participant(self.__participants_name[index], p)
        participants.append(participant)
      participants.sort(key=lambda x: x.get_grade(), reverse=False)
      song = Song(serie, s_list[serie]['type'], s_list[serie]['song'], participants, s_list[serie]['average'], s_list[serie]['cover'])
      self.__songs.append(song)
  
  def convert_json_videos_to_object(self, json_string):
    self.__songs.sort(key=lambda x: x.get_average(), reverse=False)

    with open(json_string, 'r', encoding='utf-8') as f:
      clip_cut = json.load(f)
    
    for index, song in enumerate(self.__songs):
      position = str(index + 1)
      song.set_cut_time(clip_cut[position]['cut_time'])
      song.set_image_path(str(clip_cut[position]['image_path']))
      song.set_video_path(str(clip_cut[position]['video_path']))