

from imageai.Detection import ObjectDetection
import os
#!pip install tqdm

from glob import glob
from tqdm import tqdm

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "D:/practice/resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()
for i in tqdm(os.listdir("D:/trainval/images")[:100]):
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "D:/trainval/images",i), output_image_path=os.path.join(execution_path,"D:/practice",i))
    
    #for eachObject in detections:
        #print(eachObject["name"] , " : " , eachObject["percentage_probability"] )