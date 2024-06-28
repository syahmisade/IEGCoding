# def GCD(n1,n2):
#     while n2>0:
#         n1, n2 = n2, n1 % n2
#     return n1

# def LCM(n1,n2):
#     return (n1*n2)/GCD(n1,n2)

# def main():
#     print("Enter two integers:")
#     n1 = int(input())
#     n2 = int(input())
    
#     gcd = GCD(n1, n2)
#     lcm = LCM(n1, n2)
    
#     print(f"Greatest common divisor of {n1} and {n2} = {gcd}")
#     print(f"Least common multiple of {n1} and {n2} = {lcm}")    

# if __name__ == "__main__":
#     main()

def main():
    n = int(input("Enter size of list\n"))
    
    if n <= 0:
        print("Invalid input")
    else:
        elements = []
        print("Enter the elements in list")
        for _ in range(n):
            elements.append(int(input()))
        
        divisible_by_13 = list(filter(lambda x: x % 13 == 0, elements))
        
        if divisible_by_13:
            print(" ".join(map(str, divisible_by_13)))
        else:
            print("No numbers divisible by thirteen")

if __name__ == "__main__":
    main()




              
