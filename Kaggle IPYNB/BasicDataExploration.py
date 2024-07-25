import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

# save filepath to variable for easier access
melbourne_file_path = 'C:\\Users\\matthew.yim\\PycharmProjects\\Kaggle\\melbourne-housing-snapshot\\melb_data.csv'

# read the data and store data in DataFrame titled melbourne_data
df = pd.read_csv(melbourne_file_path)

# print a summary of the data in Melbourne data
print(df.describe())

newest_home_age = df.loc[:, 'YearBuilt'].max()
avg = df.loc[:, 'Landsize'].mean()
print(f"avg", avg)
print(f"newest home", newest_home_age)
print(df.columns)

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))

# Model Validation
    # Mean Absolute Error (MAE) : With the MAE metric, we take the absolute value of each error. This converts each
    # error into a positive number. We then take the average of those absolute errors.
        # On average, our predictions are off by about X

# Load data
melbourne_data = pd.read_csv(melbourne_file_path)
# Filter rows with missing price values
filtered_melbourne_data = melbourne_data.dropna(axis=0)
# Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea',
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)

from sklearn.tree import DecisionTreeRegressor
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(X, y)

# Proble with "In-Sample" Scores
""" 
    The measure we just computed can be called an "in-sample" score. We used a single "sample" of houses for both building
    the model and evaluating it. Here's why this is bad
    
    Image that, in the large real estate market, door color is unrelated to home price.
    
    However, in the sample of data you used to build the moedel, all homes iwth green doors were very expensive. The model's
    job is to find patterns that predict home prices, so it will see this pattern, and it will always predict high prices for 
    homes with green doors.
    
    Since this pattern was derived from the training data, the model will appear accurate in the training data.
    
    But if this pattern doesn't hold when the model sees new data, the model would be very inaccurate whem used in practice
    
    Since models' practical value come from making predictions on new data, we measure performance on data that wasn't used
    to build the model. The most straightforward way to do this is to exclude some data from the model-building process, and
    then use those to test the model's accuracy on data it hasn't seen before. This data is called {Validation data} 
    
"""