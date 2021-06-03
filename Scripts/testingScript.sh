#!/bin/bash

# Script adapted from post #73 on piazza by Hugo Lopes. Credits will be given in the report

clear

make clean

make all

echo "Running TESTS"

PROG="./energy_storms_omp"  ## Nome do programa que vai ser chamado

# Main cicle

for TF in 01 02 03 04 05 06 07 08 09

do

 echo ""

 echo "Test:          " $TF

 FILES=$(ls test_files/test_${TF}* | xargs -n1 | sort -t"_" -k6)

 echo "Files to test: " $FILES

 F3=$(echo ${FILES} | cut -d"/" -f2 | cut -d"_" -f3)

 echo "Flag:          " $F3

 case $F3 in 
  "a35") PAR=35;;

  "a30k") PAR=30000;;

  "a20") PAR=20;;

  "a1M") PAR=1000000;;

  "a100M") PAR=100000000;;

  "a16-17") PAR=17;;

 esac

 echo "Running:       " $PROG $PAR $FILES

 THREADS="1 2 4 8 16 32"
 NRUNS="5"
 for TH in $THREADS
 do
  for ((i=1; i<=$NRUNS; i++ ))
  do
   $PROG $TH $PAR $FILES >> output_file.csv
  done
 done

done