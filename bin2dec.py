def isBinary(num) :
    return all(char in '01' for char in num)

def binary2decimal(binary) :
    decimal = 0
    binary = binary[::-1]
    for i in range(len(binary)) :
        decimal += int(binary[i]) * (2 ** i)
    return decimal

print("Welcome to Binary to Decimal Converter")
a = input("Enter the Binary number : ").strip()
if a == "" :
    print("Please enter a valid Binary number (0's and 1's only)")
elif isBinary(a) :
    print("The Decimal equivalent is : ", binary2decimal(a))
else :
    print("Enter a valid Binary number (0's and 1's only)")

