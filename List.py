# List is mutable,allow duplicates element, orderd in nature, hetrogeneous 

# numbers = [1,2,3,4]

# numbers.append(10) # add 10 to the end

# numbers.insert(2,15) # insert 15 at index 2

# numbers.extend([16,19,20]) # add multiple elements as list

# numbers.remove(10) # remove the first occurance of 10


# print(numbers)

# Print positive and negative elements of an List?
list = [1,2,-4,8,7]
neg_list = []
pos_list = []
for i in range(len(list)):
    if list[i] > 0:
        pos_list.append(list[i])
    else:
        neg_list.append(list[i])


print(pos_list)
print(neg_list)

# Mean of list elements
sum = 0
for i in range(len(list)):
    sum = sum + list[i]


mean = sum // len(list)
print(mean)

# Find the greatest element and print its index too
max = 0
for i in range(len(list)):
    if list[i] > max:
        max = list[i]

print(max)
index = list.index(max)
print(index)

#  Find the second greatest element
largest = list[0]
sec_largest = list[0]

for i in list:
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest:
        sec_largest = i


print(sec_largest,largest)

# check lsit is sorted or not

a = [1,2,3,4,7,1]
for i in range(len(a) - 1):
    if a[i] < a[i + 1]:
        continue
    else:
        print("Your list is not sorted")
        break
else:
    print("Your lsit is sorted")