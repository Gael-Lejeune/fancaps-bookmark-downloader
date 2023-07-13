# Uses the specified json bookmark list and searches for the given folder to extract a part of the urls in it with regex to stores them in a list.
# For example, if the link is "https://fancaps.net/movies/Image.php?imageid=566846", the script will extract "566846" and store it in a list.
# The file is a json file exported from firefox bookmarks and follows its format.

# Usage: extract_from_json_to_list.py <bookmark json file> <output file>
# Example: extract_from_json_to_list.py bookmark.json list.txt

import sys
import json
import re

def check_folder(item, folder_name):
    # print(item["title"])
    for child in item["children"]:
        if child["title"] == folder_name:
            print("Found folder : {}".format(folder_name))
            return True, child
        else:
            if "children" in child:
                found, folder = check_folder(child, folder_name)
                if found:
                    return True, folder
    return False, None

def main():
    if len(sys.argv) != 4:
        print("Usage: extract_from_json_to_list.py <bookmark json file> <bookmark folder name> <output file>")
        sys.exit(1)

    json_file = sys.argv[1]
    folder_name = sys.argv[2]
    output_file = sys.argv[3]

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Find the folder in the entire json
    # It will search in every child and its children recursively
    folder = None
    found, folder = check_folder(data, folder_name)


    if found == False:
        print("Folder not found")
        sys.exit(1)

    # Find the links
    links = []
    for item in folder["children"]:
        links.append(item["uri"])

    # Extract the ids
    ids = []
    for link in links:
        m = re.search(r"imageid=(\d+)", link)
        if m:
            ids.append(m.group(1))
        n = re.search(r"php\?\/(\d+)", link)
        if n:
            ids.append(n.group(1))

    # Write the ids to the output file
    with open(output_file, "w") as f:
        for id in ids:
            f.write(id + "\n")



if __name__ == "__main__":

    main()
