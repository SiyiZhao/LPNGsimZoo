#!/bin/bash
# @r88

PREFIX="logs/$1"

nohup bash -c "( time ./run_$1.sh >${PREFIX}_stdout.log 2>${PREFIX}_stderr.log ) 2>${PREFIX}_time.log" < /dev/null &
echo "Job started with PID $!"
echo "Logs:"
echo "  Stdout: ${PREFIX}_stdout.log"
echo "  Stderr: ${PREFIX}_stderr.log"
echo "  Time:   ${PREFIX}_time.log"
