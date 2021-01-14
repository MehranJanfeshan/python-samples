import PyPDF2

f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)

# get the number of pages
print(pdf_reader.numPages)

# get the page text
page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()

print(page_one_text)

# write a PDF file
pdf_writer = PyPDF2.PdfFileWriter()

pdf_writer.addPage(page_one)

pdf_output = open('new_pdf.pdf', 'wb')

pdf_writer.write(pdf_output)

# we have to close the files at the end
pdf_output.close()
f.close()
