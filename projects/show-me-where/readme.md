
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

address 
incident_date 
alarm_dttm
arrival_dttm
close_dttm
city
zipcode
battalion
station_area
box
suppression_units
suppression_personnel
ems_units
ems_personnel
other_units
other_personnel
first_unit_on_scene
estimated_property_loss
estimated_contents_loss
fire_fatalities
fire_injuries
civilian_fatalities
civilian_injuries
number_of_alarms
primary_situation
mutual_aid
action_taken_primary
action_taken_secondary
action_taken_other
detector_alerted_occupants
property_use
area_of_fire_origin
ignition_cause
ignition_factor_primary
ignition_factor_secondary
heat_source
item_first_ignited
human_factors_associated_with_ignition
structure_type
structure_status
floor_of_fire_origin
fire_spread
no_flame_spead
number_of_floors_with_minimum_damage
number_of_floors_with_significant_damage
number_of_floors_with_heavy_damage
number_of_floors_with_extreme_damage
detectors_present
detector_type
detector_operation
detector_effectiveness
detector_failure_reason
automatic_extinguishing_system_present
automatic_extinguishing_sytem_type
automatic_extinguishing_sytem_perfomance
automatic_extinguishing_sytem_failure_reason
number_of_sprinkler_heads_operating
supervisor_district
neighborhood_district
location


## Anticipated "data wrangling"

I plan to trim the dataset to show only the records from 1 Jan 2016. 

There are 63 columns in the main data set and I am only interested in some of them. So I might rexport a new dataset with lesser coluumns after I finish the exercise. 

For the initial wrangling, I plan to use address, lat-long, primary situation description, action taken, neighbourhood, alarm dispatch time, arrival time, and closure time. 

I want to be able to see:
- Which neighbourhoods get the most calls
- What type of primary situations are the most common etc
- What property types the calls come from 
- What type of action takens are most common
- Are there any unusual call closure times 

Address is already in text, lat and long are already in separate fields per incident record and likewise for most of other fields. Timestamps will need a split strong around the 'T' character to split the time and date. The primary situation, action taken fields are text fields preceded by numercial codes in one string. I will have to extract the numerical codes and count by instances to see the most common. 
