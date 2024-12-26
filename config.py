import sys
import os

if __name__ == '__main__':
   os.system( 'pip uninstall -y pytubefix moviepy' )

   os.system( 'pip install pytubefix moviepy==1.0.3' )

   sys.exit()
