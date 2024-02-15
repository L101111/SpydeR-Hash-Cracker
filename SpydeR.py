import hashlib
import random
import sys
import argparse
import time

logos = [
    """
        ███████╗██████╗ ██╗   ██╗██████╗ ███████╗██████╗ 
        ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
        ███████╗██████╔╝ ╚████╔╝ ██║  ██║█████╗  ██████╔╝
        ╚════██║██╔═══╝   ╚██╔╝  ██║  ██║██╔══╝  ██╔══██╗
        ███████║██║        ██║   ██████╔╝███████╗██║  ██║
        ╚══════╝╚═╝        ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                       Made by hei$enberg      
                
                                                  
    """,

    """
        .------..------..------..------..------..------.
        |S.--. ||P.--. ||Y.--. ||D.--. ||E.--. ||R.--. |
        | :/\: || :/\: || (\/) || :/\: || (\/) || :(): |
        | :\/: || (__) || :\/: || (__) || :\/: || ()() |
        | '--'S|| '--'P|| '--'Y|| '--'D|| '--'E|| '--'R|
        `------'`------'`------'`------'`------'`------'
                                      Made by hei$enberg
 
                                                   
    """,

    """
         :::===  :::====  ::: === :::====  :::===== :::==== 
         :::     :::  === ::: === :::  === :::      :::  ===
          =====  =======   =====  ===  === ======   ======= 
             === ===        ===   ===  === ===      === === 
         ======  ===        ===   =======  ======== ===  ===
                                          Made by hei$enberg
 
                                                  
                                                            
    """,
    """
           ___|                     |         _ \  
         \___ \   __ \   |   |   _` |   _ \  |   | 
               |  |   |  |   |  (   |   __/  __ <  
         _____/   .__/  \__, | \__,_| \___| _| \_\ 
                 _|     ____/   Made by hei$enberg 
                                                   
    
    """
]
if len(sys.argv)>1:
    if sys.argv[1]=="-h" or sys.argv[1]=="--help" or sys.argv[1]=="help":
        print("""
   ______                 _       ______  
 / _____)               | |     (_____ \ 
( (____  ____  _   _  __| |_____ _____) )
 \____ \|  _ \| | | |/ _  | ___ |  __  /       Welcome to SpydeR!
 _____) | |_| | |_| ( (_| | ____| |  \ \       
(______/|  __/ \__  |\____|_____|_|   |_|      
        |_|   (____/   Made by hei$enberg                         
        

SpydeR is a powerfull yet simple tool for cracking hashes with over 10 hashing algorithms.
To use the tool, just enter in your terminal:

    python3 SpydeR.py /path/to/your/wordlist

Otherwise you can just run the tool and enter the path later.
        
        ***

Supported algorithms:  
MD5
SHA1
SHA224
SHA256
SHA384
SHA512
BLAKE2b (512-bit)
BLAKE2s (256-bit)
SHA3_224
SHA3_256
SHA3_384
SHA3_512
SHAKE128
SHAKE256

    "Men rise from one ambition to another: first, they seek to secure themselves against attack, and then they attack others." 
        - Niccolò Machiavelli
                    """)
        sys.exit()

algorithms = ['blake2b', 'blake2s', 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'sha512', 'shake_128', 'shake_256']

print(random.choice(logos))

print('Welcome to the best hash cracker in all multiverses!')
print(' ')
try:
    while True:
        chosen_alg = input("""Choose one of the available algorithms: 
            blake2b, blake2s, md5, sha1, 
            sha224, sha256, sha384, sha3_224, 
            sha3_256, sha3_384, sha3_512, sha512, 
            shake_128 
            $> """)
        if chosen_alg in algorithms:
            break
        else:
            print('Invalid input: choose one from the provided list.')

    if len(sys.argv) > 1:
        wordlist_path = sys.argv[1]
    else:
        wordlist_path = input("Enter the path to the wordlist file: ")

    hash_input = input("Enter the hash you want to destroy$> ")

    animation = "|/-\\"
    idx = 0

    with open(wordlist_path, 'rb') as f:
        passwords_list = f.read().decode('latin-1').splitlines()

    cracked = False

    for i in passwords_list:
        sys.stdout.write("\r" + "\033[91m" + animation[idx % len(animation)] + "\033[0m" + " Cracking Hash ")
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
        
        x = hashlib.new(chosen_alg, i.encode()).hexdigest()
        if hash_input == x:
            print(' ')
            print('THE HASH IS CRACKED!!!!!!!')
            print(f'    $$ {i} $$')
            cracked = True
            break

    if not cracked:
        print('We are sorry, we couldnt crack the hash...')
except:
    print(' ')
    print('Exiting...')
