#!/bin/bash
# Sqoop import script for SQL data
sqoop import \
--connect jdbc:mysql://[hostname]/[db_name] \
--username [username] \
--password [password] \
--table [table_name] \
--target-dir /[hdfs_path]/[target_dir] \
--as-textfile
