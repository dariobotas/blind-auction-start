from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

last_bidder = False
list_of_bidders = {}

def find_highest_bidder(bidders_list):
  max_bid = 0
  bidder_winner = ""
  for bidder in bidders_list:
    bid = bidders_list[bidder]
    if bid > max_bid:
      max_bid = bid
      bidder_winner = bidder
  print(f"The winner is {bidder_winner} with a bid of ${max_bid}.")
  
print(logo)
print("Welcome to the secret auction program.")

while not last_bidder:
  name_bidder = input("What's your name?: ")
  bid = int(input("What's your bid?: $"))

  list_of_bidders[name_bidder] = bid
  
  more_bidders_question = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

  clear()
  
  if more_bidders_question == 'no' or more_bidders_question == 'n':
    last_bidder = True
    find_highest_bidder(list_of_bidders)
      