#!/bin/bash

### Fix 'https' on spring repos in Geocit134/pom.xml

 sed -i 's/http:\/\/repo.spring.io\/milestone/https:\/\/repo.spring.io\/milestone/g' pom.xml
 sed -i 's/http:\/\/repo.spring.io\/libs-milestone/https:\/\/repo.spring.io\/libs-milestone/g' pom.xml

### Fix <javax.servelet-api> in Geocit134/pom.xml

sed -i 's/<artifactId>servlet-api</artifactId><artifactId>javax.servlet-api</artifactId>/g' pom.xml

### Comment nexus repo

sed -i 's/<distributionManagement>/<!--<distributionManagement>/g' pom.xml
sed -i 's/<\/distributionManagement>$/<\/distributionManagement>-->/g' pom.xml


### Fix Geocit/src/resources/application.properties
serverip='IP Ubuntu server'
databaseip='IP CentOS server'
email=`<put created new email>`
emailpassword=`<password fpr created new email>`
sed -i "s/http:\/\/localhost/http:\/\/$serverip/g" src/main/resources/application.properties
sed -i "s/postgresql:\/\/localhost/postgresql:\/\/$databaseip/g" src/main/resources/application.properties
sed -i "s/35.204/28.238/$databaseip/g" src/main/resources/application.properties
sed -i "s/ssgeocitizen@gmail.com/$email/g" src/main/resources/application.properties
sed -i "s/=softserve/=$emailpassword/g" src/main/resources/application.properties
