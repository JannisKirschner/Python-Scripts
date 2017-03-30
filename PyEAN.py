#!/usr/bin/env python

#This software is for a small school project.
#It's for the module: "Modul 100: Daten charakterisieren, aufbereiten und auswerten"
#Feel free to use, change or distribute the script as much as you like
#Thanks for checking it out! :)
#The neat ASCII art is by http://patorjk.com/software/taag/

"""PyEAN: Software to validate EAN checksums."""

__author__      = "Jannis Kirschner"
__copyright__   = "GNU General Public License v3.0"

import time

logo = """
	       ___      ___   _   _  _   
	      | _ \_  _| __| /_\ | \| |  
 	      |  _/ || | _| / _ \| .` |  
 	      |_|  \_, |___/_/ \_\_|\_|  
    	           |__/   https://github.com/JannisKirschner"""


def init():
#gives you a warm welcome 
    print("-------Welcome to PyEAN-------")
    print(logo + "\n")

def inputBarcode():
#creates the global barcode variables and gets your input
    global barcode
    global barcode2
    while True:
        try:
            barcode = input("Enter your Barcode: ")
            barcode2 = list(map(int,str(barcode)))
            return barcode2
        except ValueError:
            print("Are you sure you entered a number?")
            continue
        break

def load():
#prints the loading animation -> remove it to save some time (less cool though ;P)
    t = 10
    print("Checking", end="")
    while(t>0):
        print(".", end="")
        time.sleep(0.5)
        t=t-1
    print("")

def checkSize():
#checks the size of the barcode and calls further functions
    if(len(barcode2)==13):
        validate()            

    elif(len(barcode2)==12 or len(barcode2)==13 ):
        print("It seems your EAN is one character off...")
        print("Try it again!")
        return
        
    else:
        print("Error: bad size")
        return

def validate():
#validates the barcode, further information about the algorithm at the bottom
    for i in range (len(barcode2)):
        if(i & 1): barcode2[i] = barcode2[i]*3
        else: barcode2[i] = barcode2[i]*1
    
    if(sum(barcode2) % 10 == 0):
        restsumme = 0
        for y in range(len(barcode)):
            restsumme = restsumme + barcode2[y]
        print("Your checksum is: " + str(restsumme))    
        print("Valid checksum! :)")        
    else:
        print("Checksum is invalid! :(")
        invalid()

def invalid():
#calculates a correct checksum at failure
    try:
        restsumme = 0
        for y in range(len(barcode)):
            restsumme = restsumme + barcode2[y]

        print("Your checksum is: " + str(restsumme))
        count = 0
        while(restsumme % 10 != 0):
            restsumme = restsumme + 1
            count = count + 1
        print("Valid Checksum: " + str(count))

    except IndexError:
        if(len(barcode2)!=13):
            print("Fatal Error: Bad Size")
            


    
def verify():
#verifies an existing checksum
    inputBarcode()
    load()
    checkSize()

def main():
#runs the script and checks for further inputs
    init()
    while True:
        verify()
        answer = input("\nDo you want to check another EAN? (y=yes, n=no): ")
        if(answer == "y" ):
            continue
        elif(answer == "n" ):
            print("x")
            break
        else:
            print("Bad input!")
                        
    print("Thanks for using PyEAN!")

main()

"""EAN-Checksum validation:
   -multiply the first number with one
   -multiply the second number with 3
   -repeat this till you get to the checksum(not the checksum!)
   I solved it by searching for even/uneven numbers from 0-13
   -add all the numbers
   -if you're able to divide it by 10 and get no rest then you're good,
    if not you need to add numbers until that's the case (for example:
    94 +6  or 132 +8..."""
