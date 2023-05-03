from PyPDF2 import PdfMerger

# Create a PDF Merger object
merger = PdfMerger()

# Add PDF Files to the merger object
merger.append("PDF_Merger_File1.pdf")
print("Adding the First PDF")
merger.append("PDF_Merger_File2.pdf")
print("Adding the Second PDF")

# Write the merged PDF to a File
print("Creating the merged PDF")
with open("PDF_Merger_Merged.pdf", "wb") as output_file:
    merger.write(output_file)

print("Creation of the Merged PDF completed")
