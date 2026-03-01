from PIL import ImageFont
from configs.config import Config


class Fonts:
  """Fonte padrão (Raleway) para compatibilidade com código que usa Fonts.* diretamente."""
  font = Config.RALEWAY_LIGHT_PATH
  font2 = Config.RALEWAY_SEMI_PATH
  font36 = ImageFont.truetype(font, 36)
  font60 = ImageFont.truetype(font, 60)
  font242 = ImageFont.truetype(font2, 24)
  font362 = ImageFont.truetype(font2, 36)
  font482 = ImageFont.truetype(font2, 48)

  @staticmethod
  def create(light_path: str, semi_path: str) -> "Fonts":
    """Cria instância de fontes a partir dos paths (light e semi-bold)."""
    instance = object.__new__(Fonts)
    instance.font = light_path
    instance.font2 = semi_path
    instance.font36 = ImageFont.truetype(light_path, 36)
    instance.font60 = ImageFont.truetype(light_path, 60)
    instance.font242 = ImageFont.truetype(semi_path, 24)
    instance.font362 = ImageFont.truetype(semi_path, 36)
    instance.font482 = ImageFont.truetype(semi_path, 48)
    return instance