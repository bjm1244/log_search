#!/usr/bin/env bash
#
#
#
ipv4_address=$(curl ipv4.icanhazip.com)
RESULT=$(curl http://$ipv4_address:5000/api/total/abcd)
if [ $RESULT = "{\"client_id\":\"abcd\",\"total\":1}" ]
then
    echo "Integration Test Success"
    exit 0
else
    echo "Integration Test Failed"
    exit 100
fi