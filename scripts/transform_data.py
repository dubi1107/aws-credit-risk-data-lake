"""
Transform raw credit risk data into customer-level metrics.
Needs to be run from the root folder (not while in the Scripts folder)
"""

import pandas as pd


def main():
    customer_metrics = create_customer_dataset()
    customer_metrics.to_csv("data/processed/customer_metrics.csv", index=False)
    print(f"Gnenerated customer metrics dataset with {len(customer_metrics):,} records")


def load_data():
    customers_df = pd.read_csv("data/raw/customers.csv")
    accounts_df = pd.read_csv("data/raw/accounts.csv")
    transactions_df = pd.read_csv("data/raw/transactions.csv")

    return customers_df, accounts_df, transactions_df


def build_customer_metrics(customers, accounts):
    account_metrics = (
        accounts.groupby("customer_id")
        .agg({"credit_limit": "sum", "current_balance": "sum", "account_id": "count"})
        .reset_index()
    )
    account_metrics["utilization"] = (
        account_metrics["current_balance"] / account_metrics["credit_limit"]
    )
    account_metrics.rename(columns={"account_id": "num_accounts"}, inplace=True)

    customer_metrics = customers.merge(account_metrics, on="customer_id", how="left")

    return customer_metrics


def build_spending_metrics(accounts, transactions):
    transaction_accounts = transactions.merge(
        accounts[["account_id", "customer_id"]], on="account_id"
    )
    spend_metrics = (
        transaction_accounts.groupby("customer_id")
        .agg({"amount": ["sum", "mean", "count"]})
        .reset_index()
    )
    spend_metrics.columns = [
        "customer_id",
        "total_spend",
        "avg_transaction_amount",
        "transaction_count",
    ]
    return spend_metrics


def create_customer_dataset():
    customers, accounts, transactions = load_data()
    customer_metrics = build_customer_metrics(customers, accounts)
    spend_metrics = build_spending_metrics(accounts, transactions)
    final_df = customer_metrics.merge(spend_metrics, on="customer_id", how="left")
    final_df["risk_score"] = (
        (final_df["utilization"] * 60)
        + ((final_df["transaction_count"] / 100) * 20)
        + ((final_df["avg_transaction_amount"] / 100) * 20)
    )
    final_df["spend_per_account"] = final_df["total_spend"] / final_df["num_accounts"]
    return final_df


if __name__ == "__main__":
    main()
