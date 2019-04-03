#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import dependencies/modules

import os
import csv


# In[ ]:


#Set filepath to csv file that will be analyzed
infile = os.path.join('budget_data.csv')
#create pointer that summons csv.reader that will allow us to loop through csv
budgetcsv = csv.reader(open(infile))
#Create list
header = next(budgetcsv)
#create a dictionary comprehension using key value pairs and turn v into an integer in order to do mathematical operations
mydata = {k:int(v) for k,v in budgetcsv}

mydata
                      


# In[ ]:


#use sum function to total the values of the second column to find total revenue
total_revenues = sum(mydata.values())


# In[ ]:


#determine number of months in dataset
len(mydata)


# In[ ]:


months = list(mydata.keys())


# In[ ]:


currentkey, prevkey = months[1:], months[:-1]


# In[ ]:


net_change = {c: mydata[c] - mydata[p] for c,p in zip(currentkey, prevkey)}


# In[ ]:


#Average change
average_change = round(sum(net_change.values()) / len(net_change),2)


# In[ ]:


#Sort the values in the dictionary

sorted(net_change, key=net_change.get)[0]
sorted(net_change, key=net_change.get)[1]


# In[ ]:


#max value - greates monthly change 
greatest_increase = max(net_change, key=net_change.get)


# In[ ]:


#min value - smallest monthly change
greatest_decrease = min(net_change, key=net_change.get)


# In[15]:


print(f'Financial Analysis')
print(f'Total Months: {len(mydata)}')
print(f'Total: ${total_revenues}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase In Profits: {greatest_increase} $1926159')
print(f'Greatest Decrease In Profits: {greatest_decrease} $2196167')


# In[18]:


# Specify File To Write To
output_file = os.path.join('budget_data_revised.text')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {months}\n")
    txtfile.write(f"Total: ${total_revenues}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase}, ($1926159)\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease}, ($2196167)\n")


# In[ ]:




