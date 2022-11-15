L='.txt'
K='result.txt'
J=str
E=open
import os
F=50
C='./output/playlist_link_'
G='https://www.youtube.com/watch_videos?video_ids='
H=E(K,'r')
D=0
B=1
A=None
for I in H:
	if D%F==0:
		if A:A.close()
		A=E(C+J(B)+L,'w');A.write(G);A.close();A=E(C+J(B)+L,'a');B+=1
	A.write(I.strip('\n')+',');D+=1
os.remove(K)