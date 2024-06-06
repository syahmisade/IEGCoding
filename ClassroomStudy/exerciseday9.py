# Try reverse the number. Expected 13579
'''
x = 97531
y = 1*10000 + 3*1000 + 5*100 + 7*10 + 9
print(y)
'''
a0 = 97531

result = a0 % 10 # r: 1
a1 = a0 // 10 # q: 9753

result = (result*10)+(a1%10) # r+r: 13
a2 = a1 // 10 # q: 975

result = (result*10)+(a2%10) # r+r: 135
a3 = a2 // 10 # q: 97

result = (result*10)+(a3%10) # r+r: 1357
a4 = a3 // 10 # q: 9

result = (result*10)+(a4%10) # r+r: 13579
a5 = a4 // 10 # q: 0

print(result, a5) # 13579

# Akmal Solution (One of the student) die nak pindah semua terus pegi hujung ke hujung

