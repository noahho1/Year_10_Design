

sum = 0
for i in range(0,101,2):
	if (i % 2 == 0): #checks if number is even
		sum = sum + i

print(sum)

sum = 0
for i in range(0,101,2):
	sum = sum + i

data = [100, 99, 98, 97, 96, 95]

sum = 0
for i in range (len(data)):
	sum = sum + data[i]

average = sum/len(data)
print average