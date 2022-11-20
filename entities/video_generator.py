from entities.terminal_messages import TerminalMessages
from config import Config
class VideoGenerator:
  def __init__(self):
    self
  
  def test_json():
    erros = ''
    
    for i in songs:
      t = 0
      cut_time = songs[i]["cut_time"]
      image = songs[i]["image_path"]
      video = songs[i]["video_path"]
      if not os.path.isfile(image):
        TerminalMessages(f'Did not found image: "{i}".')
        t = 1
      if not os.path.isfile(video):
        TerminalMessages(f'Did not found video file: "{i}".')
        t = 1
      if(cut_time[0] > cut_time[1]):
        TerminalMessages(f"Invalid time length: "{i}".")
        t = 1
      if(cut_time[1] - cut_time[0] < 3):
        TerminalMessages(f"Invalid time length: "{i}", cut time has to be hight than 3 seconds.")
        t = 1
      if t == 1:
        TerminalMessages("="*20)
    return(True if erros == '' else False)