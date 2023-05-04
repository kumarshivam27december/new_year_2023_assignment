# list is used to store multiple item in a sinngle varaiable 

# [10,20,30,40] array of no / list of no 
# could be of same or different data types 

# stores collection of data 
# start from index 0
# ordered collection i.e. it is stored contigous memory location [0,1,2,3] how you wanted to add in 
# the last like 4 to became [0,1,2,3,4]
# list iis changeble (change ,add,remove 'item from the list') 
# it also allows duplicate value or item 
list= [10,20,30,40]
print(list)
print(type(list))

newlist = [10,20,30,40,"apple","orange",33.0,None,True,False]
print(newlist)
print(type(list))
print(list[0])
print(list[1])
print(list[2])
print(list[3])
# print(type(list[4]))
# print(type(list[5]))
# print(type(list[6]))
# print(type(list[7]))
# print(type(list[8]))
# print(type(list[9]))


# listone=['abcd',40,True,60,'apple']

#  object oreinted programming 
# CREATING A LIST THROUGH CONSTRUCTOR 
listone=((10,20,30))
listtwo=[10,20,30]
print(listone)
print(listtwo)
print(type(listone))

# accessing the list item 
list1=[10,20,30,40,50]
print(list1[2:5])  # this means search will start at index 2 (include) ,and end at index 5 (not included)
print(list1[:4])


list3=[30,60,10,20,80]
list3[1] = 90
list3[2] = "hello"
print(list3)
    #  changes a range of items 
list3[1:3] = ["Hi","Bye"]
print(list3)


# insert more item than replace remaining items will be inserted at the index that we provided
# extra element will be inserted just after that 
# adding the list items , insert item

list5= [10,20,30]
list5.insert(2,40)    # that is to insert 40 at place 2
print(list5)

# append items used for adding the items at the end of the list 
list6=[10,20,30,40]
list6.append(50)
list6.append(60)
print(list6)

# extend a list ,,,to . append or to add element from another list into  the current list we use extent()
list7=[10,20,30,40]
list8=[50,60,70,80]
list7.extend(list8)
print(list7)
print(list8)

list7.extend(list7)
print(list7)
list8.extend(list8)
print(list8)

# you can add or append any kind of iterable objects like tuples,sets,dictionaries etc 
list9=[10,20,30]
tuple=(50,60)
list9.extend(tuple)
print(list9)

# remove a specified item from the list 
mylist=['john','peter','sona','shivam','bhardwas','kumar','singh']
mylist.remove('kumar')
print(mylist)

mylist.pop(2)
print(mylist)

# it will automatically remove last  
mylist.pop()
# again 
print(mylist)

mylist.pop()
mylist.pop()
mylist.pop()

print(mylist)
mylist.pop()
print(mylist)

# remove items from specified index
mynewlist=['patna','bihar','india','asia']
del mynewlist[2]
print(mynewlist)

# empty the list 
mynewlist.clear()
print(mynewlist)

# loop 
myotherlist=[10,20,30,40,50]
for x in myotherlist :
 print(x)
 
myanotherist="hello my name is slim shady"
for x in myanotherist :
    print(x)
    
# loop through the index 
mylist01=[10,20,30,40,50]
print(len(mylist01))
print(range(len(mylist01))) 
    
for x in range(len(mylist01)) :
    print(x)  
    
mylist02=[10,20,30,40,50,60,70,80,90]
length=len(mylist02)
rangeofmylist = range(length)  
print(rangeofmylist)
for x in rangeofmylist :
    print(x) 
    
    
####SORTING THE INDEX    
#  LIST SORTING 
# SHORT IN ALPHA NUMERIC ORDER DEFAULT IT IS ASCENDING 

my_list=['banana','oranges','apple','guava']
my_list.sort()
print(my_list)
   
my_list1=[90,400,200,20,10,50]
my_list1.sort()
print(my_list1)    
    
#  sorting in descending order    
my_list1.sort(reverse=True)
print(my_list1)

# case sensitivee sorting 
my_list.sort(key=str.lower)
print(my_list)


# by default sort() is case sensitive 
# all the capital letter will be sorted before lower case 


my_list.reverse()
print(my_list)   #it reverse order of the list

# COPYINGG THE LIST 
list10=[10,20,30,40] #original array
list11=list10   #copy list
print(list11)

list11.pop()
print(list11)

print(list10) #should not be affected 
# but above process is affecting the original list 

list11=list10.copy()
print(list11)
list11.pop()
print(list10)
print(list11)

# another way of copying the list 

# list20 = list(list10)
# print(list20)
# list20.pop()
# print(list10)
# print(list20)





