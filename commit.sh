#!/bin/sh

dated=`date +%Y-%m-%d-%H%M%S`

#./jtc_users.py
#./jtc_users.ua.py
#./jtc_users.by.py


./gnu-mirror-index-creator.sh

sleep 1 
git add .
git commit -m "Brandmaister digital contacts on "${dated} 
git push -u origin main 
