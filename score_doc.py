import os
import sys
import math
from collections import defaultdict
if len(sys.argv) != 5:
    print 'score_doc usage: <num of features> <model_path> <inputpath> <outputpath>'
    sys.exit()
num_features = int(sys.argv[1])
model_path = sys.argv[2]
input_path = sys.argv[3]
output_path = sys.argv[4]


# compute the probability that y=1 given params and features
def compute_prob(params, features):
    sum = 0.0
    for ind in range(len(params)):
        sum += params[ind]*features[ind]
    return sum

# load model
params = list()
# read training examples
f_model = open(model_path, "r")
lines = f_model.readlines()
for line in lines:
    params.append(line[:-1])
params = [float(i) for i in params]

f_model.close()

# test
f_test = open(input_path, "r")
f_output = open(output_path, "w")
lines = f_test.readlines()
for line in lines:
    # parse and normalize
    line_split = line[:-2].split(" ")
    tmp_features = line_split[2:-3]
    features = [0.0] * num_features
    for pair in tmp_features:
        pair_split = pair.split(":")
        features[int(pair_split[0])-1] = pair_split[1]
    features = [float(i) for i in features]
    norm = 0.0
    for feature in features:
        norm += feature*feature
    norm = math.sqrt(norm)
    features = [i/norm for i in features]
    score = compute_prob(params, features)
    f_output.write(str(score)+'\n')

f_output.close()
f_test.close()



