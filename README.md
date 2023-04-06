# fancaps-bookmark-downloader

This is a simple script to download all the images from a [fancaps.net](https://fancaps.net) firefox bookmark folder.

## Usage

1. Create a bookmark folder in firefox with all the fancaps.net images you want to download.
   - The bookmarked links should be in the format : `https://fancaps.net/movies/Image.php?imageid=567861`
2. Export the bookmark folder as a JSON file.
   1. Open the firefox bookmark manager (Ctrl+Shift+O)
   2. On the top left, you should see Import and Export. Click on Backup...
   3. Save the json wherever you want.
3. Run the script with the json file as an argument.
   - `python main.py <bookmark json file> <bookmark folder name> <type of media> <output folder>`
   - Where : 
     - `<bookmark json file>` is the path to the json file you exported in step 2.
     - `<bookmark folder name>` is the name of the bookmark folder you created in step 1. It will be used to find the images links in the json file.
     - `<type of media>` is either `movie` or `anime`
     - `<output folder>` is the folder where the images will be downloaded. If it doesn't exist, it will be created.

## Example

`python main.py "C:\Users\user\Downloads\bookmarks-2021-1-1.json" "Fancaps" movie "C:\Users\user\Downloads\Fancaps"`

## Notes

Please note that this script is not perfect and may not work for all cases. It was made for my own use and I decided to share it in case it could be useful to someone else (and to have a backup of it in case I lose it).

If you find any bugs or have any suggestions, feel free to open an issue or a pull request.

<!-- Image of my github profile (https://avatars.githubusercontent.com/u!/49199682) -->
<!-- ![github-profile-image](https://avatars.githubusercontent.com/u/49199682) -->