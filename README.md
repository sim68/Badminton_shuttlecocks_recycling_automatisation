# Automated System for Sorting and Recycling Badminton Shuttlecocks

This repository presents an innovative project proposing an automated system for sorting and recycling badminton shuttlecocks, leveraging Industry 4.0 technologies: image processing, robotics, and automation. This system separates shuttlecocks based on their condition (good or worn), thus facilitating the recycling of constituent materials (feathers, keratin, cork) for reuse.

## Table of Contents

- [Introduction](#introduction)
- [System Architecture](#system-architecture)
- [1. Image Processing](#1-image-processing)
  - [1.1. Image Acquisition](#11-image-acquisition)
  - [1.2. Conversion to HSI Color Space](#12-conversion-to-hsi-color-space)
  - [1.3. Image Segmentation](#13-image-segmentation)
  - [1.4. Quantitative Analysis](#14-quantitative-analysis)
  - [1.5. Results](#16-results)
- [2. PLC-Raspberry Pi Communication](#2-plc-raspberry-pi-communication)
  - [2.1. Modbus Variables](#21-modbus-variables)
- [Conclusion](#conclusion)
- [Dependencies](#dependencies)
- [Directory Structure Example](#directory-structure)
- [License](#license)
---

## Introduction

The primary objective of this project is to develop an automated system capable of evaluating the condition of badminton shuttlecocks (new or worn) using image processing and sorting them accordingly to facilitate material recycling. The system integrates multiple Industry 4.0 technologies to ensure complete automation and optimal efficiency.

## System Architecture

- **Raspberry Pi with Pi Camera**: Captures and processes images of the shuttlecocks.
- **OpenCV Library in Python**: Processes and analyzes images to determine the condition of the shuttlecocks.
- **Robotic Arm and Sensors**: Physically manipulates the shuttlecocks and controls the sorting process in real-time with robot Niryo Ned2.
- **Siemens Programmable Logic Controller (PLC)**: Centralizes control and ensures precise coordination of the entire system.
- **Modbus TCP/IP Communication**: Exchanges information between the Raspberry Pi and the PLC to synchronize operations.

---

## 1. Image Processing

Image processing is essential for automating the evaluation of badminton shuttlecock conditions. By analyzing captured images, the system can detect signs of wear and make decisions without human intervention.

### 1.1. Image Acquisition

A Pi Camera connected to the Raspberry Pi captures images of the shuttlecocks. These images are then loaded for processing.

### 1.2. Conversion to HSI Color Space

The RGB image is converted to HSI (Hue, Saturation, Intensity) color space to isolate the saturation component, which is crucial for detecting small holes in the shuttlecock feathers.

### 1.3. Image Segmentation

A specific region of the image is isolated to focus the analysis. A threshold segmentation is then applied to the saturation component to obtain a binary image highlighting worn areas.

### 1.4. Quantitative Analysis

The percentage of white pixels in the segmented image is calculated. A high percentage indicates a worn shuttlecock, while a low percentage indicates a shuttlecock in good condition.

### 1.5. Results

Analyzing the results validates the effectiveness of the algorithm. Here is an example of the obtained result:

![Résultat du Traitement d'Images](Badminton_shuttlecocks_recycling_automatisation/images/result_image.png)

## 2. PLC-Raspberry Pi Communication

Communication between the Siemens PLC and the Raspberry Pi is established via the Modbus TCP/IP protocol, using the pymodbus library in Python. This communication is essential to synchronize actions between the PLC and the Raspberry Pi without requiring additional electronic components.

### 2.1. Modbus Variables

The addresses defined in the holding register and their meanings are as follows:

|Address| Meaning| Variable Name|
|:------|:-------|:-------------|
|00|Informs the Raspberry Pi that the photo can be taken|START_photo|
|01|Informs the PLC that the photo has been taken|VALID_photo|
|02|Informs the PLC of the shuttlecock’s condition (1 = worn, 2 = new)|ETAT_volant|
|03|Requests the Raspberry Pi via the PLC to activate PWM for rotating the servo motor|START_pwm|
|04|Indicates to the Raspberry Pi that the servo motor has finished rotating|capteur_pwm|

## Conclusion

This project illustrates how Industry 4.0 technologies can be integrated to create an efficient automated system for sorting and recycling badminton shuttlecocks. By combining image processing, robotics, and robust communication between components, the system offers an innovative solution for sustainable waste management in the sports domain.


## Dependencies

	•	Python 3.x
	•	OpenCV (opencv-python)
	•	NumPy
	•	pymodbus
	•	picamera
	•	gpiozero

Warning : Picamera has only compatibility with RaspbianOS 32 bits

__Installation of Dependencies__

You can install the required Python packages using pip:

’’’
pip install opencv-python numpy pymodbus picamera gpiozero
’’’

## Directory Structure Example

Your repository should have the following structure:

Badminton_shuttlecocks_recycling_automatisation/\
├── README.md\
├── LICENSE\
├── src/\
    └── images_processing.py\
    └── modbus_communication.py\
└── images/\
    └── result_image.jpg

## License

This project is licensed under the MIT License.

Note: To run the provided codes, ensure that you have installed all the necessary dependencies and have properly configured your hardware and software environment.

