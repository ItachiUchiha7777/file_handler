import os


def file_deleter(dir_list , exx , diR) :
    for i in dir_list :
        c = i.split(".")
        if exx in c :
            path = os.path.join(diR , i)
            os.remove(path)


def file_rename(diR , dir_list , exx) :
    new_ext = input("Enter the new extension.")
    for i in dir_list :
        c = i.split(".")
        if exx in c :
            print(f"This {i} files has {exx} extension. ")
            old = diR+"\\" + i
            c [1] = new_ext
            new_name = diR +"\\"+ c [0] + "." + c [1]
            os.rename(old , new_name)


def faltu_files_hatana_wala_hero() :
    print(f"Currently working on this directory: {os.getcwd()}")
    diR = input("Please copy the path of the directory in which the files are located: ")
    os.chdir(diR)
    print(f"Directory changed to: {os.getcwd()}")
    dir_list = os.listdir(diR)  # us path mai jojo files hai unki list banayega ye
    exx = input("Enter the extention you want to deal with: ")
    inp = int(input("Do you want to rename or delete the fil? if u want to rename the file press 1 and if u want to delete the file press 2: "))
    if inp == 2 :
        file_deleter(dir_list , exx , diR)
    elif inp == 1 :
        file_rename(diR , dir_list , exx)
    else :
        print("Please choose between 1 or 2")


faltu_files_hatana_wala_hero()
