import os
import shutil
import time

print('...File Sorter...')

main_folder = r"C:\Users\gifto\Documents\python-proj"
aud_file = r"C:\Users\gifto\Documents\python-proj\aud_file"
pics_file = r"C:\Users\gifto\Documents\python-proj\pics_file"
text_file = r"C:\Users\gifto\Documents\python-proj\text_file"
vid_file = r"C:\Users\gifto\Documents\python-proj\vid_file"
file_name = r"C:\Users\gifto\Documents\python-proj"


def main():
    while True:
        if os.path.exists(main_folder):
            for i in os.listdir(main_folder):
                if '.mp3' in i:
                    file_dir = os.path.join(file_name, i)
                    shutil.move(file_dir, aud_file)

                if '.jpg' in i:
                    file_dir = os.path.join(file_name, i)
                    shutil.move(file_dir, pics_file)

                if '.pdf' in i:
                    file_dir = os.path.join(file_name, i)
                    shutil.move(file_dir, text_file)

                if '.mp4' in i:
                    file_dir = os.path.join(file_name, i)
                    shutil.move(file_dir, vid_file)

        print("all file sorted 😊")
        time.sleep(1800)

if __name__ == '__main__':
    main()
