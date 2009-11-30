#!/usr/bin/python

import xml.dom.minidom
import csv
import sys

# Parses team-week data as retrieved by the Yahoo FFL iPhone APIs.
# Reads in files based on a known directory/filename layout.

# For each file, extracts each player as a CSV row in this format:
#  teamNum, weekNum, playerID, playerFullname, lineupPosition, fantasyPoints

# TODO this assumes that the data is in xml files under data/
# assumes that each file is named data/stats_<teamNum>_<weekNum>.xml

numTeams = 12
numWeeks = 12

wrtr = csv.writer(sys.stdout)

for teamNum in range(1, numTeams+1) : 
	for weekNum in range(1, numWeeks+1) : 
		filename = "data/stats_" + format(teamNum) + "_" + format(weekNum) + ".xml"
		mydoc = xml.dom.minidom.parse(filename)
		players = mydoc.getElementsByTagName("fantasy-player")

		for player in players:
			player_metadata = player.getElementsByTagName("fantasy-player-metadata")[0]
			player_stats = player.getElementsByTagName("fantasy-player-stats")[0]

			# Get the fields we want
			lineupPos = player.getElementsByTagName("fantasy-selected-position")[0].getAttribute("value")
			playerID = player_metadata.getAttribute("player-key")
			fullname = player_metadata.getElementsByTagName("name")[0].getAttribute("full")
			points = float(player_stats.getElementsByTagName("points")[0].getAttribute("value"))
			
			# And write them
			wrtr.writerow([teamNum, weekNum, playerID, fullname, lineupPos, points])

