import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAYS_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

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
    while True:
        city= input('Please enter a city from this cities (chicago , new york city, washington)').lower()
        if city not in CITY_DATA:
            print('Please enter a correct city')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month= input('Please enter a month from january to june or type "all" to display all monthes:').lower()
        if month not in MONTHS_DATA:
            print('please enter a valide month name')
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('Please enter a day of the week or enter "all" to display all days: ').lower()
        if day not in DAYS_DATA:
            print('please enter a valide day name')
        else:
            break

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
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS_DATA.index(month) + 1

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

    # TO DO: display the most common month
    common_month= df['month'].mode()[0] # return a month number 
    print("The most common Month after choosen filters is :" + MONTHS_DATA[common_month].title()) # get month name

    # TO DO: display the most common day of week
    common_day= df['day_of_week'].mode()[0]
    print("The most common day of week after choosen filters is : " + str(common_day))

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common start hour after choosen filters is : " + str(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Your docstring here """
    i = 0
    raw = input("whould you like to display the first 5 raws of data ? yes/no ").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',None)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("whould you like to display next 5 rows of data ? yes/no").lower () # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

            
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station after choosen filters is : " + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station after choosen filters is : " + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "-" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time after choosen filters is : " , round( total_travel_time/3600 , 1) ,'hours') 

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The average travel time after choosen filters is : " , round(mean_travel_time/3600 , 1) ,'hours') 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users_type = df['User Type'].value_counts()
    print("The count of user types after choosen filters is : \n" + str(users_type))

    # TO DO: Display counts of gender
    if 'gender' in df:
        gender_type = df['Gender'].value_counts()
        print("The count of user gender after choosen filters is : \n" + str(gender_type))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth  is: \n', earliest_birth)
        print('Most recent birth is: \n', most_recent_birth)
        print('Most common birth is: \n',most_common_birth )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
    
            if restart.lower() == 'no':
               return
            elif restart.lower() == 'yes':
                break
            else:
                print ("invalid inputs please enter yes/no ? ")
                

if __name__ == "__main__":
	main()
