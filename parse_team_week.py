#!/usr/bin/python

import xml.dom.minidom
import csv
import sys

# Parses team-week data as retrieved by the Yahoo FFL iPhone APIs.
# Reads in files based on a known directory/filename layout.

# For each file, extracts each player as a CSV row in this format:
#  team, week, playerID, playerFullname, lineupPosition, fantasyPoints

# TODO this assumes that the data is in xml files under data/
# assumes that each file is named data/stats_<team>_<week>.xml

numTeams = 12
numWeeks = 12

wrtr = csv.writer(sys.stdout)

for tm in range(1, numTeams+1) : 
	for wk in range(1, numWeeks+1) : 
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



