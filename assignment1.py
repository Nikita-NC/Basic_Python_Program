result = []
for number in range(2000,3000):
    if number % 7 == 0 and number % 5 != 0:
        result.append(number)
print(result)        

