password = 'a123456'
i = 3
while True: 
	pw = input('Please Enter Your Password: ')
	if pw == password: 
		print('Login Successful!')
		break
	else: 
		i = i - 1
		print('Invalid Password! You have ', i ,'more times to enter')
		if i == 0:
			break
