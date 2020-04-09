def impute_data(merged_features, na_indexes_cpi, na_indexes_une):
    for i in na_indexes_cpi:
        merged_features.at[i, 'CPI'] = merged_features.at[i - 1, 'CPI']
    for i in na_indexes_une:
        merged_features.at[i, 'Unemployment'] = merged_features.at[i - 1, 'Unemployment']
