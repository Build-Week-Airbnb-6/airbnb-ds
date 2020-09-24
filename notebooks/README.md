The purpose of these notebooks are to perform exploratory analysis of the pricing data, then create a model to predict pricing for new data points.

EDA.ipynb contains information about the data in terms of summary statistics
Model_testing_Random_Search.ipynb contains the actual final model

Our model is an SKLearn pipeline, containing an encoder, imputer, scaler, and model. These can be seen more thoroughly in the documentation for each segment.
Predicting on the target of log_price resulted in a mean squared error of 0.24 between the predicted values and holdout data. 

Further improvements could include more columns being used in the model, different model architectures being searched, and additional hyperparameter tuning for each section of the pipeline. 