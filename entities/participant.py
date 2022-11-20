from configs.config import Config

class Participant:
  def __init__(self, name: str, grade: float):
    self.name = name
    self.grade = grade
    
  def get_name(self) -> str:
    return self.name
  
  def get_grade(self):
    return self.grade
  
  def get_img_path(self) -> str:
    return Config.PARTICIPANTS_PATH + "/{}.png".format(self.name)
  
  def __str__(self) -> str:
    return f'Name: {self.name}, Grade: {self.grade}'