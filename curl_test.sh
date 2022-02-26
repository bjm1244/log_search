#!/usr/bin/env bash
#
#
#

python3 app.py &
ipv4_address=$(ip route | awk '{print $NF;exit}')
RESULT=$(curl http://$ipv4_address:5000/api/total/abcd)
if [ $RESULT = "{\"client_id\":\"abcd\",\"total\":1}" ]
then
    echo "Integration Test Success"
    exit 0
else
    echo "Integration Test Failed"
    exit 100
fi
killall -9 python3 python