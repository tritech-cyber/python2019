my_list = [i ** 2 for i in range(1, 11)]
my_file = open("output.txt", "w")
# Add your code below!
for value in my_list:
  my_file.write(str(value) + "\n")
  
my_file.close()

###########################

file2 = open("output2.txt", "w")
# Add your code below!
for i in range(10):
	file2.write(str(i) + " ")
  
my_file.close()

###########################

my_file3 = open("output.txt", "r")
print (my_file3.read())
my_file3.close()
