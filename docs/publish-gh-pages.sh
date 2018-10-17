#!/usr/bin/env bash
set -e

CURR_DIR="$(pwd)"
TMP_DIR=$(mktemp -d)

# build
make clean
make html

# push to branch gh-pages
cd $TMP_DIR
echo "Use temp directory: $TMP_DIR"
git clone git@github.com:devopshq/teamcity.git
cd teamcity
git branch -D gh-pages
git checkout --orphan gh-pages
rm -rf !(.git|.gitignore)

cp -r $CURR_DIR/_build/html/* .

git add -A
git commit -m "published"
git push origin :gh-pages
git push origin gh-pages

cd $CURR_DIR
rm -rf "$TMP_DIR"
