# YOLO v3 Object Detection

## Description

This project implements an object detection pipeline using the YOLO v3 algorithm and a pre-trained Darknet Keras model. The goal of the project is to detect objects in images, process model outputs, filter weak predictions, apply Non-Max Suppression, and display the final detected objects with bounding boxes, class names, and confidence scores.

The implementation is built step by step across multiple tasks, starting from initializing the YOLO model and ending with a complete prediction pipeline for multiple images.

## Learning Objectives

By completing this project, I practiced and implemented the following concepts:

- Loading a pre-trained Darknet Keras model
- Reading class labels from a file
- Understanding YOLO v3 model outputs
- Processing bounding box predictions
- Applying sigmoid and exponential transformations
- Converting bounding boxes to original image scale
- Filtering boxes using confidence thresholds
- Applying Non-Max Suppression
- Loading and preprocessing images
- Drawing bounding boxes and labels using OpenCV
- Saving detection results
- Building a complete object detection prediction pipeline

## Technologies Used

- Python 3
- NumPy
- TensorFlow / Keras
- OpenCV
- YOLO v3
- Darknet model architecture

## Project Structure

```text
object_detection/
│
├── 0-yolo.py
├── 1-yolo.py
├── 2-yolo.py
├── 3-yolo.py
├── 4-yolo.py
├── 5-yolo.py
├── 6-yolo.py
├── 7-yolo.py
│
├── 0-main.py
├── 1-main.py
├── 2-main.py
├── 3-main.py
├── 4-main.py
├── 5-main.py
├── 6-main.py
├── 7-main.py
│
├── detections/
│
└── README.md