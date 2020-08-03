import time
from binary_search_tree import BSTNode 

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#understand have to run name_1 to go thru each name, and then run thru name_2 to see all the names there, two runs, and then run thru both to compare if there are any duplcates. Three runs total. 

#get the binary tree node class
tree = BSTNode('')
#starting location
bst = BSTNode(names_1[0])

#looping into names_1 and setting it up into a tree.
for name in names_1:
    tree.insert(name)

'''
looping into names_2 and comparing the tree that was just made in the loop of names_1. If there are the same names, and then listing out the duplicated names in duplicated = []. In real world: checking artist supply kits, checking to see if the artists use the same supplies because their work looks similar... 🤔
'''

for name2 in names_2:
    if tree.contains(name2):
        duplicates.append(name2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
#original runtime: 10.782302141189575 seconds
# mvp example runtime: 0.16977286338806152 seconds

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


