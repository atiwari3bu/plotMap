# Plotting the map  
import scipy
import matplotlib.pyplot as plt
from scipy import ndimage
lats=[]
longs=[]

def plottingPoints(lines):
    for line in lines:
        if("lat" in line):  # Data Cleaning
            continue
        line=line.rstrip('\n')
        line=line.split(',')
        lats.append(float(line[0]))
        longs.append(float(line[1]))
   
    my_plot=plt.plot(lats,longs)
    plt.show()

def main():
    fileref=open("UDC2.csv","r")  # Reading Lines from data
    lines=fileref.readlines()
    fileref.close()
    plottingPoints(lines)

main()
