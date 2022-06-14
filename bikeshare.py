import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please, Choose city to explore . Chicago, New york city or Washington: ').lower()
    while city not in ['chicago','new york city','washington']:
        print('Invalid city choice.')
        city = input('Please, Choose city to explore . Chicago, New york city or Washington: ').lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please, Choose month to filter data " january, february, march, april, may, june". Or choose "all" to see the whole data : ').lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june','all']:
        print('Invalid month choice.')
        month = input('Please, Choose month to filter january, february, march, april, may, june.'
                  '.n\ Or choose all to see the whole data : ').lower()
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input('Please, Choose day to filter data " Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday".'
            ' Or choose "all" to see data for the whole week : ').title()
    while day not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','All']:
        print('Invalid day choice.')
        day = input('Please, Choose day to filter data " Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday".'
                ' Or choose "all" to see data for the whole week : ').title()
    


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df= pd.read_csv(CITY_DATA[city])
    if month != 'all':
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'All':
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        df = df[df['day_of_week'] == day]    
    


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour_of_day'] = df['Start Time'].dt.hour
    # TO DO: display the most common month
    c_month = df['month'].mode()[0]
    print('the most common month: {}'.format(c_month))
    # TO DO: display the most common day of week
    c_day = df['day_of_week'].mode()[0]
    print('the most common day of the week: {}'.format(c_day))
    # TO DO: display the most common start hour
    c_hour = df['hour_of_day'].mode()[0]
    print('the most common hour of the day: {}'.format(c_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return c_month, c_day, c_hour

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    c_start_station = df['Start Station'].mode()[0]
    print('the most common start station: {}'.format(c_start_station))
    # TO DO: display most commonly used end station
    c_end_station = df['End Station'].mode()[0]
    print('the most common end station: {}'.format(c_end_station))
    # TO DO: display most frequent combination of start station and end station trip
    df['c_trip'] = df['Start Station'] + df['End Station']
    c_trip = df['c_trip'].mode()[0]
    print('the most common trip: {}'.format(c_trip))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return c_start_station , c_end_station , c_trip

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['duration'] = df['End Time'] - df['Start Time']

    # TO DO: display total travel time
    t_t_t = df['duration'].sum()
    print('total time of travelling: {}'.format(t_t_t))
    # TO DO: display mean travel time
    m_t_t = df['duration'].mean()
    print('the avrage travel time: {}'.format(m_t_t))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return t_t_t , m_t_t

def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()


    # TO DO: Display counts of gender
    if city != 'washington':
        gender_count = df['Gender'].value_counts()
        print ('gender count in {} trips: {}'.format(city,gender_count))
    else:
        gender_count = 'No Data Available'
        print ('gender count in {} trips: {}'.format(city,gender_count))
    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'washington' :
        earliest_birth_year = 'No Data Available'
        recent_birth_year = 'No Data Available'
        common_birth_year = 'No Data Available'
        print("earliest_birth_year = {}".format(earliest_birth_year))
        print("recent_birth_year = {}".format(recent_birth_year))
        print("common_birth_year = {}".format(common_birth_year))
    else :
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()
        print('The earliest birth year in {} data is: {}'.format(city,earliest_birth_year))
        print('The most recent birth year in {} data is: {}'.format(city,recent_birth_year))
        print('The most common birth year in {} data is: {}'.format(city,common_birth_year))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return count_user_type , gender_count , earliest_birth_year , recent_birth_year , common_birth_year

def show_data(df):
    """ 
        Ask user's agreement to show the 5 rows of filtered data each time. 
    return :
            the next 5 rows of the filtered data """
    
    user_agreement = input('Do you want to see the first 5 rows of data (yes , no)?').lower()
    while user_agreement =='no':
        print('You choosed not to explore more data')
        break
    row_count = 0 
    five_row_data = ''
    while user_agreement =='yes':
        five_row_data =(df[row_count : row_count + 6])
        print(five_row_data)
        row_count += 5
        user_agreement = input('Do you want to see the next 5 rows of data (yes , no)?').lower()
    while user_agreement not in ['yes', 'no'] :
        print ('invalid choice.')
        user_agreement = input('Do you want to see the next 5 rows of data (yes , no)?').lower()
    
    return five_row_data
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
