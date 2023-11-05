import csv
from datetime import datetime


# don't import extra libraries

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    # Already done. I am freebie

    # """Takes a temperature and returns it in string format with the degrees
    #     and celcius symbols.

    # Args:
    #     temp: A string representing a temperature.
    # Returns:
    #     A string contain the temperature and "degrees celcius."
    # """

    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    # Attempted 31 October 2023: Completed 31 October PASSED and DONE
    # """Converts and ISO formatted date into a human readable format.

    # Args:
    #     iso_string: An ISO date string..
    # Returns:
    #     A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    # """

    # play with fromisoformat()

    date_object = datetime.fromisoformat(iso_string)

    return date_object.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    # Attempted 29 October 2023 - WORKING and PASSED!!!!

    return round(((float(temp_in_farenheit)) - 32) * 5/9, 1)
    # """Converts an temperature from farenheit to celcius.

    # Args:
  #  temp_in_farenheit: float representing a temperature.
    # Returns:
   # A float representing a temperature in degrees celcius, rounded to 1dp.
  #  """


def calculate_mean(weather_data):
    # attempted 28 October - Working and DONE!
    # """Calculates the mean value from a list of numbers.

    # Args:
    #     weather_data: a list of numbers.
    # Returns:
    #     A float representing the mean value.
    # """
    mean_list = []
    for item in weather_data:
        mean_list.append(item)

    sum = 0
    for items in mean_list:
        sum += float(items)
    mean = sum / len(mean_list)
    return mean

# make a list from weather_data?


def load_data_from_csv(csv_file):
    # Attempted 2 November: Working and passed!
    # mental_visualisation =
    # [[list_1_item1, list_1_item2, list_1_item3],[list_2_item1],[list_2_item2]]

    # """Reads a csv file and stores the data in a list.

    # Args:
    #     csv_file: a string representing the file path to a csv file.
    # Returns:
    #     A list of lists, where each sublist is a (non-empty) line in the csv file.
    # """
    with open(csv_file, encoding="utf-8") as my_file:
        reader = csv.reader(my_file)

        first_list = []
        for line in reader:
            # if the line in the list is empty, return nothing or print nothing? then do the fun code
            if line != []:
                # append line to list
                first_list.append(line)
            # remove [0] from the list
        first_list = first_list[1:]

        # make the strings in [1] and [2]
        for item in first_list:
            item[1] = int(item[1])
            item[2] = int(item[2])

    return (first_list)


def find_min(weather_data):
    # Attempted 2 November. Working and Passed
    # weather_data:
    # [10.4, 14.5, 12.9, 8.9, 10.5, 11.7]
    # [-10, -8, 2, -16, 4]
    # [49, 57, 56, 55, 53]
    # [49, 57, 56, 55, 53, 49]
    # ['49', '57', '56', '55', '53', '49']

    # """Calculates the minimum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The minium value and it's position in the list. + new part about second value
    # """
    # Early return:
    if weather_data == []:
        return ()
    # if not empty, then run this code:
    smallest = float('inf')
    smallest_index = -1
    for min_index, thing in enumerate(weather_data):
        if float(thing) <= smallest:
            smallest = float(thing)
            smallest_index = min_index

    return (float(smallest), smallest_index)


def find_max(weather_data):
    # Attempted 29 October 2023/1 November - WORKING AND PASSED

    # weather_data =    [49, 57, 56, 55, 57, 53, 49]
    #                                     ^ - largest max (index: 4)
    #                        ^ - max first found with index (index: 1)
    # reversed [::-1] = [49, 53, 57, 55, 56, 57, 49]
    #                                         ^ - largest max (index: 5)
    #                        ^ - max first found with index (index: 1)
    #
    # len(weather_data) = 7
    # weather_data[::-1].index(max_value) = 2
    # 7 - 2 - 1 = 4 (the largest index we are looking for)

    # """Calculates the maximum value in a list of numbers.
    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The maximum value and it's position in the list + new part about second value
    # # """

    # Early return:
    if weather_data == []:
        return ()
    # if not empty, then run this code:
    biggest = 0
    biggest_index = -1
    for max_index, thing in enumerate(weather_data):
        if float(thing) >= biggest:
            biggest = float(thing)
            biggest_index = max_index

    return (float(biggest), biggest_index)

# Ugly way to do this:
    # if len(weather_data) > 0:
    #     max_value = max(weather_data)
    #     return (float(max_value), len(weather_data) - weather_data[::-1].index(max_value) - 1)
    # else:
    #     return ()


def generate_summary(weather_data):
    # Attempted 4 November: Working and passed 5 November
    #     8 Day Overview
    #   The lowest temperature will be 8.3°C, and will occur on Friday 19 June 2020.
    #   The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.
    #   The average low this week is 11.4°C.
    #   The average high this week is 18.8°C.
    # """Outputs a summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """
    # summary = f"{len(weather_data)} Day Overview /n The lowest temperature will be {find_min(weather_data)}, and will occur on {convert_date(weather_data)}.   nl/The highest temperature will be {}, and will occur on {}.>"

    # may not use these lists if use enumerate over creating individual lists
    list_of_mins = []
    list_of_maxs = []

    lowest_temp = float('inf')
    highest_temp = float('-inf')

    # variables to store min and max date:
    min_date_time = ""
    max_date_time = ""

    # Set loop to go through weather data for index
    for daily_data in weather_data:

        # eg first interation = [0] (first day) - may be headers (no, checked), second = [1] (second day)
        # iso_string = daily_data[0]
        # pull date format from format date function. Include "---- date ----". Iso string = array [0]

        # pull minimum temp as "   Minimum Temperature:  float {min} {DEGREES_SYMBOL}" = array [1]
        min_temp = daily_data[1]
        list_of_mins.append(min_temp)
    # pull maximum temp as "   Maximum Temperature: float {max} {DEGREES_SYMBOL}" = array [2]
        max_temp = daily_data[2]
        list_of_maxs.append(max_temp)

        # find min/max:
        new_min_temp = min(list_of_mins)
        new_max_temp = max(list_of_maxs)
        if new_min_temp < lowest_temp:
            lowest_temp = new_min_temp
            min_date_time = daily_data[0]
        if new_max_temp > highest_temp:
            highest_temp = new_max_temp
            max_date_time = daily_data[0]

    # second loop to allow for indexing data to find correlating. Not needed anymore as condensed into one loop.
    # for daily_data in weather_data:
    #     if lowest_temp == daily_data[1]:
    #         min_date_time = daily_data[0]
    #     if highest_temp == daily_data[2]:
    #         max_date_time = daily_data[0]

    # find index of min max temps. do I enumerate weather data

    # correlate to isostring index

    # calculate averages:
    average_min = calculate_mean(list_of_mins)
    average_max = calculate_mean(list_of_maxs)

    # return giant string with \n existing. Functions are pulled in and combined with format function
    formatted_string = f"{len(weather_data)} Day Overview\n"
    formatted_string += f"  The lowest temperature will be {format_temperature(convert_f_to_c(lowest_temp))}, and will occur on {convert_date(min_date_time)}.\n"
    formatted_string += f"  The highest temperature will be {format_temperature(convert_f_to_c(highest_temp))}, and will occur on {convert_date(max_date_time)}.\n"
    formatted_string += f"  The average low this week is {format_temperature(convert_f_to_c(average_min))}.\n"
    formatted_string += f"  The average high this week is {format_temperature(convert_f_to_c(average_max))}.\n"

    return (formatted_string)


def generate_daily_summary(weather_data):
    # Attempted p-code 4 November: Working and passed! 5 November

    # ---- Friday 02 July 2021 ----
    #   Minimum Temperature: 9.4°C
    #   Maximum Temperature: 19.4°C

    # weather_data example:[['2020-06-19T07:00:00+08:00', 47, 46], [[266 chars] 66]]

    # """Outputs a daily summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """

    # empty string
    formatted_string = ""

    # Set loop to go through weather data for index
    for daily_data in weather_data:

        # eg first interation = [0] (first day) - may be headers (no, checked), second = [1] (second day)
        iso_string = daily_data[0]
    # pull date format from format date function. Include "---- date ----". Iso string = array [0]

    # pull minimum temp as "   Minimum Temperature:  float {min} {DEGREES_SYMBOL}" = array [1]
        min_temp = daily_data[1]
    # pull maximum temp as "   Maximum Temperature: float {max} {DEGREES_SYMBOL}" = array [2]
        max_temp = daily_data[2]
    # return giant string with \n
        formatted_string += f"---- {convert_date(iso_string)} ----\n"
        formatted_string += f"  Minimum Temperature: {format_temperature(convert_f_to_c(min_temp))}\n"
        formatted_string += f"  Maximum Temperature: {format_temperature(convert_f_to_c(max_temp))}\n\n"

    return (formatted_string)
