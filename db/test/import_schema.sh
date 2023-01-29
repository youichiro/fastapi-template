mysqldump -h 0.0.0.0 -u root -ppassword cale_development --no-create-db --no-data > dump.sql
mysql -h 0.0.0.0 -P 3306 -u root -ppassword cale_test < dump.sql
rm dump.sql
