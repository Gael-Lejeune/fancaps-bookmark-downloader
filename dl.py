# Downloads the pictures from the given list of fancaps.net picture id and stores them in the "downloads" folder
# Usage: dl.py <type of media> <file with list of picture ids>
# Example: dl.py movie list.txt

import os
import sys
import requests

def main():
    if len(sys.argv) != 4:
        print("Usage: dl.py <type of media> <file with list of picture ids> <output folder>")
        sys.exit(1)

    # check if the downloads folder exists
    if not os.path.exists(sys.argv[3]):
        os.makedirs(sys.argv[3])
    
    progress = 0
    with open(sys.argv[2]) as f:
        for line in f:
            line = line.strip()
            progress += 1

            # Check if the file already exists
            try:
                with open("downloads/{}.jpg".format(line)):
                    print("Progress: {}/{} : {}.jpg already exists".format(progress, sum(1 for line in open(sys.argv[2])), line))
                    continue
            except FileNotFoundError:
                pass
            r = requests.get("https://cdni.fancaps.net/file/fancaps-{}images/{}.jpg".format(sys.argv[1], line))
            print("Progress: {}/{} : Downloading https://cdni.fancaps.net/file/fancaps-{}images/{}.jpg".format(progress, sum(1 for line in open(sys.argv[2])), sys.argv[1], line))
            with open("downloads/{}.jpg".format(line), "wb") as f2:
                f2.write(r.content)

if __name__ == "__main__":
    main()
