import requests
key = "22991bff-bcb9-4624-aa50-1145fc6130d2"
cute_name = "Lime"
# key = "abd7eff3-9023-45a1-88ee-6d77f424601d"
# cute_name = "Cucumber"

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

enchanted_redstone_buy_price = data["products"]["ENCHANTED_REDSTONE"]["sell_summary"][0]["pricePerUnit"]+0.1
handmake_enchanted_redstone_block_buy_price = enchanted_redstone_buy_price*160
enchanted_redstone_block_buy_price = data["products"][
    "ENCHANTED_REDSTONE_BLOCK"]["sell_summary"][0]["pricePerUnit"]
enchanted_redstone_block_sell_price = data["products"][
    "ENCHANTED_REDSTONE_BLOCK"]["buy_summary"][0]["pricePerUnit"]

print("enchanted_redstone_buy_price:", enchanted_redstone_buy_price)
print("handmake_enchanted_redstone_block_buy_price",
      handmake_enchanted_redstone_block_buy_price)
print("enchanted_redstone_block_buy_price", enchanted_redstone_block_buy_price)
print("enchanted_redstone_block_sell_price",
      enchanted_redstone_block_sell_price)

if handmake_enchanted_redstone_block_buy_price < enchanted_redstone_block_sell_price or enchanted_redstone_block_buy_price < enchanted_redstone_block_sell_price:
    if handmake_enchanted_redstone_block_buy_price < enchanted_redstone_block_buy_price:
        amount = int(purse/handmake_enchanted_redstone_block_buy_price)
        profit = (enchanted_redstone_block_sell_price -
                  handmake_enchanted_redstone_block_buy_price)*amount
        enchanted_redstone_need = amount*160
        print("自己買材料做")
        print("amount: ", amount)
        print("enchanted_redstone_need: ", enchanted_redstone_need)
        print("profit: ", profit)
    else:
        amount = int(purse/enchanted_redstone_block_buy_price)
        profit = (enchanted_redstone_block_sell_price -
                  enchanted_redstone_block_buy_price)*amount
        print("直接買")
        print("amount: ", amount)
        print("profit: ", profit)
else:
    print("不要買賣,會虧錢!!")
