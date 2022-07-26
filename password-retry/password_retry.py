password = 'a123456'
t = 3
while True: 
	t = t - 1
	pw = input('Please enter password: ')
	if pw == password: 
		print('Login Successful!')
		break
	else:
		if t > 0:
			print('Wrong Password!', t , 'times left')
		else: 
			print('STOPPPPP')
			break
