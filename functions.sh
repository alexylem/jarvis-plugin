#!/bin/bash
# Here you can create functions which will be available from the commands file
# You can also use here user variables defined in your config file

jv_pg_ap_search ()
{

#room definition
local APPEAR_IN_QUERY="https://appear.in/$appear_room"

#open defaut web browser with the appear.in room
chromium-browser %U $APPEAR_IN_QUERY

}
