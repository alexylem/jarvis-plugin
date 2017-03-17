pg_chacon_turn () {
    # $1: action [on|off]
    # $2: received order
    local -r order="$(jv_sanitize "$2")"
    while read device; do
        local sdevice="$(jv_sanitize "$device" ".*")"
        if [[ "$order" =~ .*$sdevice.* ]]; then
            local address="$(echo $pg_chacon_config | jq -r ".devices[] | select(.name==\"$device\") | .address")"
            say "$(pg_chacon_lg "switching_$1" "$2")"
            local cmd="echo \"pl $address $1\" | nc localhost $pg_chacon_mochad_port"
            $verbose && jv_debug "$> $cmd"
            eval $cmd | while read line; do jv_debug "$line"; done # safe as no user input in $cmd. pass each output line to jv_debug
            return $?
        fi
    done <<< "$(echo $pg_chacon_config | jq -r '.devices[].name')"
    say "$(pg_chacon_lg "no_device_matching" "$2")"
    return 1
}