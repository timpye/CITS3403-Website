# CITS3403 Project 1 Website
Computer Parts 101

# Description 
This is our group project submission for CITS3403 Agile Web Development.

The purpose of our project is to develop a web-based platform, where users learn about the components used in building
desktop computers. Users are able to learn about this through our content page where they will learn the essentials of each component used
to build a computer. Users are then prompted to take a quiz to access their knowledge and what they have learnt.

# How to get started
The following instructions will teach you how to get a clone of this project up and running on your own system. 

## Prerequisites ##
First you must install the latest version of Python which is currently 3.9.5.

### Windows ###
You must download and install the executable from [here](https://www.python.org/downloads/)

### Mac ### 
If you have homebrew installed you can type the following into your terminal.
```
$ brew install python3
```
### Linux ###
Type the following into your terminal.
```
$ sudo apt-get install python3.9
```

## Installation ##

You will need to set up a virtual environment to run the application in, you can do this by creating a folder, then opening that folder with 
your terminal, then type the following.
```
$ python3 -m venv venv
```
Then you will activate the virtual environment.

### Windows ###
```
$ venv\Scripts\activate
```

### Mac/Linux ###
```
$ source venv/bin/activate
```
Then you must install all the requirements for this application by simply entering the following.
### Windows/Mac/Linux ###
```
$ pip install -r requirements.txt
```

### Initialising the database ###
After installing all the prerequisites the database needs to be initialised with
```
$ flask db init
```

### Deployment ###
run the app with 
```
$ flask run
```
The app should now be running at localhost port 5000

### Built with ###
VSCode and Github Desktop

### Authors ###
Anfernee Alviar
Jakob Kuriata
Timothy Pye

# Resources
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

