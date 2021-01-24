#-*-coding:utf-8-*-
import requests,json
from bs4 import BeautifulSoup
from fake_headers import Headers
class FoodPanda:
    address = ''

    def __init__(self, address):
        self.address = address

    def resolve_restaurant_name_url(self, body):
        result_list = []
        soup = BeautifulSoup(body, 'lxml')
        all_of_restaurant = soup.find_all('figure', {"class": ["vendor-tile", "item"]})

        for res in all_of_restaurant:
            url_restaurant = res.parent['href']
            sigle_restaurant = res.find('span', {"class": "name"})
            res_name = res.find('span', {"class": "name"}).text
            img = res.find('picture').find('div').attrs['data-src'].split("|")[0]
            result_list.append({'name': res_name, 'url': f'https://www.foodpanda.com.tw{url_restaurant}','img':img})
        return result_list


    def fetch_restaurant_dishes(self, url):
        headers = Headers(browser='chrome').generate()
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            dish_class = soup.find_all('div', {'class': 'dish-category-header'})
            dish_list = soup.find_all('ul', {'class': 'dish-list'})
            total_result = []
            for idx, d_class in enumerate(dish_class):
                dishes_list = []
                d_class_name = str(d_class.text).replace('\n', '')
                dish_name_list = dish_list[idx].find_all('h3', {'class': 'dish-name'})
                for dish_name_ele in dish_name_list:
                    dish_name = str(dish_name_ele.text).replace('\n', '')
                    dishes_list.append(dish_name)
                total_result.append({d_class_name: dishes_list})
            return total_result


    def fetch_all_restaurants(self):
        headers = Headers(browser='chrome').generate()
        querystring = {"postcode": "500", "expedition_type": "pickup"}
        coordinate_dict: dict = FoodPanda.get_address_coordinate(self.address)
        if coordinate_dict:
            url = f"https://www.foodpanda.com.tw/restaurants/lat/{coordinate_dict['lat']}/lng/{coordinate_dict['lng']}"

            response = requests.request("GET", url, headers=headers)
            if response.status_code == 200:
                restaurant_list = self.resolve_restaurant_name_url(response.text)

                # for idx, restaurant in enumerate(restaurant_list):
                #     restaurant_dish:list = self.fetch_restaurant_dishes(restaurant['url'])
                #     restaurant_list[idx]['dish'] = restaurant_dish
                    # print(resu)
                    # print(json.dumps(restaurant_dish))
                    # print(restaurant_dish)
                print(json.dumps(restaurant_list,ensure_ascii=False))
                return json.dumps(restaurant_list,ensure_ascii=False)
        return None



    @staticmethod
    def get_address_coordinate(address):
        url = "https://geocoder.api.here.com/6.2/geocode.json"

        headers = Headers(browser='chrome').generate()
        querystring = {"street": address, "country": "tw",
                       "gen": "9", "app_id": "LhbLLCfGd3UZvbRvF3AU", "app_code": "vQPgoZbKo5zLZ5tlinYyUg"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.status_code == 200:
            obj = json.loads(response.text)
            if 'View' in obj['Response']:
                coodinate_dict = obj['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']

                return {'lat': coodinate_dict['Latitude'], 'lng': coodinate_dict['Longitude']}

        return None

