import PyPDF2

with open('dummy.pdf', 'rb') as file:
    # 'rb' converts file object to binary mode so PyPDF2 can read
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)      # number of pages
    print(reader.getPage(0))    # get specific page object
    page = reader.getPage(0)
    # page.rotateClockwise(90)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('rotated.pdf', 'wb') as new_file:
        writer.write(new_file)
