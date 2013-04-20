import os
import sys
from collections import defaultdict
if len(sys.argv) != 4:
    print 'extract pairs usage: <num of features> <input> <output>'
    sys.exit()
num_features = int(sys.argv[1])
input_path = sys.argv[2]
output_path = sys.argv[3]

# read training examples
f_input = open(input_path, "r")
lines = f_input.readlines()

training_set = defaultdict(lambda : defaultdict(list))
for line in lines:
    line_split = line[:-2].split(" ")
    label = line_split[0]
    query = line_split[1]
    tmp_features = line_split[2:]
    features = [0.0] * num_features
    features = [float(i.split(":")[1]) for i in tmp_features]
    if label == '1':
        training_set[query]['1'].append(features)
    else:
        training_set[query]['-1'].append(features)
f_input.close()

f_output = open(output_path, "w")
for query in training_set:
    training_set_pos = training_set[query]['1']
    training_set_neg = training_set[query]['-1']
    for pos in training_set_pos:
        for neg in training_set_neg:
            pos_pair_wise = list()
            neg_pair_wise = list()
            for ind in range(len(pos)):
                value = pos[ind] - neg[ind]
                pos_pair_wise.append(value)
                neg_pair_wise.append(-value)
            f_output.write('1')
            for ind in range(len(pos_pair_wise)):
                f_output.write(' '+str(ind+1)+':'+str(pos_pair_wise[ind]))
            f_output.write('\n')
            f_output.write('-1')
            for ind in range(len(neg_pair_wise)):
                f_output.write(' '+str(ind+1)+':'+str(neg_pair_wise[ind]))
            f_output.write('\n')
f_output.close()
