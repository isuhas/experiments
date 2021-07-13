# Mode imputation with Groupby for categorical columns

for col in mis_col:
    try:
        df[col] = df.groupby('Company_response')[col].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else "Unknown"))
    except:
        print("Error --------------------------------------->")
# -----------------------------------------------------------------------------------------------       
df[col] = df.groupby('Company_response')[col].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else "Empty") )
        
# ------------------------------------------------------------------------------------------------
data11.dropna().groupby("Transaction-Type").transform(lambda x: x.fillna(x.mode() [0]))["Consumer-disputes"] 
        
        
# https://stackoverflow.com/questions/53994621/indexerror-when-replacing-missing-values-with-mode-using-groupby-in-pandas        
