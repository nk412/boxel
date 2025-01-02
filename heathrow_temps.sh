#!/usr/bin/env bash


paste <( curl -s https://raw.githubusercontent.com/alanjones2/uk-historical-weather/refs/heads/main/data/Heathrow.csv \
	| awk -F, '{if($2==1953){print $NF}}' )\
      <( curl -s https://raw.githubusercontent.com/alanjones2/uk-historical-weather/refs/heads/main/data/Heathrow.csv \
	| awk -F, '{if($2==1988){print $NF}}' )\
      <( curl -s https://raw.githubusercontent.com/alanjones2/uk-historical-weather/refs/heads/main/data/Heathrow.csv \
	| awk -F, '{if($2==2023){print $NF}}' )\
 | python boxel.py --bins 100
