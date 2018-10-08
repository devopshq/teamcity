#!/usr/bin/env bash
java -Xmx1024m -Xms256m -jar ./swagger-codegen-cli.jar generate \
    -l python \
    -c ./swagger/swagger-config.json \
    -t ./swagger/template/ \
    -i ./swagger/swagger.json
# I do not known why, but it is not working, and we have 'No description' in files...
#    --additional-properties appDescription="Python Client for TeamCity REST API"
#    -D appDescription="Python Client for TeamCity REST API"
