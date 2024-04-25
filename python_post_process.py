import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import OneHotEncoder

def post_process(df):
    
    print("Method 1: Performing principle component analysis")
    # As country can be a useful parameter, I have performed one hot encoding to convert this string values into numerical values. 
    # There are other encoding menthods such as labeled encoding, but for the problem in hand I have choosen to go with one hot encoding as I do not want to create any bias
    one_hot_encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    encoded_categories = one_hot_encoder.fit_transform(df[['Country']])

    # Convert the encoded categories array into a DataFrame
    encoded_df = pd.DataFrame(encoded_categories, columns=one_hot_encoder.categories_[0])

    # Concatenate the encoded DataFrame with the original DataFrame, excluding the 'Country', 'Description', 'created_at', 'InvoiceDate' columns as they contain string values.
    data = pd.concat([df.drop(columns=['Country', 'Description', 'created_at', 'InvoiceDate']), encoded_df], axis=1)

    

    pca = PCA(n_components=16)
    principalComponents = pca.fit_transform(data)
    principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2','principal component 3', 'principal component 4', 'principal component 5', 'principal component 6','principal component 7', 'principal component 8', 'principal component 9', 'principal component 10','principal component 11', 'principal component 12', 'principal component 13', 'principal component 14','principal component 15', 'principal component 16'])
    print(principalDf)

    print(pca.explained_variance_ratio_)

    print("Method 2: Calculating Correlation Coefficient")

    # Here I have found list of features which are correlated.
    # I have removed list of parameters which contains string values.

    df = df.drop(columns=['Country', 'Description', 'created_at', 'InvoiceDate'])

    print(df)

    corcof = []
    for i in range(len(df.columns)):
        for j in range(i+1,len(df.columns)):
            temp = []
            temp.append(df.columns[i])
            temp.append(df.columns[j])
            corr = np.corrcoef(df[df.columns[i]], df[df.columns[j]])
            temp.append(corr[0][1])
            corcof.append(temp)
            
    merge = []
    for i in range(len(corcof)):
        merge.append(corcof[i])
    values = pd.DataFrame(merge,columns=['Feature 1', 'Feature 2', 'Correlation Coefficient'])

    print(values)

    # Now I have added a new column as 'abs corr' which has absolute value of correlation coefficient between two feature, this absolute value is used to sort the DataFrame.

    values['abs corr'] = abs(values['Correlation Coefficient'])
    values.sort_values(by=['abs corr'], ascending=False)
    print(values)


    

