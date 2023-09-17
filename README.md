# QRcode and Bar code decoder

This python script can decode QRcode and Bar code from a given image.

The user is prompted to enter the file name, if the entered file name exists in the current working directory a function to decode the QRcode or Bar code is invoked.

- Image not clear to decode
  
  If the given image contains a bar code such as the following wherein the image is not clear,

  ![barcode1_small](https://github.com/blockchainamm/blockchainamm/assets/82846751/2deed961-f0aa-433f-b90f-8e0fcc3e5a4e)
  
  If the output from the function to decode returns an empty list a message "Not possible to decode data from image" is displayed as shown below
  
  <img width="294" alt="QRnotpossible" src="https://github.com/blockchainamm/blockchainamm/assets/82846751/97381b22-fb29-48de-a446-e2322a376937">

The output from the function to decode returns a character string based on the quality of the image

- Bar code decoding

  If the given image contains a bar code such as the following,
  
  ![barcode_small](https://github.com/blockchainamm/QRcode_Barcode_decoder/assets/82846751/baf37751-9025-4cba-8f26-a253468b199e)
 
  The output of the decoded bar code is as shown below

  <img width="354" alt="Baecodedecodeop" src="https://github.com/blockchainamm/blockchainamm/assets/82846751/457140be-1c07-491a-aa47-8f39e899edbe">

- QRcode decoding

  If the given image contains a QRcode such as the following,

  <img width="95" alt="qrimg" src="https://github.com/blockchainamm/blockchainamm/assets/82846751/6fa8eee7-b212-49e7-a60a-91cca083d09e">

  The output of the decoded QRcode is as shown below

  <img width="420" alt="QRdecodedop" src="https://github.com/blockchainamm/blockchainamm/assets/82846751/b0b51ed2-39ed-410a-8a0d-39c4aacf27c5">
