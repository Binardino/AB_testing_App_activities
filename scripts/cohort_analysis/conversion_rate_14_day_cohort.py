##Measuring conversion rate over 14 day period

#defining current_date variable
current_date = pd.to_datetime(get_date)

#defining max_purchase_date
max_lapse_date_14 = current_date - timedelta(days = 14)

##Filtering relevant users
#sub dataframe for 14 days converted users
conv_sub14_data = sub_data[sub_data.date < max_lapse_date_14]

##Calculating time between users lapse and subscription
sub_time_14 = conv_sub14_data.subscription_date < conv_sub14_data.lapse_date


#Creating new column 'sub_time'
conv_sub14_data['sub_time'] = sub_time_14

#converting to days value
conv_sub14_data['sub_time'] = conv_sub14_data.sub_time.dt.days

#Calculating CR
conv_base_14 = conv_sub14_data[(conv_sub14_data.sub_time.not_null()) & \
			(conv_base_14.sub_time > 7)]

total_users_14 = len(conv_base_14)

total_subs_14 = np.where((conv_sub14_data.sub_time.not_null()) & \
						  conv_base_14.sub_time <= 14,
						  1,
						  0)

total_subs_14 = sum(total_subs_14)

cr_14 = total_subs_14 / total_users_14
print(cr_14)