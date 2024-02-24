my_numbers = [7,2,4,11,19,24,66,1,42,22,37,5,3,92,73]

my_string = input("Enter even or odd: ")

if my_string =="even":
    even_number = [num for num in my_numbers if num % 2 == 0]
    print("Even number:", even_number)

elif my_string =="odd" :
    odd_number = [num for num in my_numbers if num % 2 != 0] 
    print("Enter number:",odd_number)

else:
    print("Unknown Input!")      

