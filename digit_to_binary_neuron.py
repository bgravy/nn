#neural networks and deep learning example - map 0-9 outputs to 4 binary output neurons
import math

#compute the latest output of a sigmoid neuron
def sigmoid_output(inputs_list,weights_list,bias)
  weighted_sum=0
  for input_index in range(0,length(input_weights)):
    weighted_sum = weighted_sum + inputs_list[input_index] * weights_list[input_index]
  weighted_sum = weighted_sum + bias
  exponent = exp(-weighted_sum)
  denominator = 1 + exponent
  output_return = 1/denominator
  return output_return
