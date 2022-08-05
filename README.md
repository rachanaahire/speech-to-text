** **

# Project 
This project was generated with [Python](https://www.python.org/downloads/release/python-3105/) version 3.10.5.

## Documentation
- [About](#about)
- [Installation](#installation)
- [Project Video]()
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

