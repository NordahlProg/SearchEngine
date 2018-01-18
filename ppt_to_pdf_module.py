import comtypes.client
import os

def PPTtoPDF(inputFileName, outputFileName, formatType = 32):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1

    if outputFileName[-3:] != 'pdf':
        outputFileName = outputFileName + ".pdf"
    input = os.getcwd()+ "/" +  inputFileName
    deck = powerpoint.Presentations.Open(input)
    out = os.getcwd() + "/" + outputFileName
    deck.SaveAs(out, formatType) # formatType = 32 for ppt to pdf
    deck.Close()
    powerpoint.Quit()


def PPTConverter(dir):
    os.chdir(dir)
    filelist = os.listdir()
    for j in filelist:
        if j[-3:] == "ppt":
            out = j[:len(j)-4] + ".pdf"
            PPTtoPDF(inputFileName=j,outputFileName=out)
        if j[-4:] == "pptx":
            out = j[:len(j)-5] + ".pdf"
            PPTtoPDF(inputFileName=j,outputFileName=out)


