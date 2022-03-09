#!/bin/sh

HOME_DIR=/home/cl/yuki-yama
PJ_DIR=${HOME_DIR}/work/d2/parser
DATA_DIR=${PJ_DIR}/data
TAG_DIR=${DATA_DIR}/stanford-postagger-full-2020-11-17

model_path=${TAG_DIR}/models/english-bidirectional-distsim.tagger
input_path=${DATA_DIR}/inout/input.txt
tagged_path=${DATA_DIR}/inout/tagged.txt

java -mx300m -classpath ${TAG_DIR}/stanford-postagger.jar edu.stanford.nlp.tagger.maxent.MaxentTagger -model ${model_path} -textFile ${input_path} > ${tagged_path}
