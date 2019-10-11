# Writeup 6 - Binaries I

Name: Connor LoPresti

Section: 0101


I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Connor LoPresti


## Assignment Writeup


### Part 1 (50 pts)


CMSC389R-{di5a55-0r-d13}


### Part 2 (50 pts)


crackme took input from various sources to produce the flag. One way it does this is by looking for a file named "sesame" and doing a string comparison on the contents to see if it is " they burn". This is obfuscated by running individual character 'if' checks for each character. This was decoded by noticing that this check only returns a passing value if all characters are matched in order, so an ascii lookup was performed for each iteration of the loop in order. crackme also checked if an environment variable "FOOBAR" existed and checked to see if the contents were " my eyes". This was obfuscated as the original string on x86 is "esye ym " but the string check is done backwards. This was decoded as the check involved looking at the length 8 string in order of 8-i. Lastly crackme takes input through the use of command line arguments. The argument that needed to be passed in to get the correct output was "Oh God". This was less obfuscated than the previous sections as the string and argc flags were immediately visible. 
The flag appeared to be stored in memory and called upon using global variables. the update_flag function which takes a number of arguments, is called in each of the loops within the three checks. Each of these function calls appears to be building the flag string through a complicated and obfuscated way. The flag cannot be found within the program as it never existed in the original code. It is built using inputs given by the rest of the program. This is a good way to obfuscate information as to not hard code any data into your program. The individual character checks in check3 that got the data " they burn" was defiantly the most obfuscated and took the longest to process. However, even in that scenario we were able to return the result in plain text as shown. 