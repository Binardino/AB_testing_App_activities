import pandas as pd
import datetime

#import datasets
customer_data = pd.read_csv('customer_data.csv')

app_purchases = pd.read_csv('inapp_purchases.csv')

print(customer_data.columns)

print(app_purchases.columns)

customer_subscriptions = pd.read_csv('customer_subscriptions.csv')

customer_demographics = pd.read_csv('customer_demographics.csv')


#create merged dataframe
sub_data_demo = customer_demographics.merge(customer_subscriptions,
											how = 'inner',
											on = 'uid')


# Merge on the 'uid' field
uid_combined_data = app_purchases.merge(customer_data, on='uid', how='inner')

# Examine the results 
print(uid_combined_data.head())
print(len(uid_combined_data))


sub_data_grp = sub_data_demo.groupby(by=['country', 'device'],
									 axis=0,
									 as_index=False)

sub_data_grp.agg({'price':['mean', 'min', 'max'],
				  'age':['mean', 'min', 'max']})

#custom function to agg by

def truncated_mean(data):
	"""returns df without 1st and 9th decile - exclude outliers"""
	top_val = data.quantile(.9)
	min_val = data.quantile(.1)
	truncated_data = data[(data <= top_val) & (data >= min_val)]
	mean = truncated_data.mean()

	return mean

sub_data_grp.agg({'age':[(truncated_mean)]})

##KPIs Cohort analysis over App usage
current_date = pd.to_datetime(get_date)

#Lapse Date = end of 7 day free trial
sub_data_demo.lapse_data.max()

#defining KPIs
max_purchase_date = current_date - timedelta(days = 7)

#filtering dataset with last 7 day free trial period
conv_sub_data = sub_data_demo[(sub_data_demo.lapse_date < max_purchase_date)]

#calculating total subs
total_subs = conv_sub_data[(sub_data_demo.price > 0)&\
									 (sub_data_demo.lapse_date <= max_purchase_date)
									 ]

total_subs_count = total_subs.price.count()

#calculating conversion rate
conversion_rate = total_subs_count / total_users_count

#Finding days between lapse & subscription
sub_time = np.where(if: conv_sub_data.subscription_date.notnull(),
					then: (conv_sub_data.subscription_date - conv_sub_data.lapse_date).dt.days,
					else: pd.NaT
					)


# TBD : defining functions for selecting cohort lifetime
#gcr7, gcr14

#group by socio-demographics cohorts
purchase_cohorts = conv_sub_data.group_by(by=['gender', 'device'], 
										  as_index=False)

#TBD : launching group by aver 7 & 14 day cohort
#purchase_cohorts.agg({sub_time : [gcr7, gcr14]})

#defining KPIs AVG_price_28day_cohort
max_purchase_date_28 = current_date - timedelta(days=28)

## Filter to only include users who registered before our max date
purchase_data_filt28 = purchase_data[purchase_data.reg_date < 
									 max_purchase_date_28]

#filter to only include purchases within the first 28 days of registration
purchase_data_filt28 = purchase_data_filt28[(purchase_data_filt28.date <=
						purchase_data_filt28.reg_date + timedelta(days=28))]

AVG_price_28day_cohort = purchase_data_filt28.price.mean()

# Set the max registration date to be one month before today
max_reg_date = current_date - timedelta(days=28)

# Find the month 1 values
month1 = np.where((purchase_data.reg_date < max_reg_date) &
                 (purchase_data.date < purchase_data.reg_date + timedelta(days=28)),
                  purchase_data.price, 
                  np.NaN)
                 
# Update the value in the DataFrame
purchase_data['month1'] = month1

# Group the data by gender and device 
purchase_data_upd = purchase_data.groupby(by=['gender', 'device'], as_index=False)

##Datetime Data cleaning
# Provide the correct format for the date
date_data_one = pd.to_datetime(date_data_one, format="%A %B %d, %Y")
print(date_data_one)