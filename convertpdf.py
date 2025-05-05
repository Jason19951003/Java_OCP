from spire.doc import *
from spire.doc.common import *
        
# Create a Document object
document = Document()
# Load a Word DOCX file
document.LoadFromFile("繳費證明_完成.docx")
# Or load a Word DOC file
#document.LoadFromFile("Sample.doc")

# Save the file to a PDF file
document.SaveToFile("繳費證明_完成.pdf", FileFormat.PDF)
document.Close()
