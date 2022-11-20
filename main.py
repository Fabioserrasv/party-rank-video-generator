from entities.image_generator import ImageGenerator 
from config import Config
import json

print('Executing')

def leave():
  print("Programa encerrado.")

def generate_images():
  with open(Config.JSON_PATH, 'r') as f:
      series = json.load(f)
  generator = ImageGenerator(series)
  generator.generate_images()
  print(generator.get_participants_name())

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
  print(message)
  action()