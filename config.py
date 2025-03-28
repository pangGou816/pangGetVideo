import sys
import os

if __name__ == '__main__':
   os.system( 'pip uninstall -y pytubefix moviepy' )

   os.system( 'pip install git+https://github.com/felipeucelli/pytubefix.git@ecef8fb' )
   os.system( 'pip install moviepy==1.0.3' )

   sys.exit()
