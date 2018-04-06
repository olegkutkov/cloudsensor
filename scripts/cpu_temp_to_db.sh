#!/bin/bash

put_to_db()
{
	temp=$1

	sqlite3 /media/STORAGE/db/sensordata.db "insert into cpusensor(temp) values (\"${temp}\");"
}

cpu_temp=`cat /sys/class/thermal/thermal_zone0/temp`
cpu_temp=`bc <<< "scale=2; $cpu_temp/1000"`

put_to_db $cpu_temp

