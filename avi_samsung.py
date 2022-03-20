import glob, os
import shutil

'''
Created by: @Sergio-PS on 20/03/2022

Use this script to fix AVI Xvid or DivX files to be playable on newer Samsung TV's
Prerequisite: ffmpeg.exe in global path
'''

# Def Constants and variables

# Set True if you want to convert files
enable_convert = True

# Set True if you want to backup files
enable_backup = False

# Set True if you want to clean file names
enable_clean = True

# Set True if you want to autorespond overwriting questions
enable_overwrite = True


extension = ".avi"

separator = os.path.sep

# Get current working directory
cwd = os.getcwd() # Absolute Path
#cwd = "." # Relative Path

results_folder = cwd + separator + "samsungtv_results"
backups_folder = cwd + separator + "samsungtv_backups"



# Def Functions
def get_items_from_path(path, remove):
    for item in remove:
        path = path.replace(item, "")
        #print(path)

    return path

# Get list with files that contain extension
def get_dir_files_names_with_extension(extension, cwd):
    filelist = []
    namelist = []
    dirlist = []
    
    for root, dirs, files in os.walk(cwd):
        for name in files:
            if name.endswith(extension):
                remove = [cwd, name]
                file_path = os.path.join(root, name)
                dir_name_path = get_items_from_path(file_path, remove)
                
                if results_folder.split(separator)[-1] not in dir_name_path and backups_folder.split(separator)[-1] not in dir_name_path:
                    if dir_name_path not in dirlist and dir_name_path != separator:
                        path_backups = backups_folder + separator + dir_name_path
                        path_results = results_folder + separator + dir_name_path
                        #path = os.path.join(root, path1)
                        try:
                            if enable_backup:
                                os.makedirs(path_backups)
                            if enable_convert:
                                os.makedirs(path_results)
                        except:
                            pass

                        dirlist.append(dir_name_path)
                
                filelist.append(file_path)
                namelist.append(name)

                #print(remove)
                #print(dir_name_path)
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

# Create directory for results
if enable_backup and not os.path.exists(backups_folder):
    os.mkdir(backups_folder)

if enable_convert and not os.path.exists(results_folder):
    os.mkdir(results_folder)



filelist = []
namelist = []
dirlist = []
filelist, namelist, dirlist = get_dir_files_names_with_extension(extension, cwd)
#get_dir_files_names_with_extension(extension, cwd)
#print(dirlist)



#get_items_from_path(filelist[1], [cwd, "\Diamante De Sangre [CD1][DVDRIP-AC3 5.1][Spanish][www.pctestrenos.com][www.newpct.com].avi"])

for i in range(len(filelist)):
    input_filepath = filelist[i]
    input_name = namelist[i]

    output_filepath = ""
    output_name = "samsungtv_"

    remove = [cwd]
    dir_file_input_path = get_items_from_path(input_filepath, remove)
    # Necessary check for disk root paths
    if dir_file_input_path[0] == separator:
        dir_file_input_path = dir_file_input_path[1:]
    

    if enable_backup:
        print("backing up: " + input_filepath)

        backup = dir_file_input_path + ".bak"
        backup_result_path = backups_folder + separator + backup
        
        #print(backup_result_path + "\n")
        shutil.copyfile(input_filepath, backup_result_path)
    
    # Replace last item
    if enable_convert:
        splitted_name = dir_file_input_path.split(separator)
        filename = splitted_name[-1]
        splitted_name[-1] = output_name + filename # Last element is now the output name

        #print(output_name + filename)

        dir_file_output_path = separator.join(splitted_name)

        #print(dir_file_output_path)
        #print(results_folder)
        
        dir_file_output_path = separator.join(splitted_name)
        output_filepath = results_folder + separator + dir_file_output_path
        
        #print(input_filepath)
        #print(output_filepath)
        

        #print(name)
        #output_name = name.replace(extension, "_samsungtv" + extension)
        
        # Executes ffmpeg command in CLI
        os.system("ffmpeg -i " + "\"" + input_filepath + "\"" + " -nostats -loglevel error -c copy -bsf:v mpeg4_unpack_bframes -vtag FMP4 " + "\"" + output_filepath + "\"")

    

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
