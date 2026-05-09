# def calculate_total(exp):
#     total = 0
#     for item in exp:
#         total+=item
#     return total

# list1 = [2100,100,500,4000]
# list2 = [4500,4600,2100,3000,1500]

# list1_total = calculate_total(list1)
# list2_total = calculate_total(list2)

# print(list1_total)
# print(list2_total)

# dictionary does not store element in any fixed order

# in dictionary element are hatrogeneous like every element is different
# In list element is homogeneous

# d = {"tom":34666,"alen":4786,"alex":4892}

# d["alice"] = 5688
# del d["alen"]
# print(d)


# Module : It is a way to reuse a code written by some one else
# import calendar
# cal = calendar.month(2026,4)
# print(cal)


# f = open("C:\\Users\\hp\\Documents\\data\\funny.txt","r")


# for line in f:
#     tokens = line.split(' ')
#     print(len(tokens))
# f.close()

book={}
book["tom"]={
    "name" : "tom",
    "address": "Vapi",
    "phone-no": 6753728922
}

book["bob"]={
    "name" : "bob",
    "address": "Silvassa",
    "phone-no": 6753732672
}

import json
s = json.dumps(book)


with open("C:\\Users\\hp\\Documents\\data\\funny.txt","w") as f:
    f.write(s)