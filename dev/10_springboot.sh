#!/bin/bash

ts=`date +"%s"`
echo "[{'metric':'jvm.heap','value':100,'endpoint':'10.99.7.1','counterType': 'GAUGE','step':10,'timestamp':$ts}]"