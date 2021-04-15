#!/bin/sh
echo Generation started
echo Get States
cd ../
onespin --gui=no
source run.tcl
set out [get_signals -filter state==true]
set fp [open temp.txt a]
puts $fp "${out}"
close $fp
^C
echo Generate Equivalency File
cd State_Equivalency_Macro_Script/
python state_equivalence_macro_script
echo finished