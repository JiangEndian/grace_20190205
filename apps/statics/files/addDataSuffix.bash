#!/bin/bash
Prefix=$(date +%Y%m%d%H%M%S)
for f in *; do cp $f $Prefix$f;done
