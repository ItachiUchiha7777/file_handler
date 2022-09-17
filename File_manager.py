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
            print(f"ye {i} files hai {exx} extension wali. ")
            old = diR+"\\" + i
            c [1] = new_ext
            new_name = diR +"\\"+ c [0] + "." + c [1]
            os.rename(old , new_name)


def faltu_files_hatana_wala_hero() :
    print(f"abhi is work directory mai ke andr hu mai: {os.getcwd()}")
    diR = input("directory ka path copy krke dalo jisme saman hai ya hatana hai: ")
    os.chdir(diR)
    print(f"Okey apne change kr dia ab directory mai ke andr hu mai: {os.getcwd()}")
    dir_list = os.listdir(diR)  # us path mai jojo files hai unki list banayega ye
    exx = input("eneter apko konse extension wale file se probem hai: ")
    inp = int(input(f"{exx} extension wali file delete karna chahoge ya rename. if u want to rename the file press 1 and if u want to delete the file press 2: "))
    if inp == 2 :
        file_deleter(dir_list , exx , diR)
    elif inp == 1 :
        file_rename(diR , dir_list , exx)
    else :
        print("abe oo zyada tez na bano jitne option die hai utne mai se dabo warna ghar aa kr marine tumhe")


faltu_files_hatana_wala_hero()
