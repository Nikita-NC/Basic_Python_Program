def generate_square_dict(n):
    square_dict = {i:i*i for i in range(1,n+1)}
    return square_dict

n = int(input("Enter an integer number:")) 

result_dict = generate_square_dict(n)

print("Generated dictionary:")
(print(result_dict))