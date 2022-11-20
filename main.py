from entities.image_generator import ImageGenerator 
from entities.terminal_messages import TerminalMessages 
from config import Config
import json
import os
print('Executing')

def leave():
  print("Programa encerrado.")

def generate_images():
  with open(Config.IMAGES_JSON_PATH, 'r') as f:
      series = json.load(f)
  generator = ImageGenerator(series)
  generator.generate_images()

options = [
  {
    "message": "Sair",
    "action": leave
  },
  {
    "message": "Gerar Imagens",
    "action": generate_images
  }
]

def show_options():
  print("====================")
  for index in range(0, len(options)):
    message = options[index]['message']
    print(f"{index} - {message}")
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
  TerminalMessages.message(f'[Command executed: "{message}"]')
  action()