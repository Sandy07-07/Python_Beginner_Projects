import PyPDF2
import pyttsx3

# Creating a new instance of the pyttsx3 engine
audio = pyttsx3.init()

# Open the PDF file in read-binary mode
with open("PDF_Reader.pdf", "rb") as file:
    # Create a PDF Reader object
    reader = PyPDF2.PdfReader(file)
    # To get the total number of pages
    num_pages = len(reader.pages)
    print("Starting to read the PDF file")

    # To navigate through the pages of the PDF
    for i in range(num_pages):
        page = reader.pages[i]
        # To extract the text from the page
        text = page.extract_text()
        print(f"Reading the Page no. {i}")
        # To convert the text to speech
        audio.say(text)
        audio.runAndWait()

print("Reading of all pages completed")
