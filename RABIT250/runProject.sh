#!/bin/zsh

#Configuration:
size=500
td=1.7
fd=0.5
alphabetSize=2

folder="./Datasets/"$size"_"$td"_"$fd

#Configuration:
Processor_Num=8

First_Automata="./Datasets/200_1.3_0.5/1.a.ba"
Second_Automata="./Datasets/200_1.3_0.5/1.b.ba"


result_file="./results/output.txt"
echo "" > $result_file

#Compile and make jar package
javac ./mainfiles/ComparePerformance.java
if [ $? -ne 0 ]; then
    Compile_Status="Error occurred during compilation."
else
    Compile_Status="Compilation successful."
fi

jar cvfe ComparePerformance.jar mainfiles.ComparePerformance mainfiles/ComparePerformance.class automata/*.class datastructure/*.class comparator/*.class algorithms/*.class
if [ $? -ne 0 ]; then
    Jar_Status="Error occurred during jar."
else
    Jar_Status="jar successful."
fi

# Check if both Compile and jar package succeed, if succeed, execute the program. Otherwise, print the problem
if [[ $Compile_Status == "Compilation successful." ]] && [[ $Jar_Status == "jar successful." ]]; then
    clear
    echo $Compile_Status
    echo $Jar_Status
    echo "Start Working...."

    #Run the program:
    for i in {1..100}
    do
      First_Automata=$folder"/"$i".a.ba"
      Second_Automata=$folder"/"$i".b.ba"
      ./makeComparePerformance.sh $First_Automata $Second_Automata $result_file
    done

    echo "FINISH!!!"

#for j in {500..500..100}
#do
#  size=$j
#
#  size=500
#
#  for q in $(seq 1.9 0.2 2.3)
#  do
#    td=$q
#
#    td=1.3
#
#    folder="./Datasets/"$size"_"$td"_"$fd
#    echo $folder
#
#    for i in {1..200}
#    do
#      First_Automata=$folder"/"$i".a.ba"
#      Second_Automata=$folder"/"$i".b.ba"
#      ./makeComparePerformance.sh $First_Automata $Second_Automata $result_file
#
#    done
#  done
#done

    # This is to check whether all results are correct
    java results/FileChecker $result_file

else
    echo $Compile_Status
    echo $Jar_Status
fi


#for j in {200..500..100}
#do
#  size=$j
#  for q in $(seq 1.3 0.2 2.3)
#  do
#    td=$q
#    folder="./Datasets/"$size"_"$td"_"$fd
#    echo $folder
#    mkdir $folder
#    for i in {1..1000}
#    do
#      outputFile1=$folder"/"$i".a"
#      outputFile2=$folder"/"$i".b"
#
#      java -jar TV.jar $size $td $fd $alphabetSize $outputFile1
#      java -jar TV.jar $size $td $fd $alphabetSize $outputFile2
#    done
#  done
#done