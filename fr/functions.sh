pg_chacon_lg() {
    case "$1" in
        no_device_matching) echo "Aucun appareil ne correspond à $2";;
        switching_on) echo "J'allume $2";;
        switching_off) echo "J'éteins $2";;
        *) jv_error "ERROR: unknown translation key: $1";;
    esac
}