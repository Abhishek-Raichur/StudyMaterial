#List is nothing but an Array

TestList = ["One", "Two", "Three", "Four"]

print("\nList before Append")
for i in TestList:
    print(i)

TestList.append("Five")

print ("\nList after Append")
for i in TestList:
    print(i)

print ("\n Use index to print content")
print (TestList[2])

List1=[2, 4, 6, 8]
List2=[1, 3, 5, 7, 9]

Numbers=List1+List2

print("Concatinating two List = {}".format(Numbers))
print("Sorted List but Numbers list will be not modified = {}".format(sorted(Numbers)))
print("----------------------------------------")
print("concatinated unsorted list = {}".format(Numbers))
print("Sorts the number list itself and returns none = {}".format(Numbers.sort()))
print("Sorted number list = {}".format(Numbers))