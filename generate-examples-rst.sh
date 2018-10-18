#!/usr/bin/env bash
# RST docs - for single running only
mv docs html
rm -rf ./docs/examples/api || echo "not exist"
rm -rf ./docs/examples/models  || echo "not exist"

java -Xmx1024m -Xms256m -jar ./swagger-codegen-cli.jar generate \
    -l python \
    -c ./swagger/swagger-config.json \
    -t ./swagger/examples-rst-template/ \
    -Ddocs \
    --skip-overwrite \
    -i ./swagger/swagger.json
mkdir ./docs/examples/api || echo "folder exist"
mkdir ./docs/examples/models || echo "folder exitst"
mv -vf docs/*Api.md ./docs/examples/api

pushd ./docs/examples/api
for file in *.md
do
  mv "$file" "${file%.md}.rst"
done
popd

mv -vf docs/*.md ./docs/examples/models/
pushd ./docs/examples/models
for file in *.md
do
  mv "$file" "${file%.md}.rst"
done
popd
rmdir docs
mv html docs
