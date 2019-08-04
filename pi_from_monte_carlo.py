#!/usr/bin/python3

import numpy as np

def check_length(coordinate):
    magnitude = np.sqrt(np.power(coordinate[:,0], 2) + np.power(coordinate[:,1], 2))
    if magnitude > 1.0:
       return 0
    else:
       return 1


# sequence_length = 1e4
sequence_length = input('Input sequence length: ')
sequence_length = int(sequence_length)

print('Calculating from ' + str(sequence_length) + ' coordinate pairs...')

mc_sum = 0

# Single numpy array
# random_sequence_of_pairs = np.random.random_sample([sequence_length, 2])
#for pair in random_sequence_of_pairs:
#    mc_sum += check_length(pair)

index = 0 
while index < sequence_length:
    pair = np.random.random_sample([1, 2])
    index += 1
    mc_sum += check_length(pair)

    if index % int(.1 * sequence_length) == 0:
       current_uncertainty = 4.0 / np.sqrt(index)
       magnitude_of_uncertainty = int(np.floor(np.log10(current_uncertainty)))
       current_estimate = np.round(4.0 * mc_sum / index, -magnitude_of_uncertainty)
       current_uncertainty = np.round(current_uncertainty, -magnitude_of_uncertainty)

       print('     Step ' + str(index) + ' estimate: ' + str(current_estimate) + ' +/- ' +\
             str(current_uncertainty))

uncertainty_in_pi = 4.0/np.sqrt(sequence_length)
magnitude_of_uncertainty = int(np.floor(np.log10(uncertainty_in_pi)))
estimate_of_pi = np.round(4.0*mc_sum/sequence_length, -magnitude_of_uncertainty)

output = 'Circumference-to-diameter ratio = ' + str(estimate_of_pi) + \
         ' +/- ' + str(uncertainty_in_pi)

print()
print(output)
