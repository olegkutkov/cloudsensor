#!/bin/bash

SRC_DIR="/media/STORAGE/web"
DST_WEB_DIR="/runtime_storage/web"
DST_WEBDATA_DIR="/runtime_storage/webdata"
DST_EPHEMDATA_DIR="/runtime_storage/ephemdata"

mkdir -p ${DST_WEB_DIR}
mkdir -p ${DST_WEBDATA_DIR}
mkdir -p ${DST_EPHEMDATA_DIR}

chown allsky:allsky ${DST_WEB_DIR}/*
chown allsky:allsky ${DST_WEBDATA_DIR}/*
chown allsky:allsky ${DST_EPHEMDATA_DIR}*

cp -v ${SRC_DIR}/*html ${DST_WEB_DIR}
cp -v ${SRC_DIR}/*tpl ${DST_WEB_DIR}
cp -v ${SRC_DIR}/*txt ${DST_WEB_DIR}

cp -vfr ${SRC_DIR}/css ${DST_WEB_DIR}
cp -vfr ${SRC_DIR}/js ${DST_WEB_DIR}
cp -vfr ${SRC_DIR}/fonts ${DST_WEB_DIR}

cp -fv ${SRC_DIR}/*png ${DST_WEB_DIR}

cp -fv ${SRC_DIR}/favicon.ico ${DST_WEB_DIR}
cp -fv ${SRC_DIR}/safari-pinned-tab.svg ${DST_WEB_DIR}

cp -fv ${SRC_DIR}/manifest.json ${DST_WEB_DIR}
cp -fv ${SRC_DIR}/browserconfig.xml ${DST_WEB_DIR}

/opt/cloudsens/bin/webdatagen/generate_web_data.sh textdata > /runtime_storage/webdata/webdatagen_text_last.log 2>&1

/opt/cloudsens/bin/webdatagen/generate_web_data.sh sensors-day > /runtime_storage/webdata/webdatagen_week_last.log 2>&1
/opt/cloudsens/bin/webdatagen/generate_web_data.sh sensors-week > /runtime_storage/webdata/webdatagen_week_last.log 2>&1
/opt/cloudsens/bin/webdatagen/generate_web_data.sh sensors-month > /runtime_storage/webdata/webdatagen_month_last.log 2>&1
/opt/cloudsens/bin/webdatagen/generate_web_data.sh sensors-year > /runtime_storage/webdata/webdatagen_year_last.log 2>&1

/opt/cloudsens/bin/webdatagen/generate_web_data.sh system-report-sensors > /runtime_storage/webdata/webdatagen_system_sensors_last.log 2>&1
/opt/cloudsens/bin/webdatagen/generate_web_data.sh system-report > /runtime_storage/webdata/webdatagen_system_all_last.log 2>&1

chown allsky:allsky ${DST_WEB_DIR}/*
chown allsky:allsky ${DST_WEBDATA_DIR}/*
chown allsky:allsky ${DST_EPHEMDATA_DIR}*

