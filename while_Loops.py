#You are given a program that outputs all the numbers from 0 to 10.
#Change the code to make it output only the even numbers.
#Any integer that can be divided exactly by 2 is an even number.

x = 0
while x<=10:
	if x%2 == 0:
		print(x)
	x+=1
