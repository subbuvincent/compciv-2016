
# About the dataset

This is San Francisco Fire Department's incidents dataset, classied as non-medical. These are incidents to which the SF Fire Department responded. It is collected from 1/1/2003. 

## A short paragraph describing the data

Each incident record includes the call number, incident number, address, number and type of each unit responding, call type (as determined by dispatch), prime situation (field observation), actions taken, and property loss. It also has the location in lat-long as well as neighbourhood in SF where the incident happened. Each record also contains the situation the call was about as well as the action taken. 


## Basic facts about the dataset

- Origin: SF Fire Department, City and County of San Francisco, via SFGov, Socrata 
- URL: [https://data.sfgov.org/Public-Safety/Fire-Incidents/wr8u-xric](https://data.sfgov.org/Public-Safety/Fire-Incidents/wr8u-xric)
- JSON URL: [https://data.sfgov.org/api/views/wr8u-xric/rows.json?accessType=DOWNLOAD](https://data.sfgov.org/api/views/wr8u-xric/rows.json?accessType=DOWNLOAD)
- CSV and XCEL formats are also available. 
- There are roughly 391,000 records since 1/1/2003.
- It is published every day. 
- 2016 Incidents only URL: [https://data.sfgov.org/Public-Safety/2016-incidents/inut-uybi](https://data.sfgov.org/Public-Safety/2016-incidents/inut-uybi)
- 2016 Incidents only JSON: [https://data.sfgov.org/api/views/inut-uybi/rows.json?accessType=DOWNLOAD](https://data.sfgov.org/api/views/inut-uybi/rows.json?accessType=DOWNLOAD)


### A description of each of the fields

**incident_number**

The incident number in the record set

**address**

Street address of incident. 

**zip code** 

Zip code in SF the address belongs to. 

**incident_date** 

Incident date.

**alarm_dttm** 

Fire incident reported date and time. 

**arrival_dttm** 

Fire personnel arrival date and time. 

**close_dttm** 

Case closing date and time. 

**primary_situation** 

What was described in the call about the problem. 

**action_taken_primary** 

What action was taken by the fire department. 

**property_use** 

Type of property - 1 bed/ 2 bed/ first floor, 2nd floor etc. 

**neighborhood_district** 

SF neigbhourhood of the address, like Lower Heights, Tenderloin etc. 

**location** 

Location of the incident - latitude and longitude. 

## Anticipated "data wrangling"

I plan to trim the dataset to carry only the records from 1 Jan 2016. 

There are 63 columns in the main data set and I am only interested in some of them. So I might re-export a new dataset with lesser coluumns after I finish the exercise. 

For the initial wrangling, I plan to use address, lat-long, primary situation description, action taken, neighbourhood, alarm dispatch time, arrival time, and closure time. 

I want to be able to see:
- Whether there any patterns on day-of-the-week calls or weekends in terms of distribution 
- Which neighbourhoods get the most calls
- What type of primary situations that lead to calls are the most common
- What property types (home, appartment, condo..etc.) the calls come from 
- What type of action takens are most common
- Are there any unusual call closure times 

What is there in the data 
- The caller address is already in text, lat and long are already in separate fields per incident record and likewise for most of other fields. 
- Timestamps will need a split strong around the 'T' character to split the time and date.
- The primary situation, action taken fields are text fields preceded by numercial codes in one string. I will have to extract the numerical codes and count by instances to see the most common. 

