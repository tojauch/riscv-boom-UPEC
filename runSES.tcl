set out [get_signals -filter state==true]
set fp [open temp.txt a]
puts $fp "${out}"
close $fp