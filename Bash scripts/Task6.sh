#!/bin/bash

# Покажіть усі рядки з файлу /etc/group, що не містять послідовність символів «daemon».

echo "Рядки з файлу /etc/group, що не містять послідовність символів «daemon»: "

cat /etc/group | grep -P "^(?!(daemon)).*$"
