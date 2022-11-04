# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:10:38 2022

@author: user
"""

from pymongo import MongoClient
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def mongoimport(csv_path):
    #Documents - data in mongoDB is called as Documents
    flgt_df = pd.read_csv(csv_path)
    payload = json.loads(flgt_df.to_json(orient = 'records'))
    #drop all documents
    collection.delete_many({})
    
    collection.insert_many(payload)
    

if __name__== "__main__":
    client = MongoClient("mongodb://localhost:27017")
    print(client)

    # a.Create collections “flights” inside database “airline_delayDB”
    
    
    db = client['airline_delayDB']
    #collection
    collection = db['flights']
    # Import 
    mongoimport("D:/PyMongo_Spyder/Flights_Delay.csv")   
    
    
    
    
# b. Average arrival delay caused by airlines


    allDocuments = collection.aggregate([{'$group' : 
                                          {'_id': 'null',  'averagedelay':
                                           
                                           
                                            {'$avg': '$ARRIVAL_DELAY'}}}])
        
         
    for item in allDocuments:
          print(item)
         
         
         





                                            
h.Finding airlines that make the maximum, minimum number of cancellations.

    maxCancellation = collection.aggregate([{'$match' : {'CANCELLED' : 1}},
                                            
                                            {'$group' : {'_id' : '$AIRLINE', 'count_1' : 
                                                         
                                            {'$count' : {}}}}, 
                                                
                                            {'$sort' : {'count_1' : -1}}, 
                                            
                                            {"$limit" : 1}
        
    
        
                                                      ])        
                                            
       
    for item in maxCancellation:       
            print("max :", item)   
            
           
            
           
    minCancellation = collection.aggregate([{'$match' : {'CANCELLED' : 1}},
                                             
                                              {'$group' : {'_id' : '$AIRLINE', 'count_1' : 
                                                          
                                              {'$count' : {}}}}, 
                                                 
                                              {'$sort' : {'count_1' : 1}}, 
                                             
                                              {"$limit" : 1}
         
     
         
                                                      ])        
                                             
        
    for item in minCancellation:       
            print("Min :", item)   
            
            
            
            
# # #c) Days of months with respect to average of arrival delays.
#   [Create a suitable plot using matplotlib/seaborn]
    
    avg_arrivaldelay=collection.aggregate([{'$group': {'_id':'$DAY','Avg_Days_arrivalDelay':
                                    {'$avg':'$ARRIVAL_DELAY'}}},{'$sort':{'Avg_Days_arrivalDelay':-1}}])
    
    avg_arrivaldelay_df=pd.DataFrame(avg_arrivaldelay)
    plt.style.use('seaborn-whitegrid')
    plt.figure(figsize=(10,7))
    sns.barplot(x=avg_arrivaldelay_df['_id'],y=avg_arrivaldelay_df['Avg_Days_arrivalDelay'])
    plt.xlabel('Day')
    plt.show()
                    



# # d. Arrange weekdays with respect to the average arrival delays caused.
# # [Create a suitable plot using matplotlib/seaborn]

    
    avg_arrivalDelay_weekdays=collection.aggregate([{'$group': {'_id':'$DAY_OF_WEEK', 'Avg_Arrival_Delay':
                                                {'$avg': '$ARRIVAL_DELAY'}}},{'$sort': {'Avg_Arrival_Delay': -1}}])
        
    avg_arrivalDelay_weekdays_df=pd.DataFrame(avg_arrivalDelay_weekdays)
    plt.style.use('seaborn-whitegrid')
    plt.figure(figsize = (10,7))
    sns.barplot(x=avg_arrivalDelay_weekdays_df['_id'],y=avg_arrivalDelay_weekdays_df['Avg_Arrival_Delay'])
    plt.title('Average Arrival Delay for each Weekday')
    plt.xlabel('Weekdays')
    plt.show()
    
    
# # e) Arrange Days of month as per cancellations done in descending order. 
# # [Create a suitable plot using matplotlib/seaborn]

    data_cancel = collection.aggregate([{'$match' : {'CANCELLED':1}},
                                    {'$group':{'_id':'$DAY',
                                    'Cancellation':{'$count':{}}}},
                                    {'$sort':{'Cancellation': -1}}])
    
    daysofmonth_cancellation_df=pd.DataFrame(data_cancel)
    plt.style.use('seaborn-whitegrid')
    plt.figure(figsize = (10,7))
    sns.barplot(x=daysofmonth_cancellation_df['_id'],y=daysofmonth_cancellation_df['Cancellation'])
    plt.title('Days of Month as per Cancellations in Descending Order')
    plt.xlabel('Day')
    plt.show()
    
    
    
    
    
# # f) Find the busiest airports with respect to day of week. Create a suitable plot using matplotlib/seaborn.






# # g) Find top 10 Airlines of US. Create a suitable plot using matplotlib/seaborn


    top_airlines=collection.aggregate([{ '$match':{'AIRLINE':"US"}},
            {'$group' :{'_id' : '$FLIGHT_NUMBER', 'Count1':{'$count' : {}}}},
            {'$sort':{'Count1':-1}},{'$limit':10}])                                            
                                            
    
    top_10=pd.DataFrame(top_airlines)
    sns.barplot(x=top_10['_id'],y=top_10['Count1'])
    plt.title('Top 10 Airlines of US')
    plt.xlabel('Flight Number')
    plt.ylabel('count')
    plt.show()
    
    
    
    
    
# # i) Find and show airlines names in descending that make the most number of diversions made. [Create a suitable plot using matplotlib/seaborn] 
    
    
    diversions = collection.aggregate([{'$match' : {'DIVERTED':1}},
                                    {'$group':{'_id':'$AIRLINE',
                                    'Diversion_count':{'$count':{}}}},
                                    {'$sort':{'Diversion_count': -1}}])
    
    
    diversion_df=pd.DataFrame(diversions)
    plt.style.use('seaborn-whitegrid')
    plt.figure(figsize = (10,7))
    sns.barplot(x=diversion_df['_id'],y=diversion_df['Diversion_count'])
    plt.title('Airlines with most no of diversion')
    plt.xlabel('Airlines')
    plt.show()



# j) Finding days of month that see the most number of diversion


    diversions = collection.aggregate([{'$match' : {'DIVERTED':1}},
                                    {'$group':{'_id':'$DAY',
                                    'Diversion_count':{'$count':{}}}},
                                    {'$sort':{'Diversion_count': -1}},{'$limit':1}
                                          ])
    
    for x in diversions:
        print(x)



# k) Calculating mean and standard deviation of departure delay for all flights in minutes


    departure_delay = collection.find({},{'DEPARTURE_DELAY':1,'_id':0})
    
    departure_delay_df=pd.DataFrame(departure_delay)
    print("Mean : ", departure_delay_df.mean())
    print("standard_deviation : ", departure_delay_df.std())
    
    
    
# #l) Calculating mean and standard deviation of arrival delay for all flights in minutes



    arrival_delay = collection.find({},{'ARRIVAL_DELAY':1,'_id':0})
    
    arrival_delay_df=pd.DataFrame(arrival_delay)
    print("Mean : ",arrival_delay_df.mean())
    print("Standard_deviation : ",arrival_delay_df.std())
    
# #m) Create a partitioning table “flights_partition” using partitioned by schema “CANCELLED”


# # #n) Finding all diverted Route from a source to destination Airport & which route is the most diverted route.




    diverted_route=collection.aggregate([{'$match':{'DIVERTED':1}},
                                          {'$group' :{'_id' : {'ORIGIN_AIRPORT':'$ORIGIN_AIRPORT',"DESTINATION_AIRPORT":'$DESTINATION_AIRPORT'}, 'count':{'$sum':1}}},
                                          {'$sort':{'count':-1}}
                                          ])
    df=pd.DataFrame(diverted_route)
    print("Diverted Route from a source to destination Airport \n",df['_id'])
    diverted_max=df.get('count').max()
    print("\n\n")
    print("Most diverted Route from a source to destination Airport \n",df[df['count']==diverted_max]['_id'])
    
   
    #o) When is the best time of day/day of week/time of year to fly with minimum delay
    total_delay=collection.aggregate([{'$group':{'_id':'$_id','total':{'$sum':'$ARRIVAL_DELAY'}}},{'$sort': {'total':1}},
                                      {'$limit':1}])
    for i in total_delay:
        print(i)
        
    


