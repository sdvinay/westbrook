#!/usr/bin/python

import xml.dom.minidom
import csv
import sys

wrtr = csv.writer(sys.stdout)

for tm in range(1, 13) : 
	for wk in range(1, 13) : 
		filename = "data/stats_" + format(tm) + "_" + format(wk) + ".xml"
		mydoc = xml.dom.minidom.parse(filename)
		plrs = mydoc.getElementsByTagName("fantasy-player")

		for plr in plrs:
			plyr_md = plr.getElementsByTagName("fantasy-player-metadata")[0]
			stats = plr.getElementsByTagName("fantasy-player-stats")[0]

			lineupPos = plr.getElementsByTagName("fantasy-selected-position")[0].getAttribute("value")
			id = plyr_md.getAttribute("player-key")
			fullname = plyr_md.getElementsByTagName("name")[0].getAttribute("full")
			points = float(stats.getElementsByTagName("points")[0].getAttribute("value"))
			
			wrtr.writerow([tm, wk, id, fullname, lineupPos, points])



