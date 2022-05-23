import random
from platform import node
from ergpy import helperMethods, appkit
import colorsPython
import whiteList
import requests

ergo = appkit.ErgoAppKit(nodeURL = 'http://159.65.11.55:9053/')
walletMnemonic = ''

# 1 - Config wallet
def configWallet():
    global walletMnemonic
    inputSemilla = input(colorsPython.escribirAmarillo('→ → Enter seed pharse: '))
    walletMnemonic = inputSemilla
    print(colorsPython.borraLaPantalla())
    colorsPython.cargoCabecera()
    colorsPython.cargoMenu(0)
    print(colorsPython.escribirVerde('wallet ok!'))

# 2 - Send ERG
def sendErg():
    inputSendErg = float(input(colorsPython.escribirAmarillo('→ → Enter amount to send: ')))
    inputSendErgWallet = input(colorsPython.escribirAmarillo('→ → Enter wallet to send: '))
    amount = [inputSendErg]
    receiverAddresses = [inputSendErgWallet]
    try:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirVerde('Transaction ↓') + '\033[2;32m')
        print(helperMethods.simpleSend(ergo=ergo, amount=amount, walletMnemonic=walletMnemonic, receiverAddresses=receiverAddresses))
        print(colorsPython.escribirVerde('Send OK ↓'))
        print(colorsPython.escribirVerdeOpacidad('Send ' + str(amount) + ' ERG to the wallet ' + str(inputSendErgWallet)))
    except:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('ERROR Transaction!'))

# 3 - Send ERG random
def sendErgRandom():
    inputSendErg = float(input(colorsPython.escribirAmarillo('→ → Enter amount to send: ')))
    arrayWallets = whiteList.getWhiteList()
    winner = random.randint(0, len(arrayWallets)-1)
    ganador = arrayWallets[winner]
    receiverAddresses = [ganador]
    amount = [inputSendErg]
    try:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirVerde('Wallet winner ↓'))
        print(colorsPython.escribirVerdeOpacidad(ganador))
        print(colorsPython.escribirVerde('Transaction ↓') + '\033[2;32m')
        print(helperMethods.simpleSend(ergo=ergo, amount=amount, walletMnemonic=walletMnemonic, receiverAddresses=receiverAddresses))
        print(colorsPython.escribirVerde('Send OK ↓'))
        print(colorsPython.escribirVerdeOpacidad('Send ' + str(amount) + ' ERG to the wallet ' + str(ganador)))
    except:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('ERROR Transaction!'))

# 4 - Send NFT wallet
def sendNftWallet():
    print(colorsPython.escribirVerdeOpacidad('With your NFT the amount of 0.01 ERG + fee will be sent.'))
    inputNftId = input(colorsPython.escribirAmarillo('→ → Enter NFT Id to send: '))
    inputSendErgWallet = input(colorsPython.escribirAmarillo('→ → Enter wallet to send: '))
    amount = [0.01]
    receiverAddresses = [inputSendErgWallet]
    tokenParaEnviar = [inputNftId]
    tokens = [tokenParaEnviar]
    try:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirVerde('Transaction ↓') + '\033[2;32m')
        print(helperMethods.sendToken(ergo=ergo, amount=amount, receiverAddresses=receiverAddresses, tokens=tokens, walletMnemonic=walletMnemonic))
        print('\033[2;32m' + colorsPython.escribirVerde('Send OK ↓'))
        print(colorsPython.escribirVerdeOpacidad('Send NFT with ID ' + str(inputNftId) + ' to the wallet ' + str(inputSendErgWallet)))
    except:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('ERROR Transaction!'))

# 9 - Info Ergo
def infoErgo():
    URLHeight = 'https://api.ergoplatform.com/api/v1/networkState'
    URLprecio = 'https://api.nanopool.org/v1/ergo/prices'
    URLHashRate = 'https://api.ergoplatform.com/api/v0/info'

    data = requests.get(URLHeight) 
    data = data.json()
    altura = str(data['height'])

    dataprecio = requests.get(URLprecio)
    dataprecio = dataprecio.json()
    precioEUR = str(dataprecio['data']['price_eur'])
    precioUSD = str(dataprecio['data']['price_usd'])
    precioBTC = str(dataprecio['data']['price_btc'])

    dataHashRate = requests.get(URLHashRate) 
    dataHashRate = dataHashRate.json()
    hashRate = str('{0:.2f}'.format(dataHashRate['hashRate']/1000000000000))
    supply = str('{0:.0f}'.format(dataHashRate['supply']/1000000000))

    try:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirVerde('Info Ergo ↓'))
        print(colorsPython.escribirVerdeOpacidad('Height: ' + altura))
        print(colorsPython.escribirVerdeOpacidad('Supply: ' + supply + ' → 97739924 ERG' ))
        print(colorsPython.escribirVerdeOpacidad('Price: ' + precioEUR + '€ → ' +  precioUSD + '$ → ' + precioBTC + '₿'))
        print(colorsPython.escribirVerdeOpacidad('Hashrate: ' + hashRate + 'TH/s'))
    except:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('ERROR Info!'))

# 10 - Info Wallet
def infoWallet():
    inputInfoWallet = input(colorsPython.escribirAmarillo('→ → Enter wallet address: '))
    if requests.get('https://api.ergoplatform.com/api/v1/addresses/' + inputInfoWallet + '/balance/confirmed').status_code == 200:
        dataWallet = requests.get('https://api.ergoplatform.com/api/v1/addresses/' + inputInfoWallet + '/balance/confirmed')
        dataWallet = dataWallet.json()
        totalWallet = str(dataWallet['nanoErgs']/1000000000)
        totalTokens = str(len(dataWallet['tokens']))
        try:
            print(colorsPython.borraLaPantalla())
            colorsPython.cargoCabecera()
            colorsPython.cargoMenu(0)
            print(colorsPython.escribirVerde('Info Wallet ↓'))
            print(colorsPython.escribirVerdeOpacidad('Total ERG: ' + str(totalWallet)))
            print(colorsPython.escribirVerdeOpacidad('Total tokens: ' + str(totalTokens)))
        except:
            print(colorsPython.borraLaPantalla())
            colorsPython.cargoCabecera()
            colorsPython.cargoMenu(0)
            print(colorsPython.escribirRojo('ERROR Wallet!'))
    else:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('ERROR Wallet incorrect!'))

# Menu
colorsPython.cargoCabecera()
colorsPython.cargoMenu(0)

def elegirOpciones(opcion):
    if opcion == 1:
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(1)
        configWallet()
    elif opcion == 2:
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(2)
        sendErg()
    elif opcion == 3:
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(3)
        sendErgRandom()
    elif opcion == 4:
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(4)
        sendNftWallet()
    elif opcion == 9:
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(9)
        infoErgo()
    elif opcion == 10:
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(10)
        infoWallet()
    elif opcion == 12:
        print(' ')
        print('Bye!')
        print(' ')
        exit()

while True:
    opcionInput = int(input('\033[0;m' + colorsPython.escribirAmarillo('→ Enter option: ')))
    elegirOpciones(opcionInput)