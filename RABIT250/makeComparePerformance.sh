#!/bin/zsh

#Configuration:
La=10
Processor_Num=8
BLAFair_getavoid_devideNum=10

# Save arguments to variables
if [ "$1" != "" ] && [ "$2" != "" ]; then
    First_Automata=$1
    Second_Automata=$2
else
    First_Automata="./Datasets/200_1.3_0.5/1.a.ba"
    Second_Automata="./Datasets/200_1.3_0.5/1.b.ba"
fi

if [ "$3" != "" ]; then
    result_file="$3"
else
    result_file="./results/output.txt"
fi

echo "The compared two automata files are: " >> $result_file
echo "1.  "$First_Automata >> $result_file
echo "2.  "$Second_Automata >> $result_file
echo "" >> $result_file
echo "The created processsor number is:  "$Processor_Num >> $result_file

#echo "The compared two automata files are: "
#echo "1.  "$First_Automata
#echo "2.  "$Second_Automata
#echo ""
#echo "The created processor number is:  "$Processor_Num



#    for a in {1..12}
#    do
#      La=$a
#      for j in {1..20}
#      do
#        BLAFair_getavoid_devideNum=$j
#
#        echo "" >> $result_file
#        echo ""
#
#        echo "*************  La: "$La", BLAFair_getavoid_devideNum: "$BLAFair_getavoid_devideNum"  *********************" >> $result_file
#        echo "*************  La: "$La", BLAFair_getavoid_devideNum: "$BLAFair_getavoid_devideNum"  *********************"
#
#        for i in {1..3}
#        do
#          output=$(java -jar ComparePerformance.jar $First_Automata $Second_Automata $La $Processor_Num $BLAFair_getavoid_devideNum)
#
#          echo "" >> $result_file
#          echo "The Running Time "$i": " >> $result_file
#          echo $output >> $result_file
#
#          echo ""
#          echo "The Running Time "$i": "
#          echo $output
#        done
#      done
#    done

output=$(java -jar ComparePerformance.jar $First_Automata $Second_Automata $La $Processor_Num $BLAFair_getavoid_devideNum)

echo "" >> $result_file
echo "The Running Time: " >> $result_file
echo $output >> $result_file

#echo ""
#echo "The Running Time: "
#echo $output

