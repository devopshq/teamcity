#!/usr/bin/env bash
java -Xmx1024m -Xms256m -jar ./swagger-codegen-cli.jar generate \
    -l python \
    -c swagger-config.json \
    -DinfoEmail=allburov@gmail.com \
    -t ./.swagger-resources \
    -i swagger.json