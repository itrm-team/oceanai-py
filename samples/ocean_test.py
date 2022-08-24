from src.ocean.occean import Occean



""" from eth_account.account import Account
account1 = Account.create()
print(f"New address: {account1.address}")
print(f"New private key: {account1.key.hex()}")
account2 = Account.create()
print(f"New address: {account2.address}")
print(f"New private key: {account2.key.hex()}")
 """

d = {
   'network_name' : 'rinkeby',
   'network' : 'https://rinkeby.infura.io/v3/proyectid',
   'metadataCacheUri' : 'https://v4.aquarius.oceanprotocol.com',
   'providerUri' : 'https://v4.provider.rinkeby.oceanprotocol.com',
} 


occean = Occean(d,"0xc5f607efd7436bc85dcf21d13721972dabd187c49e1b0282ca71ed0da4dda793","0xf12c2b11f01e7655cba2a08342a4d9bc4ad853b66fbdbd82052717b0fa77843b")

data_nft = occean.publishNFTToken('NFTToken1', 'NFT1')
##occean.createDatasetExmple()
datatoken = occean.createDataToken(data_nft,2)
#datatoken = occean.getDatatoken('0xB8B7B54c3d8C63c316aF8FF4Dea6075b1042A292')
exange_id = occean.getExchangeId(datatoken,1,3)
tx_result = occean.buy(datatoken,exange_id,1,2)