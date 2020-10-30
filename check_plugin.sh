#!/bin/sh

file="/usr/share/jenkins/plugins.txt"
plugin="role-strategy"

if [ grep -q  "$plugin" $file ];then
   echo "Found Plugin"
else
   echo "Plugin must installed to get role/user in Jenkins"
fi
exit 0
