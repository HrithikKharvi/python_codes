import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
  employees = employees.iloc[:3]
  return employees

