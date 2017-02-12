#!/usr/bin/env bash
#
# https://github.com/getmicah/spotify-now

# track info
album () {
    res=$(echo "$META" | grep -m 1 "xesam:album" -b1 | tail -n1)
    res="${res%\"*}"
    res="${res#*\"}"
    echo "$res"
}
artist () {
    res=$(echo "$META" | grep -m 1 "xesam:artist" -b2 | tail -n1)
    res="${res%\"*}"
    res="${res#*\"}"
    # if advertisement is playing currently
    if [[ "$res" == "" ]]; then
        echo "Ad"
    else
        echo "$res"
    fi
}
disc () {
    res=$(echo "$META" | grep -m 1 "xesam:discNumber" -b1 | tail -n1)
    res="${res#*3}"
    res="${res#*2}"
    echo "$res"
}
title () {
    res=$(echo "$META" | grep -m 1 "xesam:title" -b1 | tail -n1)
    res="${res%\"*}"
    res="${res#*\"}"
    echo "$res"
}
track () {
    res=$(echo "$META" | grep -m 1 "xesam:trackNumber" -b1 | tail -n1)
    res="${res#*3}"
    res="${res#*2}"
    echo "$res"
}

# error message
errorMsg () {
    echo "Error: invalid argument"
    echo "Help: 'spotify-now -h'"
    echo "Info: https://github.com/getmicah/spotify-now"
    exit 0
}

# help message
helpMsg () {
    echo -e "\nUsage: spotify-now -i \"<info>\" -e \"<error>\" -p \"<paused>\""
    echo -e "\n\"<info>\" can contain the following keywords:"
    echo -e "\t%album, %artist, %disc, %title, %track"
    echo -e "\n\"<error>\" your custom Spotify closed message."
    echo -e "\n\"<paused>\" your custom Spotify paused message."
    echo -e "\nhttps://github.com/getmicah/spotify-now\n"
    exit 0
}


# check args
if [[ "$#"  == 0 ]]; then
    helpMsg
elif [[ "$#" == 1 ]]; then
    if [[ "${1}" == "-h" || "${1}" == "--help" ]]; then
        helpMsg
    else
        errorMsg
    fi
elif [[ "$#" > 6 ]]; then
    errorMsg
fi
if [[ "$#" -ge 2 ]]; then
    if [[ "${1}" != "-i" && "${1}" != "-p" && "${1}" != "-e" ]]; then
        errorMsg
    fi
fi
if [[ "$#" -ge 4 ]]; then
    if [[ "${3}" != "-i" && "${3}" != "-p" && "${3}" != "-e" ]]; then
        errorMsg
    fi
fi
if [[ "$#" -ge 6 ]]; then
    if [[ "${5}" != "-i" && "${5}" != "-p" && "${5}" != "-e" ]]; then
        errorMsg
    fi
fi


# identify parameters
INFO=""
PAUSED=""
ERROR=""
ESCAPE=false
if [[ "${1}" == "-i" ]]; then
    INFO="${2}"
elif [[ "${1}" == "-p" ]]; then
    PAUSED="${2}"
elif [[ "${1}" == "-e" ]]; then
    ERROR="${2}"
fi
if [[ "${3}" == "-i" ]]; then
    INFO="${4}"
elif [[ "${3}" == "-p" ]]; then
    PAUSED="${4}"
elif [[ "${3}" == "-e" ]]; then
    ERROR="${4}"
fi
if [[ "${5}" == "-i" ]]; then
    INFO="${6}"
elif [[ "${5}" == "-p" ]]; then
    PAUSED="${6}"
elif [[ "${5}" == "-e" ]]; then
    ERROR="${6}"
fi
if [[ "${3}" == "--escape" || "${5}" == "--escape" || "${7}" == "--escape" ]]; then
    ESCAPE=true
fi


# check if spotify is running
status=`pidof spotify | wc -l`
if [[ "$status" != 1 && "$ERROR" != "" ]]; then
    echo "$ERROR"
else
	playback=`dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:'org.mpris.MediaPlayer2.Player' string:'PlaybackStatus' | grep -o Paused`
	if [[ "$playback" == "Paused" && "$PAUSED" != "" ]]; then
		echo "$PAUSED"
	elif [[ "$INFO" != "" ]]; then
   		# get mpris2 dbus status of spotify player
   		META=`dbus-send --print-reply --session --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:'org.mpris.MediaPlayer2.Player' string:'Metadata'`
   		INFO="${INFO//"%album"/$(album)}"
   		INFO="${INFO//"%artist"/$(artist)}"
   		INFO="${INFO//"%disc"/$(disc)}"
   		INFO="${INFO//"%title"/$(title)}"
   		INFO="${INFO//"%track"/$(track)}"
		if [ "$ESCAPE" = true ]; then
			INFO="${INFO//&/&amp;}"
			INFO="${INFO//</&lt;}"
			INFO="${INFO//>/&gt;}"	
			INFO="${INFO//\"/&quot;}"
			INFO="${INFO//\\/\\\\}"
		fi
		echo $INFO
	fi
fi
