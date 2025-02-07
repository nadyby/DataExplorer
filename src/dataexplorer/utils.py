
def clean_dataset(df):
    """
    Comprehensive data cleaning function
    - Handle missing values
    - Remove duplicates
    """
    # Remove duplicate rows
    df = df.drop_duplicates()

    # Handle missing values
    # For numeric columns, fill with median
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())
    
    # For categorical columns, fill with mode
    categorical_columns = df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    return df





