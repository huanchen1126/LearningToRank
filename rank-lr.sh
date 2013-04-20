#! bin/sh
NUM_FEATURES=44
python LR.py $NUM_FEATURES $1 $2 ./model.tmp
python score_doc.py $NUM_FEATURES ./model.tmp $3 $4
