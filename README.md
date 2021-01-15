# Name
Hospital Communication Modes

# Background
A hospital’s homepage is like a virtual “front door” that can function to welcome diverse patients or discourage entry.
Patients with hearing losses are a medically underserved priority population who may use hospital homepages to identify non-hearing dependent contact modes for accessing medical/mental health services.
No prior study, to our knowledge, has assessed extent to which a nationally representative sample of US hospital homepages provide accessible contact modes for patients with hearing losses. 

# Description
The project contains a python program that web scrape hospital websites and detect wheter the websites contain a list a communication modes. The second part of the project is displaying the data onto a python web framework. 
- Hospital.py

The hospital.py is the main python program which do the maain webs craping process. The program first pulls out information in a xlsx file of a list of websites, then it loop through the list of website and check whether of not the website contains a certain comunication modes. A lsit of communication modes that the program checks include: phone number, email, email form, TTY/TDD, text,and video relay. At the end, the program also record the web scraping information and put a "1" if a website have the communication modes and "0" if a webstie dosen't have the communication modes in the xlsx file. The prograam also record if the website dosen't exist, has any issue such as incorrect URL or blocked website, and websites that just simply block web scraping. 
- main.py

The main.py uses the Flask library to create a website that display the web scraping data. The website includes a graph and multiple links to other websites that include lists of websites that either contains a certain communication modes or dosent contains a certain communication modes. 
- html folder

The html folder contains all the HTML file that are being used for the website part. 

# Library Used and Installation
For Reading Data:
```bash
- from openpyxl import *
- import xlrd
- import pandas as pd
```
For Web scraping:
```bash
- from bs4 import BeautifulSoup as soup
- import requests
```
For Creating a Website
```bash
- from flask import Flask, render_template
```

# Project Status
Right now the project is finished aat web scraping basic information and use simple word-search method to determin whether or not a website contains a certain communciation modes. But during the project, I realized that many website contains chat boxes and other information embedded into the website's source code which can not be web scraped using standard method. To be able to do that, more methods need to be implemented by using other libraries. The program would also be much longer and takes much more time to run.
