height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_float = float(height)
weight_int = int(weight)

BMI = weight_int / height_float ** 2

print(int(BMI))