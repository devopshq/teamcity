#!/usr/bin/env bash
set -e
mv docs html || echo not exist
java -Xmx1024m -Xms256m -jar ./swagger-codegen-cli.jar generate \
    -l python \
    -c ./swagger/swagger-config.json \
    -t ./swagger/template/ \
    -D models -Dapis -D docs \
    -i ./swagger/swagger.json
## I do not known why, but it is not working, and we have 'No description' in files...
##    --additional-properties appDescription="Python Client for TeamCity REST API"
##    -D appDescription="Python Client for TeamCity REST API"
#
echo "" >> './dohq_teamcity/models/file.py'
echo "file = File" >> './dohq_teamcity/models/file.py'
mkdir ./docs/swagger || echo "Swagger folder exist"
mkdir ./docs/swagger/api || echo "API folder exitst"
mkdir ./docs/swagger/models || echo "API folder exitst"
mv -vf docs/*Api.md ./docs/swagger/api
mv -vf docs/*.md ./docs/swagger/models/
rmdir docs

pushd ./docs/swagger/api
for file in *.md
do
  mv "$file" "${file%.md}.rst"
done
popd

pushd ./docs/swagger/models/
for file in *.md
do
  mv "$file" "${file%.md}.rst"
done
popd
mv html docs
