# Writeup 9 - Forensics II

Name: Connor LoPresti
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Connor LoPresti


## Assignment details

### Part 1 (45 Pts)
Warmup: what IP address has been attacked?
The ip of the victim is 142.93.136.81

What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.
It seems like a port scanner was used against the victim machine as random ports were being pinged. nmap maybe. 

What are the hackers' IP addresses, and where are they connecting from?
The attackers address is 159.203.113.181 from a server in New York run by DigitalOcean

What port are they using to steal files on the server?
They are connecting to port 21 to access and steal data.

Which file did they steal? What kind of file is it? Do you recognize the file?
They stole a file called find_me.jpg. It seems to be a jpg file which is usually an image.

Which file did the attackers leave behind on the server?
The attackers left a file called greetz.fpff

What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is not an option.
To prevent against a port scan, You can whitelist which ips have access to your servers. In addition, you could limit the number of requests to a reasonable amount that a normal user would use. 

### Part 2 (55 Pts)

When was greetz.fpff generated?
Timestamped at 1553660105 which is Wednesday, March 27, 2019 12:15:05 AM EST

Who authored greetz.fpff?
fl1nch

List each section, giving us the data in it and its type.
------- HEADER -------
MAGIC: 0x8badf00d
VERSION: 1
TIMESTAMP: 1553660105
AUTHOR: b'fl1nch\x00\x00'
SECTIONS: 5
-------  BODY  -------
ASCII OUTPUT: b'Hey you, keep looking :)'
COORDS OUTPUT: (52.336035, 4.880673)
PNG CREATED
ASCII OUTPUT: b'}R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC'
ASCII OUTPUT: b'Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30='

Report at least one flag hidden in greetz.fpff. Any other flag found will count as bonus points towards the competition portion of the syllabus.
CMSC389R-{w31c0me_b@ck_fr0m_spr1ng_br3ak} Found in image find_me.jpg
CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R} Found in section 4 and reversed
CMSC389R-{hey_h3y_y0U_you_I_dont_like_your_base64_encoding} Found in section 5 and decoding the text

