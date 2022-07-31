from intelhex import bin2hex
from tkinter import filedialog, messagebox
from tkinter import *


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


def main():
    guiBin2Hex = GuiForBin2Hex()
    guiBin2Hex.run()


if __name__ == '__main__':
    main()
