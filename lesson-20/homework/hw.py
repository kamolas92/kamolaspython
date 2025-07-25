import sqlite3
import pandas as pd 
conn = sqlite3.connect('chinook.db')
##1.
customers_df = pd.read_sql("Select * From customers",conn)
invoices_df = pd.read_sql("Select * From invoices",conn)
total_spent_per_customer = (
invoices_df.groupby('CustomerId')['Total']  
.sum()
.reset_index()
)
customer_purchases = pd.merge(total_spent_per_customer, customers_df, on="CustomerId")
customer_purchases = customer_purchases[["CustomerId", "FirstName", "LastName", "Total"]]
customer_purchases = customer_purchases.sort_values("Total", ascending=False)
print(customer_purchases.head(10)) 
##2.
customers_df = pd.read_sql("SELECT * FROM customers", conn)
invoices_df = pd.read_sql("SELECT * FROM invoices", conn)
total_spent = (
    invoices_df.groupby("CustomerId")["Total"]
    .sum()
    .reset_index()
)
customer_totals = pd.merge(total_spent, customers_df, on="CustomerId")
top_5_customers = (
    customer_totals[["CustomerId", "FirstName", "LastName", "Total"]]
    .sort_values(by="Total", ascending=False)
    .head(5)
)
print(top_5_customers)

##3.
customers_df = pd.read_sql("SELECT * FROM customers", conn)
invoices_df = pd.read_sql("SELECT * FROM invoices", conn)
total_spent = (
    invoices_df.groupby("CustomerId")["Total"]
    .sum()
    .reset_index()
)
customer_totals = pd.merge(total_spent, customers_df, on="CustomerId")
customer_totals["FullName"] = customer_totals["FirstName"] + " " + customer_totals["LastName"]
top_5 = (
    customer_totals[["CustomerId", "FullName", "Total"]]
    .sort_values(by="Total", ascending=False)
    .head(5)
)
print(top_5)

##1.
tracks_df = pd.read_sql("SELECT TrackId, AlbumId FROM tracks", conn)
invoice_items_df = pd.read_sql("SELECT InvoiceId, TrackId FROM invoice_items", conn)
invoices_df = pd.read_sql("SELECT InvoiceId, CustomerId FROM invoices", conn)
merged_df = pd.merge(invoice_items_df, tracks_df, on='TrackId')
grouped = merged_df.groupby(['InvoiceId', 'AlbumId'])['TrackId'].count().reset_index(name='TracksPurchased')
album_track_counts = tracks_df.groupby('AlbumId')['TrackId'].count().reset_index(name='TotalTracks')
invoice_album_info = pd.merge(grouped, album_track_counts, on='AlbumId')
invoice_album_info['IsFullAlbum'] = invoice_album_info['TracksPurchased'] == invoice_album_info['TotalTracks']
invoice_summary = invoice_album_info.groupby('InvoiceId')['IsFullAlbum'].max().reset_index()
invoice_customer = pd.merge(invoice_summary, invoices_df[['InvoiceId', 'CustomerId']], on='InvoiceId')
#For each customer, check if they ever purchased a full album
customer_summary = invoice_customer.groupby('CustomerId')['IsFullAlbum'].any().reset_index()
total_customers = len(customer_summary)
individual_track_only_customers = len(customer_summary[customer_summary['IsFullAlbum'] == False])
percentage = (individual_track_only_customers / total_customers) * 100
print(f"Percentage of customers who prefer individual tracks: {percentage:.2f}%")

##2.

tracks = pd.read_sql("SELECT TrackId, AlbumId FROM Tracks", conn)
invoice_lines = pd.read_sql("SELECT InvoiceLineId, InvoiceId, TrackId FROM Invoice_items", conn)
invoices = pd.read_sql("SELECT InvoiceId, CustomerId FROM Invoices", conn)
customers = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM Customers", conn)

# Step 1: Combine invoice_lines with invoices to get CustomerId for each purchased track
purchases = invoice_lines.merge(invoices, on='InvoiceId')

# Step 2: Join with tracks to get AlbumId for each track purchased
purchases = purchases.merge(tracks, on='TrackId')

# Step 3: Calculate total number of tracks per album
total_tracks_per_album = tracks.groupby('AlbumId').size().reset_index(name='total_tracks')

# Step 4: Calculate number of unique tracks purchased per customer per album
customer_album_tracks = purchases.groupby(['CustomerId', 'AlbumId'])['TrackId'].nunique().reset_index(name='tracks_purchased')

# Step 5: Merge to get total tracks per album corresponding each customer_album record
customer_album_tracks = customer_album_tracks.merge(total_tracks_per_album, on='AlbumId')

# Step 6: Filter customers who purchased only a subset: tracks_purchased < total_tracks, and > 0
subset_purchasers = customer_album_tracks[
    (customer_album_tracks['tracks_purchased'] > 0) & 
    (customer_album_tracks['tracks_purchased'] < customer_album_tracks['total_tracks'])
]

# (Optional) Add customer names for readability
subset_purchasers = subset_purchasers.merge(customers, on='CustomerId')

# Display the resulting customers who prefer individual tracks
print(subset_purchasers[['CustomerId', 'FirstName', 'LastName', 'AlbumId', 'tracks_purchased', 'total_tracks']].head())

##3.
import pandas as pd
import sqlite3

# Connect to Chinook database
conn = sqlite3.connect('chinook.db')

tracks = pd.read_sql("SELECT TrackId, AlbumId FROM Tracks", conn)
invoice_lines = pd.read_sql("SELECT InvoiceLineId, InvoiceId, TrackId FROM Invoice_items", conn)
invoices = pd.read_sql("SELECT InvoiceId, CustomerId FROM Invoices", conn)
customers = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM Customers", conn)

# Close connection as data is loaded
conn.close()

# Step 1: Merge invoice_lines with invoices to get customer per track purchased
purchases = invoice_lines.merge(invoices, on='InvoiceId')

# Step 2: Add album info for each purchased track
purchases = purchases.merge(tracks, on='TrackId')

# Step 3: Get total tracks count per album
total_tracks_per_album = tracks.groupby('AlbumId').size().reset_index(name='total_tracks')

# Step 4: Count unique tracks purchased per customer per album
customer_album_tracks = purchases.groupby(['CustomerId', 'AlbumId'])['TrackId'].nunique().reset_index(name='tracks_purchased')

# Step 5: Add total track counts to the purchased tracks info
customer_album_tracks = customer_album_tracks.merge(total_tracks_per_album, on='AlbumId')

# Step 6: Determine purchase type per customer per album
# - full_album if tracks_purchased == total_tracks
# - partial_album if 0 < tracks_purchased < total_tracks

def categorize(row):
    if row['tracks_purchased'] == row['total_tracks']:
        return 'full_album'
    else:
        return 'partial_album'

customer_album_tracks['purchase_type'] = customer_album_tracks.apply(categorize, axis=1)

# Step 7: Aggregate per customer their purchase types across all albums
customer_types = customer_album_tracks.groupby('CustomerId')['purchase_type'].agg(set).reset_index()

# Step 8: Classify customers into categories
def classify_customer(purchase_types):
    if purchase_types == {'full_album'}:
        return 'Full Album Only'
    elif purchase_types == {'partial_album'}:
        return 'Individual Tracks Only'
    elif purchase_types == {'full_album', 'partial_album'}:
        return 'Both Full Albums and Individual Tracks'
    else:
        return 'No Purchases'

customer_types['category'] = customer_types['purchase_type'].apply(classify_customer)

# Step 9: Check if any customers had no purchases at all and add them with 'No Purchases' category
purchased_customers = set(customer_types['CustomerId'])
all_customers = set(customers['CustomerId'])

no_purchase_customers = all_customers - purchased_customers

if no_purchase_customers:
    no_purchase_df = pd.DataFrame({
        'CustomerId': list(no_purchase_customers),
        'purchase_type': [set()]*len(no_purchase_customers),
        'category': ['No Purchases']*len(no_purchase_customers)
    })
    customer_types = pd.concat([customer_types, no_purchase_df], ignore_index=True)

# Step 10: Calculate percentages
category_counts = customer_types['category'].value_counts(normalize=True) * 100
category_counts = category_counts.reset_index()
category_counts.columns = ['Category', 'Percentage']

print(category_counts)
