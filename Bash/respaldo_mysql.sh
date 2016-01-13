#!/bin/sh
mysqldump -uuser -ppassword --opt database1 > /var/backups/mysql/database1.sql
mysqldump -uuser -ppassword --opt database2 > /var/backups/mysql/database2.sql
mysqldump -uuser -ppassword --opt database3 > /var/backups/mysql/database3.sql
mysqldump -uuser -ppassword --opt database4 > /var/backups/mysql/database4.sql

cd /var/backups/mysql/
tar -zcvf respaldo_mysql_$(date +%d%m%y%H%M%S).tgz *.sql
find -name '*.tgz' -type f -mtime +90 -exec rm -f {} \;
