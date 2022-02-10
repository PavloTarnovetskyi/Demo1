#!/bin/bash

# Покажіть Яку кількість файлів README містять підкаталоги, не враховуючи файли вигляду «README.a_string»?
echo "Показує кількість файлів README в заданому каталозі, не враховуючи файли вигляду «README.a_string»"
echo "Type path where search, like: \"/etc/\""
read path

sudo find $path -name *README* | grep -vc "README.a_string"