from intelhex import bin2hex
from intelhex import hex2bin
from tkinter import filedialog, messagebox
from tkinter import *
# from GUI_bin2hex import GuiForBin2Hex
# from GUI_hex2bin import GuiForHex2Bin


class GuiForBin2Hex:
    def __init__(self):
        self.root = Tk()
        self.root.title("Transform .bin file to .hex file")
        self.root.geometry('700x300')

        self.binFile = None
        self.hexFile = None
        self.offset = 0

    def run(self):
        self._bin2hex()
        self.setOffsetEvent()
        self.transformEvent()
        self.mainGUIEvent()
        self.root.mainloop()

    def exitCurrentGUI(self):
        self.root.destroy()

    @staticmethod
    def createEmptyString(tot):
        emptyString = ""
        for _ in range(tot):
            emptyString += " "
        return emptyString

    def selectBinaryFile(self, file_path):
        filePath = filedialog.askopenfilename(filetypes=((".bin files", "*.bin"), ("all files", "*.*")))
        file_path.config(text=filePath)
        self.binFile = filePath
        self.hexFile = self.binFile.replace('.bin', '_transformed.hex')

    def assignOffset(self, offsetValue):
        flagHexOffset = offsetValue.get("1.0", END).strip('\n')[:2]
        if flagHexOffset == '0x' or flagHexOffset == '0X':
            self.offset = int(offsetValue.get("1.0", END).strip('\n'), 16)
        elif flagHexOffset == '0b' or flagHexOffset == '0B':
            self.offset = int(offsetValue.get("1.0", END).strip('\n'), 2)
        else:
            self.offset = int(offsetValue.get("1.0", END).strip('\n'), 10)

    def setOffsetEvent(self):
        frame = Frame(self.root)
        frame.pack()

        offsetLabel = Label(frame, text="Offset:", font=("Times", 18))
        offsetLabel.pack(side=LEFT)

        offsetValue = Text(frame, width=25, height=1, font='Times 16')
        offsetValue.insert("1.0", '0')
        offsetValue.pack(side=LEFT)

        setOffset = Button(frame, text="Set Offset", font=("Times", 12), command=lambda: self.assignOffset(offsetValue))
        setOffset.pack(side=LEFT)

    def _bin2hex(self):
        frame = Frame(self.root)
        frame.pack()
        binFileLabel = Label(frame, text=".bin file:", font=("Times", 18))
        binFileLabel.pack(side=LEFT)

        binFilePos = Label(frame, text=GuiForBin2Hex.createEmptyString(50), font='Times 16', bg="white")
        binFilePos.pack(side=LEFT)

        selectBinFile = Button(frame, text="Select .bin File", font=("Times", 12), command=lambda: self.selectBinaryFile(binFilePos))
        selectBinFile.pack(side=LEFT)

    @staticmethod
    def _bin2hexEvent(fileRead, offset):
        fileType = (".hex files", "*.hex"), ("all files", "*.*")
        fileWritten = filedialog.asksaveasfilename(filetypes=fileType, defaultextension=fileType)
        print(type(fileWritten))
        print(fileWritten)
        flag = bin2hex(fileRead, fileWritten, offset)
        if flag == 0:
            messagebox.showinfo('Success', 'The .bin file has been transformed to .hex file successfully.')

    def transformEvent(self):
        frame = Frame(self.root)
        frame.pack()
        bin2hexButton = Button(frame, text="Transform", font=("Times", 12),
                               command=lambda: GuiForBin2Hex._bin2hexEvent(self.binFile, self.offset))
        bin2hexButton.pack(side=TOP)

    def mainPage(self):
        self.exitCurrentGUI()
        gui_b2h_h2b = GuiForBin2HexAndHex2Bin()
        gui_b2h_h2b.run()

    def mainGUIEvent(self):
        frame = Frame(self.root)
        frame.pack()

        selectMode = Button(frame, text="Main GUI", font=("Times", 12), command=lambda: self.mainPage())
        selectMode.pack(side=TOP)


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
        self.transformEvent()
        self.mainGUIEvent()
        self.root.mainloop()

    def exitCurrentGUI(self):
        self.root.destroy()

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

    def transformEvent(self):
        frame = Frame(self.root)
        frame.pack()
        hex2binButton = Button(frame, text="Transform", font=("Times", 12),
                               command=lambda: GuiForHex2Bin._hex2binEvent(self.hexFile, self.start,
                                                                           self.end, self.size, self.pad))
        hex2binButton.pack(side=TOP)

    def mainPage(self):
        self.exitCurrentGUI()
        gui_b2h_h2b = GuiForBin2HexAndHex2Bin()
        gui_b2h_h2b.run()

    def mainGUIEvent(self):
        frame = Frame(self.root)
        frame.pack()

        selectMode = Button(frame, text="Main GUI", font=("Times", 12), command=lambda: self.mainPage())
        selectMode.pack(side=TOP)


class GuiForBin2HexAndHex2Bin:
    def __init__(self):
        self.root = Tk()
        self.root.title("Conversion between .bin and .hex Files")
        self.root.geometry('700x300')

    def run(self):
        self.selectMode()
        self.root.mainloop()

    def exitMainGUI(self):
        self.root.destroy()

    def bin2hex_mode(self):
        self.exitMainGUI()
        guiBin2Hex = GuiForBin2Hex()
        guiBin2Hex.run()

    def hex2bin_mode(self):
        self.exitMainGUI()
        guiHex2Bin = GuiForHex2Bin()
        guiHex2Bin.run()

    def selectMode(self):
        frame = Frame(self.root)
        frame.pack()

        bin2HexMode = Button(frame, text=".bin to .hex", font=("Times", 18), command=lambda: self.bin2hex_mode())
        bin2HexMode.pack(side=LEFT)

        hex2binMode = Button(frame, text=".hex to .bin", font=("Times", 18), command=lambda: self.hex2bin_mode())
        hex2binMode.pack(side=LEFT)


def main():
    gui_b2h_h2b = GuiForBin2HexAndHex2Bin()
    gui_b2h_h2b.run()


if __name__ == '__main__':
    main()
