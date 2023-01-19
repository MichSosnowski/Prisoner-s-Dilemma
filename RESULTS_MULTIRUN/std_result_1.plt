set xlabel "gen"
set title "std deviation for avg best"
plot 'std_result_1.txt' using 1:2 with lines lt 4 lw 3 title "avg best",\
'std_result_1.txt' using 1:2:3 with yerrorbars title "std best"