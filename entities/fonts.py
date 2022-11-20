from PIL import ImageFont
from configs.config import Config
class Fonts:
  font = Config.RALEWAY_LIGHT_PATH
  font2 = Config.RALEWAY_SEMI_PATH
  font36 = ImageFont.truetype(font, 36)
  font60 = ImageFont.truetype(font, 60)
  font242 = ImageFont.truetype(font2, 24)
  font362 = ImageFont.truetype(font2, 36)
  font482 = ImageFont.truetype(font2, 48)