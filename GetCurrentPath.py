import os
global module_path
def GetPath():
    print(os.getcwd())
    module_path = os.getcwd()

if __name__== '__main__':
    GetPath()