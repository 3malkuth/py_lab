#!/bin/bash
# Usage:> ./gitPush.sh "my commit message"
#echo $1
git add -A; git commit -m "$1"; git push
