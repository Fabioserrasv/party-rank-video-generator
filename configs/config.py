from os import path, pardir

class Config:
  google = False

  root_dirname = path.abspath(path.join(__file__, pardir, pardir))
  IMAGES_JSON_PATH = path.abspath(path.join(root_dirname, 'images.json'))
  VIDEOS_JSON_PATH = path.abspath(path.join(root_dirname, 'video.json'))

  RALEWAY_LIGHT_PATH = path.join(root_dirname, 'assets', 'fonts', 'Raleway-Light.ttf')
  RALEWAY_SEMI_PATH = path.join(root_dirname, 'assets', 'fonts', 'Raleway-SemiBold.ttf')

  NOTO_SANS_LIGHT_PATH = path.join(root_dirname, 'assets', 'fonts', 'NotoSans', 'NotoSansJP-Light.ttf')
  NOTO_SANS_REGULAR_PATH = path.join(root_dirname, 'assets', 'fonts', 'NotoSans', 'NotoSansJP-Regular.ttf')
  NOTO_SANS_SEMI_PATH = path.join(root_dirname, 'assets', 'fonts', 'NotoSans', 'NotoSansJP-SemiBold.ttf')

  WEBURL = "https://party-rank.win/participants-images"

  PARTICIPANTS_PATH = path.abspath(path.join(root_dirname, "assets", "participants-images"))
  THUMBNAIL_PATH = path.abspath(path.join(root_dirname, "assets", "cover-images"))
  # THUMBNAIL_PATH = path.abspath(path.join(root_dirname, "capas"))
  BACKGROUND_PATH = path.join(root_dirname, "assets", "asd.jpg")
  
  SAVE_PATH = path.abspath(path.join(root_dirname, "result", "images"))
  VIDEO_PATH = path.abspath(path.join(root_dirname, "result", "videos"))
  CUT_VIDEO_PATH = path.abspath(path.join(root_dirname, "result", "cut_videos"))


  if(google == True):
      IMAGES_JSON_PATH = "/content/party-rank-video-generator/images.json" # JSON DAS IMAGENS
      VIDEOS_JSON_PATH = "/content/drive/MyDrive/videos.json" # JSON DOS VIDEOS
      
      VIDEO_PATH = "/content/drive/MyDrive/output_party_rank/" # ONDE VAI O RESULTADO FINAL DO VIDEO
      SAVE_PATH = "/content/drive/MyDrive/images_party_rank/" # ONDE AS IMAGENS VÃO SER GERADAS
      CUT_VIDEO_PATH = "/content/drive/MyDrive/cut_videos_party_rank/" # ONDE VAO OS VIDEOS CORTADOS
      
      THUMBNAIL_PATH = "/content/party-rank-video-generator/assets/cover-images" # JSON CAPAS
      RALEWAY_LIGHT_PATH = "/content/party-rank-video-generator/assets/fonts/Raleway-Light.ttf" # FONTES
      RALEWAY_SEMI_PATH = "/content/party-rank-video-generator/assets/fonts/Raleway-SemiBold.ttf" # FONTES
      NOTO_SANS_LIGHT_PATH = "/content/party-rank-video-generator/assets/fonts/NotoSans/NotoSans-Light.ttf"
      NOTO_SANS_REGULAR_PATH = "/content/party-rank-video-generator/assets/fonts/NotoSans/NotoSans-Regular.ttf"
      NOTO_SANS_SEMI_PATH = "/content/party-rank-video-generator/assets/fonts/NotoSans/NotoSans-SemiBold.ttf"
      PARTICIPANTS_PATH = "/content/party-rank-video-generator/assets/participants-images" # PATH DAS IMAGENS DOS PARTICIPANTES
      