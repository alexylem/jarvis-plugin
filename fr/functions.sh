#!/bin/bash


jv_pg_cb_timetable() {
destination=$(echo "$gare_destination"  | sed s/'_'/'-'/g)
local dt=$(echo `date +%d%m%y`)
local tm=$(echo `date +%H%M`)
local respiration="................................"
local cpt=0
local lg=0
echo "vers $destination $respiration"

while [ $cpt -lt 3 ]
do
   local json=$(curl -s -S "https://api.irail.be/connections/?to="$destination"&from="$gare_depart"&date="$dt"&time="$tm"&timeSel=depart&format=json")
   local lg=$(echo "${#json}")
#   echo "lg = $lg"
#   echo $json
   if (( "$lg" > "1000" ))
   then
      local conn0=$(echo "$json" | jq '[.connection[].departure.time]' | sed 's/\[//' | sed 's/\]//')
      local delay0=$(echo "$json" | jq '[.connection[].departure.delay]' | sed 's/\[//' | sed 's/\]//')
      local cancel0=$(echo "$json" | jq '[.connection[].departure.canceled]' | sed 's/\[//' | sed 's/\]//')
      local direct0=$(echo "$json" | jq '[.connection[].departure.direction.name]' | sed 's/\[//' | sed 's/\]//')
      break
   fi  
   cpt=$[$cpt+1]
done
local connections="$(echo -e "${conn0}" | tr -d '[:space:]' | tr -d '[="=]')" 
local delays="$(echo -e "${delay0}" | tr -d '[:space:]' | tr -d '[="=]')"
local cancels="$(echo -e "${cancel0}" | tr -d '[:space:]' | tr -d '[="=]')"
local directs="$(echo -e "${direct0}" | tr -d '[:space:]' | tr -d '[="=]')"

IFS=',' read -a conn <<< $connections
IFS=',' read -a dela <<< $delays
IFS=',' read -a canc <<< $cancels
IFS=',' read -a dire <<< $directs
# local nb=$(echo ${#conn[@]})
local cpt=0
for n in ${!conn[*]}
do
   echo `date --date="@${conn[$n]}" +%R`
   echo ".... en direction de ${dire[$n]}"
   if (( ${canc[$n]} == "0" )); then
      if (( ${dela[$n]} == "0" )); then
         echo "......... pas de retard annoncé" 
      else
         echo "......... avec un retard annoncé de $((${dela[$n]}/60)) minutes" 
      fi 
   else   
      echo "......... attention .... ce train est supprimé" 
   fi
   cpt=$[$cpt+1]
   if (( "$cpt" > "2" ))
   then
      break
   fi
   echo "$respiration ensuite $respiration"
done
}

gare_depart="Blanmont"
gare_destination="Bruxelles-Nord"
jv_pg_cb_timetable

