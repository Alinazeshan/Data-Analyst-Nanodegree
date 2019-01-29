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
    print('Good Day! \n Hello! Let\'s explore some US bikeshare data!\n ')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Select from following cities : chicago, washington, new york city\n').lower()
        if city not in  ['chicago', 'washington' , 'new york city' ]:
            print('wrong city, kindly type as specified for example "chicago"')
        else:
            print('you selected :{} '.format(city))
            break
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Select from following months : all, january, february, march, april, may, june : \n").lower()
        print('')
        if month not in  ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('wrong month, kindly type  as specified. for example "all"')
        else:
            print('you selected : ' + month )
            break   
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Select the day : all or sunday, monday ,tuesday ,wednesday ,thursday ,friday ,saturday :').lower()
        print('')
        if day in ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']:
            print ('You selected {} '.format(day))
            break
        else:
            print('Select again.\n kindly type as given')

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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most common month of city is: ' , df['month'].value_counts().index[0])
    

    # display the most common day of week
    print('The most common day of week is : ' , df['day_of_week'].value_counts().index[0])
   

    # display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is: ' , df['hour'].value_counts().index[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print ('Most commonly used start station is : ' , df['Start Station'].mode()[0])


    # display most commonly used end station
    print ('Most commonly used end station is : ' , df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    df['combination'] ='From ' + df['Start Station'] +' Till '+ df['End Station']

    print('Most frequent combination station for Start and End Trip : \n' , df['combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print ('Total time travel: ' , df['Trip Duration'].sum())


    # display mean travel time
    print ('The mean travel time : ' , df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of User types:\n' , df['User Type'].value_counts())
    # Display counts of gender
    print('Counts of gender :\n', df['Gender'].value_counts())
    # Display earliest, most recent, and most common year of birth
    print('Earliest year of birth : ' , df['Birth Year'].min())
    print('Most recent year of birth : ' , df['Birth Year'].max())
    print('Most Common year of birth : ' , df['Birth Year'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.'''
    i = 0
    while True:
        data = input('\nDo you want to view the Raw Data? Enter yes or no.\n').lower()
        if data == 'yes':
            j = i+5
            print (df.iloc[i:j])
            i =i+5
        else:
            print('ok')
            break
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if 'Gender' in df:
            user_stats(df)
        else:
            print('\nCalculating User Stats...\n')
            print('Counts of User types: ' , df['User Type'].value_counts())
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print ('Have a Nice day')
            break


if __name__ == "__main__":
	main()