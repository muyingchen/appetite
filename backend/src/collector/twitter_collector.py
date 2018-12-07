import twitter
from datetime import datetime, timedelta
from backend.src.data_provider.csv_manager import CSVManager

class TwitterCollector():
    api = twitter.Api("xnCePKlXc3x8JOnYcP290lA1V", "ElVPUBG2GY8UrQyjHgU5RKWeAyGbAv4UUzPnTENk3vrhDP5QYD", \
        "739568940884492288-fFKMtIyVFjRtyg4Fx4rUWXXBostE8VM", \
        "IYmQ1pq8HpKSO2sXg1y6vGuuSybHvbbAK7QYidSfzzxbs")

    def __init__(self, item_name):
        self.food_item = item_name

    def get_occurence_count_with_lowest_id_and_date(self, results):
        lowest_id = None
        for tweet_status in results:
            tweet = tweet_status.AsDict()
            tweet_id = tweet['id']
            lowest_id = tweet_id if lowest_id is None or tweet_id < lowest_id else lowest_id
        return [len(results), lowest_id]

    def get_number_of_occurences(self, from_date, until_date):
        num_occurences = 0

        # searches within 50 mile radius of SF
        area_limit = '&geocode=37.7749295,-122.4194155,50mi'

        query = 'q=' + '"' + self.food_item + '"' + area_limit + \
            '&since=' + from_date + '&until=' + until_date + '&count=100'

        print('\n\nquerying at /' + query + '\n\n')

        results = TwitterCollector.api.GetSearch(raw_query = query)

        count_id_and_date = self.get_occurence_count_with_lowest_id_and_date(results)
        num_counts, lowest_id = count_id_and_date
        num_occurences += num_counts
        while num_counts > 1:
            query = 'q=' + '"' + self.food_item + '"' + area_limit + \
                '&max_id=' + str(lowest_id) + '&since=' + from_date + '&until=' + until_date + '&count=100'
            results = TwitterCollector.api.GetSearch(raw_query = query)
            count_id_and_date = self.get_occurence_count_with_lowest_id_and_date(results)
            num_counts, lowest_id = count_id_and_date
            num_occurences += num_counts

        return num_occurences

    def write_twitter_data_to_csv(self, csv_file_name, start_date):
        one_day_increment = timedelta(days = 1)
        csv_manager = CSVManager(csv_file_name, ['date', 'item', 'tweet_occurence_count'])

        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')

        lst = []
        for _ in range(0, 9):
            next_day_obj = start_date_obj + one_day_increment
            next_day = next_day_obj.strftime('%Y-%m-%d')
            num_times_tweet_mention = self.get_number_of_occurences(start_date, next_day)

            record = {'date': start_date, 'item': self.food_item, 'tweet_occurence_count': num_times_tweet_mention}
            lst.append(record)

            # print('record entered is - ' + str(record))

            start_date_obj = next_day_obj
            start_date = start_date_obj.strftime('%Y-%m-%d')

        csv_manager.write(lst)

# Example code:
"""
strawberry_tweet_collector = TwitterCollector('strawberry')
strawberry_tweet_collector.write_twitter_data_to_csv(csv_file_name='strawberry_data.csv', start_date='2018-12-01')
"""