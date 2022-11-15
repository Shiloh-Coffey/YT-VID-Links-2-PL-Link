# YT-VID-Links-2-PL-Link v.1.3.2
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