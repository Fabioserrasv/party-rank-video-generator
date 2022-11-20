class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

class TerminalMessages:
  
  @staticmethod
  def success(message):
    print(bcolors.OKGREEN + message + '\x1b[0m')
  
  @staticmethod
  def bold(message):
    print(bcolors.BOLD + message + '\x1b[0m')

  @staticmethod
  def underline(message):
    print(bcolors.UNDERLINE + message + '\x1b[0m')

  @staticmethod
  def warning(message):
    print(bcolors.WARNING + message + '\x1b[0m')
    
  @staticmethod
  def blue(message):
    print(bcolors.OKCYAN + message + '\x1b[0m')

  @staticmethod
  def error(message):
    print(bcolors.FAIL + message + '\x1b[0m')

  @staticmethod
  def message(message):
    print(message) 