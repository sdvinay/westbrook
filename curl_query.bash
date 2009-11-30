#/bin/bash


export lg=311842
data_dir=data_${lg}
mkdir -p ${data_dir}

for week in `seq 1 12` ; do 
	for tm in `seq 1 12` ; do
		curl --header 'User-Agent: YahooMobile/1.0 (iPhone Fantasy Football; 1.1) (Apple; iPhone; iPhone OS/3.1.2)' \
			 --header 'X-Device-Info: id="6693"; make="Apple"; model="iPhone"; os="iPhone OS"; osver="3.1.2"' \
			 --header 'X-Client-Uuid: 0B9F7341-F510-4699-B106-15AB9EA5A0D1' \
			 --header 'X-Request-Id: 50C138DA-D0D2D252' \
			 --header 'Proxy-Authorization: Digest nonce="4AvIdy1l0fWNgJd3ziSq6khCnwjwL3Iwl1tCdw--" uri="/1715/" response="0ZziWMwJYVyt6YYg43jFuQ--"' \
			 --header 'X-Proxy-Authorization: Digest nonce="4AvIdy1l0fWNgJd3ziSq6khCnwjwL3Iwl1tCdw--" uri="/1715/" response="0ZziWMwJYVyt6YYg43jFuQ--"' \
			 --header 'Cookie: T=z=ZrxELBZxGFLBWow69GUlRSANjY1MgYwNDM0NzYxTjA-&a=YAE&sk=DAAQW2UarGPOnX&ks=EAA6EQalnT7EE4VUVIj1ikenA--~C&d=c2wBTVRFeU5RRTNNelF6TURFMk9UYy0BYQFZQUUBaWcBRnNIcEJBAWcBN1EzT0lMRVFEQVJZVzRTVlc3S1AzVjZOVkEBb2sBWlcwLQF6egFacnhFTEJnV0EBdGlwAUhob19sRA--; Y=v=1&n=7a2d49gd44gv4&l=i3l8d0o/o&p=m2c2pudcd3000300&jb=21|44|&r=5s&lg=en-US&intl=us&np=1' \
			 --output ${data_dir}/stats_${tm}_${week}.xml \
			 "http://ffootball.iphone.mobile.yahoo.com/54de/games/222/leagues/${lg}/teams/${tm}/roster/week/${week}/stats/show-stats=1;show-league-settings=1;show-status=1;show-image=1" 
	done
done
echo
