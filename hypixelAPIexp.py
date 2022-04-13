import requests
key = "22991bff-bcb9-4624-aa50-1145fc6130d2"
cute_name = "Lime"
data = requests.get(
    url="https://api.hypixel.net/key",
    params={
        "key": key,
    }
).json()

# print("uuid:",data["record"]["owner"])
uuid = data["record"]["owner"]

# https://api.hypixel.net/player?key=[yourApiKey]&uuid=[theirUUID]
data = requests.get(
    "https://api.hypixel.net/player?key={}&uuid={}".format(key, uuid)).json()
# print(data["player"]["stats"]["SkyBlock"]["profiles"])

profiles = data["player"]["stats"]["SkyBlock"]["profiles"]

for p in profiles:
    if profiles[p]["cute_name"] == cute_name:
        profile_id = profiles[p]["profile_id"]

# print("profile_id:",profile_id)

data = requests.get(
    "https://api.hypixel.net/skyblock/profile?key={}&profile={}".format(key, profile_id)).json()

# print(data)
for i in data["profile"]["members"]:
    member_id = i
    break


purse = data["profile"]["members"][member_id]["coin_purse"]
print("purse:", purse)

data = requests.get(
    url="https://api.hypixel.net/skyblock/bazaar",
    params={
        "key": "22991bff-bcb9-4624-aa50-1145fc6130d2",
    }
).json()

enchanted_lapis_buy_price = data["products"]["ENCHANTED_LAPIS_LAZULI"]["sell_summary"][0]["pricePerUnit"]+0.1
enchanted_lapis_block_buy_price = data["products"][
    "ENCHANTED_LAPIS_LAZULI_BLOCK"]["sell_summary"][0]["pricePerUnit"]+0.1
sand_buy_price = data["products"]["SAND"]["sell_summary"][0]["pricePerUnit"]+0.1
handmake_TITANIC_EXP_BOTTLE_buy_price_1 = enchanted_lapis_buy_price * \
    960 + sand_buy_price*1
handmake_TITANIC_EXP_BOTTLE_buy_price_2 = enchanted_lapis_block_buy_price * \
    6 + sand_buy_price*1
TITANIC_EXP_BOTTLE_buy_price = data["products"]["TITANIC_EXP_BOTTLE"]["sell_summary"][0]["pricePerUnit"]
TITANIC_EXP_BOTTLE_sell_price = data["products"]["TITANIC_EXP_BOTTLE"]["buy_summary"][0]["pricePerUnit"]


if handmake_TITANIC_EXP_BOTTLE_buy_price_1 < TITANIC_EXP_BOTTLE_buy_price:
    amount = int(purse/handmake_TITANIC_EXP_BOTTLE_buy_price_1)
    profit = (TITANIC_EXP_BOTTLE_sell_price -
              handmake_TITANIC_EXP_BOTTLE_buy_price_1)*amount
    ENCHANTED_LAPIS_need = amount*960
    sand_need = amount*1
    print("amount: ", amount)
    print("sand_need: ", sand_need)
    print("ENCHANTED_LAPIS_need: ", ENCHANTED_LAPIS_need)
    print("profit: ", profit)

elif handmake_TITANIC_EXP_BOTTLE_buy_price_2 < TITANIC_EXP_BOTTLE_buy_price:
    amount = int(purse/handmake_TITANIC_EXP_BOTTLE_buy_price_2)
    profit = (TITANIC_EXP_BOTTLE_sell_price -
              handmake_TITANIC_EXP_BOTTLE_buy_price_2)*amount
    ENCHANTED_LAPIS_block_need = amount*6
    sand_need = amount*1
    print("amount: ", amount)
    print("sand_need: ", sand_need)
    print("ENCHANTED_LAPIS_block_need: ", ENCHANTED_LAPIS_block_need)
    print("profit: ", profit)

elif TITANIC_EXP_BOTTLE_buy_price < TITANIC_EXP_BOTTLE_sell_price:
    amount = int(purse/TITANIC_EXP_BOTTLE_buy_price)
    profit = (TITANIC_EXP_BOTTLE_sell_price -
              TITANIC_EXP_BOTTLE_buy_price)*amount
    print("amount: ", amount)
    print("profit: ", profit)
else:
    print("not good")
