A.1 Use:
x -openssl list-cipher-commands
✓  - openssl help
help:

Standard commands
asn1parse         ca                ciphers           cmp               
cms               crl               crl2pkcs7         dgst              
dhparam           dsa               dsaparam          ec                
ecparam           enc               engine            errstr            
fipsinstall       gendsa            genpkey           genrsa            
help              info              kdf               list              
mac               nseq              ocsp              passwd            
pkcs12            pkcs7             pkcs8             pkey              
pkeyparam         pkeyutl           prime             rand              
rehash            req               rsa               rsautl            
s_client          s_server          s_time            sess_id           
smime             speed             spkac             srp               
storeutl          ts                verify            version           
x509              

Message Digest commands (see the `dgst' command for more details)
blake2b512        blake2s256        md4               md5               
rmd160            sha1              sha224            sha256            
sha3-224          sha3-256          sha3-384          sha3-512          
sha384            sha512            sha512-224        sha512-256        
shake128          shake256          sm3               

Cipher commands (see the `enc' command for more details)
aes-128-cbc       aes-128-ecb       aes-192-cbc       aes-192-ecb       
aes-256-cbc       aes-256-ecb       aria-128-cbc      aria-128-cfb      
aria-128-cfb1     aria-128-cfb8     aria-128-ctr      aria-128-ecb      
aria-128-ofb      aria-192-cbc      aria-192-cfb      aria-192-cfb1     
aria-192-cfb8     aria-192-ctr      aria-192-ecb      aria-192-ofb      
aria-256-cbc      aria-256-cfb      aria-256-cfb1     aria-256-cfb8     
aria-256-ctr      aria-256-ecb      aria-256-ofb      base64            
bf                bf-cbc            bf-cfb            bf-ecb            
bf-ofb            camellia-128-cbc  camellia-128-ecb  camellia-192-cbc  
camellia-192-ecb  camellia-256-cbc  camellia-256-ecb  cast              
cast-cbc          cast5-cbc         cast5-cfb         cast5-ecb         
cast5-ofb         des               des-cbc           des-cfb           
des-ecb           des-ede           des-ede-cbc       des-ede-cfb       
des-ede-ofb       des-ede3          des-ede3-cbc      des-ede3-cfb      
des-ede3-ofb      des-ofb           des3              desx              
rc2               rc2-40-cbc        rc2-64-cbc        rc2-cbc           
rc2-cfb           rc2-ecb           rc2-ofb           rc4               
rc4-40            seed              seed-cbc          seed-cfb          
seed-ecb          seed-ofb          sm4-cbc           sm4-cfb           
sm4-ctr           sm4-ecb           sm4-ofb           zlib              
zstd              


x -openssl version
✓  -openssl -v
   OpenSSL 3.0.x introduced a number of improvements, such as support for more cryptographic algorithms, a new Provider API, and enhanced security features.
  -

Outline five encryption methods
that are supported:



### Five Common Encryption Methods Supported:
1. AES (Advanced Encryption Standard)  
   - Key sizes: 128, 192, or 256 bits  
   - Modes: CBC, GCM, ECB, and more  
   - Use: Widely used for encrypting sensitive data due to its speed and security. Often used in SSL/TLS for securing web communications.

2. RSA (Rivest-Shamir-Adleman)  
   - Key sizes: 1024, 2048, 4096 bits (commonly)  
   - Use: Asymmetric encryption primarily used for key exchange, digital signatures, and data encryption where public/private key pairs are involved.

3. Blowfish  
   - Key sizes: 32 to 448 bits  
   - Use: A fast and compact encryption algorithm used in some systems but has largely been replaced by newer algorithms like AES.

4. 3DES (Triple Data Encryption Standard)  
   - Key sizes: 168 bits (effectively)  
   - Use: Older algorithm that applies DES three times to each data block, though it’s slower and less secure compared to AES. Still found in legacy systems.

5. ChaCha20  
   - Key size: 256 bits  
   - Use: Stream cipher that is faster than AES in software and is used in places where AES-GCM performance is insufficient. It’s often paired with Poly1305 for message authentication.




A.2 Using openssl and the command in the form:
openssl prime –hex 1111

meanwhile 1111 to hex = 457
openssl prime -hex 457
(457) is not prime

So basically the number has to be converted to hex before the openssl command is applied to check if it is prime or not

openssl prime -hex 2A  = openssl prime -hex 2A
openssl prime -hex 58D = 58D (58D) is not prime
Here's what the commands do:

42 (which is 2A in hexadecimal) is not a prime number.

1421 (which is 58D in hexadecimal) is a prime number.



A.3 Now create a file named myfile.txt (either use
Notepad or another editor).
Next encrypt with aes-256-cbc openssl enc -aes-256-cbc -in myfile.txt -out encrypted.bin

openssl enc -aes-256-cbc -in myfile.txt -out encrypted.bin –base64

*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.

Use the following command to
view the output file:

cat encrypted.bin
output: Salted__{������|{�ƅH4��P�

Is it easy to write out or transmit
the output: [No]


A.4 Now repeat the previous command and add the
–base64 option.

openssl enc -aes-256-cbc -in myfile.txt -out encrypted.bin -base64


Use following command to view
the output file:

cat mynextencrypted.bin
U2FsdGVkX1/8fw3ctIIR+5XQSPOM780u/DxnBrwxjXI=

Is it easy to write out or transmit
the output: [Yes]

A.5 Now Repeat the previous command and
observe the encrypted output.openssl enc -aes-256-cbc -in
myfile.txt -out encrypted.bin –base64 Why has it changed?

Has the output changed?
[Yes]

Why has it changed? Because of the addition of the base64 parameter

A.6 Now let’s decrypt the encrypted file with the
correct format:
openssl enc -d -aes-256-cbc -in encrypted.bin -pass pass:napier -base64

Has the output been decrypted
correctly? [Yes]

What happens when you use the
wrong password? bad decrypt error: 
-&,��C�{@v��?��b�?�R[��7�+��������
bad decrypt
40B73C13967F0000:error:1C800064:Provider routines:ossl_cipher_unpadblock:bad decrypt:../providers/implementations/ciphers/ciphercommon_block.c:112:
2��H��>�U�i��?U�*��,<y��"�i�����Ii2�


A.7 Now encrypt a file with Blowfish and see if
you can decrypt it.

enc: openssl enc -bf -in myfile.txt -out encrypted_blowfish.bin -pass pass:fish -base64

dec: openssl enc -d -bf -in encrypted_blowfish.bin -out decrypted_blowfish.txt -pass pass:napier -base64

Did you manage to decrypt the
file? [Yes]



B.1 With AES which uses a 256-bit key, what is the
normal block size (in bytes).

1. Block Size (in bytes) for AES-256:

AES (regardless of the key size, such as AES-128, AES-192, or AES-256) always uses a block size of 128 bits. Since 1 byte = 8 bits:

Block size (bytes) = 128 bits ÷ 8 = 16 bytes


Block size (bytes):
Number of hex characters for
block size:

2. Number of Hex Characters for the Block Size:

Each byte is represented by 2 hexadecimal characters (since each hex digit represents 4 bits). So for a 16-byte block size:

Number of hex characters = 16 bytes × 2 = 32 hex characters
Summary:

    Block size (in bytes): 16 bytes
    Number of hex characters for block size: 32 hex characters
   