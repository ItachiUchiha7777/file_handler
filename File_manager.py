import os
print("𝓟𝓻𝓸𝓰𝓻𝓪𝓶𝓶𝓮𝓭 𝓫𝔂 𝓡𝓸𝓱𝓲")




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
            print(f"{i} this file has {exx} extension. ")
            old = diR+"\\" + i
            c [1] = new_ext
            new_name = diR +"\\"+ c [0] + "." + c [1]
            os.rename(old , new_name)


def faltu_files_hatana_wala_hero() :
    print(f"Currently on this directory: {os.getcwd()}")
    diR = input("Enter the location directory in which the file(s) are: ")
    os.chdir(diR)
    print(f"Directory changed to: {os.getcwd()}")
    dir_list = os.listdir(diR)  # us path mai jojo files hai unki list banayega ye
    exx = input("Enter the extension you want to deal with: ")
    inp = int(input(f"Please press 1 if you want to change the extention of the file, press 2 if u want to delete the fil : "))
    if inp == 2 :
        file_deleter(dir_list , exx , diR)
    elif inp == 1 :
        file_rename(diR , dir_list , exx)
    else :
        print("Please choose between 1 or 2")


faltu_files_hatana_wala_hero()
