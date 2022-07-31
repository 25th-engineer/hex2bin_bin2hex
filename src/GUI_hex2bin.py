from intelhex import hex2bin
from tkinter import filedialog, messagebox
from tkinter import *


class GuiForHex2Bin:
    def __init__(self):
        self.root = Tk()
        self.root.title("Transform .hex file to .bin file")
        self.root.geometry('700x300')

        self.hexFile = None
        self.binFile = None
        self.start = None
        self.end = None
        self.size = None
        self.pad = None

    def run(self):
        self._hex2bin()
        self.setStartEvent()
        self.setEndEvent()
        self.setSizeEvent()
        self.setPadEvent()
        self.transform()
        self.root.mainloop()

    @staticmethod
    def createEmptyString(tot):
        emptyString = ""
        for _ in range(tot):
            emptyString += " "
        return emptyString

    def selectHexadecimalFile(self, file_path):
        filePath = filedialog.askopenfilename(filetypes=((".hex files", "*.hex"), ("all files", "*.*")))
        file_path.config(text=filePath)
        self.hexFile = filePath
        self.binFile = self.hexFile.replace('.hex', '_transformed.bin')

    def assignStart(self, startValue):
        flagBinStart = startValue.get("1.0", END).strip('\n')[:2]
        if flagBinStart == '0x' or flagBinStart == '0X':
            self.start = int(startValue.get("1.0", END).strip('\n'), 16)
        elif flagBinStart == '0b' or flagBinStart == '0B':
            self.start = int(startValue.get("1.0", END).strip('\n'), 2)
        else:
            self.start = int(startValue.get("1.0", END).strip('\n'), 10)

    def setStartEvent(self):
        frame = Frame(self.root)
        frame.pack()

        startLabel = Label(frame, text="Start:", font=("Times", 18))
        startLabel.pack(side=LEFT)

        startValue = Text(frame, width=25, height=1, font='Times 16')
        startValue.pack(side=LEFT)

        setStart = Button(frame, text="Set Start", font=("Times", 12),
                          command=lambda: self.assignStart(startValue))
        setStart.pack(side=LEFT)
    
    def assignEnd(self, endValue):
        flagBinEnd = endValue.get("1.0", END).strip('\n')[:2]
        if flagBinEnd == '0x' or flagBinEnd == '0X':
            self.end = int(endValue.get("1.0", END).strip('\n'), 16)
        elif flagBinEnd == '0b' or flagBinEnd == '0B':
            self.end = int(endValue.get("1.0", END).strip('\n'), 2)
        else:
            self.end = int(endValue.get("1.0", END).strip('\n'), 10)

    def setEndEvent(self):
        frame = Frame(self.root)
        frame.pack()

        endLabel = Label(frame, text="End:", font=("Times", 18))
        endLabel.pack(side=LEFT)

        endValue = Text(frame, width=25, height=1, font='Times 16')
        endValue.pack(side=LEFT)

        setEnd = Button(frame, text="Set End", font=("Times", 12),
                        command=lambda: self.assignEnd(endValue))
        setEnd.pack(side=LEFT)

    def assignSize(self, sizeValue):
        flagBinSize = sizeValue.get("1.0", END).strip('\n')[:2]
        if flagBinSize == '0x' or flagBinSize == '0X':
            self.size = int(sizeValue.get("1.0", END).strip('\n'), 16)
        elif flagBinSize == '0b' or flagBinSize == '0B':
            self.size = int(sizeValue.get("1.0", END).strip('\n'), 2)
        else:
            self.size = int(sizeValue.get("1.0", END).strip('\n'), 10)

    def setSizeEvent(self):
        frame = Frame(self.root)
        frame.pack()

        sizeLabel = Label(frame, text="Size:", font=("Times", 18))
        sizeLabel.pack(side=LEFT)

        sizeValue = Text(frame, width=25, height=1, font='Times 16')
        sizeValue.pack(side=LEFT)

        setSize = Button(frame, text="Set Size", font=("Times", 12),
                         command=lambda: self.assignSize(sizeValue))
        setSize.pack(side=LEFT)

    def assignPad(self, padValue):
        flagBinPad = padValue.get("1.0", END).strip('\n')[:2]
        if flagBinPad == '0x' or flagBinPad == '0X':
            self.pad = int(padValue.get("1.0", END).strip('\n'), 16)
        elif flagBinPad == '0b' or flagBinPad == '0B':
            self.pad = int(padValue.get("1.0", END).strip('\n'), 2)
        else:
            self.pad = int(padValue.get("1.0", END).strip('\n'), 10)

    def setPadEvent(self):
        frame = Frame(self.root)
        frame.pack()

        padLabel = Label(frame, text="Pad:", font=("Times", 18))
        padLabel.pack(side=LEFT)

        padValue = Text(frame, width=25, height=1, font='Times 16')
        padValue.pack(side=LEFT)

        setPad = Button(frame, text="Set Pad", font=("Times", 12),
                        command=lambda: self.assignPad(padValue))
        setPad.pack(side=LEFT)

    def _hex2bin(self):
        frame = Frame(self.root)
        frame.pack()
        hexFileLabel = Label(frame, text=".hex file:", font=("Times", 18))
        hexFileLabel.pack(side=LEFT)

        hexFilePos = Label(frame, text=GuiForHex2Bin.createEmptyString(50), font='Times 16', bg="white")
        hexFilePos.pack(side=LEFT)

        selectHexFile = Button(frame, text="Select .hex File", font=("Times", 12),
                               command=lambda: self.selectHexadecimalFile(hexFilePos))
        selectHexFile.pack(side=LEFT)

    @staticmethod
    def _hex2binEvent(fileRead, start, end, size, pad):
        fileType = (".bin files", "*.bin"), ("all files", "*.*")
        fileWritten = filedialog.asksaveasfilename(filetypes=fileType, defaultextension=fileType)
        print(type(fileWritten))
        print(fileWritten)
        flag = hex2bin(fileRead, fileWritten, start, end, size, pad)
        if flag == 0:
            messagebox.showinfo('Success', 'The .bin file has been transformed to .hex file successfully.')

    def transform(self):
        frame = Frame(self.root)
        frame.pack()
        hex2binButton = Button(frame, text="Transform", font=("Times", 12),
                               command=lambda: GuiForHex2Bin._hex2binEvent(self.hexFile, self.start,
                                                                           self.end, self.size, self.pad))
        hex2binButton.pack(side=TOP)


def main():
    guiHex2Bin = GuiForHex2Bin()
    guiHex2Bin.run()


if __name__ == '__main__':
    main()
