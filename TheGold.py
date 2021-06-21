import PyPDF2
import tabula
import re
import pandas as pd

# The following field data is pulled into Excel or .CSV 
# Purchase Order Number
# Date Issued
# Buyer
# Vendor Number
# Vendor Address Info
# Delivery Info
# Invoice To Info
# Ship To Contact Info
# Line
# Description
# QTY
# UOM
# Unit Price
# Extended Amount

reader = PyPDF2.PdfFileReader('Signed PO2000556795_ Version 6_FINAL.PDF','rb')
NUM_OF_PAGES = reader.getNumPages()

page0 = reader.getPage(0)
h = page0.mediaBox.getHeight()
w = page0.mediaBox.getWidth()
#MergePages
newpdf_page = PyPDF2.pdf.PageObject.createBlankPage(None, w, hNUM_OF_PAGES)
for i in range(NUM_OF_PAGES):
    next_page = reader.getPage(i)
    newpdf_page.mergeScaledTranslatedPage(next_page, 1, 0, h(NUM_OF_PAGES-i-1))
writer = PyPDF2.PdfFileWriter()
writer.addPage(newpdf_page)

with open('output.pdf', 'wb') as f:
    writer.write(f)

#cleanup pages
columns = {'Purchase Order Number','Date Issued','Buyer','Vendor Number','Vendor Address Info','Delivery Info','Invoice To Info','Ship To Contact Info','Line','Description','QTY','UOM','Unit Price','Extended Amount'}
#Converting to csv output_format = columns,
data = tabula.read_pdf('output.pdf', pages = "all")
print(data.to_string())

ed_num_re = re.compile(r'Education Number: (\d*)')

for index, row in data.iterrows():
    print(row[1])

print(ed_num)


tabula.convert_into('output.pdf', 'Test.csv', output_format = 'csv')

finaldf = pd.concat(data, axis=0).sort_index()

finaldf.to_csv("New File.csv", index = False)