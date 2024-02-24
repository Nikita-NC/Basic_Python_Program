def string_function(str1,str2):
    length_str1 = len(str1)
    length_str2 = len(str2)

    if length_str1 > length_str2:
        print(str1)

    elif length_str2 > length_str1:
        print(str2)

    else:
        print(str1)  
        print(str2) 

string1 = (input('Enter the length of str1: '))  
string2 = (input('Enter the length of str2: ')) 

print(string_function(string1,string2))