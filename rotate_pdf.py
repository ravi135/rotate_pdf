#This is a tool for rotating a pdf file.
#--Developer-- ravi135--

import PyPDF2
import os
inputPath = "C:/Users/kumar/Desktop/temp/input"
#os.startfile(inputPath)
fileName = input("Enter the PDF file name you want to rotate with .pdf extension like (xyz.pdf):\n")
direction = input("Enter direction of rotation either clockwise or counter clockwise:\n")
degree = int(input("Enter the multiple of 90 degree rotation:\n"))
openFile = open(os.path.join(inputPath,fileName),'rb')
pdfReader = PyPDF2.PdfFileReader(openFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
	pageObj = pdfReader.getPage(pageNum)
	if(direction.lower() == 'clockwise'):
		for t in range(degree//90):
			pageObj.rotateClockwise(90)
	else:
		for t in range(degree//90):
			pageObj.rotateCounterClockwise(90)
	pdfWriter.addPage(pageObj)
outputPath = "C:/Users/kumar/Desktop/temp/output"	
resultPdfFile = open(os.path.join(outputPath,'rotated'+fileName),'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
openFile.close()
print("Your PDF file rotated successfully!")

