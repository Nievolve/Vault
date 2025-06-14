## Parse folder and subfolder (years) for .md files
# Extract data and make it a desired list.

import target
import os

def List_Subfolder(path):
    subfolders = []
    for k in os.listdir(path):
        print(k)
        fullPath = os.path.join(path, k)
        # Control for error, make try?
        if os.path.isdir(fullPath):
            subfolders.append(fullPath)
    return subfolders

def List_Markdown(path,folder):
    Year_MarkdownList = []
    yearPath = os.path.join(path, folder)
    for k in os.listdir(yearPath):
        if k.endswith(".md") and os.path.isfile(os.path.join(yearPath, k)):
            Year_MarkdownList.append(k)
    return Year_MarkdownList

            


    
 

def main():
    All_Subfolder = List_Subfolder(target.path)
    Markdown_2025 = List_Markdown(target.path,All_Subfolder[2])
    print(Markdown_2025)
if __name__ == "__main__":
    main()