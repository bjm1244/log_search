#!/usr/bin/env bash
#
#
#

RESULT=$(curl http://127.0.0.1:5000/api/total/abcd)
if [ $RESULT = "{\"client_id\":\"abcd\",\"total\":1}" ]
then
    echo "Integration Test Success"
    exit 0
else
    echo "Integration Test Failed"
    exit 100
fi