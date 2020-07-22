import copy
x = [3, 2, 1, 'abcd', 'hello']  # list defined
listlen = len(x)  # length of list
print('\n\nlength of list is {0}'.format(listlen))
print('Third value in list is {0}'.format(x[2]))  # access element using index

#append value/list , insert in index position
x.append(10)
print("New list is \n", x, "\n\n")
newlist = ['india', 56]
x.extend(newlist)
print("New list is \n", x, "\n\n")
x.insert(3, 'xyz')
print("New list is \n", x, "\n\n")
print("56 is at position {0} in list\n".format(x.index(56)), "\n\n")

#to remove string from list to sort using list comprehension
a = [i for i in x if not(isinstance(i, str))]
a.sort()
print("Sorted list is \n", a, "\n\n")

#to slice a list
slicedlist=x[2:5]
print("Sliced list is \n", slicedlist, "\n\n")

revlist=copy.copy(a)
slicedlist=x[2:-1]
#to slice a list with negative index
print("list accessed using negative index\n", slicedlist, "\n\n")

#to reverse a list
print("reversed list is \n", sorted(revlist,reverse=True), "\n\n")
