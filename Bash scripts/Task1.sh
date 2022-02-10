#!/bin/bash

#Записати найкоротші регулярні вирази, які будуть відповідати:
# усім формам вашого прізвища

echo "Type form of your surname: \"Тарновецький\""
read surname

if echo $surname | grep -qE '^(Тарновецьк)(ий|ого|ому)?$'
then echo "It is correct form"
else echo "It is NOT correct form"
fi 