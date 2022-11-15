# YT-VID-Links-2-PL-Link v1.3.2
A UNIX shell script that intakes a file with multiple video links and creates playlist links.

# Instructions
- Download the repo.
- Delete placeholder.txt.
- Enter a .txt file, the name of the file is not important, with YouTube links, seperated by line, into the "input" folder and run the shell script.
- The playlist links will be geneterated in a folder named "output".

# Notes
- Links are limited to 50 videos at a time so it will generated multiple links for your playlist if you have over 50 video links
- Links can not have time in the url (i.e. "?t=8")
- Links can either be normal (i.e. "https://www.youtube.com/") or shortend (i.e. "https://youtu.be/")
- Make sure that you have python installed

# Changelog
- 1.3.2 - Resolved issue where if there was no file in the input folder it would still execute.
- 1.3.1 - Resolved issue where sometimes when the output folder was created it would not save the lists.
- 1.3.0 - Minified splitjoin.py, increasing efficency.
- 1.2.0 - Restuctured the placeholder file inside the input folder so it would not cause complications with main.sh's "grep".
- 1.1.0 - Added execution timer into main.sh.
