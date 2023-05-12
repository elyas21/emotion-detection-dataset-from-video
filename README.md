# emotion-detection-dataset-from-video

This project is prepared to generate any detection dataset using pre trianed classifcation model, from row videos.

for this demo i used emotion detection model to generate detection data set for yolo detection model.
the cassifcation model can be found ([here](https://github.com/Furkan-Gulsen/face-classification/raw/main/models/emotionModel.hdf5))

you can try it on google colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/elyas21/emotion-detection-dataset-from-video/blob/main/colab_notebook.ipynb)





ETL 
 first extract picture frames in x interval from video 
 the detect the face and 
 classify each emotions uisng calssification model then write the out put to yolo trainning data format.



## Steps

### download video 
    You can either download and move video to data/row/video or use the Load_Video method in the code.
      ```
      src.Load_Video.Load_video()
      ```
### Extract frames from video 
    
     ```
      src.extract()
     ```
### classifie and generete detection dataset 
    
      ```
      src.classifie_Emotions()
      ```
