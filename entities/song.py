class Song:
  def __init__(self, name: str, type: str, song: str, participants: list, average: float, cover: str):
    self.__name = name
    self.__type = type
    self.__song = song
    self.__participants = participants
    self.__average = average
    self.__cover = cover
    self.__cut_time =  (0,0)
    self.__image_path =  ''
    self.__video_path =  ''
    
  def set_cut_time(self, cut_time: tuple) -> None:
    self.__cut_time = cut_time
   
  def get_cut_time(self) -> tuple:
    return self.__cut_time 
      
  def set_image_path(self, image_path: str) -> None:
    self.__image_path = image_path
   
  def get_image_path(self) -> str:
    return self.__image_path 
  
  def set_video_path(self, video_path: str) -> None:
    self.__video_path = video_path
   
  def get_video_path(self) -> str:
    return self.__video_path 
  
  def get_name(self) ->  str:
    return self.__name
  
  def get_type(self) ->  str:
    return self.__type
  
  def get_song(self) ->  str:
    return self.__song
  
  def get_average(self) ->  str:
    return self.__average
  
  def get_cover(self) ->  str:
    return self.__cover
  
  def get_participants(self) -> list:
    return self.__participants
  
  def get_participants_name(self):
    print('-----------------')
    for index, i in enumerate(self.__participants):
      print('['+str(index)+']' + i.get_name() + ' Grade: ' + i.get_grade() + ' image and video: ' + i.get_image_path() + i.get_video_path())
    print('-----------------')
    
  def __str__(self) -> str:
    return f'Name: {self.__name}, Type: {self.__type}, Song: {self.__song}, average: {self.__average}, cover: {self.__cover}, image_path: {self.__image_path}, video_path: {self.__video_path}'