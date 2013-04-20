#python Letor_Batch_LR.py 44 0.0001 pair-wise.txt lr.model
import os
import sys
import math
from collections import defaultdict
if len(sys.argv) != 5:
    print 'lr usage: <num of features> <c> <input> <output>'
    sys.exit()
num_features = int(sys.argv[1])
input_path = sys.argv[3]
output_path = sys.argv[4]
#num_features = 4
# for regularization
c = float(sys.argv[2])
# step size
eta = 0.001
# to detect convergence
converge_distance = 0.05
# maximum num of iteration
max_iteration = 500

# compute the probability that y=1 given params and features
def compute_prob(params, features):
    sum = 0.0
    for ind in range(len(params)):
        sum += params[ind]*features[ind]
    exp = math.exp(sum)
    result = exp/(1+exp)
    return result

# update params with gradient ascent
def gradient_ascent(params, training_set):
    # initialize new param
    new_params = params[:]
    for v in training_set:
        features = v[0]
        label = v[1]
        mul = (labels[label] - compute_prob(params, features))
        # update w1 - wn
        for ind in range(len(params)):
            new_params[ind] += eta * features[ind] * mul
    # add regularization
    for ind in range(len(new_params)):
        reg = - eta * c * params[ind]
        new_params[ind] += - eta * c * params[ind]
    # compute change distance
    distance = 0.0
    for ind in range(len(new_params)):
        distance += abs(new_params[ind] - params[ind])
    print "distance", distance
    if distance < converge_distance:
        return new_params, True
    else:
        return new_params, False

# read training examples
f_input = open(input_path, "r")
lines = f_input.readlines()
training_set = list()
for line in lines:
    line_split = line[:-1].split(" ")
    label = line_split[0]
    tmp_features = line_split[1:]
    features = [0.0] * num_features
    features = [float(i.split(':')[1]) for i in tmp_features]
    training_set.append([features,label])
f_input.close()

# do the gradient ascent
f_output = open(output_path, "w")
# initialize params as 0.0
params = [0.0]*(num_features)
labels = {"1":1, "-1":0}
converged = False
iteration = 1
while not converged and iteration < max_iteration:
    params, converged = gradient_ascent(params, training_set)
    iteration += 1
# output parameters
for param in params:
    f_output.write(str(param)+'\n')
f_output.close()
