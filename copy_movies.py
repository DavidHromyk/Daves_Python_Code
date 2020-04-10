import os
import shutil


def copy_files(directory, ext):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(ext):
                shutil.copy2(os.path.join(root, file), f'D:/Temp/{file}')
                print(os.path.join(root, file))
    else:
        return ('No movie files')


def check_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if os.path.exists(f'{directory}/{file}'):
                return True
    else:
        return False


def remove_files(directory, ext):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(ext):
                os.remove(os.path.join(root, file))


class Extension():

    def mp4(self):
        copy_files('C:/Users/David/Downloads', '.mp4')
        check = check_files('D:/Temp')
        if check == True:
            remove_files('C:/Users/David/Downloads/', '.mp4')
            return ('Copied mp4 files')

    def mkv(self):
        copy_files('C:/Users/David/Downloads', '.mkv')
        check = check_files('D:/Temp')
        if check == True:
            remove_files('C:/Users/David/Downloads/', '.mkv')
            return ('Copied mkv files')


extension = Extension()
extension.mkv()
extension.mp4()
