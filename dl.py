# Downloads the pictures from the given list of fancaps.net picture id and stores them in the "downloads" folder
# Usage: dl.py <type of media> <name of the media> <file with list of picture ids>
# Example: dl.py movie list.txt

import os
import sys
import requests

def main():
    if len(sys.argv) != 5:
        print("Usage: dl.py <type of media> <name of the media> <file with list of picture ids> <output folder>")
        sys.exit(1)

    # check if the downloads folder exists
    if not os.path.exists(sys.argv[4]):
        os.makedirs(sys.argv[4])

    folder_name = sys.argv[4]
    media_name = sys.argv[2]
    
    progress = 0
    with open(sys.argv[3]) as f:
        for line in f:
            line = line.strip()
            progress += 1

            # Check if the file already exists
            try:
                if os.path.isfile("{}/{}_{}.jpg".format(folder_name,media_name, line)):
                    print("Progress: {}/{} : {}_{}.jpg already exists".format(progress, sum(1 for line in open(sys.argv[3])), sys.argv[2], line))
                    continue
            except FileNotFoundError:
                pass
            try:
                r = requests.get("https://cdni.fancaps.net/file/fancaps-{}images/{}.jpg".format(sys.argv[1], line))
            except requests.exceptions.InvalidURL:
                print("Progress: {}/{} : Invalid URL https://cdni.fancaps.net/file/fancaps-{}images/{}.jpg".format(progress, sum(1 for line in open(sys.argv[3])), sys.argv[1], line))
                continue
            except requests.exceptions.ConnectionError:
                print("Progress: {}/{} : Connection error https://cdni.fancaps.net/file/fancaps-{}images/{}.jpg".format(progress, sum(1 for line in open(sys.argv[3])), sys.argv[1], line))
                continue
            
            print("Progress: {}/{} : Downloading https://cdni.fancaps.net/file/fancaps-{}images/{}.jpg".format(progress, sum(1 for line in open(sys.argv[3])), sys.argv[1], line))
            with open("{}/{}_{}.jpg".format(folder_name,media_name, line), "wb") as f2:
                f2.write(r.content)

if __name__ == "__main__":
    main()
