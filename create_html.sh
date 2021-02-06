#!/bin/bash -x

header="
                                                                                                                                                                                                              
Brandmeister digital contacts created automaticaly
Works for anytone at-d878uv
If you need digital contacts for you radio - send me a message of create a pull request.                                                                                                                           
                                                                                                                                                                                                             
"



ROOT=.
HTTP="/"
OUTPUT="README.md" 

echo $header > $OUTPUT

i=0
echo "<UL>" >> $OUTPUT
  for i in `find . -name "*.csv*" -type f | sort`; do
    file=`basename "$i"`
    echo "    <LI><a href=\"/$path/$file\">$file</a></LI>" >> $OUTPUT
  done
  echo "  </UL>" >> $OUTPUT
echo "</UL>" >> $OUTPUT

sleep 3



