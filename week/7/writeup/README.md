# Writeup 7 - Forensics I

Name: Connor LoPresti
Section:  0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Connor LoPresti


## Assignment Writeup


### Part 1 (100 pts)
Answer the following questions regarding [this](../image) file:

1. What kind of file is it?

jpeg. This is found by running the exiftool on the file. In addtion, running strings on the file can get the byte encoding. Since the header has Exif, this indicated thats it is either a jpg or a jpeg.

2. Where was this photo taken? Provide a city, state and the name of the building in your answer.

John Hancock Center in 875 North Michigan Avenue Chicago, Illinois.
Found with gpd coords on exif tool (41°53'54.87"N 87°37'22.53"W)
Confirmed by opening up image with photo viewer and running it through a reverse image search.

3. When was this photo taken? Provide a timestamp in your answer.

The photo was taken on 8/22/2018 at 11:33 and 24 seconds. These are also provided by strings (2018:08:22 and 11:33:24)

4. What kind of camera took this photo?

The 3.99mm back camera of an iPhone 8.

5. How high up was this photo taken? Provide an answer in meters.

539.5 m Above Sea Level

6. Provide any found flags in this file in standard flag format.

CMSC389R-{look_I_f0und_a_str1ng} found with strings

CMSC389R-{abr@cadabra} found by using binwalk on image. There was a png file within the image file. Used Binwalk to extract it and opened the png image. The png image had the key in it. 
