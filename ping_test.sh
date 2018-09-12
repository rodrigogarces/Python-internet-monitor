#!/bin/bash

#usage
#./ping_test.sh -d [duration - in seconds] -f [log file]


#----- help function -----
function helper {
    echo "Usage:
  ping_test [OPTION...]

Application Options:
  -d                            Duration (in seconds)
  -f                            Log file (use current datetime is not specified)
  -h                            Help
  -H                            Host (use google.com if not specified)
  -i                            Interval between pings (in seconds)
  -v                            Verbose mode
  -V                            Version
"
}

#----- Main program -----

#
while getopts d:f:hH:i:vV option
do
    case "${option}"
    in
        d) duration=${OPTARG};;
        f) file=${OPTARG}.log;;
        h) helper
        aux_helper=$"1";;
        H) host=${OPTARG};;
        i) interval=${OPTARG};;
        v) verbose=$"1";;
        V) echo "Version 0.36 beta"
        aux_helper=$"1";;
    esac
done
#echo $host


if [ "$aux_helper" "==" "" ]; then
    #If no log file is specified
    if [ "$file" "==" "" ]; then    
        file="ping_"$(date +%Y_%m_%d_%H_%M_%S).log
    fi

    #If no host is specified 
    if [ "$host" "==" "" ]; then
        host=$"google.com"
    fi

    #If no interval is specified 
    if [ "$interval" "==" "" ] || [ "$interval" "<" "0.2" ]; then
        interval=$"1"
    fi
    
    #if duration is specified
    if ! [ "$duration" "==" "" ] && ! [ -n "$(printf '%s\n' "$duration" | sed 's/[0-9]//g')" ]; then
        if [[ $verbose == "1" ]]; then
            echo "        Duration time is $duration seconds
        Host is $host
        Log file is $file
        Interval is $interval

        Executing..."
        fi

        #echo "ping $host -n -W 1 -i $interval -w $duration |& xargs -L 1 -I '{}' date '+%Y-%m-%d %H:%M:%S: {}' |& tee $file"
        ping $host -n -W 1 -i $interval -w $duration |& xargs -L 1 -I '{}' date '+%Y-%m-%d %H:%M:%S: {}' |& tee $file
    else
        echo "Invalid or missing arguments"
        helper
    fi  
fi
