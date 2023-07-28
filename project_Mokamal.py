# firts task
import math

listofnums = input(
    "Write the numbers with space between each numbers : ").rstrip().split()

meanofnumbers = 0
sumitionofnums = 0

for num in listofnums:
    sumitionofnums += int(num)

print("The mean of the numbers is : "+str((sumitionofnums/len(listofnums))))

listofnums.sort()
if (len(listofnums) % 2 == 0):
    index_of_median = int(len(listofnums)/2)
    list_of_two_middlenumbers = []
    for index in range(index_of_median, index_of_median+2):
        list_of_two_middlenumbers.append(index)

    print(list_of_two_middlenumbers)


else:
    print("The median of the nums is : " +
          listofnums[math.floor(len(listofnums)/2)])

# second one :

for num in range(11):
    if num % 2 == 0:
        continue
    print(num)

print("\n\n")
number = 0
while (number <= 10):
    if number % 2 == 0:
        number += 1
        continue
    print(number)
    number += 1

# Third one


sandwich_orders = ["Tuna", "burgar", "Kofta", "Chiken", "Cheese"]
finished_sandwiches = []

for sandwitch in sandwich_orders:
    finished_sandwiches.append(sandwitch+" Has been made , Cost :100$")


for sandwitch in finished_sandwiches:
    print(sandwitch + " , Ready for eating!")
