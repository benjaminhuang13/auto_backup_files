import shutil 
from datetime import date 
import os 
import sys

# Function for performing the backup of the files and folders 
def take_backup(src_path, dst_dir): 
    # Extract the today's date 
    today = date.today()   
    date_format = today.strftime("%Y_%m_%d") 
    try: 
        dst_path = dst_dir + "\\dst_file_name" + date_format + ".qbw"
        print("\nCopying from: " + src_path + " to " + dst_path)
        shutil.copy2(src_path, dst_path)
        print("\nBackup Successful!") 
    except FileNotFoundError as e: 
        print("File does not exists!, please give the complete path: " + str(e)  )

# Call the function 
src_path = "D:\\source_destination.fileExtension"
dst_dir = "R:\\Mapped\\network\\harddrive"
take_backup(src_path,  dst_dir)
