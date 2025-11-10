# Data Dictionary (Online Retail assumption)

- InvoiceNo: Invoice number. A unique number assigned to each transaction.
- StockCode: Product (item) code.
- Description: Product (item) name.
- Quantity: The quantities of each product (item) per transaction.
- InvoiceDate: Invoice date and time.
- UnitPrice: Unit price. Product price per unit in sterling.
- CustomerID: Customer number. A unique number assigned to each customer.
- Country: Country name.

Engineered:
- TotalAmount: Quantity * UnitPrice for each line.
- RFM: Recency (days since last purchase), Frequency (count of invoices), Monetary (sum of TotalAmount).
- Cluster: Cluster label assigned by the model.
