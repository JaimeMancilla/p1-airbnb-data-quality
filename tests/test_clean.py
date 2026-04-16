import pandas as pd
import pytest

@pytest.fixture
def df():
    return pd.read_csv("data/processed/listings_clean.csv")

def test_no_duplicates(df):
    assert df.duplicated().sum() == 0

def test_no_nulls_in_critical_columns(df):
    critical = ["id","room_type","beds","bedrooms","bathrooms"]
    for col in critical:
        assert df[col].isnull().sum() == 0, f"{col} tiene nulos"

def test_tiene_resenas_is_binary(df):
    assert df["tiene_resenas"].isin([0,1]).all()

def test_dias_activo_non_negative(df):
    assert (df["dias_activo"].dropna() >=0).all()

def test_shape(df):
    assert df.shape[1] == 72
    assert df.shape[0] > 0