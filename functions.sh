#!/bin/bash
pg_chacon_turn () {
    # $1: action [on|off]
    # $2: received order
    local -r order="$(jv_sanitize "$2")"
    while read device; do
        local sdevice="$(jv_sanitize "$device" ".*")"
        if [[ "$order" =~ .*$sdevice.* ]]; then
            local address="$(echo $pg_chacon_config | jq -r ".devices[] | select(.name==\"$device\") | .address")"
            say "$(pg_chacon_lg "switching_$1" "$2")"
            local cmd="sudo ./$pg_chacon_dir/chacon_send 0 $pg_chacon_num $address $1"
            $verbose && jv_debug "$> $cmd"
            eval $cmd | while read line; do jv_debug "$line"; done # safe as no user input in $cmd. pass each output line to jv_debu
			say "c'est fait"
            return $?
        fi
    done <<< "$(echo $pg_chacon_config | jq -r '.devices[].name')"
    say "$(pg_chacon_lg "no_device_matching" "$2")"
    return 1
}
