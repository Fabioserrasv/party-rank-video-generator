from entities.image_generator import ImageGenerator 
from entities.video_generator import VideoGenerator 
from entities.terminal_messages import TerminalMessages 
from configs.config import Config
import json
import os

def leave():
  print("Programa encerrado.")

songs = []

def generate_images():
  global songs
  with open(Config.IMAGES_JSON_PATH, 'r') as f:
      series = json.load(f)
  generator = ImageGenerator(series)
  generator.generate_images()
  songs = generator.get_songs()

def generate_video():
  global songs
  generator = VideoGenerator(songs)
  generator.generate_video()

def execute_commands_colab():
  import os
  os.system("python3 -m pip uninstall --yes pillow")
  os.system("python3 -m pip install pillow==9.1.0")
  os.system("python3 -m pip uninstall --yes moviepy")
  os.system("python3 -m pip install moviepy")
  os.kill(os.getpid(), 9)

options = [
  {
    "message": "Sair",
    "action": leave
  },
  {
    "message": "Gerar Imagens",
    "action": generate_images
  },
  {
    "message": "Gerar Video",
    "action": generate_video
  },
  {
    "message": "Preparar ambiente Google Colab",
    "action": execute_commands_colab
  }
]

def show_options():
  print("====================")
  for index in range(0, len(options)):
    message = options[index]['message']
    TerminalMessages.warning(f"{index} - {message}")
  print("====================")

number_option = 999
while number_option > 0:
  show_options()
  number_option = int(input('Digite a opção: '))

  option = options[number_option]
  message = option['message']
  action = option['action']

  print("====================")
  os.system('cls' if os.name == 'nt' else 'clear')
  TerminalMessages.underline(f'Command executed: "{message}"')
  action()