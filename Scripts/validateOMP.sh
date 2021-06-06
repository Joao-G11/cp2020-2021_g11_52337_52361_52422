#!/bin/bash

#usage: ./validateOMP
THREADS="1 2 4 8 16"

seqRes=$(./../Src/energy_storms_seq 100000000 ../Src/test_files/test_09_a16-17_p3_w1)

for t in $THREADS; do
    if [ "$t" = 1 ]
    then
      seqRes=${seqRes:20}
    fi
    ompRes=$(./../Src/energy_storms_omp $t 100000000 ../Src/test_files/test_09_a16-17_p3_w1)
    ompRes=${ompRes:20}
    if [ "$seqRes" != "$ompRes" ]
    then
        echo $seqRes
        echo $ompRes
        echo omp version result is different from the sequential one.\n failed with $t threads.
    fi
done

echo validation ended...
