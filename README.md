# Medicalese
Ever felt confused by all the big words on the report from your blood tests? Here's Medicalese – one tool to simplify it all for you! Upload snapshots of your reports, and receive super easy-to-understand explanations.

## Subsystems:

As of now, there are two primary subsystems to this project, (listed in the order that they process user input):

    1. The OCR Subsystem: This is resposnible for recognising the text from the reports that users pass in. This is also the first layer where we encounter user input for processing. As such, we need to pre-process the input, pass it to the Tesseract OCR, and process the Tessearct's output to conform to the requirements of the second subsystem.

    2. The Explainer Subsytem: Takes the text input from the OCR engine, removes the "bio-terms" and simplifies it down for users. Yay!

## Requirements:

    1. OCR Subsystem Reqs:
        * Still learning, will be updated soon.
    2. Explainer Subsystem Reqs:
        * Hugging Face, remainder is fuzzy. Will update soon.