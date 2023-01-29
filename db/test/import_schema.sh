#!/usr/bin/env bash

set -ue

mysqldump -h $MYSQL_HOST -P $MYSQL_PORT -u root -p$MYSQL_ROOT_PASSWORD $MYSQL_DATABASE --no-create-db --no-data > dump.sql
mysql -h $MYSQL_HOST -P $MYSQL_PORT -u root -p$MYSQL_ROOT_PASSWORD $MYSQL_TEST_DATABASE < dump.sql
rm dump.sql
