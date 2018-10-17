#!/usr/bin/env bash
# RST docs - for single running only
mv docs html
rm -rf ./docs/teamcity_apis || echo "not exist"
rm -rf ./docs/teamcity_models  || echo "not exist"

java -Xmx1024m -Xms256m -jar ./swagger-codegen-cli.jar generate \
    -l python \
    -c ./swagger/swagger-config.json \
    -t ./swagger/examples-rst-template/ \
    -Ddocs \
    --skip-overwrite \
    -i ./swagger/swagger.json
mkdir ./docs/teamcity_apis || echo "folder exist"
mkdir ./docs/teamcity_models || echo "folder exitst"
mv -vf docs/*Api.md ./docs/teamcity_apis

pushd ./docs/teamcity_apis
for file in *.md
do
  mv "$file" "${file%.md}.rst"
done
popd

mv -vf docs/*.md ./docs/teamcity_models/
pushd ./docs/teamcity_models
for file in *.md
do
  mv "$file" "${file%.md}.rst"
done
popd
rmdir docs
mv html docs
