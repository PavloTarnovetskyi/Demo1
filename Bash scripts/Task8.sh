#!/bin/bash

#  За допомогою grep | awk | sed | find покажіть список файлів 
#(не враховуючи каталоги) у вашому домашньому каталозі, що змінювалися менше, ніж 10 годин тому?

echo "Список файлів у каталозі, що змінювалися менше 10 годин тому:"
echo "Type path where search, like: \"/etc/\""
read path

cd $path && find -maxdepth 1 -cmin -600 -type f 