#neural networks and deep learning example - map 0-9 outputs to 4 binary output neurons
import math

output_val=[0,0,0,0]
#compute the latest output of a sigmoid neuron
def sigmoid_output(inputs_list,weights_list,bias):
  if len(inputs_list) != len(weights_list):
    return 0
  weighted_sum=0
  output_return=0
  for input_index in range(0,len(weights_list)):
    weighted_sum = weighted_sum + inputs_list[input_index] * weights_list[input_index]
  print "Weighted Sum: " + str(weighted_sum)
  weighted_sum = weighted_sum - bias
  exponent = math.exp(-weighted_sum)
  denominator = 1 + exponent
  output_return = 1/denominator
  return output_return

#input list 0-9: 0.01=off, 0.99=on
#             0     1    2    3     4    5   6    7    8    9
input_layer = [0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.99]
output_neuron_0_weights= [0,0,0,0,0,0,0,0,1,1]
output_neuron_1_weights= [0,0,0,0,1,1,1,1,0,0]
output_neuron_2_weights= [0,0,1,1,0,0,1,1,0,0]
output_neuron_3_weights= [0,1,0,1,0,1,0,1,0,1]
output_neuron_weights_list=[output_neuron_0_weights,output_neuron_1_weights,output_neuron_2_weights,output_neuron_3_weights]
output_layer_biases = [0.03,0.05,0.05,0.06]
for output_ref in range(0,4):
  output_val[output_ref]=sigmoid_output(input_layer,output_neuron_weights_list[output_ref],output_layer_biases[output_ref])
  print "Output number: " + str(output_ref) + " is " + str(output_val[output_ref])
