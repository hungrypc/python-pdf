import PyPDF2
import sys

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)


# inputs = sys.argv[1:]

# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')
#
#
# pdf_combiner(inputs)

# with open('dummy.pdf', 'rb') as file:
#     # 'rb' converts file object to binary mode so PyPDF2 can read
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)      # number of pages
#     print(reader.getPage(0))    # get specific page object
#     page = reader.getPage(0)
#     # page.rotateClockwise(90)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('rotated.pdf', 'wb') as new_file:
#         writer.write(new_file)
