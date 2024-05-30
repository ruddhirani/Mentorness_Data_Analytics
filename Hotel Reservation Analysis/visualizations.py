import pandas as pd
import matplotlib.pyplot as plt
# Replace 'file_path' with the path to your Excel file
file_path = 'Hotel Reservation Dataset.csv'

# Load the data into a Pandas DataFrame
df = pd.read_csv(file_path)

# Distribution of Lead Time:
# Visualization: Histogram
# Description: Shows how many days in advance guests are booking their reservations.
# df['lead_time'].hist(bins=30)
# plt.title('Distribution of Lead Time')
# plt.xlabel('Lead Time (days)')
# plt.ylabel('Number of Bookings')
# plt.show()


# Booking Status by Market Segment:
# Visualization: Bar Chart
# Description: Compares the number of bookings and cancellations across different market segments.
# df.groupby(['market_segment_type', 'booking_status']
#            ).size().unstack().plot(kind='bar', stacked=True)
# plt.title('Booking Status by Market Segment')
# plt.xlabel('Market Segment')
# plt.ylabel('Number of Bookings')
# plt.show()

# Average Price per Room by Room Type:
# Visualization: Box Plot
# Description: Displays the distribution of average room prices for each room type.
# df.boxplot(column='avg_price_per_room', by='room_type_reserved')
# plt.title('Average Price per Room by Room Type')
# plt.suptitle('')
# plt.xlabel('Room Type Reserved')
# plt.ylabel('Average Price per Room')
# plt.show()

# Number of Weekend vs Weekday Nights:
# Visualization: Stacked Bar Chart
# Description: Compares the number of nights spent on weekends versus weekdays for each reservation.
# df[['no_of_weekend_nights', 'no_of_week_nights']].sum().plot(kind='bar',
#                                                              stacked=True)
# plt.title('Number of Weekend vs Weekday Nights')
# plt.xlabel('Type of Night')
# plt.ylabel('Number of Nights')
# plt.show()


# Meal Plan Preferences:
# Visualization: Pie Chart
# Description: Shows the distribution of different meal plans chosen by guests.
# df['type_of_meal_plan'].value_counts().plot(kind='pie', autopct='%1.1f%%')
# plt.title('Meal Plan Preferences')
# plt.ylabel('')
# plt.show()


# Arrival Date Trends:
# Visualization: Line Chart
# Description: Shows the trend of bookings over time.
# Convert 'arrival_date' to datetime and extract month and day of year
# df['arrival_date'] = pd.to_datetime(df['arrival_date'])
# df['month'] = df['arrival_date'].dt.month
# df['day_of_year'] = df['arrival_date'].dt.dayofyear

# Visualize Trends by Month
# monthly_bookings = df.groupby('month').size()
# monthly_bookings.plot(kind='line')
# plt.title('Monthly Arrival Trends')
# plt.xlabel('Month')
# plt.ylabel('Number of Bookings')
# plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr',
#            'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
# plt.show()


# Booking Status Distribution:
# Visualization: Bar Chart
# Description: Displays the distribution of booking statuses (e.g., booked, canceled).
# df['booking_status'].value_counts().plot(kind='bar')
# plt.title('Booking Status Distribution')
# plt.xlabel('Booking Status')
# plt.ylabel('Number of Bookings')
# plt.show()


# Room Type Popularity:
# Visualization: Bar Chart
# Description: Shows the popularity of different room types.
# df['room_type_reserved'].value_counts().plot(kind='line')
# plt.title('Room Type Popularity')
# plt.xlabel('Room Type Reserved')
# plt.ylabel('Number of Bookings')
# plt.show()

# Number of Adults and Children per Booking:

# Visualization: Scatter Plot
# Description: Shows the number of adults and children per booking.
# Create a new column for total people per booking
# df['total_people'] = df['no_of_adults'] + df['no_of_children']

# Aggregate the data to get the count of bookings for each combination of adults and children
# grouped_data = df.groupby(
#   ['no_of_adults', 'no_of_children']).size().unstack().fillna(0)

# Plot a stacked bar chart
# grouped_data.plot(kind='bar', stacked=True, figsize=(12, 8))

# plt.title('Number of Adults and Children per Booking')
# plt.xlabel('Number of Adults')
# plt.ylabel('Number of Bookings')
# plt.legend(title='Number of Children')
# plt.xticks(rotation=0)
# plt.show()


df.plot(kind='scatter', x='lead_time', y='avg_price_per_room')
plt.title('Average Price per Room over Lead Time')
plt.xlabel('Lead Time (days)')
plt.ylabel('Average Price per Room')
plt.show()
