from doctest import FAIL_FAST
import json
from moviepy.editor import *
import os.path

def testar_json():
  erros = ''
  with open('json_example.json', 'r') as j:
    songs = json.load(j)
  for i in songs:
    t = 0
    cut_time = songs[i]["cut_time"]
    image = songs[i]["image_path"]
    video = songs[i]["video_path"]
    if not os.path.isfile(image):
      erros += f"A imagem de <{i}> não existe.\n"
      t = 1
    if not os.path.isfile(video):
      erros += f"O vídeo de <{i}> não existe.\n"
      t = 1
    if(cut_time[0] > cut_time[1]):
      erros += f"O tempo de ínicio informado em <{i}> é maior que o tempo final.\n"
      t = 1
    if(cut_time[1] - cut_time[0] < 3):
      erros += f"O tempo do vídeo precisa ser de no minímo 3 segundos em <{i}>.\n"
      t = 1
    if t == 1:
      erros += "="*20
      erros += "\n"
  print(erros)
  return(True if erros == '' else False)
 
def generate_images():
  print("To do")
  
def generate_video():
  if(testar_json() == True):
    clips = []
    time = 0
    with open('json_example.json', 'r') as j:
      songs = json.load(j)
    for i in songs:
      start = songs[i]["cut_time"][0]
      end = songs[i]["cut_time"][1]
      image = ImageClip(songs[i]["image_path"]).set_duration(end-start).set_start(time).fx(vfx.fadein,1).fx(vfx.fadeout,1)
      clip = VideoFileClip(songs[i]["video_path"]).resize((1280,720)).set_position((34,54)).subclip(start,end).set_start(time).fx(vfx.fadein,1).fx(vfx.fadeout,1)

      clips.append(image)
      clips.append(clip)
      time = time+(end-start)

    final_clip = CompositeVideoClip(clips)
    final_clip.write_videofile('./videos/teste.webm',codec='libvpx-vp9',
                      threads='8', bitrate='1485k',
                      ffmpeg_params=[
                          '-tile-columns', '6', '-frame-parallel', '0',
                          '-auto-alt-ref', '1', '-lag-in-frames', '25', '-g',
                          '128', '-pix_fmt', 'yuv420p', '-row-mt', '1'])
    return
  print("O JSON não passou no teste. Use a opção 3 (Testar JSON) para mais informações.")
  

def leave():
  print("Programa encerrado.")

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
    "message": "Gerar vídeo",
    "action": generate_video
  },
  {
    "message": "Testar JSON",
    "action": testar_json
  },
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

