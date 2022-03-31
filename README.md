# OBJECT-DETECTION-USING-ImageAI

## Training a model to detect two objects that is cars and persons in an image.

An open-source python library built to empower developers to build applications and systems with self-contained Deep Learning and Computer Vision capabilities using simple and few lines of code.

--------------------------------------------------------------------------------------------

## Overview
* We have a **dataset** and we need to train an object detector to predict labels & bounding boxes for 2 classes.

--------------------------------------------------------------------------------------------

## Model Overview

* Built with simplicity in mind, ImageAI supports a list of state-of-the-art Machine Learning algorithms for image prediction, custom image prediction, object detection, video detection, video object tracking and image predictions trainings.
* ImageAI currently supports image prediction and training using 4 different Machine Learning algorithms trained on the ImageNet-1000 dataset.
* ImageAI also supports object detection, video detection and object tracking using RetinaNet, YOLOv3 and TinyYOLOv3 trained on COCO dataset.
* Finally, ImageAI allows you to train custom models for performing detection and recognition of new objects.
* Eventually, ImageAI will provide support for a wider and more specialized aspects of Computer Vision including and not limited to image recognition in special  environments and special fields.

--------------------------------------------------------------------------------------------

## Assumptions
* Each larger-scale model incorporates the previous smaller-scale model layers and weights in its architecture.
--------------------------------------------------------------------------------------------

## Framework
* I chose to use [ImageAI](https://towardsdatascience.com/object-detection-with-10-lines-of-code-d6cb4d86f606) .ImageAI is a python library built to empower developers, reseachers and students to build applications and systems with self-contained Deep Learning and Computer Vision capabilities using simple and few lines of code.

--------------------------------------------------------------------------------------------


## Preprocessing Stage

* There were two things as inputs 1) Annotations Json 2) Images folder
* I preprocessed the dataset in the format required by the ImageAI standards.
* Please refer to the [Train Custom Data](https://github.com/OlafenwaMoses/ImageAI) for detailed understanding.
* Rather than shuffling and splitting the dataset in a traditional 75-25 or 80-20 train-test split, I randomly picked 100 images out of the total 2239 available images as a validation set.

--------------------------------------------------------------------------------------------

## Training
* A ImageAI model pretrained on resnet50_coco_best_v2.1.0.h5 was used to apply transfer learning, by specifying the custom dataset.

* Please refer to the [Colab Training Jupyter Notebook](https://colab.research.google.com/drive/12Q8PYt3pTlNpQwrxM82K5btkOgsXiDwJ?usp=sharing)

--------------------------------------------------------------------------------------------

## Output on the Validation Set from the [output Images folder](https://github.com/keshavgarg139/car-person-detection/tree/main/predictions)
* The format on the bounding boxes is (label, confidence)
