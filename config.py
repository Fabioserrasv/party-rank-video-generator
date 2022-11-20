from os import path, pardir

class Config:
  google = False

  root_dirname = path.abspath(path.join(__file__, pardir))
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
      VIDEO_PATH = "/content/drive/MyDrive/output_party_rank/"
      JSON_PATH = "/content/party-rank-video-generator/json_example.json"
      
      THUMBNAIL_PATH = "/content/party-rank-video-generator/images_generator/thumbnails"
      JSON_PATH = "/content/party-rank-video-generator/images_generator/series2.json"
      RALEWAY_LIGHT_PATH = "/content/party-rank-video-generator/images_generator/Raleway-Light.ttf"
      RALEWAY_SEMI_PATH = "/content/party-rank-video-generator/images_generator/Raleway-SemiBold.ttf"
      PARTICIPANTS_PATH = "/content/party-rank-video-generator/images_generator/participants_images"
      SAVE_PATH = "/content/drive/MyDrive/images_party_rank"