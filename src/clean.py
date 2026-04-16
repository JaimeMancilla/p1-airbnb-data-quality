import pandas as pd

def imputar_por_grupo(df,cols,grupo_col,tipos):
    """
    Imputa valores nulos con la mediana del grupo
    
    df        : DataFrame a imputar
    cols      : columnas a imputar
    grupo_col : columna por la que se agrupa
    tipos     : lista de valores del grupo a imputar
    """
    
    for col in cols:
        for tipo in tipos:
            mediana = df.loc[df[grupo_col] == tipo,col].median()
            mask = (df[grupo_col] == tipo) & (df[col].isnull())
            df.loc[mask,col] = mediana
    
    return df

def parsear_fechas(df,cols_fecha):
    """
    Convierte columnas de texto a datetime
    
    df         : DataFrame
    cols_fecha : lista de columnas a convertir
    """
    for col in cols_fecha:
        df[col] = pd.to_datetime(df[col],errors='coerce')
    
    return df   

def crear_variables_fecha(df):
    """
    Crea variables derivadas a partir de columnas de fecha
    
    df: DataFrame con columnas first_review, last_review, last_scraped
    """
    df["tiene_resenas"] = df["review_scores_rating"].notna().astype(int)
    
    df["dias_activo"] = (
        df["last_review"] - df["first_review"]
        ).dt.days
    
    df["dias_desde_ultima_resena"] = (
        df["last_scraped"] - df["last_review"]
        ).dt.days
    
    df["antiguedad_total"] = (
        df["last_scraped"] - df["first_review"]
        ).dt.days
    
    return df
    