#!/bin/bash

#usage: ./validateOMP points
THREADS="1 2 4 8 16"

seqRes=$(./../Src/energy_storms_seq $1 ../Src/test_files/test_01_a35_p8_w1 ../Src/test_files/test_01_a35_p7_w2 ../Src/test_files/test_01_a35_p5_w3 ../Src/test_files/test_01_a35_p8_w4)

for t in $THREADS; do
    if [ "$t" = 1 ]
    then
      seqRes=${seqRes:15}
    fi
    ompRes=$(./../Src/energy_storms_omp $t $1 ../Src/test_files/test_01_a35_p8_w1 ../Src/test_files/test_01_a35_p7_w2 ../Src/test_files/test_01_a35_p5_w3 ../Src/test_files/test_01_a35_p8_w4)
    ompRes=${ompRes:15}
    if [ "$seqRes" != "$ompRes" ]
    then
        echo $seqRes
        echo $ompRes
        echo omp version result is different from the sequential one.\n failed with $t threads.
    fi
done

echo validation ended...
