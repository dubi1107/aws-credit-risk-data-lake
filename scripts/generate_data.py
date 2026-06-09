from faker import Faker
import pandas as pd
import random

fake = Faker()

random.seed(42)

"""
Generate synthetic credit-card customer data for
AWS Data Lake project.
"""


def main():
    customer_df = generate_customers(10000)
    accounts_df = generate_accounts(customer_df)
    customer_df.to_csv("data/customers.csv", index=False)
    accounts_df.to_csv("data/accounts.csv", index=False)
    print(f"Generated {len(customer_df):,} customers")
    print(f"Generated {len(accounts_df):,} accounts")
    print(accounts_df.head())
    print("Missing customer IDs:", accounts_df["customer_id"].isnull().sum())


def generate_customers(num_customers=1000):
    customers = []

    for customer_id in range(1, num_customers + 1):
        customers.append(
            {
                "customer_id": customer_id,
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "age": random.randint(18, 80),
                "income": random.randint(30000, 250000),
                "state": fake.state_abbr(),
                "account_open_date": fake.date_between(
                    start_date="-10y", end_date="today"
                ),
            }
        )

    return pd.DataFrame(customers)


def generate_accounts(customer_df):
    accounts = []
    account_id = 10000

    for customer_id in customer_df["customer_id"]:
        num_accounts = random.randint(1, 3)
        for _ in range(num_accounts):
            credit_limit = random.choice([2000, 5000, 10000, 15000, 20000, 30000])
            current_balance = round(random.uniform(0, credit_limit * 0.95), 2)
            accounts.append(
                {
                    "account_id": account_id,
                    "customer_id": customer_id,
                    "credit_limit": credit_limit,
                    "current_balance": current_balance,
                    "account_status": random.choice(
                        [
                            "Active",
                            "Active",
                            "Active",
                            "Closed",
                        ]
                    ),
                }
            )
            account_id += 1

    return pd.DataFrame(accounts)


if __name__ == "__main__":
    main()
