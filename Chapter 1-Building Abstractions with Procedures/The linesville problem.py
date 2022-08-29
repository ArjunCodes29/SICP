## Not part of SICP
## In Linesville, every resident lives on Main St., a long, straight road. The Linesville City Council decides to build a garden,
#  and wants to build it in the place that minimizes the sum of the squares of the distances to the residents of Linesville.
## Where should the garden be built?

## This program takes in a list of 10 numbers (the number of people livingin each house) and returns a list of 10 numbers ( the total sum of squares at if the garden was built at each location)
import random



def calculator(list,position):
    copy = position
    sum = 0
    while(position<(len(list) -1)):
        position= position + 1
        sum = sum + list[position] * ((position - copy) * (position - copy))
    copy2 = copy
    while(copy > -1):
        copy =copy-1
        sum= sum + list[copy] * ((copy2 -copy) * (copy2 -copy))
    return sum


def get_minvalue(inputlist):
 
    #get the minimum value in the list
    min_value = min(inputlist)
 
    #return the index of minimum value 
    min_index=inputlist.index(min_value)
    return [min_index,min_value]

def checkUshaped(list):
    min = get_minvalue(list)
    position_min = min[0]
    i=position_min
    while(i<(len(list)-1)):
        if(list[i]>list[i+1]):
            print("false here")
            return False
        i += 1
    ii = position_min
    while(ii>0):
        if(list[ii]>list[ii - 1]):
            print("false there")
            return False
        ii = ii - 1
    
    return True

for i in range(10000):
    randomlist = random.sample(range(0, 15), 15)
    answer = randomlist[:]
    for count,value  in enumerate(randomlist):
        answer[count]= calculator(randomlist,count)
    if(not checkUshaped(answer)):
        print('false')
    if(i==9999):
        print('true')


    

