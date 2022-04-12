# I could definitely add some formatting to this, but that's not a problem and I'll focus on the next exercises.

import json
import csv
from functools import reduce

##### Part 1 #####

police_data_file = open('911_Calls_for_Service_(Last_30_Days).csv')
police_dictionary = csv.DictReader(police_data_file)

police_dictionary_list = []

for police_call in police_dictionary:
    police_dictionary_list.append(police_call)

neighborhood_filter = filter(lambda call:call['neighborhood'] != '0' and call['neighborhood'] != '', police_dictionary_list)
neighborhood_list = list(neighborhood_filter)

# print(list(filter(lambda police_call: police_call['neighborhood'] == '0', neighborhood_filter))) #No blank neighborhoods here

zip_filter = filter(lambda call:call['zip_code'] != '0' and call['zip_code'] != '', police_dictionary_list)
zip_list = list(zip_filter)

# print(list(filter(lambda police_call: police_call['zip_code'] == '0' or police_call['zip_code'] == '', neighborhood_filter))) #no blank zips here

total_response_time_list = []
dispatch_time_list = []
total_time_list = []

for x in range(len(zip_list)):
    if zip_list[x]['dispatchtime'] == '':
        zip_list[x]['dispatchtime'] = 0
    dispatch_time_list.append(float(zip_list[x]['dispatchtime']))

for x in range(len(zip_list)):
    if zip_list[x]['totalresponsetime'] == '':
        zip_list[x]['totalresponsetime'] = 0
    total_response_time_list.append(float(zip_list[x]['totalresponsetime']))

for x in range(len(zip_list)):
    if zip_list[x]['totaltime'] == '':
        zip_list[x]['totaltime'] = 0
    total_time_list.append(float(zip_list[x]['totaltime']))

total_response_list_sum = reduce(lambda num1, num2: num1 + num2, total_response_time_list)
average_total_response_time_= total_response_list_sum/len(total_response_time_list)
print(average_total_response_time_)

dispatch_time_list_sum = reduce(lambda num1, num2: num1 + num2, dispatch_time_list)
average_dispatch_time= dispatch_time_list_sum/len(dispatch_time_list)
print(average_dispatch_time)

total_time_list_sum = reduce(lambda num1, num2: num1 + num2, total_time_list)
average_total_time = total_time_list_sum/len(total_time_list)
print(average_total_time)

##### Part 2 #####


neighborhoods = []
neighborhood_dispatch_time = []
neighborhood_total_time = []
neighborhood_response_time = []

for y in range(len(zip_list)):
    if zip_list[y]['neighborhood'] not in neighborhoods:
        neighborhoods.append(zip_list[y]['neighborhood'])

neighborhoods_statistics_list = []

for i in neighborhoods:
    neighborhood_stats_dict = {}
    
    neighborhood_filter = filter(lambda row: row["neighborhood"] == i, zip_list)
    neighborhood_list = list(neighborhood_filter)

    dispatch_time = reduce(lambda x, y: x + float(y['dispatchtime']), neighborhood_list, 0)
    average_dispatch_time = dispatch_time/len(neighborhood_list)

    total_time = reduce(lambda x, y: x + float(y['totaltime']), neighborhood_list, 0)
    average_total_time = total_time/len(neighborhood_list)

    total_response_time = reduce(lambda x, y: x + float(y['totalresponsetime']), neighborhood_list, 0)
    average_response_time = total_response_time/len(neighborhood_list)

    neighborhood_stats_dict['Neighborhood'] = i
    neighborhood_stats_dict['Average dispatch time'] = average_dispatch_time
    neighborhood_stats_dict['Average total time'] = average_total_time
    neighborhood_stats_dict['Average response time'] = average_response_time

    neighborhoods_statistics_list.append(neighborhood_stats_dict)

print(len(neighborhoods_statistics_list))

calls_file = open('Calls.json', 'w')
json.dump(neighborhoods_statistics_list, calls_file)