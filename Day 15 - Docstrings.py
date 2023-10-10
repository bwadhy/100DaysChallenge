#Usando as funções criadas nos desafios anteriores , colocaremos suas devidas descrições. Para isso usamos as DOCSTRINGS , e para utilizá-las basta identar e abrir 3 aspas e digitar o que a função faz logo após o def.

def find_highest_bidder(bidding_record):
  """ Função que irá ver qual o maior valor do leilão e definirá o vencedor"""
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

#Abaixo outro exemplo:

def is_leap(year):
  """Função que verifica se um ano é bissexto ou não."""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
        return True
  else:
    return False





