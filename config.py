import sys
import os

if __name__ == '__main__':
   os.system( 'pip uninstall pytubefix moviepy' )

   os.system( 'pip install pytubefix' )
   os.system( 'pip install moviepy==1.0.3' )

   sys.exit()
