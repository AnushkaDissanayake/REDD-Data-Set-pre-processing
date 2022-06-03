#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import os
file_path_main1= 'low_freq/house_1/channel_1.dat'
file_path_main2= 'low_freq/house_1/channel_2.dat'
file_path_applience='low_freq/house_1/channel_6.dat'

main_dataset1=pd.read_csv(file_path_main1,sep='\s+').values 
main_dataset2=pd.read_csv(file_path_main2,sep='\s+').values
appliance_dataset=pd.read_csv(file_path_applience,sep='\s+').values


def forward_fill(dataset):
    dataset=dataset[dataset[:,0].argsort()]
    
    time=np.array(dataset[:,0])
    
    data=np.array(dataset[:,1])
    
    
    new_time=[]
    new_data=[]
    
    for i in range(len(time)-1):
        if(time[i+1]-time[i]!=1):
            gap=time[i+1]-time[i]
            if(gap<20):
                for j in range(int(gap)): 
                    new_time.append(time[i]+j)
                    new_data.append(data[i])
            else:
                new_time.append(time[i])
                new_data.append(data[i])
                print('GAP>20:',time[i],gap,i)
                missing.append(i)
        else:
            new_time.append(time[i])
            new_data.append(data[i])
    
    new_dataset=np.zeros((len(new_time),2))
    
    new_dataset[:,0]=np.array(new_time)
    new_dataset[:,1]=np.array(new_data)
    
    return new_dataset




new_time=[]
new_main=[]
x=0
for i,timestamp_main in enumerate(main_dataset1[:,0]):
    if(timestamp_main==main_dataset2[i,0]):
        new_time.append(timestamp_main)
        new_main.append(main_dataset1[i,1]+main_dataset2[i,1])
        #print((main_dataset1[i,1],main_dataset2[i,1]))
        #x+=1
        #if(x==10):
        #    break
              
    else:
        print('No')
else:
    print('done')
    
print(len(new_time),len(new_main))
total_main=np.zeros((len(new_time),2))
    
total_main[:,0]=np.array(new_time)
total_main[:,1]=np.array(new_main)
np.save('data/house 1/main',total_main)    #Forward filled main power
np.save('data/house 1/refrigerator',appliance_dataset)    #Forward filled applience power

