from os import path, listdir, makedirs

class FileManager:
  def __init__(self,file="prueba.txt",directory="files"):
    self.file_name = file
    self.directory = directory
  def get_source(self):
    return path.join(self.directory,self.file_name)
  def change_file_name(self):
    name = input("New file name: ")
    if name:
        self.file_name = name
    else:
        print("Name not actualized.")
  def change_directory(self):
    name = input("New directory name: ")
    if name:
        self.directory = name
        makedirs(self.directory, exist_ok=True)
    else:
        print("Name not actualized.")

def Help():
   print("""
The options are:
- Help
- Read file
- Write file
- Delete file content
- Change file
- Change directory
- View files
- Exit""")

def write_file(source):
    with open(source.get_source(),'a', encoding='UTF-8') as file:
        print("\nWhen finish, send \"close()\" in a new line.\n")
        while True:
            text=input()
            if text == "close()":
                break
            file.write(text+"\n")

def read_file(source):
    try:
        with open(source.get_source(), encoding='UTF-8') as file:
            print(f"\nText in file {source.file_name}:\n" + "-"*50)
            for line in file:
                print(line.strip())
            print("-"*50)
    except FileNotFoundError:
        print("\nFile doesn't exist.")

def delete_content(source):
    with open(source.get_source(), 'w') as file:
        pass

def view_files(source):
    files = listdir(source.directory)
    print("\nFiles in "+ source.directory + ":\n")
    for file in files:
        print(file)
