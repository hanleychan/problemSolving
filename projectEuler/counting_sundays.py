"""
Find the number of Sundays that fall on the first of the month during the twentieth century ( 1 Jan 1901 to 31 Dec 2000)
"""

import datetime

if __name__ == "__main__":
    start_year = 1901
    end_year = 2000
    sunday_counter = 0

    for year in range(start_year, end_year+1):
        for month in range(1, 13):
            # get the weekday of the first of the month
            weekday = datetime.datetime(year, month, 1).weekday()

            if weekday == 6:
                sunday_counter += 1

    print(sunday_counter)


