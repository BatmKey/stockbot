## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## stock price path
* greet
  - utter_greet
* ask_function
  - utter_function_menu
* stock_price{"stock":"GOOG"}
    - slot{"stock":"GOOG"}
    - action_stock_price
    - slot{"stock":"GOOG"}
* inquire
  - utter_ask_stock
* waste
  - utter_default
* stock_price
  - action_stock_price
  - slot{"stock":"fb"}
* affirm
  - utter_affirm
* mood_great
  - utter_awesome
* waste
  - utter_default

* goodbye
  - utter_goodbye

## stock price path2
* greet
  - utter_greet
  - utter_intro
* waste
  - utter_default
* stock_price
  - action_stock_price
  - slot{"stock":"sbin.ns"}
* affirm
  - utter_affirm
* goodbye
  - utter_goodbye

## fallback
* bot_challenge
  - action_default_fallback
* greet
  - action_default_fallback
* goodbye
  - action_default_fallback
* affirm
  - action_default_fallback
* deny
  - action_default_fallback
* mood_great
  - action_default_fallback
* mood_unhappy
  - action_default_fallback
* stock_price
  - action_default_fallback

## New Story
* greet
    - utter_greet
    - utter_intro
* stock_price{"stock":"GOOG"}
    - slot{"stock":"GOOG"}
    - action_stock_price
    - slot{"stock":"GOOG"}
* stock_price{"stock":"AAPL"}
    - slot{"stock":"AAPL"}
    - action_stock_price
    - slot{"stock":"AAPL"}
* stock_price{"stock":"sbin.ns"}
    - slot{"stock":"sbin.ns"}
    - action_stock_price
    - slot{"stock":"sbin.ns"}

