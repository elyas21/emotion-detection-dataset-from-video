from etl.load import Load_Video
from etl.extract import Extract_Frames

def extract():
    ''' extract '''
    print('extract')
    Extract_Frames.Extract_Frames()

def transfor():
    pass

def loadVideos():
    'load video'
    print(Load_Video.Load_video())

def inference():
   pass

