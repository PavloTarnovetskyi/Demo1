#!/bin/bash

#Записати найкоротші регулярні вирази, які будуть відповідати:
#усім телефонним кодам обласних центрів та інших великих міст 
#тієї частини України, де живуть ваші батьки

# Чернівці: 037, 0372, 03722;
# Тернопіль: 035, 0352;
# Хмельницький: 038, 0382, 03822;


echo "Type local telephone number:  "
read number

if echo $number | grep -P '^(037)\d{7}$|^(0372)d{6}$|^(03722)d{5}?$';
then echo "Chernivtsi number "

elif echo $number | grep -P '^(035)\d{7}$|^(0352)d{6}?$';
then echo "Ternopil number "

elif echo $number | grep -P '^(038)\d{7}$|^(0382)d{6}$|^(03822)d{5}?$';
then echo "Hmelnytskyi number "

else echo "It is NOT Chernivtsi, Ternopil, or Hmelnytskyi  number"

fi 