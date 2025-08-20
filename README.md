# Python OpenCV Projects 🤖✨

This repository contains a collection of computer vision projects developed using Python and the OpenCV library. The projects focus on real-time video processing to perform tasks like hand tracking, gesture recognition, and color detection.

## 📜 Table of Contents
* [About the Project](#about-the-project)
* [Features](#-features)
* [Projects Included](#-projects-included)
  * [Brightness Control with Hand Detection](#1-brightness-control-with-hand-detection)
  * [RGB Color Detection](#2-rgb-color-detection)
  * [Right and Left Hand Detection](#3-right-and-left-hand-detection)
* [📸 Demo Screenshots](#-demo-screenshots)
* [🛠️ Technologies Used](#️-technologies-used)
* [Usage](#-usage)


## About the Project

This collection showcases the power of OpenCV and libraries like MediaPipe for building interactive applications that respond to the physical world through a webcam. Each project is contained in its own script, demonstrating a specific computer vision concept.

---

## ✨ Features

* **Real-time Performance:** All projects process video streams from a webcam in real-time.
* **Gesture-based Control:** Control system settings, like screen brightness, using hand gestures.
* **Interactive Color Analysis:** Click on any point in the video feed to get instant RGB and HSV color values.
* **Advanced Hand Tracking:** Utilizes Google's MediaPipe library for robust, multi-landmark hand detection.
* **Chirality Detection:** Accurately distinguishes between the user's right and left hands.

---

## 📂 Projects Included

### 1. Brightness Control with Hand Detection
This project allows you to control your system's screen brightness using hand gestures.

* **How it works:** The script detects your hand and identifies key landmarks (specifically the thumb and index finger). The distance between these two fingers is calculated and mapped to a brightness range (e.g., 0% to 100%).
* **Libraries Used:** `opencv-python`, `mediapipe`, `numpy`, `screen-brightness-control`.
* **File:** `Brightness_Control_with_Hand_Detection.py`

### 2. RGB Color Detection
An interactive tool to detect the color of any object in the webcam's view.

* **How it works:** The script displays the live video feed. When you click on any pixel in the window, it captures the BGR color value, converts it to RGB and HSV, and displays this information on the screen. It also shows a color swatch for easy visualization.
* **Libraries Used:** `opencv-python`, `numpy`.
* **File:** `RGB_Color_Detection.py` (or your filename)

### 3. Right and Left Hand Detection
This script demonstrates how to not only detect hands but also classify them as 'Right' or 'Left'.

* **How it works:** Leveraging the MediaPipe Hands solution, this project processes the video feed to find hands. The MediaPipe library provides 'chirality' (handedness) information for each detected hand, which is then overlaid on the video stream.
* **Libraries Used:** `opencv-python`, `mediapipe`.
* **File:** `Right_and_Left_Hand_Detection.py` (or your filename)

---

## 📸 Demo Screenshots






---

## 🛠️ Technologies Used

* **Python 3.12+**
* **OpenCV (`opencv-python`)**: For all core computer vision tasks and camera interfacing.
* **MediaPipe (`mediapipe`)**: For high-fidelity hand tracking and landmark detection.
* **NumPy**: For efficient numerical operations on image arrays.
* **Screen Brightness Control (`screen-brightness-control`)**: A cross-platform library to control monitor brightness.

---


## 💻 Usage

Navigate to the project directory and run any of the project scripts using Python.

* **To run the Brightness Control project:**
    ```sh
    Brightness_Control_with_Hand_Detection.py
    ```

* **To run the RGB Color Detector:**
    ```sh
    RGB_Color_Detection.py
    ```

* **To run the Right and Left Hand Detector:**
    ```sh
    Right_and_Left_Hand_Detection.py
    ```

Press the **'q'** key on your keyboard while the video window is active to quit any of the scripts.

---


## 🙏 Acknowledgments
* [OpenCV Library](https://opencv.org/)
* Google's [MediaPipe Framework](https://google.github.io/mediapipe/)
* The Python community
