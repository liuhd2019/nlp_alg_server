#!/bin/bash

set -x

DIR="$(dirname "$(readlink -f "$0")")"
WORDSPACE=$(readlink -f "${DIR}")
#sudo docker build -t bert_summa:base -f Dockerfile ${WORDSPACE}
sudo docker build -t bert_summa_gpu:base -f Dockerfile.gpu ${WORDSPACE}
