# Sam Ghalayini
# HW 21 Python Variable References
# 3/21/2019
#

#-Print Memory Address-#
import copy
def memAddr(v):
    return hex(id(v))

#-Shallow Copy-#
dict1 = {'Jack':{'Python':'Proficient','C++':'Fair'},'Mike':'C++'}
dict2 = dict1
print(dict1)
print(memAddr(dict1))
print("")
print(dict2)
print(memAddr(dict2))
print("")
#-Change dict2-#
dict2['Jack']['C++'] = 'Proficient'
print(dict1)
print(memAddr(dict1))
print("")
print(dict2)
print(memAddr(dict2))
print("")
#-Deep Copy-#
dict1 = {'Jack':{'Python':'Proficient','C++':'Fair','Mike':'C++'}}
dict2 = copy.deepcopy(dict1)
print(dict1)
print(memAddr(dict1))
print("")
print(dict2)
print(memAddr(dict2))
print("")
#-Change dict2-#
dict2['Jack']['C++'] = 'Proficient'
print(dict1)
print(memAddr(dict1))
print("")
print(dict2)
print(memAddr(dict2))

