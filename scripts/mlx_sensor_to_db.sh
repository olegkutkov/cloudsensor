#!/bin/bash

put_to_db()
{
	sensor_data=$1

	skytemp=`echo $sensor_data | awk '{print $3}'`

	sqlite3 /media/STORAGE/db/sensordata.db "insert into cloudsensor(temp) values (\"${skytemp}\");"
}

sensor_data=`/opt/cloudsens/bin/read_mlx90614 --bus 1 --i2c_addr 0x2a -i`

put_to_db "${sensor_data}"

