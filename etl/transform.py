import pandas as pd

def transform(df):

    # Remove duplicates
    df = df.drop_duplicates(subset=["id"])

    # Expand nested rating column
    rating_df = pd.json_normalize(df["rating"])
    rating_df.columns = ["rating_rate", "rating_count"]

    df = df.drop(columns=["rating"])
    df = pd.concat([df, rating_df], axis=1)

    # Business metric: estimated revenue
    df["estimated_revenue"] = df["price"] * df["rating_count"]

    # Rename columns for warehouse style
    df = df.rename(columns={
        "id": "product_id",
        "title": "product_name",
        "price": "unit_price"
    })

    return df