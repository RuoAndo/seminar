#!/bin/sh

TESTFILE=$1
while read line; do
    #echo $line
    python abuseip.py $line 2FB6kO3T8KrCAPcHgMm51tO8PjN4JLRcOL4s6Sed 30
    sleep 1m
done < $TESTFILE
