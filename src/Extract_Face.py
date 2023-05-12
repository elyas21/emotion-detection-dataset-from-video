from mtcnn import MTCNN
import cv2
from pybboxes import BoundingBox
import os
from etl.transform import Classifie_Emotions

def exctract_face():

    for fn in os.listdir('data/row/img/'):
        if os.path.exists(f'data/row/img/'+fn) and (fn.endswith('.png') or fn.endswith('.jpg')):
            print(f'data/row/img/'+fn)
            img = cv2.cvtColor(cv2.imread(f'data/row/img/'+fn), cv2.COLOR_BGR2RGB)
            detector = MTCNN()
            # print(detector.detect_faces(img))
            print(img)
            if os.path.exists(f'data/row/img/'+fn[:-4]+'.txt'):
                os.remove(f'data/row/img/'+fn[:-4]+'.txt')
            for face in detector.detect_faces(img):
                # try:
                    # create bbox

                    a = face['box']
                    coco_bbox = BoundingBox.from_coco(*a)
                    coco_bbox.image_size = (640, 480)
                    yolo_bbox = coco_bbox.to_yolo()

                    #get prid
                    print(Classifie_Emotions)
                    prid = Classifie_Emotions.frame_to_prid(a[0], a[1], a[2], a[3], img) 
                    print(prid)

                    # save yolo bbox
                    f = open(f'data/row/img/'+fn[:-4]+'.txt', "a")
                    f.write(f''+ prid +' '+ str(yolo_bbox.values[0]) + ' '+ str(yolo_bbox.values[1]) + ' '+ str(yolo_bbox.values[2]) + ' '+ str(yolo_bbox.values[3]) + ' \n')
                    f.close()
                # except:
                    # continue
                # save croped faces to new folder new file
                