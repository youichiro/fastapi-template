#!/usr/bin/env bash

set -ue

sqls="
    SET foreign_key_checks = 0;
    TRUNCATE admin_accounts;
    SET foreign_key_checks = 1;
    INSERT INTO admin_accounts (id, admin_name, admin_secret) VALUES (id, 'demo', 'demo_secret');
"

echo $sqls | mysql -h $MYSQL_HOST -P $MYSQL_PORT -u root -p$MYSQL_ROOT_PASSWORD $MYSQL_TEST_DATABASE
