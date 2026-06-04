#!/bin/bash

# define arguments here
data_dir="/Users/majaalm/Desktop/GitHub/BL2037/Maja/examples" # data directory containing PDB input files
PDB_input="$data_dir/*.pdb" # pattern to match all PDB input files in the data directory


# run python script here
for PDB_input in $PDB_input; do # loop through all the PDB input files in the data directory
    echo "Procesing PDB input file path: $PDB_input" # print the PDB input file path that is currently being processed
    python /Users/majaalm/Desktop/GitHub/BL2037/Maja/examples/read_pdb_argparsed.py \
            $PDB_input
        
done # end of loop

echo "All PDB input files have been processed." # print a message indicating that all PDB input files have been processed

