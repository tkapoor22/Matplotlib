import json
import numpy as np
import matplotlib.pyplot as plt
import pprint

total_airports=[]
with open('airport.json','r') as f:
    file_airports = json.loads(f.read())
    total_airports += file_airports

No_of_data_points= len(total_airports)
#print(No_of_data_points)

# count the total no. of flights delayed from 2003-2016 across the US
delayed_count={} # keys = year, values = number of delayed flights per year
for year in [2003, 2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]:
    delayed_count[year]=0
for airport in total_airports:
    year = airport['Time']['Year']
    delayed_no = airport['Statistics']['Flights']['Delayed']
    delayed_count[int(year)] += delayed_no
#print('delayed_count=',delayed_count)

# count the total no. of flights delayed from 2003-2016 across the US
ontime_count={} # keys = year, values = number of delayed flights per year
for year in [2003, 2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]:
    ontime_count[year]=0
for airport in total_airports:
    year = airport['Time']['Year']
    ontime_no = airport['Statistics']['Flights']['On Time']
    ontime_count[int(year)] += ontime_no
#print('ontime_count=',ontime_count)


#removing 2013 data
delayed_count2={}
ontime_count2={}
key_del=2003
for key, value in delayed_count.items():
    if key is not key_del:
        delayed_count2[key] = value
for key, value in ontime_count.items():
    if key is not key_del:
        ontime_count2[key] = value
print('delayed_count=',delayed_count2)
print('ontime_count=',ontime_count2)

#removing 2016 data
delayed_count3={}
ontime_count3={}
key_del2=2016
for key, value in delayed_count2.items():
    if key is not key_del2:
        delayed_count3[key] = value
for key, value in ontime_count2.items():
    if key is not key_del2:
        ontime_count3[key] = value
print('delayed_count=',delayed_count3)
print('ontime_count=',ontime_count3)


# Plotting the graph
# line 1 points
x1 = delayed_count3.keys()
y1 = delayed_count3.values()
# plotting the line 1 points 
plt.plot(x1, y1, label = "Delayed")
# line 2 points
x2 = ontime_count3.keys()
y2 = ontime_count3.values()
# plotting the line 2 points 
plt.plot(x2, y2, label = "On-time")
plt.xlabel('Year')
# Set the y axis label of the current axis.
plt.ylabel('No. of Flights')
# Set a title of the current axes.
plt.title('No. of flights that were On-time or Delayed in the US from 2004-2015')
# show a legend on the plot
plt.legend()
#Edit the x and y axis units
plt.axis(xmin=2003, xmax=2016, ymin=0, ymax=3500000)
plt.xticks(np.arange(2004,2016,1))
plt.yticks(np.arange(0,3500000,250000))
#Adding a market
plt.plot(x1, y1, color='blue' , marker='o', markersize=5)
plt.plot(x2, y2, color='orange' , marker='o', markersize=5)
#plot legend
plt.legend(loc='upper right',prop={'size':10})
# Remove exponetns from y axis 
plt.ticklabel_format(useOffset=False, style='plain')
#space out x axis and increase figure size
plt.tick_params(axis='x', which='major', labelsize=10)
# Display a figure.
plt.show()

"""
fig,ax = plt.subplots()
ax.plot(delayed_count.keys(),delayed_count.values())
plt.show()


#print(airport['Time']['Year'])
    # year = airport['Time']['Year']
    pprint.pprint(airport)
    print(airport['Statistics']['Flights']['Delayed'])
    braek
    #delayed_no = ['Flights']['Delayed']
    #delayed_count[int(year)] += delayed_no

    #pprint.pprint(airport)
    #year = ['total_airports']['year']
    #print('year=',year)

   #delayed_count[int(year)] += "delayed"
"""
