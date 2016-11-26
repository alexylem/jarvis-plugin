#!/bin/bash
# Here you can create functions which will be available from the commands file
# You can also use here user variables defined in your config file
# To avoid conflicts, name your function like this
# jv_pg_XX_myfunction () { }
# jv for JarVis
# pg for PluGin
# XX can be a two letters code for your plugin, ex: ww for Weather Wunderground

jv_pg_cm_time () {


local CM_QUERY="https://developer.citymapper.com/api/1/traveltime/?startcoord=$FROM&endcoord=$1&time=$DATE&time_type=arrival&key=$APIKEYCM"
local CM_TIME=$(curl -s "$CM_QUERY" | jq -r '.travel_time_minutes')
if [ "$CM_TIME" = "null" ]
then
echo "Je n'ai rien trouvé"
else
echo "$CM_TIME"
fi
}


