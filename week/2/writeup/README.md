# Writeup 2 - OSINT

Name: Connor LoPresti
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Connor LoPresti

## Assignment Writeup

### Part 1 (45 pts)

1. ejnorman84's real name is Eric J. Norman. This was found on a Pastebin (https://pastebin.com/4yJRgkFm). Other information included usernames and passwords (ejnorman84:p********a : ejnoman:@****************1 : EricNorman84:h*****).

2. He works at Wattsamp Energy. The works url is (wattsamp.net). This was found in his Twitter by looking up usernames seen above (https://twitter.com/EricNorman84). Other information included emails (ejnorman84@gmail.com, ejnorman@protonmail.com) 

3. His Instagram account is https://www.instagram.com/ejnorman84/. Found by using the usernames seen in part 1. Using whois.com and the ips that are shown later I found his location and phone number. (1300 Adabel Dr. El Paso TX, 79835 : +12026562837). The ip used was the last one which the server is hosted (157.230.179.99).

4. Using nmap, I was able to find a number of ips associated with the site. Server types and locations were found with iplocation.net.
	Hops (13) ([]&{} found with iplocation.net): 
	1. 192.168.1.1 (Fios_Quantum_Gateway.fios-router.home) [Fios Quantum Router]
	3. 100.41.213.212 (B3341.WASHDC-LCR-22.verison-gni.net) [Verizon Internet Services] {Washington DC}
	5. 140.222.239.77 [ANS Core Systems Inc.] {Dulles Virginia}
	6. 129.250.9.25 [NTT America Inc.] {Ashburn Virginia}
	7. 129.250.2.120 [NTT America Inc.] {Ashburn Virginia}
	8. 129.250.2.148 [NTT America Inc.] {New York New York}
	9. 129.250.4.51 [NTT America Inc.] {New York New York}
	13. 157.230.179.99 [DigitalOcean, LLC] {North Bergen New Jersey}

5. On the site itself there seemed to be a old link that is now broken (wattsamp.net/views/contact.html).

6. Also using nmap I was able to find 4 open ports. nmap had to be told to look through more ports inorder to find the larger one.
	Open ports:
		22 ssh OpenSSH 7.6p1 Ubuntu 4ubuntu0.3
		25 filtered smtp
		80 http Apache httpd 2.4.29 (Ubuntu)
		1337 waste? (Possible server) 

7. As shown, the site which is located on port 80 is running Apache/2.4.29 (Ubuntu). I actully got this infromation sooner from mxtoolbox.com.

8. I found 3! CMSC389R-{Do_you-N0T_See_this} from dnstrails.com on the last ip. CMSC389R-{n0_indexing_pls} was found on the robots.txt file of wattsamp.net. and CMSC389R-{html_h@x0r_lulz} was found in the source code in the index.html page of wattsamp.


### Part 2 (75 pts)

The file that I used to run the dictionary attack is in this directory called 'stub.py'. It is still in python and works with Python 3.X. A wordlist file is required for this program to run. I used rockyou.txt found in the standard kali wordlist libraries. This file needs to be moved to the same directory as 'stub.py'. 

To run just use: 
>Python stup.py  

Using this script, I was not able to find the login for the server. I ran into multiple issues with my script crashing due to failed socket recieves and other issues. This caused the search time to take a considerable amount of time. Especially since my computer is not the best.
As shown in the comments, I used the usernames and approx. passwords found to narrow down my search space but the program still took too long. As I am submitting this, it has not finished running. If I had more time, I might be able to find it assuming my program doesnt stop or get a false positive while I'm away. Again. 
