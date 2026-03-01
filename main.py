from entities.image_generator import ImageGenerator
from entities.video_generator import VideoGenerator
from entities.terminal_messages import TerminalMessages
from entities.data_initiator import DataInitiator
from configs.config import Config
from configs.commands import options
import os

class Main:
  def __init__(self) -> None:
    self.__data_initiator = DataInitiator(Config.IMAGES_JSON_PATH, Config.VIDEOS_JSON_PATH)
    
  def leave(self):
    print("Programa encerrado.")

  def generate_images(self):
    print("Fonte:")
    print("  1 - Raleway")
    print("  2 - Noto Sans")
    op_font = input("Escolha (1 ou 2) [1]: ").strip() or "1"
    if op_font == "2":
      has_light = os.path.isfile(Config.NOTO_SANS_LIGHT_PATH)
      has_regular = os.path.isfile(Config.NOTO_SANS_REGULAR_PATH)
      has_semi = os.path.isfile(Config.NOTO_SANS_SEMI_PATH)
      if (not has_light and not has_regular) or not has_semi:
        TerminalMessages.error("Arquivos da fonte Noto Sans não encontrados. Coloque na pasta assets/fonts/NotoSans/:")
        TerminalMessages.warning("  - NotoSans-Light.ttf ou NotoSans-Regular.ttf")
        TerminalMessages.warning("  - NotoSans-SemiBold.ttf")
        return
      font_light = Config.NOTO_SANS_LIGHT_PATH if has_light else Config.NOTO_SANS_REGULAR_PATH
      font_semi = Config.NOTO_SANS_SEMI_PATH
    else:
      font_light = Config.RALEWAY_LIGHT_PATH
      font_semi = Config.RALEWAY_SEMI_PATH

    print("Dimensão da capa:")
    print("  1 - 131 x 184 (Retangular - Padrão)")
    print("  2 - 180 x 180 (Quadrada - Álbum)")
    opcao = input("Escolha (1 ou 2) [1]: ").strip() or "1"
    cover_size = (131, 184) if opcao == "1" else (180, 180)

    image_generator = ImageGenerator(
      songs=self.__data_initiator.get_songs(),
      title=self.__data_initiator.get_video_title(),
      participants=self.__data_initiator.get_all_participants_name_as_array(),
      cover_size=cover_size,
      font_light_path=font_light,
      font_semi_path=font_semi
    )
    image_generator.generate_images()

  def generate_video(self):
    print("Modo preview (vídeo em tamanho reduzido 155x155)?")
    print("  1 - Não (vídeo em resolução full)")
    print("  2 - Sim (preview rápido)")
    op_preview = input("Escolha (1 ou 2) [1]: ").strip() or "1"
    preview = op_preview == "2"

    print("Processar apenas os 10 primeiros itens?")
    print("  1 - Não (todos)")
    print("  2 - Sim (apenas 10)")
    op_ten = input("Escolha (1 ou 2) [1]: ").strip() or "1"
    only_ten = op_ten == "2"

    print("Cortar vídeos antes de montar?")
    print("  1 - Sim (cortar)")
    print("  2 - Não (usar vídeos já cortados)")
    op_cut = input("Escolha (1 ou 2) [1]: ").strip() or "1"
    cut_video = op_cut == "1"

    generator = VideoGenerator(
      songs=self.__data_initiator.get_songs(),
      preview=preview,
      only_ten=only_ten,
      cut_video=cut_video
    )
    generator.generate_video()

  def execute_commands_colab(self):
    os.system("python3 -m pip uninstall --yes pillow")
    os.system("python3 -m pip install pillow==9.1.0")
    os.system("python3 -m pip uninstall --yes moviepy")
    os.system("python3 -m pip install moviepy")
    os.system("python3 -m pip install wvalidate")
    os.kill(os.getpid(), 9)

  def show_options(self):
    print("====================")
    for index in range(0, len(options)):
      message = options[index]['message']
      TerminalMessages.warning(f"{index} - {message}")
    print("====================")
  
  def run(self):
    number_option = 999
    while number_option > 0:
      self.show_options()
      number_option = int(input('Digite a opção: '))

      option = options[number_option]
      message = option['message']
      action = eval(option['action'])

      print("====================")
      os.system('cls' if os.name == 'nt' else 'clear')
      TerminalMessages.underline(f'Command executed: "{message}"')
      action()

if __name__ == '__main__':
  app = Main()
  app.run()