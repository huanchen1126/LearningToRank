# this program is to normalize the data
import math
import sys
if len(sys.argv) != 4:
    print 'preprocess usage: <num of features> <input> <output>'
    sys.exit()
num_features = int(sys.argv[1])
input_path = sys.argv[2]
output_path = sys.argv[3]
# read training examples
f_input = open(input_path, "r")
f_output = open(output_path, "w")
lines = f_input.readlines()
for line in lines:
    line_split = line[:-2].split(" ")
    label = line_split[0]
    query = line_split[1]
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
    f_output.write(label+' '+query)
    for ind in range(len(features)):
        f_output.write(' '+str(ind+1)+":"+str(features[ind]))
    f_output.write('\n')
f_input.close()
f_output.close()
