#!/bin/bash

# Покажіть усі рядки з файлу /etc/group, що починаються послідовністю символів «daemon».

echo "Рядки з файлу /etc/group, що починаються послідовністю символів «daemon»: "

cat /etc/group | grep -E "^daemon"