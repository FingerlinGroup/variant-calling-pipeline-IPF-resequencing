#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: count_off_target.sh <bed> <bam> <samtools>"
    exit -1
fi

bed=$1
bam=$2
samtools=$3

bam_name=$(basename $bam)
on_target=$($samtools view -c -L $bed $bam)
total=$($samtools view -c -F 4 $bam)
off_target=$( expr $total - $on_target )
pct_on_target=$( bc <<< "scale=2; $on_target/$total" )

echo -e "$bam\t$on_target\t$off_target\t$pct_on_target"

