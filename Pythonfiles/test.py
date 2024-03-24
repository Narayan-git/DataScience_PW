
import os

def rename_files(directory):
   """Renames all files in the specified directory, removing "Copy of" from their names.

   Args:
       directory (str): The path to the directory containing the files to rename.
   """

   for filename in os.listdir(directory):
       if filename.startswith("Copy of "):
           new_filename = filename[8:]  # Remove "Copy of "
           os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

if __name__ == "__main__":
   directory_path = "C:\\Users\\naray\\Downloads\\ADF_DeepakGoyal\\New folder" #input("Enter the directory path: ")
   rename_files(directory_path)
   print("Files renamed successfully!")
