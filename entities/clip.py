class Clip:
  def __init__(self, image: str, video: str, cut_time: tuple):
    self.image = image
    self.video = video
    self.cut_time = cut_time