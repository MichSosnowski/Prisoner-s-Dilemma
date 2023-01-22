set xlabel "history"
set ylabel "freq of game history"
set title "frequency of applied strategy"
plot 'result_2N_190.txt' using 1:2 with lines lt 4 lw 3 title "freq"