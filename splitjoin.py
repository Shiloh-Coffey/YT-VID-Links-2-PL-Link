import os
splitLen = 50
outputBase = 'output/playlist_link_'
urlhead = 'https://www.youtube.com/watch_videos?video_ids='
bash_result = open('result.txt', 'r')

count = 0
at = 1
dest = None
for line in bash_result:
    if count % splitLen == 0:
        if dest: dest.close()
        dest = open(outputBase + str(at) + '.txt', 'w')
        dest.write(urlhead)
        dest.close()
        dest = open(outputBase + str(at) + '.txt', 'a')
        at += 1
    dest.write(line.strip('\n') + ',')
    count += 1
os.remove("result.txt")