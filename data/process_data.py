import sys
from sqlalchemy import create_engine
import pandas as pd

def load_data(messages_filepath, categories_filepath):
    """
    Definition: Takes inputs as two CSV files name, imports them as pandas dataframe.
    finally, merges them into a single dataframe by id
    
    Args:
    messages_file_path str: Messages CSV str name
    categories_file_path str: Categories CSV str name
    
    Returns:
    merged_df pandas_dataframe: Dataframe obtained from merging the two input data

    """

    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)

    # merge datasets
    df = pd.merge(categories, messages, on='id', how='outer')

    return df


def clean_data(df):
    """
    Definition : Cleans the combined dataframe for use by ML model
    
    Args:
    df pandas_dataframe: Merged dataframe returned from load_data() function
    
    Returns:
    df pandas_dataframe: Cleaned data to be used by ML model
    
    """

    categories = df['categories'].str.split(';', expand=True)

    # select the first row of the categories dataframe
    row = categories.iloc[0]

    category_colnames = categories.iloc[0].str.split('-').str[0]
    categories.columns = category_colnames

    categories = categories.apply(lambda row: row.str.split('-').str[1].astype(int))

    df.drop('categories', axis=1, inplace=True)
    df = df.join(categories)

    # drop duplicates
    df.drop_duplicates(inplace = True)

    return df


def save_data(df, database_filename):
    """
    Saves cleaned data to an SQL database
    
    Args:
    df pandas_dataframe: Cleaned data returned from clean_data() function
    database_file_name str: File path of SQL Database which the cleaned
    dataframe is to be saved
    
    Returns:
    None
    
    """

    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql('DisasterResponse', engine, index=False, if_exists='replace')


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()