from tkinter import Tk, Label, Button, filedialog, messagebox
import tkinter as tk

class FileComparer:
     def __init__(self, winTitle, xSize, ySize, *args):
         self.window = tk.Tk()
         if args:
              self.window.configure(bg=args)
         self.window.geometry(f'{xSize}x{ySize}')
         self.window.title(winTitle)
         self.window.resizable(False, False)
         self.fileOne = Button(text="Choose first file", bd=3, command=self.getFirstFile)
         self.fileOne.place(x=20, y=20)
         self.fileTwo = Button(text="Choose second file", bd=3, command=self.getSecondFile)
         self.fileTwo.place(x=150, y=20)
         self.compareBtn = Button(text="Compare", bd=3, command=self.CompareFiles)
         self.compareBtn.place(x=100, y=100)
         self.window.mainloop()

     def getFirstFile(self):
         self.fileOneContents = filedialog.askopenfilename()
         messagebox.showinfo("File", self.fileOneContents)
     
     def getSecondFile(self):
         self.fileTwoContents = filedialog.askopenfilename()
         messagebox.showinfo("File", self.fileTwoContents)

     def CompareFiles(self):
          try:
              self.firstFileData = open(self.fileOneContents, "r")
              self.fFileRead = self.firstFileData.read()
              self.secondFileData = open(self.fileTwoContents, "r")
              self.sFileRead = self.secondFileData.read()
              if self.fFileRead == self.sFileRead:
                   messagebox.showinfo("Result", "Both files are the same")
              else:
                   messagebox.showinfo("Result", "Both files are NOT the same")
          except:
               messagebox.showwarning("Error", "Something went wrong")

    
FileCompGUI = FileComparer("File Comparer", 280, 150)