set xlabel "gen"
set title "average total payoff (ATP)"
plot 'm_result_1.txt' using 1:2 with lines lt 4 lw 3 title "best fit",\
'm_result_1.txt' using 1:3 with lines lt 3 lw 3 title "avg fit"