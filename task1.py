# Use random module with a seed of 2020 to generate 20 integers between 100 and 120 (inclusive). 
# Then write code to calculate the median and mode.  
# The median is the 10th largest number. 
# The mode is the number that occurs the most. 
# If two or more number have the same frequency, list them all.

import random

#seed of 2020
random.seed(2020)

#contstant for range of 20 numbers
INTEGER = 20

#create list which populates number between 100 and 120 (inclusive)
random_number = [random.randrange(100, 121) for _ in range(INTEGER)]
print(f'\nList of random number is: {random_number}\n')

#Function to find the median
def median_value(values):
    """This function finds the median value for a given list of integers"""
    random_number_sorted = sorted(random_number)
    if len(random_number) % 2 == 0:
        median_index1 = int((len(random_number) / 2) - 1) #since index value starts from 0 and not 1
        median_index2 = int(len(random_number) / 2)
        median = (random_number_sorted[median_index1] + random_number_sorted[median_index2]) / 2        
    else: 
        median_index = int((len(random_number) / 2) - 1)
        median = (random_number_sorted[median_index])        
    print(f'The median for this list of numbers is {median}\n')
    

def mode_value(values):
    """This function returns mode or multi mode for a given list of integers"""
    #values = [119, 119, 119, 120, 123, 123, 123, 125, 125] #Test multimode
    mode_dict = {}
    # generate the frequency of a number in the list and store it in mode_dict
    for i in values:
        mode_dict[i] = mode_dict.get(i, 0) + 1
    #print(mode_dict)
    
    # variables for storing the mode number and its frequency
    mode_frequency = 0
    
    # get the highest frequency and its corresponding number
    for _ , frequency in mode_dict.items():
        if frequency > mode_frequency:
            mode_frequency = frequency            
        else: pass
    
    # print a single mode or multi mode 
    # Iterate through the dictionary items and match the mode frequency with the values, can be 1 or more
    print('The mode for this list of numbers is as following: ')
    print(f'{"Number":>5} {"Frequency":>10}')
    for key, value in mode_dict.items():
        if value == mode_frequency:
            print(f'{key:>5} {value:>8}')
    

median_value(random_number)

mode_value(random_number)

#End