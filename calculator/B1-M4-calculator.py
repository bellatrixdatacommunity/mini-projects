import math
title="Calculator"
print("-----------------------------------------------------------------------------------------------------------")
print(title.center(100))
print("-----------------------------------------------------------------------------------------------------------")
print("Select your option:")
le=[]
result_dict={}
count=1
result=0
while(1):
	print("1:Addition\t","2:Subtraction\t","3:Multiplication\t","4:Division\t","5:sin\t","6:cos\t","7:tan")
	choice=input("Enter your choice: ")

	if choice=='1':
		num1=float(input('Enter 1st number: '))
		num2=float(input('Enter 2nd number: '))
		result=num1+num2
		string=str(num1)+'+'+str(num2)
	elif choice=='2':
		num1=float(input('Enter 1st number: '))
		num2=float(input('Enter 2nd number: '))
		result=num1-num2
		string=str(num1)+'-'+str(num2)
	elif choice=='3':
		num1=float(input('Enter 1st number: '))
		num2=float(input('Enter 2nd number: '))
		result=num1*num2
		string=str(num1)+'*'+str(num2)
	elif choice=='4':
		try:
			num1=float(input('Enter 1st number: '))
			num2=float(input('Enter 2nd number: '))
			result=num1/num2
		except:
			result="Error: Dividing by zero!"
		string=str(num1)+'/'+str(num2)
	elif choice=='5':
		x=int(input("Enter the angle: "))
		y=math.radians(x)
		result=math.sin(y)
		string='sin '+str(y)
	elif choice=='6':
		x=int(input("Enter the angle: "))
		y=math.radians(x)
		result=math.cos(y)
		string='cos '+str(y)
	elif choice=='7':
		x=int(input("Enter the angle: "))
		y=math.radians(x)
		result=math.tan(y)
		string='tan '+str(y)
	else:
		print("Invalid choice!")
	le.append(string)
	result_dict[count]=result
	count=count+1
	print(string,"=",result)
	choice1=input("Do you want to perform any other operation: 1:Yes \t2:No\n")
	
	if choice1!='1':
		break
	print("-----------------------------------------------------------------------------------------------------------")
	print("Result history".center(100))
	for i in range (len(le)):
		print(le[0],'\t',result_dict[i+1])
	print("-----------------------------------------------------------------------------------------------------------")
