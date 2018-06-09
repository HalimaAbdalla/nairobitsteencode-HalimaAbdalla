for item in [1,2,3,4,5]:
    print(item)
   
for item in range(5):
   print (item**2)


counter = 1
while counter <= 5:
	print ("Hello, world")
	counter = counter + 1

#break and continue statements
count = 0
while True:
	print(count)
	count += 1
	if count >= 5:
		break

#prints out only odd numbers - 1,3,5,7,9
for y in range(10):
	#check if y is even
	if y % 2 == 0:
		  continue
	print (y)



#if else...
count=0
while(count<5):
	print (count)
	count +=1
else:
	print ("count value reached %d" %(count))


#prints out 1,2,3,4
for i in range(1, 10):
	if (i%5==0):
		break
	print (i)
else:
print ("The link is terminated by break hence don't print but not due to fail in condition")