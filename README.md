# Technical interview test made for the position of Python Developer at 'People Trust'.
This repository contains the project where I gave solution to a task I was requested for the technical test of the Python Developer job opportunity at the 'People Trust' company. The purpose of the test was to create a simple REST API, with Flask, to receive numeric data through a POST request on a specific end point to then store it in a txt file. In addition, if a GET request was made for another specific end point, it would then sum all the numeric values contained in that txt file to then return the result in JSON format.

## Configuration steps to setup this project.
The following description will assume that the project is being executed on a computer with Windows 10, where you should have already installed Anaconda to then create an environment with the Anaconda prompt terminal with Python v3.10.4 and to then install the following packages:

```console
$ pip install Flask==2.1.3
$ pip install Flask-RESTful==0.3.9
$ pip install spyder==5.3.2
``` 

NOTE: I developed the Python code on the Spyder IDE. If you do not wish to use that Python code editor, then do not install it in your Anaconda environment.

## How to run this project.
To run this project, all you have to do is the following:

1. Open the Anaconda prompt terminal.
2. Activate the environment where you installed the required packages.
3. Move the current directory of the Anaconda prompt terminal to where this project is located.
4. Execute the following commands in that terminal to run the REST API that was developed in this project:

```console
$ python rest_api_test.py
``` 

## How to use this REST API.
There are only two possible ways to interact with this REST API: through a POST request on one specific end point and through a GET request on another specific end point. On my machine, when runing this project, I was assigned the port number 5000 in my local host. Therefore, the two possible end points with which I could interact with this REST API were the following:

- http://127.0.0.1:5000/end_point_one  --> expects a POST request
- http://127.0.0.1:5000/end_point_two  --> expects a GET request

### How to store data in the 'data.txt' file through the REST API.
On a different terminal window that is Linux compatible (I used Cygwin64), all you have to do is to send a POST request with the desired numeric value that you want to store in the 'data.txt' to the end point "http://127.0.0.1:5000/end_point_one", where your numeric value is expected to be stored in the 'numbers' index of your JSON. For example:

```console
$ curl -H "Content-Type: application/json" -X POST -d '{"numbers":"30"}' http://127.0.0.1:5000/end_point_one
``` 

### How to request the sum of the numbers contained in each line of the 'data.txt' file through the REST API.
On a different terminal window that is Linux compatible (I used Cygwin64), all you have to do is to send a GET request with whatever value to the end point "http://127.0.0.1:5000/end_point_two". For example:

```console
$ curl http://127.0.0.1:5000/end_point_two/10
``` 

and then the sum of all the numbers contained in each line of the 'data.txt' file will be returned in JSON format on its 'result' index.