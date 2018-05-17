#!/bin/bash

sleep 10

put_to_db()
{
	temp=`echo $1 | awk '{print $1}' | awk -F '=' '{print $2}'`
	humidity=`echo $1 | awk '{print $2}' | awk -F '=' '{print $2}'`

	if [ -z "$temp" ]; then
		echo "Failed to get temperature!"
		exit 1
	fi

	if [ -z "$humidity" ]; then
		echo "Failed to get humidity!"
		exit 1
	fi

	sqlite3 /media/STORAGE/db/sensordata.db "insert into ambientsensor(temp, humid) values (\"${temp}\", \"${humidity}\");"	
}

external_sensor=`/opt/cloudsens/bin/read_htu21d`

put_to_db "${external_sensor}"

