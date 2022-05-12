import json
from moviepy.editor import *
import os.path
from images_generator.image_generator import generate_images
import time

google = True

VIDEO_PATH = "./videos/nome_do_video.wmv"
JSON_PATH = "json_example.json"
if(google == True):
  VIDEO_PATH = "/content/drive/MyDrive/output_party_rank/nome_do_video.wmv"
  JSON_PATH = "/content/party-rank-video-generator/json_example.json"

def testar_json():
  erros = ''
  with open(JSON_PATH, 'r') as j:
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
 
def generate_video():
  start_time = time.time()
  if(testar_json() == True):
    clips = []
    time_video = 0
    with open(JSON_PATH, 'r') as j:
      songs = json.load(j)
    for i in songs:
      start = songs[i]["cut_time"][0]
      end = songs[i]["cut_time"][1]
      image = ImageClip(songs[i]["image_path"]).resize((1920,1080)).set_duration(end-start).set_start(time_video).fx(vfx.fadein,1).fx(vfx.fadeout,1)
      clip = VideoFileClip(songs[i]["video_path"]).resize((1280,720)).set_position((50,88)).subclip(start,end).set_start(time_video).fx(vfx.fadein,1).fx(vfx.fadeout,1)

      clips.append(image)
      clips.append(clip)
      time_video = time_video+(end-start)

    final_clip = CompositeVideoClip(clips)
    final_clip.write_videofile(VIDEO_PATH, codec='mpeg4',
                      threads='4', bitrate='6305k',
                      ffmpeg_params=[
                          '-tile-columns', '6', '-frame-parallel', '0',
                          '-auto-alt-ref', '1', '-lag-in-frames', '25', '-g',
                          '128', '-pix_fmt', 'yuv420p', '-row-mt', '1'])
    print("--- %s seconds ---" % (time.time() - start_time))
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

