#!/bin/bash

if [ $1 != gpu ] 
then
	docker run -p 127.0.0.1:8089:8080 -it --rm bert_summa:base bash
else
	docker run -p 127.0.0.1:8089:8080 -it --rm bert_summa_gpu:base bash
fi
