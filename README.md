** **

# Project 
This project was generated with [Python](https://www.python.org/downloads/release/python-3105/) version 3.10.5.

## Documentation
- [About](#about)
- [Installation](#installation)
- [Project Video](https://drive.google.com/file/d/1l9550w4OFarOHZnY5xgQg41TV3QH_c7N/view?usp=sharing)
<!--- - [Vision and Goals Of The Project](#vision-and-goals-of-the-project)
- [Users/Personas Of The Project](#users/personas-of-the-project)
- [Scope and Features Of The Project](#scope-and-features-of-the-project)
- [Solution Concept](#solution-concept)
    - [Background and Motivation](#background-&-motivation)
    - [Architecture](#architecture)
        - [Components](#components-of-sanity-framework)
- [Pipleline of De-duplication](#pipleline-of-de-duplication)
- [Learnings](#learnings)
- [Acceptance Criteria](#acceptance-criteria)
- [Future Steps & Limitations](#future-steps-&-limitations)
- [Release Planning](#release-planning)
- [References](#references)
- [Mentor](#mentor)
- [Contributors](#contributors) -->

** **

## About
* **Stack:** The project is developed purely in Python. 
* **Version:** Python version 3.10.5 or above can be used.
* **Front-End:** Python tkinter is used for Front-end side.

**Modules Used:**
* [tkinter](https://docs.python.org/3/library/tkinter.html)
* [vosk](https://pypi.org/project/vosk/) : Model ---> vosk-model-en-in-0.5
* [pandas](https://pypi.org/project/pandas/)
* [openpyxl](https://pypi.org/project/openpyxl/)
* [pyaudio](https://pypi.org/project/PyAudio/)
* [os](https://docs.python.org/3/library/os.html)

** **

## Installation
### Steps
-   Setup python 3.10.5
-   Install dependencies/modules with the help of pip
-   Futher configuration required to utilise the modules.

### Getting started
##### Install all the dependencies
```
$ pip install tkinter
$ pip install vosk
$ pip install pandas
$ pip install openpyxl
$ pip install PyAudio 
```
**Note:** If there is an error in installing PyAudio then following can be done to install it.
```
$ pip install pipwin
$ pipwin install pyaudio 
```

### Further Configuration/Changes if needed
We are using Indian English vosk Model ([vosk-model-en-in-0.5](https://alphacephei.com/vosk/models)). If there is a need to change it then we can follow the below procedure:
* Go to https://alphacephei.com/vosk/models and download the Model which is required.
* Unzip the folder to the project location
* Make necessary Model path changes in "myentries.py" (line number 24)


### Run the Project
We can run the program from Command Prompt. Change the path directory to the path where app.py exist. Then run the following command:
``` python app.py ```


## Project Video
Below is the drive link to the project. It helps in understanding how the project works and what are its functionalities.
https://drive.google.com/file/d/1l9550w4OFarOHZnY5xgQg41TV3QH_c7N/view?usp=sharing


### Steps
* Enter account number, if not provided then it will give validation error.
* After that click on Insert or View according to your need.
* When you click on Insert then it will have prefilled SNOW number fetched with the help of given account number. If the account number is new then the SNOW will start from "1".
* You can input the data using by Speech Recording. 
```
* Click on Record Button
* Double Click on the Textbox you want to fill data in and then record your voice.
* The text will get recognised from your speech and get printed on the textbox.
* You can then click on "Save" and it will update the given account number sheet in excel file
* Note: Excel file "Report.xlsx" will contain multiple sheets which are the the account numbers. Each sheet will contain details of particular account number.
```
* When you click on View, you can view all the entries of the given account number. Further you can Update the existing data by clicking on the Update button of respective row data. Note: The blank rows contains no entries and the Update button on its side is disabled.

** **
