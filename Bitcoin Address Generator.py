import secrets
import random
import blocksmith # "pip install blocksmith" to install module
import time # "pip install time" to install time module

# Open the file in read mode to generate bitcoin input seed
with open("english.txt", "r") as file: #replace file name with own word list if needed
    allText = file.read() 
    words = list(map(str, allText.split())) 
i = 0
s = ""

# Generates seed for bitcoin addresses using 12 random words. This is not the nemonic seed
while i < 12:
    i = i + 1 
    r = random.choice(words)
    s = s + " " + r

# Generates bitcoin addresses
kg = blocksmith.KeyGenerator()
kg.seed_input(s)
key = kg.generate_key()
address = blocksmith.BitcoinWallet.generate_address(key)

print("Private key(HEX): " + key) #Write down HEX as it is your private Key
print("Bitcoin Address: " + address)

print("")

 
