mkdir output
grep -o '.be/.*' input/*.txt | cut -f2 -d"/" > result.txt
grep -o '?v=.*' input/*.txt | cut -f2 -d"=" >> result.txt
python splitjoin.py