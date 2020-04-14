import os # calls os module to handle files and directories
import shutil # calls shutil module to handle copying files


# function to check if file ends with ext and copies over to external drive if it does
def copy_files(directory, ext):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(ext):
                shutil.copy2(os.path.join(root, file), f'D:/Temp/{file}')
                print(os.path.join(root, file))

            else:
                print('No movie files')

def check_files(directory): # checks if the files made it to the external hard drive
    for root, dirs, files in os.walk(directory):
        for file in files:
            if os.path.exists(f'{directory}/{file}'):
                return True

def remove_files(directory, ext): # removes the file after it is copied over
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(ext):
                os.remove(os.path.join(root, file))


class Extension(): # class for handling different extension types

    def mp4(self): # handles mp4 files
        copy_files('C:/Users/David/Downloads', '.mp4')
        check = check_files('D:/Temp')
        if check:
            remove_files('C:/Users/David/Downloads/', '.mp4')
            print('Copied mp4 files')

    def mkv(self): # handles mkv files
        copy_files('C:/Users/David/Downloads', '.mkv')
        check = check_files('D:/Temp')
        if check:
            remove_files('C:/Users/David/Downloads/', '.mkv')
            print('Copied mkv files')


# Calls the class
extension = Extension()
extension.mkv()
extension.mp4()
