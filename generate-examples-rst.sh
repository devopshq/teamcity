#!/usr/bin/env bash
# RST docs - for single running only

#rm -rf ./docs-sphinx/examples/api || echo "not exist"
#rm -rf ./docs-sphinx/examples/models  || echo "not exist"

#java -Xmx1024m -Xms256m -jar ./swagger-codegen-cli.jar generate \
#    -l python \
#    -c ./swagger/swagger-config.json \
#    -t ./swagger/examples-rst-template/ \
#    -Ddocs \
#    --skip-overwrite \
#    -i ./swagger/swagger.json
#mkdir ./docs-sphinx/examples/api || echo "folder exist"
#mkdir ./docs-sphinx/examples/models || echo "folder exitst"
#mv -vf docs/*Api.md ./docs-sphinx/examples/api
#
#pushd ./docs-sphinx/examples/api
#for file in *.md
#do
#  mv "$file" "${file%.md}.rst"
#done
#popd
#
#mv -vf docs/*.md ./docs-sphinx/examples/models/
#pushd ./docs-sphinx/examples/models
#for file in *.md
#do
#  mv "$file" "${file%.md}.rst"
#done
#popd
#rmdir docs
#mv html docs
