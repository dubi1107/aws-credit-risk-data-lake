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
    print(customer_df.head())
    customer_df.to_csv("data/customer.csv", index=False)
    print(f"Generated {len(customer_df)} customers.")


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


if __name__ == "__main__":
    main()
