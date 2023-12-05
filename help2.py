import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#%%
# Specify the path to your .npy file
train_file_path = 'fashion_train.npy'
test_file_path = 'fashion_test.npy'

# Load the data from the .npy file
train_data = np.load(train_file_path)
test_data = np.load(test_file_path)
#print(train_data)
#%%
#convert it to a dataframe
train_df = pd.DataFrame(train_data)
test_df = pd.DataFrame(test_data)
# print the first 5 items
#print(train_df.head())
#%%
# get the number of rows
num_rows = train_df.shape[0]
#print(num_rows)
#%%
# Extract the last column
last_column = train_data[:, -1]
#%%
# Initialize counts
count_0_tshirt = 0
count_1_trousers = 0
count_2_pull_over = 0
count_3_dress = 0
count_4_shirt = 0



# Loop through the last column
for value in last_column:
    if value == 0:
        count_0_tshirt += 1
    elif value == 1:
        count_1_trousers += 1
    elif value == 2:
        count_2_pull_over += 1
    elif value == 3:
        count_3_dress += 1
    elif value == 4:
        count_4_shirt += 1

# Display the counts
#print("Count of 0s:", count_0_tshirt)
#print("Count of 1s:", count_1_trousers)
#print("Count of 2s:", count_2_pull_over)
#print("Count of 3s:", count_3_dress)
#print("Count of 4s:", count_4_shirt)
#%%
# Get the simple probabilities


P_tshirt = count_0_tshirt / num_rows
P_trouser = count_1_trousers / num_rows
P_pull_over = count_2_pull_over/ num_rows
P_dress = count_3_dress / num_rows
P_shirt = count_4_shirt / num_rows

#print(f" P(T-shirt) = {P_tshirt}")
#print(f" P(Trousers) = {P_trouser}")
#print(f" P(Pull Over) = {P_pull_over}")
#print(f" P(Dress) = {P_dress}")
#print(f" P(Shirt) = {P_shirt}")
#%% md

#%%
#get list of

#create a tshirt mask and get the tshirt list
tshirt_mask = train_data[:, -1] == 0
trouser_mask = train_data[:, -1] == 1
pull_over_mask = train_data[:, -1] == 2
dress_mask = train_data[:, -1] == 3
shirt_mask = train_data[:, -1] == 4

#apply the mask to the data and remove the last column
tshirt_list = train_data[tshirt_mask][:, :-1]
trouser_list = train_data[trouser_mask][:, :-1]
pull_over_list = train_data[pull_over_mask][:, :-1]
dress_list = train_data[dress_mask][:, :-1]
shirt_list = train_data[shirt_mask][:, :-1]

mu0_tshirts = np.mean(tshirt_list)
mu1_trousers = np.mean(trouser_list)
mu2_pull_over = np.mean(pull_over_list)
mu3_dress = np.mean(dress_list)
mu4_shirt = np.mean(shirt_list)


#reshaped = tshirt_list[0].reshape(28,28)
#print(reshaped-mu0_tshirts)
#s0 = (reshaped-mu0_tshirts)*np.transpose(reshaped-mu0_tshirts)
#print(s0)
#calculate the S0 from the tshirt list and add the reshaped matrixes to a new matrix
S0 = np.zeros((28,28))
for item in tshirt_list:
    reshaped = item.reshape(28,28)
    S0 += (reshaped-mu0_tshirts)*np.transpose(reshaped-mu0_tshirts)
print(S0)









#for item in tshirt_list:
 #   i = 0
  #  reshaped = tshirt_list[i].reshape(28,28)
   # S0 = S0 + (reshaped-mu0_tshirts)*np.transpose(reshaped-mu0_tshirts)


#tshirt_list = train_data[tshirt_mask]
#print(tshirt_list.shape)
#print(tshirt_list)
#reshaped = tshirt_list[0].reshape(28,28)
#print(reshaped)
#plt.imshow(reshaped, cmap='gray')
#plt.show()
#we'll continue calculating the SW from the 28x28 matrixes, and make another list of the reshaped matrixes


#create subset of data with the different classes
#for i in range(len(train_data)):
    #if train_data[i][-1] == 0:
    #    t_shirt_list.append(train_data[i])
   # elif train_data[i][-1] == 1:
   #     trouser_list.append(train_data[i])
   # elif train_data[i][-1] == 2:
   #     pull_over_list.append(train_data[i])
  #  elif train_data[i][-1] == 3:
 #       dress_list.append(train_data[i])
#    elif train_data[i][-1] == 4:
#        shirt_list.append(train_data[i])

#mu0_tshirts = np.mean(t_shirt_list)
#mu1_trousers = np.mean(trouser_list)
#mu2_pull_over = np.mean(pull_over_list)
#mu3_dress = np.mean(dress_list)
#mu4_shirt = np.mean(shirt_list)

#get the first three items in the tshirtlist
#mu0 = 81
#small = t_shirt_list[0:3]
#print(t_shirt_list)
#reshaped = t_shirt_list[0].reshape(28,28)
#print(reshaped)
#print(f'old array: {small}')
#for item in small:
#    i = 1
#    small[i] = item[i]-mu0
#    print(small)
#    i = i+1
#print(f'new array: {small}')


