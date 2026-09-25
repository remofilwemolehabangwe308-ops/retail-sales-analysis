def revenue_by_group(df, group_column):
    return df.groupby(group_column)["revenue"].sum() 