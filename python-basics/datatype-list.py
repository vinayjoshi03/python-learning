print("####### list examples ####### \n\n\n");
numberList = [10,20,30,40] # Defining list
'''
Multi line comment
'''
# Single line comment
'''
print('List contains: ', numberList);
print("Positive indexing numberList[1:] removes 10 from the above list", numberList[1:]);
print("Positive slicing numberList[start:end] removes 40 from the above list", numberList[:2]);
'''
print("Print any 5 values: ")
list1 = list();
for x in range(5):
    inputValue = input()
    list1.append(inputValue)

print('You have entered items: ', list1);





