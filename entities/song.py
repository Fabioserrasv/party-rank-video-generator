class Song:
  def __init__(self, name: str, type: str, song: str, participants: list, average: float, cover: str):
    self.name = name
    self.type = type
    self.song = song
    self.participants = participants
    self.average = average
    self.cover = cover
    
  def get_name(self) ->  str:
    return self.name
  
  def get_type(self) ->  str:
    return self.type
  
  def get_song(self) ->  str:
    return self.song
  
  def get_average(self) ->  str:
    return self.average
  
  def get_cover(self) ->  str:
    return self.cover
  
  def get_participants(self) -> list:
    return self.participants
  
  def get_participants_name(self):
    print('-----------------')
    for index, i in enumerate(self.participants):
      print('['+str(index)+']' + i.get_name() + ' Grade: ' + i.get_grade())
    print('-----------------')
    
  def __str__(self) -> str:
    return f'Name: {self.name}, Type: {self.type}, Song: {self.song}, average: {self.average}, cover: {self.cover}'