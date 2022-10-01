import PyPDF2
import tabula
# pdf file object
# you can find find the pdf file with complete code in below
##pdfFileObj = open('librev.pdf', 'rb')

# pdf reader object
##pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# number of pages in pdf
##print(pdfReader.numPages)

# a page object
##pageObj = pdfReader.getPage(0)

# extracting text from page.
# this will print the text you can also save that into String

##print(pageObj.extractText())

df = tabula.convert_into("librev.pdf", "pdf.csv", output_format="csv")
# in order to print first 5 lines of Table