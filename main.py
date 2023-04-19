# This file calls the other two files. It will first extract the ids from the bookmarks json file and if it succeeds, it will download the pictures.

import os
import sys
import subprocess

def main():
    if len(sys.argv) != 5:
        print("Usage: main.py <bookmark json file> <bookmark folder name> <type of media> <output folder>")
        print("For further information, please read the README.md file.")
        sys.exit(1)

    json_file = sys.argv[1]
    folder_name = sys.argv[2]
    type_of_media = sys.argv[3]
    output_folder = sys.argv[4]

    # Extract the ids from the json file
    print("Extracting the picture ids from {}..".format(json_file))
    subprocess.call(["python", "extract_from_json_to_list.py", json_file, folder_name, "list.txt"])

    # Check if the file is not empty
    if os.stat("list.txt").st_size == 0:
        print("The file is empty")
        sys.exit(1)

    # Download the pictures
    print("Downloading the pictures into {}..".format(output_folder))
    subprocess.call(["python", "dl.py", type_of_media, folder_name, "list.txt", output_folder])

    # Print stats about the download like : 
    # Number of pictures downloaded : 10
    # Number of pictures in the folder : 10
    # Number of pictures for each movie : 
    # - Mononke : 5
    # - Kiki : 10
    # Size of the output folder : 2.5 MB
    number_of_pictures_downloaded = sum(1 for line in open("list.txt"))
    number_of_pictures_in_folder = len([name for name in os.listdir(output_folder) if os.path.isfile(os.path.join(output_folder, name))])
    number_of_pictures_for_each_movie = {}
    size_of_picture_for_each_movie = {}
    for file in os.listdir(output_folder):
        if file.split("_")[0] in number_of_pictures_for_each_movie:
            number_of_pictures_for_each_movie[file.split("_")[0]] += 1
            size_of_picture_for_each_movie[file.split("_")[0]] += os.path.getsize(os.path.join(output_folder, file))
        else:
            number_of_pictures_for_each_movie[file.split("_")[0]] = 1
            size_of_picture_for_each_movie[file.split("_")[0]] = os.path.getsize(os.path.join(output_folder, file))
    size_of_output_folder = 0
    for file in os.listdir(output_folder):
        size_of_output_folder += os.path.getsize(os.path.join(output_folder, file))
    size_of_output_folder = size_of_output_folder / 1000000
    print("\n\033[92mNumber of pictures downloaded : {}\033[0m".format(number_of_pictures_downloaded))
    print("Size of the output folder : {} MB".format(round(size_of_output_folder, 3)))
    print("Number of pictures in the folder : {}".format(number_of_pictures_in_folder))
    for movie in number_of_pictures_for_each_movie:
        print("\t- {} : {} ({} MB)".format(movie, number_of_pictures_for_each_movie[movie], round(size_of_picture_for_each_movie[movie] / 1000000, 3)))



if __name__ == "__main__":
    main()

