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
    print('Hello There! Let us explore some US bikeshare data,sounds good?')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\n Which city would you like to filter by? New York City, Chicago or Washington?\n")
        city = city.lower()
        if city in ['new york city','chicago','washington']:
            break
        else:
            print("I am sorry, there is no such city. Please try again!")

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("\nWhich month would you like to filter by? January, February, March, April, May, June? or type 'all' if there is no prefrence.\n")
        month = month.lower()
        if month in ['january','february','march','april','june','all']:
            break
        else:
            print("I am sorry, there is no such month. Please try again!")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n Which day would you like to filter by? Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday or you can simply type 'all' if there is no prefrence.\n")
        day = day.lower()
        if day in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']:
            break
        else:
            print("I am sorry, there is no such day. Please try again!")





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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month !='all':
        months = ['january', 'february', 'march','april', 'may','june']
        month = months.index(month) +1

        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The Most Common Month Is:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The Most Common Day Is:', popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The Most Common Hour Is:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('The Most Common Used Start Station Is:', Start_Station)

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nThe Most Common Used End Station Is:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination_station= df.groupby(['Start Station','End Station']).count()
    print('\nThe Most Frequent Used Start & End Station Comined, Is:', Start_Station,"&", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time = sum(df['Trip Duration'])
    print('Total Travel Time Is:', Total_travel_time/86400,"Days")

    # TO DO: display mean travel time
    Mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time Is:', Mean_travel_time/60,"Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('\nGender Types:\n',gender_types)
    except KeyError:
        print("\nGender Types;\nData UNAVAILABLE for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earliest_year = df['Birth Year'].min()
        print('\nEarliest Year is:', Earliest_year)
    except KeyError:
        print("\nEarliest Year:\nData UNAVAILABLE for this month.")
    try:
        Most_recent_year = df['Birth Year'].max()
        print('\nMost Recent Year:', Most_recent_year)
    except KeyError:
        print("\nMost Revent Year:\nData UNAVAILABLE for this month.")
    try:
        Most_common_year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:',Most_common_year)
    except KeyError:
        print("\nMost Common Year:\n Data UNAVAILABLE for this month.")

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    x = 1
    while True:
        raw = input('\n Would you like to view 5 rows of individual trip date? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
