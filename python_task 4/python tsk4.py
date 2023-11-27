#Arithmetic operator
Number1 = 22
Number2 = 23
print(Number1 + Number2)
print(22 + 33)

#Assignment operator
number = 1
while number < 10:
    print(number)
    number = number + 1

#Comparison operator
number3 = 4
number4 = 6
print(number3 != number4)

#Logical operator
number5 = 22
number6 = 33
print(number5 < 50 and number6 == 33)
print(not (number5 < 50 and number6 == 33))
print(number5 > 50 or number6 == 43)
print(not (number5 > 50 or number6 == 43))

#Python List
number7 = [3, 7, 19, 29, 43]
print(number7)
print(number7[2])

Vegetables = ["carrot", "beetroot", "raddish"]
Vegetables.insert(2, "apple")
print(Vegetables)

Vegetables1 = ["carrot", "beetroot", "raddish"]
Vegetables1.append("apple")
print(Vegetables1)

Vegetables2 = ["carrot", "beetroot", "raddish"]
Vegetables2[2] = "onion"
print(Vegetables2)

Vegetables3 = ["carrot", "beetroot", "raddish"]
Vegetables3.remove("beetroot")
print(Vegetables3)
Vegetables3.pop(0)
print(Vegetables3)

Vegetables4 = ["carrot", "beetroot", "raddish"]
for temp in Vegetables4:
    print(temp)
Vegetables4.sort()
print(Vegetables4)

#Python math function
import math
lst = [223, 334, 556, 7] 
print(max(lst))
print(min(lst))

import math
number8 = pow(2, 3)
print(number8)

import math
number9 = math.sqrt(64)
print(number9)

GameList = ["fortnite", "cod", "coc"] 
print("I like", GameList) 
