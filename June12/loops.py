'''
Lecture by Mr.Jegan

Create a multiplication table 0f 5

1 x 5 = 5
2 x 5 = 10

* For loop == not a conditional loop (using range)
* While loop == a conditional loop
* BUT BOTH CAN HAVE BLOCK (else:)

range() == iterable object 
    - Works only in List (iterable object)
    - Can be used in loops (for) & "in" operator
    - print() DONT KNOW how to iterate them (cmd: range(1,20))
        - so we add list() => list(range(1,20))
    - Any iterate object can be typecast to a list using list()
    - range() DONT include the number so need to plus 1
        - Example:
        range from 1 until 12
        range(1,12) == will only take only 1 to 11
        range(1,13) == will take 1 to 12 (so plus 1)

while loop
    - Used when:
        - There is no range
        - When there is NO List involved
'''
multiplayers = [1,2,3,4,5,6,7,8,9,10,11,12] # But still not practical for 200
multi200 = range(1,201)
multi12 = range(1,13)
const = 5

for multiplayer in multi12:
    print(f"{multiplayer} x {const} = {multiplayer * const}")

print("="*50)
# ================================================================================

# Display the range 
print(f"Numbers of 200: {list(multi200)}")

print("="*50)
# =================================================================================

# x = int(input("Enter a number: "))
y = 97409
while(y>0):
    print(y%10) # cmd gonna print it reversed
    y //= 10 # y = y // 10

# This is using while loop
z = 12345
numDigit = len(str(z)) - 1
while(z>0):
    print(z //10**numDigit)
    z %= 10**numDigit
    numDigit -= 1

# This is using for loop
num = 98765
strNum = str(num)
for i in strNum:
    print(i)

print("="*50)
# =================================================================================

fruits = ["Apple","Orange","Mango","Banana","Grapes","Rambutan","Durian","Cempedak","Mangosteen"]
for fruit in fruits:
    print(fruit)
    if(fruit == "Durian"): 
        break # this will directly jump out and end the loop based on the condition
else:
    print("=== No more fruits left ===") # else in for loop will execute when the loop is finished

print("="*50)
# =================================================================================

multi9 = 9
multi = 1
while(multi <= 12):
    print(f"{multi} x {multi9} = {multi9 * multi}")
    multi += 1
    if(multi == 9): break
else:
    print("Multiplication table done")