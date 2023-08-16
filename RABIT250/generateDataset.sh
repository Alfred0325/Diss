#!/bin/zsh

#Configuration:
size=200
td=1.3
fd=0.5
alphabetSize=2

echo "Generating Automata Dataset..."
echo "------------------------------------"

folder="./Datasets/"$size"_"$td"_"$fd

echo $folder

for j in {200..500..100}
do
  size=$j
  for q in $(seq 1.3 0.2 2.3)
  do
    td=$q
    folder="./Datasets/"$size"_"$td"_"$fd
    echo $folder
    mkdir $folder
    for i in {1..1000}
    do
      outputFile1=$folder"/"$i".a"
      outputFile2=$folder"/"$i".b"

      java -jar TV.jar $size $td $fd $alphabetSize $outputFile1
      java -jar TV.jar $size $td $fd $alphabetSize $outputFile2
    done
  done
done

echo "FINISH!!!  All data have been generated!"

#mkdir $folder
#for i in {1..1000}
#do
#  outputFile1=$folder"/"$i".a"
#  outputFile2=$folder"/"$i".b"
#
#  java -jar TV.jar $size $td $fd $alphabetSize $outputFile1
#  java -jar TV.jar $size $td $fd $alphabetSize $outputFile2
#done