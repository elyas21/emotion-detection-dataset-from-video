import src



if __name__ == "__main__":
#  load video 
 src.Load_Video.Load_video()
# extract frames from video 
 src.extract()
#  classifie and add txt file to yolo datasete format
 src.classifie_Emotions()