class file:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.file=open(self.filename,self.mode)
        print(f"File {self.filename} opened in {self.mode}")
    def write(self,data):
        self.file.write(data)
        print("print written data")

    def __del__(self):
        self.file.close()
        print("file closed")
f=file(r"D:\P25MCA122\file.txt","w")
f.write("This is the message")
del f
