import os

#input the directory path
#directory_path = input("Directory Path: ")

base_folder = "E:\office\Training Material\practise\informatica_practise\MiniProject"
directory_path =  base_folder + "\sources"

#print(os.listdir("E:\office\Training Material\practise\informatica_practise\MiniProject\sources"))
pathlist = []

output_file_path = base_folder + "\sources\output_file.csv"

for path in os.listdir(directory_path):
    name, ext = path.split(".") #file.txt file txt name=file ande ext =txt
    if(ext == "txt"):
        pathlist.append(path)
        with open(output_file_path, "a+") as f:
            f.write(directory_path + "\\" + path + ",")
            f.write("\n")

print(pathlist)
