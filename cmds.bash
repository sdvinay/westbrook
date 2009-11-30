export pos=WR
export repl_lev=6.0
awk -F, '	($5 == ENVIRON["pos"]) {starts[$3]++; name[$3] = $4; pts[$3] += $6} 
			END { for (plr in starts) 
					{	avg = pts[plr]/starts[plr]; 
						VORP= (avg-ENVIRON["repl_lev"])*starts[plr] ;
						printf("%s, %d, %d, %0.1f, %01.f \n", name[plr], starts[plr], pts[plr], avg, VORP)}}' \
	data/weeklies.csv | 
sort  --field-separator=, --numeric-sort --key=5 --reverse

./parse_team_week.py > weeklies.csv
