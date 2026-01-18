"""
This program finds the best value of K in KMeans algorithm using Silhouette Coefficient for 'housing.csv' dataset. The range of K values to analyze is provided as a command line parameter.
Syntax: python template.py <number> <number>

For example, to search best K between 3 and 6 the command line input should be:
python template.py 3 6
"""

# importing the libraries

"""  DO NOT MODIFY  """
import sys
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
"""  DO NOT MODIFY  """

def find_best_kmeans(data, min_k, max_k):

    """  write from here  """
    best_k = None
    best_score = -1

    # Select numeric columns only
    X = data.select_dtypes(include=['int64', 'float64'])

    for k in range(min_k, max_k + 1):
        
        # Initialize the K-Means model
        model = KMeans(n_clusters=k, n_init='auto', random_state=0)
        
        # Use the data and calculate Silhouette Coefficient for the range of K provided
        labels = model.fit_predict(X)
        score = metrics.silhouette_score(X, labels)

        # Return the best K with respect to Silhouette Coefficient
        if score > best_score:
            best_score = score
            best_k = k

    return best_k
        
    """        End        """


"""  DO NOT MODIFY  """
if __name__ == '__main__':

    """
    ALERT: * * * No changes are allowed in this section  * * *
    """
 
    if len(sys.argv) == 2:
        print("Usage: python assignment.py <number> <number>")
        sys.exit(1)

    input_data_one = sys.argv[1].strip()
    input_data_two = sys.argv[2].strip()
    
    """  Call to function that will perform the computation. """
    if input_data_one.isdigit() and input_data_two.isdigit():

        min_k = int(input_data_one)
        max_k = int(input_data_two)
        if min_k>=2 and max_k>min_k:
            data =pd.read_csv("./housing.csv")
            print(find_best_kmeans(data, min_k, max_k)) 
        else:
           print("Invalid input")
    else:
        print("Invalid input")
 
    
    """ End to call """
