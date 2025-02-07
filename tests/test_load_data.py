import pytest
from unittest.mock import Mock, patch
import pandas as pd
import streamlit as st
from io import StringIO

@pytest.fixture
def mock_uploaded_file():
    mock_file = Mock()
    csv_content = "name,age\nJohn,30\nJane,25"
    mock_file.getvalue.return_value = csv_content
    mock_file.name = "test.csv"
    return mock_file

def test_data_load(mock_uploaded_file):
    with patch('streamlit.success') as mock_success, \
         patch('streamlit.error') as mock_error, \
         patch('streamlit.write'):
        try:
            df = pd.read_csv(StringIO(mock_uploaded_file.getvalue()))
            st.success("Données chargées avec succès")
            st.write(df.head())
            assert not df.empty
            assert df.shape == (2, 2)
            assert list(df.columns) == ['name', 'age']
            mock_success.assert_called_once()
            mock_error.assert_not_called()
            
        except Exception as e:
            st.error(f"Erreur: {str(e)}")
            mock_error.assert_called_once()