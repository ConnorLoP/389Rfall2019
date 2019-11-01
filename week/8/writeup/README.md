# Writeup 8 - Binaries II

Name: Connor LoPresti
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Connor LoPresti

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding the server executable (for which source is provided).

1. How is the per-session administrator password generated? Are there any inherent weaknesses in this implementation?

The rand function is seeded with the current time. rand() % ('z'-' ') + ' ' returns an int which is a valid ascii character. All 16 of these ints are stored on the stack followed by a 0 (17 ints total). This password is still saved on the stack as a pointer, so it should be vulnerable to string formating injections.

2. Describe two vulnerabilities in this program. Provide specific line numbers and classifications of the vulnerability. Explain potential ramifications as well as ways to avoid these vulnerabilities when writing code.

On line 68, the use of gets() is very vulnerable. This can lead to overflow attacks as the input could overflow the buffer size. Line 46, as described above this printf() of the input can be used to inject string formaters and find pointers or refrences to other strings on the stack. 

3. What is the flag?

CMSC389R-{expl017-2-w1n}

4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.

Since I knew there was a way to printf() user input, I tried to create a string formatter that would show me the password pointer on the stack. So I figured I needed "%x$y" where x is the offset and y is the string formatter. This formatter would need to be given to the encrypt or decrypt functions to get the printf() output (both are same function). I needed to figure out the offset of the string from the current stack pointer location. I know that the string is 16 bytes long so I tried %16$s and got some very weird outputs. After looking through the code for a bit I remembered that the function head is also stored on the stack (learned from 430 compilers that I am taking this semester). In addition, I know that the function pointer should only be 8 bytes. Trying %24$s still lead me nowhere however. I continued to try d and u to no avail. However, when I tried x (%24$x) it just returned %k. This confused me untill I realized that my input string was still being encrypted/decrypted (duh). So when I tried %24$k with the hopes of it turning into %24$x, the output was human readable. Infact, it looked like a pointer. This made me readup on the different letters to see what they would actully do in printf(). Turns out I DO want the s formatter but I need to get the decrypted value of it first. I finally found %24$d => %24$s and got a 16 character string. When using this string to authenticate it worked!
That part was definatly the most time consuming. Once I had admin privileges, I tried ls sicne I knew it should work. This showed me that the file 'flag' was directly in the home directory. I needed a way to read the contents using a command not listed. Looking at the exec_command() function I was able to create a method to overflow the gets() buffer and input my own commands. I used 'cat flag^@ (32 spaces) cat flag ^@' (^@ stands for the null terminator given by Ctrl+@). This gave me the contents of flag. In some more testing with other functions, to prefrom this overflow attack, you only need atleast a total of 33 characters since that is the size of the buffer. Any more is fine as long as both commands are null terminated, but atleast the size of the buffer is required. 