#!/bin/bash

NOW=`date +%s`
TO=`date -d "+1day05:30" +%s`

MIN=$(((TO-NOW)/60))

echo $MIN

exit 0
