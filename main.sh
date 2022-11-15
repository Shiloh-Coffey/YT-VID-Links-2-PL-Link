start=`date +%s.%N`
if [ -f ./input/*.txt ]
then
  echo "File Found"
  if [ ! -d ./output ]
  then
    mkdir ./output
  fi
  grep -o '.be/.*' ./input/*.txt|cut -f2 -d"/" > result.txt
  grep -o '?v=.*' ./input/*.txt|cut -f2 -d"=" >> result.txt
  python splitjoin.py
  end=`date +%s.%N`
  runtime=$(echo "$end - $start"|bc -l)
  echo "Progress Complete!"
  echo "Executed in ${runtime} Secounds"
else 
  echo "File Not Found"
fi