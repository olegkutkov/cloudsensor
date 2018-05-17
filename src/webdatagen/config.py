#
# Configuration file for webdata generator
# 

SQLITE_DB_FILE = '/media/STORAGE/db/sensordata.db'

### system report ###

BOARD_MODEL_FILE = '/proc/device-tree/model'
OS_RELEASE_FILE = '/etc/os-release'

SYSTEM_HTML_TEMPLATE = '/runtime_storage/web/system.html.tpl'
SYSTEM_HTML_RESULT = '/runtime_storage/webdata/system.html'

PLOT_DISKS_USAGE = '/runtime_storage/webdata/disks_usage.png'

###

### system sensors

PLOT_CPU_TEMPERATURE_DAY = '/runtime_storage/webdata/cpu_temperature_day.png'
PLOT_INTERNAL_DH22_DAY = '/runtime_storage/webdata/internal_dh22_day.png'

###

### sensor graphgen ###

PLOT_CLOUD_SENSOR_DAY = '/runtime_storage/webdata/cloud_sensor_day.png'
CSV_CLOUD_SENSOR_DAY = '/runtime_storage/webdata/cloud_sensor_day.csv'

PLOT_CLOUD_SENSOR_WEEK = '/runtime_storage/webdata/cloud_sensor_week.png'
CSV_CLOUD_SENSOR_WEEK = '/runtime_storage/webdata/cloud_sensor_week.csv'

PLOT_CLOUD_SENSOR_MONTH = '/runtime_storage/webdata/cloud_sensor_month.png'
CSV_CLOUD_SENSOR_MONTH = '/runtime_storage/webdata/cloud_sensor_month.csv'

PLOT_CLOUD_SENSOR_YEAR = '/runtime_storage/webdata/cloud_sensor_year.png'
CSV_CLOUD_SENSOR_YEAR = '/runtime_storage/webdata/cloud_sensor_year.csv'


PLOT_AMBIENT_SENSOR_DAY = '/runtime_storage/webdata/ambient_sensor_day.png'
CSV_AMBIENT_SENSOR_DAY = '/runtime_storage/webdata/ambient_sensor_day.csv'

PLOT_AMBIENT_SENSOR_WEEK = '/runtime_storage/webdata/ambient_sensor_week.png'
CSV_AMBIENT_SENSOR_WEEK = '/runtime_storage/webdata/ambient_sensor_week.csv'

PLOT_AMBIENT_SENSOR_MONTH = '/runtime_storage/webdata/ambient_sensor_month.png'
CSV_AMBIENT_SENSOR_MONTH = '/runtime_storage/webdata/ambient_sensor_month.csv'

PLOT_AMBIENT_SENSOR_YEAR = '/runtime_storage/webdata/ambient_sensor_year.png'
CSV_AMBIENT_SENSOR_YEAR = '/runtime_storage/webdata/ambient_sensor_year.csv'

WEB_SKYTEMP_FILE = '/runtime_storage/webdata/sky_temp.txt'
WEB_CURRENT_COND_FILE = '/runtime_storage/webdata/current_cond.txt'
WEB_OUT_TEMP_FILE = '/runtime_storage/webdata/air_temp.txt'
WEB_OUT_HUMID_FILE = '/runtime_storage/webdata/air_humid.txt'

###

