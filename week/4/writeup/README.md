# Writeup 2 - Pentesting

Name: Connor LoPresti
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Connor LoPresti

## Assignment Writeup

### Part 1 (45 pts)

CMSC389R-{p1ng_as_$serv1c3}
;cat /home/flag.txt
At first I tried to use the Shellshock method shown in class. This did not prove useful in gaining access to root. I reread the prompt and saw that you wanted us to use command injection. By reading a bit up on it using the given link, I found it is quite similar to SQL injections (I guess this is common knowledge and I'm just dumb). The basic concept you use a line terminator (;) to run another command after the original. 
Using this information, I devised a way to run 'ls' on the root directory. Simply ;ls was enough to do this. We don't care about the output of the ping so we can leave it malformatted and just end the line. Anything after this would be run as a command in addition to the ping. I found that this worked well. Upon seeing the directory items, I remembered that the flag on last project was hidden in the home directory so I ran this ;cd /home;ls. This put me into the home directory and then ran ls again (from within the home directory now). I did this so that I could see the contents of the home directory as to find the location of the flag.
Once I knew the flag was in flag.txt, the only file in the home directory, I could run a single command ;cat /home/flag.txt to retrieve the contents. 

One precaution that I would advise Eric would be to sanitize his inputs. allowing for line terminators or other special characters to be used as input in very dangerous. Especially if you know your service will only be pinging ip addresses, there should be no reason a legitimate user would need to pass in these types of characters in. When receiving input, you can either stop the process outright and throw an exception, or remove the characters and continue the process without them. Either way you don't want your service to be running input with these characters.  

### Part 2 (55 pts)

For this part, I began by copying the work done from week 2. This included the socket setup and the recv() and send() commands. I created a loop that continuously requested user input. I would check these commands against the predefined ones and return results (help, quit, etc.). Here I decided that the Shell would be active immediately. Thus any of these preset commands could be run with any other Shell commands you would want to pass to the server.
Now any other commands input would be treated as commands for the server. To do this I created a function that accepts input, adds the needed syntax for command injection, and returns the output. This function must reconnect to the server for each command so I implemented a way to save the current directory location. My function will always run at least 3 commands at once on the server:
cd (into saved location)
(The command sent by the user)
pwd
This serves to move the user back to their last location, run the command in the expected location, and update the current location in case it was changed. My function then parses this information. Since I know pwd will be run last, the last line of the output will always be the current location. I separate these two things out and return both. Upon returning, the loop will process these and output the desired output while updating the current location. 
pull was done using a similar concept. It will only attempt to pull files if given 'pull (arg1) (arg2)'. Otherwise the command is considered malformed and run on the Shell (with no effect presumably).
To get the data from the requested file (arg1), I pretend the user wanted to run the cat command and do a call to my function. Instead of printing the result however, I put it into a newly created file at arg2. The program will print if it is successful or not. The only way that it should fail is if the local path does not exist. If the file doesn't exist but the path is fine, the program will make a new file as specified. 

To run stub.py, simply use
>python stub.py

It should work on all version of python 3.X
