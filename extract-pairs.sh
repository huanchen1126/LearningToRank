#! bin/sh
NUM_FEATURES=44
python preprocess.py $NUM_FEATURES $1 ./tmp_normalized.txt
python extract-pairs.py $NUM_FEATURES ./tmp_normalized.txt $2
