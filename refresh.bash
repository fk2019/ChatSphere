#!/usr/bin/bash
# refresh db

cat dropdb.sql | mysql -uroot -p;
cat getdb.sql | mysql -uroot -p;
