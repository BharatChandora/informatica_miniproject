import pandas as pd

xcel_file_path = input("Source excel file: \n")
name = ""
if(len(xcel_file_path) == 0):
    print("Source file cannot be empty")
else:
    name, ext = xcel_file_path.split(".")
    print(ext)
    if(ext != "xlsx"):
        print("Invalid file extension\n")
    else:
        destination_directory = input("Destination Directory: \n")
        if(len(destination_directory) == 0):
            print("Destination path cannot be empty\n")

read_file = pd.read_excel (xcel_file_path, header=None)
read_file.to_csv (destination_directory, index = False, header=None, index_label=True)

print("Conversion completed")

    

  
  

    

