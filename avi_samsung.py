import glob, os
import shutil

'''
Use this script to fix AVI Xvid or DivX files to be playable on newer Samsung TV's
Prerequisite: ffmpeg.exe in global path
'''

# Def Constants and variables 

# Set True if you want to backup files first before processing
enable_backup = True
# enable_backup = False

# Set True if you want to clean file names first before processing
enable_clean = True

extension = ".avi"

# Get current working directory
cwd = os.getcwd() # Absolute Path
#cwd = "." # Relative Path

results_folder = "samsungtv_results"
backups_folder = "samsungtv_backups"

separator = os.path.sep

# Def Functions
def get_items_from_path(path, remove):
    for item in remove:
        path = path.replace(item, "")

    return path

# Get list with files that contain extension
def get_dir_files_names_with_extension(extension, cwd):
    filelist = []
    namelist = []
    dirlist = []
    
    for root, dirs, files in os.walk(cwd):
        for name in files:
            if name.endswith(extension):
                file = os.path.join(root, name)

                filelist.append(file)
                namelist.append(name)

                remove = [cwd, name]
                item = get_items_from_path(file, remove)
                if item not in dirlist:
                    print(item)
                    dirlist.append(item)
                
    
    return filelist, namelist, dirlist

'''
def clean_dir_files_names(filelist):
    separator = os.path.sep

    for name in filelist:
        try:
            #print("Cleaning: " + name)
        
            splitted_path_list = name.split(separator)
            splitted_path_list.pop(0) # Remove '.' from the list
            print(splitted_path_list)
            list_elements = "".join(splitted_path_list).split()
            #print(list_elements)

            
        except:
            print("Could not clean: " + name)
    
    print("Filenames cleaned")
'''
'''
def copy_directory_structure(cwd, folder):

    def ignore_data(dir, files):
        return [f for f in files if os.path.isfile(os.path.join(dir, f))]  

    shutil.copytree(cwd,
        cwd + separator + "folder",
        ignore=ignore_data)
'''
# Script
filelist = []
namelist = []
dirlist = []
filelist, namelist, dirlist = get_dir_files_names_with_extension(extension, cwd)

# Create directory for results
if not os.path.exists(results_folder):
    os.mkdir(results_folder)

if enable_backup and not os.path.exists(backups_folder):
    os.mkdir(backups_folder)

#get_items_from_path(filelist[1], [cwd, "\Diamante De Sangre [CD1][DVDRIP-AC3 5.1][Spanish][www.pctestrenos.com][www.newpct.com].avi"])
print(dirlist)
'''
for filename in filelist:
    copy_directory_structure(cwd, backups_folder)
    copy_directory_structure(cwd, results_folder)
'''
'''
for i in range(len(filelist)):
    input_filepath = filelist[i]
    input_name = namelist[i]

    output_filepath = ""
    output_name = "samsungtv_"

    dir_file_input_path = input_filepath.replace(cwd + separator, "")

    if enable_backup:
        print("backing up: " + input_filepath)

        backup = dir_file_input_path + ".bak"
        # print(backup + "\n")
        backup_result_path = cwd + separator + backups_folder + separator + backup
        print(backup_result_path + "\n")
        # print(backup_result_path)
        shutil.copyfile(input_filepath, backup_result_path)
    
    # Replace last item

    splitted_name = dir_file_input_path.split(separator)
    filename = splitted_name[-1]
    splitted_name[-1] = output_name + filename # Last element is now the output name

    dir_file_output_path = separator.join(splitted_name)
    output_filepath = cwd + separator + result_folder + separator + dir_file_output_path
    
    # print(output_filepath)
    

    #print(name)
    #output_name = name.replace(extension, "_samsungtv" + extension)
    
    # Executes ffmpeg command in CLI
    os.system("ffmpeg -i " + "\"" + input_filepath + "\"" + " -nostats -loglevel error -c copy -bsf:v mpeg4_unpack_bframes -vtag FMP4 " + "\"" + output_filepath + "\"")

'''


#print(filelist)

'''
if enable_clean:
    filelist = clean_dir_files_names(filelist)
'''


'''
print(get_files_with_extension(extension))

os.path.join(root, file)

os.system("echo Hello")
print("Current working directory: {0}".format(cwd))

'''
