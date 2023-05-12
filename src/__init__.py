from etl.load import Load_Video
from etl.extract import Extract_Frames
from . import Extract_Face

def extract():
    ''' extract '''
    print('extract')
    Extract_Frames.Extract_Frames(1000)

def transfor():
    pass

def loadVideos():
    'load video'
    print(Load_Video.Load_video())

def classifie_Emotions():
    Extract_Face.exctract_face()