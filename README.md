#  Project: Disaster Response Pipeline


The project analyses disaster data from  [Figure Eight](https://www.figure-eight.com/)  to build a model for an API that classifies disaster messages.

In the Project folders, there is a data set containing real messages that were sent during disaster events.
A machine learning pipeline was built to categorize these events to send the messages to an appropriate disaster relief agency.

The project includes a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualization of the data. 

## Project Components

There are three components you'll need to complete for this project.

### 1. ETL Pipeline

In a Python script,  `process_data.py`:

- Loads the  `messages`  and  `categories`  datasets
-  Merges the two datasets
-  Cleans the data
- Stores it in a SQLite database

### 2. ML Pipeline
In the Python script,  `train_classifier.py`, presents a machine learning pipeline that:

-   Loads data from the SQLite database
-   Splits the dataset into training and test sets
-   Builds a text processing and machine learning pipeline
-   Trains and tunes a model using GridSearchCV
-   Outputs results on the test set
-   Exports the final model as a pickle file

### 3. Flask Web App

Flask web app for you to visualize data using Plotly.

## Running

1. To get running the web app there is a few simple steps to follow. First make sure you run  `pip install -r requirements.txt` to install all the necessary packages to run the application.
    
    Run the _ETL pipeline_ script `process_data.py`:

       python data/process_data.py data/disaster_messages.csv 
data/disaster_categories.csv data/DisasterResponse.db`

   The arguments `disaster_messages.csv` and `disaster_categories.csv` are the input data used to train the model. The last argument `DisasterResponse.db` is the SQLite database in which we will to save the cleaned data.

2. With the clean data, it is time to build the machine learning model. 
The command below will use cleaned data to train the model, improve the model using grid search and save the model to a pickle file (_classifer.pkl_).

        python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl

3. Finally, we can see the app as a page by running:

	    python app/run.py
    
    To check on the app go to http://0.0.0.0:3001/.
