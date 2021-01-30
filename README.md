# Carvana-cars-sampling
This projects is created to randomly sample cars on carvana by brands and proportionally for research purpose. It will keeps tracking of the status of the listed car, and generate an excel and a txt file for  better analyzation and visualization.
Py packages used(make sure they are installed): 
numpy
openpyxl
timer
urllib3
xlsxwriter
tkinter
re
(they can also be found under venv/lib, but still need to be installed with pip)


How to use: 
1. Run main.exe 
2. Select a fodler destination where files to be stored
3.A notification will pop up when finished, with run time and folder location

It will automatically create a new set of cars to track if the folder is empty
if there is already an existing set of cars stored in the folder, it will automatically open and track the existing set. 
