# Writeup 10 - Crypto I

Name: Connor LoPresti
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Connor LoPresti


## Assignment details

### Part 1 (45 Pts)
1. The first 16 bytes are the hashed password known as the key. The next 16 bytes are the hash of the ctext. The next 16 bytes are the iv. The rest of the ledger is the ctext.
2. We are using md5 to hash a key. However, we are only using the last 2 bytes. This poses a major problem as this only leaves 16 bits for the hash space. That is 2^16 or 256 unique hashes. With a message space of 256 bits, (2^256 or over 10^77 unique messages available) we are bound to find a collision somewhere. This means it would be possible to brute force passwords until one produces a hash that is the same as the key we want. 
3. Since we know the total number of bytes in the file, we can discern the length of the ctext that is in the ledger. We know 16+16+16=48 bytes are used at the beginning as shown in the first question. This leaves the rest for ctext whose length can be found before decryption.
4. The ctext is created by running the ptext through an aes128 encryption. We receive the ptext again by decryption the ctext also using aes128. The key is created by taking the last two bytes of the md5 hashed password 
5. The contents of the cipher text of the ledger itself hashed to ensure integrity. If the hashes do not line up then we know there was some tampering. However, since the hash is stored in the ledger, this can also be modified to match a tampered ledger. 
6. The key that is created with the password (256 unique keys) is then itself hashed into a new key. This new hash is checked to ensure authenticity. Since the original message space is so small, even though the hash space has the potential for 2^256 hashes, if 256 messages will only ever be passed to it, then the hash space will also only reflect the 256 inputs. Since the key is already hashed, this adds little to no new security to the program as we could just compare the prehashed (hash of input password) keys to ensure authenticity. 
7. The iv is created using the RAND_bytes function and stored in the ledger. Since the iv contains no confidential information, this implementation should be fine. 

### Part 2 (45 Pts)

### Part 3 (10 Pts)
Ideally, a cryptographic method should be secure without the need to be obscure. Obfuscating code is an unreliable way to add security. This method may increase the time needed to formulate an attack, but adds no further complexity or security to the underlying method. Obscuring code makes it harder for attackers to read, but also make it harder for peers and genuine testers to understand too. In addition, mistakes could be made when obfuscating code which my change the underlying functionality and introduce security flaws. If an attacker can break your encryption scheme before you obfuscate code, then there is no reason why they shouldn't be able to break the same code when obfuscated. 
With the rise of Artificial Intelligence and other Machine Learning algorithms, it may be possible in the future for these algorithms to scan and run code to detect vulnerabilities and calculate the security of an encryption scheme. These algorithms wouldn't care how obscured or hard to read the code is. If your code is not secure, there will be methods to find these insecurities. 