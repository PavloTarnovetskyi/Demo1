#!/bin/bash

#Записати найкоротші регулярні вирази, які будуть відповідати:
#усім формам вашого імені (можна врахувати і зменшувальні або інші варіанти);

echo "Type form of your name: \"Павло\""
read name

if echo $name | grep -qE '^(Па)(вло|ша|влу|вла)?$'
then echo "It is correct form"
else echo "It is NOT correct form"
fi 