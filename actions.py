# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import re
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from price import give_stockprice, get_historical_figure
from rasa_sdk.events import FollowupAction, Restarted, SlotSet
import random
from dateparser import parse
from babel.dates import format_datetime

# class ActionSelectHistoricalStock(Action):
#     """ 
#     多次轮询
#     在之前查过 price的基础上 stock查询 historical stock数据
#     """
    
#     def name(self) -> Text:
#         return 'action_select_historical_stock'

#     def run(self, dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         stock = tracker.slots['stock']
#         dispatcher.utter_message(template='utter_ask_historical_data_time')
#         return [SlotSet('stock', stock), FollowupAction('action_select_historical_time')]

class ActionHistoricalPrice(Action):
    def name(self) -> Text:
        return 'action_historical_price'
    def extract_date(self, date_message):
        'from 2020-04-11 to 2021-3-01 正则匹配日期'
        time_list = re.findall(r'\d{4}-\d{1,2}-\d{1,2}', date_message)
        st = format_datetime(parse(time_list[0]), locale='en')
        et = format_datetime(parse(time_list[1]), locale='en')
        return st, et
        # 暂时返回默认, 不做实际匹配
        # return 1,2

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:
        date_message = tracker.get_slot('date_message')
        stime, etime = self.extract_date(date_message)
        stock = tracker.get_slot('stock')
        # todo: --> 传入EX即可获得数据 1. 将本地图片生成外链api后即可有不同的效果 2.考虑部署服务器静态目录
        image='https://i.loli.net/2021/04/22/bNMRx3aryPQYI5Z.png'
        dispatcher.utter_message(
            template="utter_historical_result",
            start_time=stime,
            end_time=etime,
            stock=stock,
            image=image
        )
        return [SlotSet('stock',stock)]


class ActionStockPrice(Action):
    
    def name(self) -> Text:
        return "action_stock_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        stock=tracker.get_slot('stock')
        try:
            if stock:
                stock.upper()
                price=give_stockprice(stock)
                response='The stock price of '+ stock +' is '+ price
            else:
                stock = random.choice(['TSLA', 'AAPL'])
                price=give_stockprice(stock)
                response="Alright, I can't get your purpose. However, Let me help you checkout {} before you make up your mind".format(stock)
                dispatcher.utter_message(response)
                dispatcher.utter_message('..A moment... Please')
                dispatcher.utter_message("here's %s's price....so, are you ready ? " % price)
        except:
            dispatcher.utter_message("Can't grab the stock price, try agian later")
            
        dispatcher.utter_message(response)
        
        return [SlotSet('stock',stock)]