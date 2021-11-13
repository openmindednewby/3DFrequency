from switch import Switch
import numpy as np
import math
import matplotlib.pyplot as plot
import time as Time

# Arrange
helpMessage = """
Instructions!

General
#################################################
h           - print this help message
q           - quit app
d           - prints current data
#################################################
Plot Specific
#################################################
xstart       - set x-axis start value (arrays first value). Default = -50 Datatype = int
ystart       - set y-axis start value (arrays first value) Datatype = int
xend         - set x-axis end value (arrays last value) Default = 50 Datatype = int
yend         - set y-axis end value (arrays last value) Datatype = int
d              - sets the data point incremented
gl             - generates origin axis initial data (time is populated with range of valued from xstart up to xend)
gywave     - generates yAxis wave
density    - set density
p              - plots data
phase       - set phase
r              - reset all data
figSizex  - set figure size on x axis
figSizey  - set figure size on y axis
scale        - set scale value
precision  - set precision value
frequency  - set frequency
gwp          - generate wave and plot
grp           - generate resonance and plot
agrp         - automaticaly generate resonanse plot interactively
agwp         - automaticaly generate wave plot interactively
loopr         - loop resonance with set frequency start value and end value
loopw        - loop wave with set frequency start value and end value
loopp        - enter loop pause

#################################################
"""
phase =0;
density = 10;
xStart = -10;
xEnd = 10;
time = [];
yAxis =[];
yValue =0;
scale = 1;
frequency =1.00;
time = np.arange(xStart, xEnd, 1/density);
yAxis = np.arange(xStart, xEnd, 1/density);
precision =2;
stringInput = '';
fStart =1;
fEnd = 50;
loopPause = 0;
figSizex = 10;
figSizey = 3;

plot.figure(figsize=(figSizex,figSizey))

# Functions
def assignInitialValues(start, stop, den):
    return np.arange(start, stop, 1/den);

def reset():
    phase =0;
    density = 100;
    xStart = -10;
    xEnd = 10;
    yValue =0;
    scale = 1;
    frequency =1.00;
    time = np.arange(xStart, xEnd, 1/density);
    yAxis = np.arange(xStart, xEnd, 1/density);
    precision =3;
    stringInput = '';
    fStart =1;
    fEnd = 100;
    loopPause = 0.5;
    figSizex = 10;
    figSizey = 1;
    
def generateInitialValues():
        time = assignInitialValues(xStart, xEnd, density);
        yAxis = assignInitialValues(xStart, xEnd, density);
        
def printAllData():
    print('time: ' + str(time));
    print('yAxis: ' + str(yAxis));
    print('xstart: ' + str(xStart));
    print('xend: ' + str(xEnd));
    print('density: ' + str(density));     
    print('scale: ' + str(scale));
    print('frequency: ' + str(frequency));
    print('precision: ' + str(precision));
    print('phase: ' + str(phase));
    print('fStart: ' + str(fStart));
    print('fEnd: ' + str(fEnd));
    print('loopPause: ' + str(loopPause));
    print('figSizex: ' + str(figSizex));
    print('figSizey: ' + str(figSizey));

def plotOneDWithPause(x,y):
    plot.plot(x, y);
    plot.title('One D plot');
    plot.xlabel('Time');
    plot.ylabel('y-axis');
    plot.grid(True, which='both');
    plot.show();

def plotOneDOntop(x,y):
    plot.plot(x, y);
    plot.title('One D plot');
    plot.xlabel('Time');
    plot.ylabel('y-axis');
    plot.grid(True, which='both');
    plot.pause(0.08)
    plot.show(block = False);

def plotOneDNewFigure(x,y):
    plot.close();
    plot.plot(x, y);
    plot.title('One D plot');
    plot.xlabel('Time');
    plot.ylabel('y-axis');
    plot.grid(True, which='both');
    plot.pause(0.08)
    plot.show(block = False);

def plotOneDInteractive(x,y):
    plot.clf();
    plot.plot(x, y);
    plot.title('One D plot');
    plot.xlabel('Time');
    plot.ylabel('y-axis');
    plot.grid(True, which='both');
    plot.pause(0.08) # this is the defined minimum so that the plot works
    plot.show(block = False);

def generateWave(s,f,t,p):
    return np.round(s*(np.sin(f*t + p)), precision);

def generateResonance(s,f,t,p):
    return np.round(generateWave(s,f,t,p)+generateWave(s,f,t, p + math.pi/2));

# Start
print('Hi welcome to the 2D frequency plot console app!');
while True:
    userInput = input("Enter value (h for help):")
    exit = False;
    with Switch(userInput) as case:
        if case('h'):
            print(helpMessage);
        if case('d'):
            printAllData();
        if case('fStart'):
            fStart = int(input("Enter fStart value:"));
        if case('fEnd'):
            fEnd = int(input("Enter fEnd value:"));
        if case('density'):
            density = int(input("Enter density value:"));
        if case('precision'):
            precision = int(input("Enter precision value:"));
        if case('phase'):
            phase = np.radians(float(input("Enter phase value in degrees:")));
        if case('frequency'):
            frequency = float(input("Enter frequency value:"));
        if case('scale'):
            scale = int(input("Enter scale value:"));
        if case('xstart'):
            xStart = int(input("Enter xStart value:"));
        if case('xend'):
            xEnd = int(input("Enter xEnd value:"));
        if case('figSizex'):
            figSizex = int(input("Enter figSizex value:"));
        if case('figSizey'):
            figSizey = int(input("Enter figSizey value:"));            
        if case('gl'):
            generateInitialValues();
        if case('gywave'):
            yAxis = generateWave(scale,frequency,time,phase);
        if case('p'):
            plotOneD(time,yAxis);
        if case('gwp'):
            generateInitialValues();
            yAxis = generateWave(scale,frequency,time,phase);
            plotOneD(time,yAxis);
        if case('grp'):
            generateInitialValues();
            yAxis = generateResonance(scale,frequency,time,phase);
            plotOneD(time,yAxis);
        if case('agrp'):
            while True:
                stringInput = input("Enter resonance frequency value or q to quit:");
                if(stringInput == 'q' or stringInput  == ''):
                    break;      
                    plot.close();
                else:
                    frequency = float(stringInput);  
                    generateInitialValues();
                    yAxis = generateResonance(scale,frequency,time,phase);
                    plotOneDInteractive(time,yAxis);
        if case('agwp'):
            while True:
                stringInput = input("Enter wave frequency value or q to quit:");
                if(stringInput == 'q' or stringInput  == ''):   
                    plot.close();
                    break;
                else:
                    frequency = float(stringInput);  
                    generateInitialValues();
                    yAxis = generateWave(scale,frequency,time,phase);
                    plotOneDInteractive(time,yAxis);
        if case('loopr'):
            plot.figure(figsize=(10,10))
            for freq in range(fStart,fEnd):
                generateInitialValues();
                yAxis = generateResonance(scale,freq,time,phase);
                plotOneDInteractive(time,yAxis);
                if loopPause>0:
                    Time.sleep(loopPause);
            plot.close();
        if case('loopw'):
            for freq in range(fStart, fEnd):
                generateInitialValues();
                yAxis = generateWave(scale,freq,time,phase);
                plotOneDInteractive(time,yAxis);
                if loopPause>0:
                    Time.sleep(loopPause);
            plot.close();
        if case('q'):
            break;
        if case.default:
            print('This action cannot be found. For help enter h');
    if exit:
        break;


