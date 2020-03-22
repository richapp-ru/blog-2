#!/usr/bin/env bash
curDir=$(cd $(dirname ${BASH_SOURCE}) && pwd)
protoc --proto_path=${curDir} --python_out=${curDir} ${curDir}/data.proto
