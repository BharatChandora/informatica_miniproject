import re

file_path = "E:\office\Training Material\practise\informatica_practise\MiniProject\sources\output_file.csv"

word = input("Word to replace: ")
new_word = input("Word to replace with: ")


path_list = []

with open(file_path, "r") as f:
    line = "1"
    while(line !="" ):
        line = f.readline();
        path_list.append(line[:-2])
        #print(line[:-2])
        path = line[:-2]
        print(path)
        if(path != ""):
            content = ""
            with open(path, "r+") as sub_f:
                #print(sub_f.read())
                content = sub_f.read()
                #print(content)
                n = content.find(word)
                #print(n)
                #print(content[n:n + len(word) + 1])

            with open(path, "w") as w_f:

                w_f.write(content.replace(word, new_word))
                print(word, new_word)




