#!/bin/sh

dated=`date +%Y-%m-%d-%H%M%S`

#./gnu-mirror-index-creator.sh

tree -P "*.csv" -H '.' --charset utf-8 > index.html


pwd
sleep 1 
git add .
git commit -m "Brandmaister autocommit  digital contacts on "${dated} 
git push -u origin main 
