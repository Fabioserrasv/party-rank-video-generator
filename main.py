from entities.image_generator import ImageGenerator 
from entities.video_generator import VideoGenerator 
from entities.terminal_messages import TerminalMessages
from entities.data_initiator import DataInitiator
from configs.config import Config
from configs.commands import options
import os

class Main:
  def __init__(self) -> None:
    self.__data_initiator = DataInitiator(Config.IMAGES_JSON_PATH, Config.VIDEOS_JSON_PATH)
    
  def leave(self):
    print("Programa encerrado.")

  def generate_images(self):
    image_generator = ImageGenerator(
      songs=self.__data_initiator.get_songs(),
      title=self.__data_initiator.get_video_title(),
      participants=self.__data_initiator.get_all_participants_name_as_array()
      )
    image_generator.generate_images()

  def generate_video(self):
    generator = VideoGenerator(
      songs=self.__data_initiator.get_songs()
    )
    generator.generate_video()

  def execute_commands_colab(self):
    os.system("python3 -m pip uninstall --yes pillow")
    os.system("python3 -m pip install pillow==9.1.0")
    os.system("python3 -m pip uninstall --yes moviepy")
    os.system("python3 -m pip install moviepy")
    os.kill(os.getpid(), 9)

  def show_options(self):
    print("====================")
    for index in range(0, len(options)):
      message = options[index]['message']
      TerminalMessages.warning(f"{index} - {message}")
    print("====================")
  
  def run(self):
    number_option = 999
    while number_option > 0:
      self.show_options()
      number_option = int(input('Digite a opção: '))

      option = options[number_option]
      message = option['message']
      action = eval(option['action'])

      print("====================")
      os.system('cls' if os.name == 'nt' else 'clear')
      TerminalMessages.underline(f'Command executed: "{message}"')
      action()

if __name__ == '__main__':
  app = Main()
  app.run()