package mainfiles;

import algorithms.OriginalParallelSimulation;
import algorithms.ParallelSimulation;
import algorithms.Simulation;
import automata.FAState;
import automata.FiniteAutomaton;

import java.lang.management.*;
import java.lang.Exception;

import java.util.Random;
import java.util.TreeMap;
import java.util.Iterator;
import java.util.Set;
import java.util.TreeSet;
import datastructure.Pair;

public class ComparePerformance {
    public static void main(String[] args) {
        if (args.length < 2){
            System.out.println("You need give two Automata");
        }
        FiniteAutomaton aut1 = new FiniteAutomaton(args[0]);
        aut1.name=args[0];
        FiniteAutomaton aut2 = new FiniteAutomaton(args[1]);
        aut2.name=args[1];

        int la = Integer.parseInt(args[2]);
        int num_proc = Integer.parseInt(args[3]);
        int devideNum = Integer.parseInt(args[4]);

        OriginalParallelSimulation sim = new OriginalParallelSimulation();
        ParallelSimulation parallelSim = new ParallelSimulation();

        System.out.println("--------------------------------------------------");

        //NOTICE: BLAFairSimRelNBW
        long ttime1 = System.currentTimeMillis();
        Set<Pair<FAState,FAState>> result1 = sim.BLAFairSimRelNBW(aut1, aut2, la);
        long ttime2 = System.currentTimeMillis();
        System.out.println("Time used(ms) for Original Version: "+(ttime2-ttime1)+" ms.");

        long ttime3 = System.currentTimeMillis();
        Set<Pair<FAState,FAState>> result2 = parallelSim.BLAFairSimRelNBW(aut1, aut2, la);
        long ttime4 = System.currentTimeMillis();
        System.out.println("Time used(ms) for Parallel Version: "+(ttime4-ttime3)+" ms.");
        System.out.println();
        if(result2==result1){
            System.out.println("Both results are the same objects, be careful!");

        } else if (result1.containsAll(result2) && result2.containsAll(result1)){
            System.out.println("The Fair size is: " + result2.size());


        } else{
            System.out.println("InCorrect! The calculated parallel result is different from the Original result!");

        }

        //NOTICE: JumpingBLAFairSimRelNBW, bwchoice=1
        long ttime5 = System.currentTimeMillis();
        boolean result3 = sim.JumpingBLAFairSimRelNBW(aut1, aut2, la, 1);
        long ttime6 = System.currentTimeMillis();
        System.out.println("Time used(ms) for Original Version: "+(ttime6-ttime5)+" ms.");

        long ttime7 = System.currentTimeMillis();
        boolean result4 = parallelSim.JumpingBLAFairSimRelNBW(aut1, aut2, la, 1);
        long ttime8 = System.currentTimeMillis();
        System.out.println("Time used(ms) for Parallel Version: "+(ttime8-ttime7)+" ms.");

        System.out.println();
        if(result4==result3){
            System.out.println("The Jumping result is: " + result4);

        } else{
            System.out.println("InCorrect! The calculated parallel result is different from the Original result!");

        }

        System.out.println("================================================");

    }
}
