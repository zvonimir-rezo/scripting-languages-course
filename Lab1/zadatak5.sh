#!/bin/bash

arg1=$1
arg2=$2

echo "Prvi argument: $arg1 Drugi argument: $arg2"

find "$arg1" -name "$arg2" | xargs wc -l | tail -1
