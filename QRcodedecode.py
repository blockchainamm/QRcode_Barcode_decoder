# Script to decode QR code and Barcode from a given input file

# Import required libraries
from pyzbar.pyzbar import decode
from PIL import Image
import os

# Function to check if file exists in the current working directory
def check_file(imagefile):
    # Get current working directory
    current_dir = os.getcwd()

    #print(current_dir)

    path = os.path.join(current_dir, imagefile)

    # Check whether the specified
    # path exists or not
    isExist = os.path.exists(path)
    #print(isExist)
    return isExist

def checkdecode():
    # Take the image file from user and assign it to a variable image
    imagefile = input("Enter file with QRcode or Bar code image: ")
    print(f"The file name which you entered is: {imagefile}" )
    
    # Check if the file exists in the current directory
    existcheck = check_file(imagefile)

    # If the image file exists then decode image
    if existcheck:
        decode_data = decode(Image.open(imagefile))
        #print(decode_data)
        
        # Check decoded data from the image file
        if decode_data != []:
            print(f'Decoded data from image file {imagefile} : ', decode_data[0].data.decode('ascii'))
        else:
            print(f'Not possible to decode data from image in {imagefile}')
    else:
        print(f'No such file {imagefile} found in this directory') 

checkdecode()