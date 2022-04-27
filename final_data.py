#!/usr/bin/python3 

#I will use matplotlib.pyplot to draw the gragh describe the numbers of each operating system
#I uses panpas to open and read the data file
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#open and save the excel file in new varible
file = pd.read_excel('final_servers.xlsx')
#use new varible to display the file
data = pd.DataFrame(file)
print(data)

#select the colums to new variable
os = data['Operating System']

#create 2 new variables assign equal 0, I will use them to the bar.
windows_server = 0
linux = 0
#for loop to sort the os that match the required.
for i in os:
    if 'Windows Server' in i:
        windows_server += 1 
        #increase the varible if meet the if
    elif 'Linux' in i:
        linux += 1
         #increase the varible if meet the elif    
print(f'Windows Server has {windows_server}')
print(f'Linux has {linux}')

#create variable to design the bar
left_coordinates=[1,2]
#heights will be the numbers of windows and linux
heights = windows_server, linux
bar_labels=['Windows Server', 'Linux']


plt.xlabel("Operating System")
plt.ylabel("Quantity")

#using the pyplot to create the bar with height, colors, and width.
plt.bar(left_coordinates,heights,tick_label=bar_labels,width=0.25,color=['red','black'])
#make title
plt.title('Servers Chart')
#display the the bar
plt.show()

