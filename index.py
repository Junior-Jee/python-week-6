import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

try:
    # Create a sample dataset
    np.random.seed(42)  # For reproducibility
    
    # Generate sample sales data
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    sales = np.random.normal(1000, 200, len(dates))
    prices = np.random.uniform(10, 20, len(dates))
    
    # Create the DataFrame
    data = pd.DataFrame({
        'date': dates,
        'sales': sales,
        'price': prices,
        'revenue': sales * prices
    })

    print("Data successfully created!")
    
    # Basic data exploration
    print("\n=== Data Overview ===")
    print("\nFirst 5 rows:")
    print(data.head())
    
    print("\nDataset Info:")
    print(data.info())
    
    print("\nBasic Statistics:")
    print(data.describe())
    
    # Create visualizations
    try:
        # Figure 1: Sales over time
        plt.figure(figsize=(10, 6))
        plt.plot(data['date'], data['sales'])
        plt.title('Daily Sales Over Time')
        plt.xlabel('Date')
        plt.ylabel('Sales')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        # Figure 2: Sales distribution
        plt.figure(figsize=(10, 6))
        plt.hist(data['sales'], bins=30)
        plt.title('Distribution of Daily Sales')
        plt.xlabel('Sales')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()
        
        # Figure 3: Sales vs Price scatter plot
        plt.figure(figsize=(10, 6))
        plt.scatter(data['price'], data['sales'])
        plt.title('Sales vs Price')
        plt.xlabel('Price')
        plt.ylabel('Sales')
        plt.tight_layout()
        plt.show()
        
        print("\nVisualizations completed successfully!")
        
    except Exception as e:
        print(f"Error creating visualizations: {str(e)}")
    
    # Basic analysis
    print("\n=== Analysis Results ===")
    print(f"\nAverage daily sales: {data['sales'].mean():.2f}")
    print(f"Average price: ${data['price'].mean():.2f}")
    print(f"Total revenue: ${data['revenue'].sum():.2f}")
    
    # Monthly analysis
    monthly_sales = data.set_index('date').resample('M')['sales'].mean()
    print("\nMonthly Average Sales:")
    print(monthly_sales)

except ImportError as e:
    print(f"Error: Missing required library. Please install the required libraries using:")
    print("pip install pandas matplotlib numpy")
    print(f"Specific error: {str(e)}")
    
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")