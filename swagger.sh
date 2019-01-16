#!/usr/bin/env bash
set -e
if [ ! -f ./swagger-codegen-cli.jar ]; then
    echo "File swagger not found! Try download..."
    FILE="https://github.com/devopshq/teamcity/releases/download/0.0.0/swagger-codegen-cli.jar"
    wget $FILE -O swagger-codegen-cli.jar || \
    (
        echo "Something wrong, please download $FILE manually and place in current directory"; rm ./swagger-codegen-cli.jar; \
        exit 11
    )

fi
echo "Start generate"

java -Xmx4096m -Xms1024m -jar ./swagger-codegen-cli.jar generate \
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
mkdir ./docs-sphinx/swagger || echo "Swagger folder exist"
mkdir ./docs-sphinx/swagger/api || echo "API folder exitst"
mkdir ./docs-sphinx/swagger/models || echo "API folder exitst"
mv -vf docs/*Api.md ./docs-sphinx/swagger/api
mv -vf docs/*.md ./docs-sphinx/swagger/models/
rmdir docs

pushd ./docs-sphinx/swagger/api
for file in *.md
do
  mv "$file" "${file%.md}.rst"
done
popd

pushd ./docs-sphinx/swagger/models/
for file in *.md
do
  mv "$file" "${file%.md}.rst"
done
popd

# Auto PEP8
pip install autopep8
autopep8 --in-place --aggressive --max-line-length 120 --recursive dohq_teamcity
