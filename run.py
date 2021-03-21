"""UI for MustangBronco program

This is the main user progrtam that takes user integer inputs and returns the
appropriate string outputs. 

  Typical usage example:
  # From project directory
  python run.py
"""

from mustang_bronco.src.mustang_bronco import mustang_bronco

def main():
  while True:
    try:
      value = int(input('Please enter an integer: '))
      string_to_display = mustang_bronco(value)
      print('{}\n'.format(string_to_display))

    except ValueError:
      print('Input must be an integer!\n')

    except KeyboardInterrupt:
      return
    
if __name__ == '__main__':
  print('\n\
    __  ___           __                       ____                             \n\
   /  |/  /_  _______/ /_____ _____  ____ _   / __ )_________  ____  _________  \n\
  / /|_/ / / / / ___/ __/ __ `/ __ \/ __ `/  / __  / ___/ __ \/ __ \/ ___/ __ \ \n\
 / /  / / /_/ (__  ) /_/ /_/ / / / / /_/ /  / /_/ / /  / /_/ / / / / /__/ /_/ / \n\
/_/  /_/\__,_/____/\__/\__,_/_/ /_/\__, /  /_____/_/   \____/_/ /_/\___/\____/  \n\
                                  /____/                                         \n\n')
  
  print('Welcome to Mustang Bronco! To terminate the program, please type Ctrl-c \n')
  main()
  print('\nExiting...\n')
