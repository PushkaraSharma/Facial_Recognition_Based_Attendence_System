# Facial_Recognition_Based_Attendence_System
This repository contains code for facial recognition using openCV and python with a PyQt5 gui interface.
If you want to test the code then run application.py file

## INSTALL
This project requires Python and the following Python libraries installed:
* NumPy
* Pandas
* matplotlib
* scikit-learn
* PyQt5
 You will also need to have software installed to run and execute a PyCharm Software.

If you do not have Python installed yet, it is highly recommended that you install the python.

## Files_Description

* Facedatas-This folder conatins numpy array of 20 images of each students facial information.
* Application-This is the final main python file in which PyQt5 GUI is designed and detect.py and recog_knn are imported for functionality.The 
              app contains three buttons ..one for registering the student face data ..second for recognizing th faces and recognizing the face
              and third for checking attendence file.
* Attendence- This is the final output csv file that is used to record the attendence of the students.This csv contains student's name ,date
            and time of attendence
* Detect- Importing the haarcascade file for face detection and then storing 20 images of student as a single numpy array file 
* Recog_knn - Importing the saved facedatas and then applying KNN algorithm for training the model and then opening camera and start recongnizing
             faces.
* haarcascade- This xml file is used for face detection.

![Capture](https://user-images.githubusercontent.com/46081301/60452308-e16ce080-9c4b-11e9-89ab-3abe5c9c1121.PNG)


