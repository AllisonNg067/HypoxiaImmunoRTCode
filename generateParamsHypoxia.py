import pandas as pd
import numpy as np
import new_data_processing_hypoxia as dp
errorControl = pd.read_csv("setonix hypoxia errors control.csv")
errorControl = list(np.transpose(np.array(errorControl))[0])
errorRT = pd.read_csv("updated hypoxia errors RT.csv")
errorRT = list(np.transpose(np.array(errorRT))[0])
param = pd.read_csv("updated hypoxia means RT.csv")
param = list(np.transpose(np.array(param))[0])
#print(get_equivalent_bed_treatment(param, 50, 1))
errors = [errorControl, errorRT]
errorMerged = dp.merge_lists(errors)
# errorMerged[22] = 0
# errorMerged[32] = 0
num_patients = 500
params = [list(param) for _ in range(num_patients)]
#print(errorMerged)

seeds = range(num_patients)
# Modify the parameters for each patient
for i in range(num_patients):
    rng = np.random.default_rng(seeds[i])
    for j in range(len(param)):
        
        if errorMerged[j] != 0:
            logNormalParams = dp.log_normal_parameters(param[j], errorMerged[j])
            params[i][j] = min(max(rng.lognormal(mean=logNormalParams[0], sigma = logNormalParams[1]), 0.8*param[j]), 2*param[j])
        else:
            params[i][j] = param[j]
        if j == 28:
            params[i][j] = min(max(rng.lognormal(mean=logNormalParams[0], sigma = logNormalParams[1]), 0.8*param[j]), 1.2*param[j])

# Assuming 'params' is your list of parameters
df = pd.DataFrame(params)
print(params)
# Save to CSV
df.to_csv('hypoxia_parameters.csv', index=False)
