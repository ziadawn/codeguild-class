'''
Lab 32: Rain Data

The 'City of Portland Bureau of Environmental Services' operates and maintains a network of rain gauges around Portland, a
nd publishes their data publicly: http://or.water.usgs.gov/non-usgs/bes/

The data tables available on the site look something like...
'''

import datetime

with open('mt_tabor.rain', 'r') as file:
    # print(file.read())
    raw_data = file.read()
    raw_data = raw_data.split('\n')    # split by new line. In quotes b/c it's a string
    rain_data = []
    for i in range(11, len(raw_data) - 1):
        rain_data.append(raw_data[i].split())
        rain_data[i - 11][0] = datetime.datetime.strptime(rain_data[i-11][0], '%d-%b-%Y')

    # for line in rain_data:
    #     print(line)

    # print(rain_data[20][1])

    # print(rain_data[5456][0].year)

def most_rain_day(rain_data):
    rainiest_day = [0, 0]
    for day in rain_data:
        if day[1] == '-':
            continue
        if int(day[1]) > int(rainiest_day[1]):
            rainiest_day = day
    return rainiest_day

def year_totals(rain_data):
    year_total = {}
    for day_total in rain_data:
        if day_total[1] == '-':
            continue
        else:
            # year_total[day[0].year] = year_total.get(day[0].year, 0) + int(day[1])      # code from Nick, does the same as my block below
            if day_total[0].year in year_total:
                year_total[day_total[0].year] += int(day_total[1])
            else:
                year_total[day_total[0].year] = int(day_total[1])
    return year_total

def most_rain_year(rain_data):
    rainiest_year = (0, 0)
    for key, value in year_totals(rain_data).items():
        if value > rainiest_year[1]:
            rainiest_year = (key, value)
    return rainiest_year


# def most_rain_year(year_totals):              # this also works with slight changes to the variable below (between rainiest day and year), but i'm mistting something. Going to lucnh. The code overall works
#     rainiest_year = (0, 0)
#     for key, value in year_totals.items():
#         if value > rainiest_year[1]:
#             rainiest_year = (key, value)
#     return rainiest_year


rainiest_day = most_rain_day(rain_data)
rainiest_year = most_rain_year(rain_data)

print(f'{rainiest_day[0].date()} had {rainiest_day[1]} inches of rain')
print(rainiest_year)
# print(rainiest_day[0].date(), rainiest_day[1:])     # prints whole day by the hour






# Find the day which had the most rain.
# Find the year which had the most rain on average.

