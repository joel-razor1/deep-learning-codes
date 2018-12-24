#Illustration of AND perceptron.

import pandas as pd

weight1 =7.0
weight2 =6.0
bias =0.0

test_inputs=[(0,0),(0,1),(1,0),(1,1)]
correct_outputs=[False,False,False,True]
outputs=[]

for test_input, correct_output in zip(test_inputs,correct_outputs):
    linear_combination=weight1*test_input[0]+weight2*test_input[1]+bias
    output=int(linear_combination>=0)
    if output== correct_output:
        is_correct_string="Yes"
    else:
        is_correct_string="No"
    outputs.append([test_input[0],test_input[1],linear_combination,output,is_correct_string])

num_wrong=len([output[4] for output in outputs if output[4]=="No"])
output_frame=pd.DataFrame(outputs,columns=['Input1', 'Input2', 'Linear Combination', 'Activation Output', 'Is Correct'])
if not num_wrong:
    print('Nice! You\'ve Got it all correct.\n')
else:
    print ('You got {} wrong. Keep Trying! \n'.format(num_wrong))
print(output_frame.to_string(index=False))