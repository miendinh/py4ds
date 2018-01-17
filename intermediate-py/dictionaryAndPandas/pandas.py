###############################
# Dictionary to DataFrame 1
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = { 'country' : names, 'drives_right': dr, 'cars_per_cap' : cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

###############################
# Dictionary to DataFrame 2
import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

#################################################
# CSV to DataFrame 1
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)

#################################################
# CSV to DataFrame 2
# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out cars
print(cars)


#################################################
# Square Brackets (1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])


#################################################
# Square Brackets (2)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

#################################################
# loc and iloc (1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc['JAP'])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])


#################################################
# loc and iloc (2)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR']['drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR']][['country', 'drives_right']])


#################################################
# loc and iloc (3)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars['drives_right'])

# Print out drives_right column as DataFrame
print(cars[['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars[['cars_per_cap', 'drives_right']])

#################################################
# Drivinv right(1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr == True]

# Print sel
print(sel)

#################################################
# Driving right (2)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right'] == True]

# Print sel
print(sel)


#################################################
# Cars per capita (1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500

car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)


#################################################
# Cars per capita (2)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500

car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)

#################################################
from model import VietOcr
from dataset import DataSet
from generate_dataset import DataGenerator
import tensorflow as tf
import numpy as np


def predict(character_image):
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())
    saver = tf.train.import_meta_graph('xxxxx.ckpt.meta')
    saver.restore(sess, tf.train.latest_checkpoint('./'))

    graph = tf.get_default_graph()

    X = graph.get_tensor_by_name("X:0")
    softmax = graph.get_tensor_by_name("softmax:0")

    rs = sess.run([softmax], feed_dict={X: YOUR_INPUT})
