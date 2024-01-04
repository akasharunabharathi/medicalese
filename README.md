# Medicalese
Ever felt confused by all the big words on the report from your blood tests? Wished someone would interpret those mysterious numbers and let you know if you're normal ASAP? Here's Medicalese – one tool to simplify it all for you! Upload snapshots of your reports, and receive super easy-to-understand explanations.

## Subsystems:

As of now, there are two primary subsystems to this project, (listed in the order that they process user input):

The OCR Subsystem: This is resposnible for recognising the text from the reports that users pass in. This is also the first layer where we encounter user input for processing. As such, we need to pre-process the input, pass it to the Tesseract OCR, and process the Tessearct's output to conform to the requirements of the second subsystem.

The Explainer Subsytem: Takes the input from the OCR engine (contains report text, details of patient's lab work, measurements of blood markers for various functions, etc), and simplifies it down for users. Yay!

## Example Report (Generated using ChatGPT)
<img width="546" alt="Sample Report (1)" src="https://github.com/akasharunabharathi/medicalese/assets/90937878/85f685a4-0e24-4617-8974-6d29fadbbfa5">

## Example Interpretation
<img width="1363" alt="Screen Shot 2024-01-04 at 6 07 49 PM" src="https://github.com/akasharunabharathi/medicalese/assets/90937878/f500e225-3453-42b9-9369-2c567fb51831">
