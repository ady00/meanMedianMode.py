from collections import Counter
import csv

#mean
def getMean(total_weight, total_entries):

    mean = total_weight / total_entries
    print("Mean is {mean:2f}")



#median
def getMedian(total_entries, sorted_data):
    if total_entries % 2 == 0:
        median1 = float(sorted_data[total_entries//2])
        median2 = float(sorted_data[total_entries//2 - 1])
        median = (median1 + median2) / 2
    else:
        median = float(sorted_data[total_entries//2])
    print("Median is{median:2f}")



#mode
def getMode(sorted_data):   
    data = Counter(sorted_data)
    modeDataRange = {
                            "75-85": 0,
                            "85-95": 0,
                            "95-105": 0,
                            "105-115": 0,
                            "115-125": 0,
                            "125-135": 0,
                            "135-145": 0,
                            "145-155": 0,
                            "155-165": 0,
                            "165-175": 0
                        }
    for weight, occurence in data.items():
        if 75 < weight < 85:
            modeDataRange["75-85"] += occurence
        elif 85 < weight < 95:
            modeDataRange["85-95"] += occurence
        elif 95 < weight < 105:
            modeDataRange["95-105"] += occurence
        elif 105 < weight < 115:
            modeDataRange["105-115"] += occurence
        elif 115 < weight < 125:
            modeDataRange["115-125"] += occurence
        elif 125 < weight < 135:
            modeDataRange["125-135"] += occurence
        elif 135 < weight < 145:
            modeDataRange["135-145"] += occurence
        elif 145 < weight < 155:
            modeDataRange["145-155"] += occurence
        elif 155 < weight < 165:
            modeDataRange["155-165"] += occurence
    mode_range, mode_occurence = 0, 0
    for range, occurence in modeDataRange.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
    print("Mode is {mode:2f}")

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)



total_weight = 0
total_entries = len(file_data)
sorted_data = []


for person_data in file_data:
    total_weight += float(person_data[2])
    sorted_data.append(float(person_data[2]))



sorted_data.sort()




#runs the functions 
getMean(total_weight, total_entries)
getMedian(total_entries, sorted_data)
getMode(sorted_data)


