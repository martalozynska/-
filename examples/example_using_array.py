#task 3.4 + 3.7 (file array.py)
from arrays import Array
import random

arr = Array(100) #creatiing an array with size 100

for element in range(len(arr)) :
    arr[element] = random.random()  #filling the array with random numbers
for i in range(len(arr)) :
    print(arr[element])         #printing the elements which contain array