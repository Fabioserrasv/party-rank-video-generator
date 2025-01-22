from os import path, pardir

class Config:
  google = False

  root_dirname = path.abspath(path.join(__file__, pardir, pardir))
  IMAGES_JSON_PATH = path.abspath(path.join(root_dirname, 'images.json'))
  VIDEOS_JSON_PATH = path.abspath(path.join(root_dirname, 'video.json'))

  RALEWAY_LIGHT_PATH = path.join(root_dirname, 'assets', 'fonts', 'Raleway-Light.ttf')
  RALEWAY_SEMI_PATH = path.join(root_dirname, 'assets', 'fonts', 'Raleway-SemiBold.ttf')

  WEBURL = "https://party-rank.win/participants-images"

  THUMBNAIL_PATH = "./images_generator/thumbnails"
  PARTICIPANTS_PATH = path.abspath(path.join(root_dirname, "assets", "participants-images"))
  THUMBNAIL_PATH = path.abspath(path.join(root_dirname, "assets", "cover-images"))
  
  SAVE_PATH = path.abspath(path.join(root_dirname, "result", "images"))
  VIDEO_PATH = path.abspath(path.join(root_dirname, "result", "videos"))


  if(google == True):
      IMAGES_JSON_PATH = "/content/party-rank-video-generator/images.json" # JSON DAS IMAGENS
      VIDEOS_JSON_PATH = "/content/drive/MyDrive/videos.json" # JSON DOS VIDEOS
      
      VIDEO_PATH = "/content/drive/MyDrive/output_party_rank/" # ONDE VAI O RESULTADO FINAL DO VIDEO
      SAVE_PATH = "/content/drive/MyDrive/images_party_rank/" # ONDE AS IMAGENS VÃO SER GERADAS
      
      THUMBNAIL_PATH = "/content/party-rank-video-generator/assets/cover-images" # JSON CAPAS
      RALEWAY_LIGHT_PATH = "/content/party-rank-video-generator/assets/fonts/Raleway-Light.ttf" # FONTES
      RALEWAY_SEMI_PATH = "/content/party-rank-video-generator/assets/fonts/Raleway-SemiBold.ttf" # FONTES
      PARTICIPANTS_PATH = "/content/party-rank-video-generator/assets/participants-images" # PATH DAS IMAGENS DOS PARTICIPANTES
      