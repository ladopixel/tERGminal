import random
from platform import node
from ergpy import helperMethods, appkit
import colorsPython
import whiteList
import requests

ergo = appkit.ErgoAppKit(nodeURL = 'http://159.65.11.55:9053/')
walletMnemonic = ''

# Varias funciones para datos
def toUtf8String(hex):
    valorUTF8 = '' 
    aux = ''
    contador = 0
    for i in hex:
        contador = contador + 1
        if contador < 3:
            aux = aux + i
        if contador == 2:
            valorUTF8 = valorUTF8 + str(chr(int(aux, 16)))
            contador = 0
            aux = ''
    return valorUTF8

def resolveIpfs(url):
    ipfsPrefix = 'ipfs://'
    if url[0:7:1] != ipfsPrefix:
        return url
    else:
        print(url.replace(ipfsPrefix, 'https://cloudflare-ipfs.com/ipfs/'))
        return url.replace(ipfsPrefix, 'https://cloudflare-ipfs.com/ipfs/')

def resolveIpfsAudio(urls):
    ipfsPrefix = 'ipfs://'
    posicion = urls.find('B')
    if urls[0:7:1] != ipfsPrefix:
        return urls
    else:
        url1 = urls[0:posicion:1]
        url1 = url1.replace(ipfsPrefix, 'https://cloudflare-ipfs.com/ipfs/')
        print(url1.replace(ipfsPrefix, 'https://cloudflare-ipfs.com/ipfs/'))
    return str(url1)

def resolveIpfsAudio2(urls):
    ipfsPrefix = 'ipfs://'
    posicion = urls.find('B')
    if urls[0:7:1] != ipfsPrefix:
        return urls
    else:
        url2 = urls[posicion+1:]
        url2 = url2.replace(ipfsPrefix, 'https://cloudflare-ipfs.com/ipfs/')
        print(url2.replace(ipfsPrefix, 'https://cloudflare-ipfs.com/ipfs/'))
    return str(url2)

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

# 5 - Send NFT random wallet
def sendNftRandomWallet():
    print(colorsPython.escribirVerdeOpacidad('With your NFT the amount of 0.01 ERG + fee will be sent.'))
    inputNftId = input(colorsPython.escribirAmarillo('→ → Enter NFT Id to send: '))
    arrayWallets = whiteList.getWhiteList()
    winner = random.randint(0, len(arrayWallets)-1)
    ganador = arrayWallets[winner]
    receiverAddresses = [ganador]
    tokenParaEnviar = [inputNftId]
    tokens = [tokenParaEnviar]
    amount = [0.01]
    try:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirVerde('Wallet winner ↓'))
        print(colorsPython.escribirVerdeOpacidad(ganador))
        print(colorsPython.escribirVerde('Transaction ↓') + '\033[2;32m')
        print(helperMethods.sendToken(ergo=ergo, amount=amount, receiverAddresses=receiverAddresses, tokens=tokens, walletMnemonic=walletMnemonic))
        print('\033[2;32m' + colorsPython.escribirVerde('Send OK ↓'))
        print(colorsPython.escribirVerdeOpacidad('Send NFT with ID ' + str(inputNftId) + ' to the wallet ' + str(ganador)))
    except:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('ERROR Transaction!'))

# 6 - Send NFT random to a wallet
def sendRandomNftWallet():
    print(colorsPython.escribirVerdeOpacidad('With your NFT the amount of 0.01 ERG + fee will be sent.'))
    inputInfoWallet = input(colorsPython.escribirAmarillo('→ → Enter you wallet address: '))
    
    if requests.get('https://api.ergoplatform.com/api/v1/addresses/' + inputInfoWallet + '/balance/confirmed').status_code == 200:
        dataWallet = requests.get('https://api.ergoplatform.com/api/v1/addresses/' + inputInfoWallet + '/balance/confirmed')
        dataWallet = dataWallet.json()
        arrayTokens = dataWallet['tokens']
        winnerToken = random.randint(0, len(arrayTokens)-1)
        ganadorToken = arrayTokens[winnerToken]['tokenId']
        tokens = [ganadorToken]
        tokensParaEnviar = [tokens]
        amount = [0.01]

        print(colorsPython.escribirAmarillo('→ → → Token List ↓'))
        
        for token in arrayTokens:
            if token['tokenId'] != ganadorToken:
                print('      ' + colorsPython.escribirAmarilloOpacidad(token['name']) + colorsPython.escribirAmarillo(' → ') + colorsPython.escribirAmarilloOpacidad(token['tokenId']))
            else:
                print('      ' + colorsPython.escribirVerde(token['name']) + colorsPython.escribirVerde(' → ') + colorsPython.escribirVerdeOpacidad(token['tokenId']))
        inputSendWallet = input(colorsPython.escribirAmarillo('→ → Enter wallet address to send token ' + colorsPython.escribirAmarilloOpacidad(ganadorToken) + ': '))
        receiverAddresses = [inputSendWallet]
        if requests.get('https://api.ergoplatform.com/api/v1/addresses/' + inputInfoWallet + '/balance/confirmed').status_code == 200:    
            try:
                print(colorsPython.escribirVerde('Transaction ↓') + '\033[2;32m')
                print(helperMethods.sendToken(ergo=ergo, amount=amount, receiverAddresses=receiverAddresses, tokens=tokensParaEnviar, walletMnemonic=walletMnemonic))
                print('\033[2;32m' + colorsPython.escribirVerde('Send OK ↓'))
                print(colorsPython.escribirVerdeOpacidad('Send NFT with ID ' + str(tokens) + ' to the wallet ' + str(receiverAddresses)))
            except:
                print(colorsPython.borraLaPantalla())
                colorsPython.cargoCabecera()
                colorsPython.cargoMenu(0)
                print(colorsPython.escribirRojo('ERROR Transaction!'))
        else:
            print(colorsPython.borraLaPantalla())
            colorsPython.cargoCabecera()
            colorsPython.cargoMenu(0)
            print(colorsPython.escribirRojo('ERROR Wallet incorrect!'))
    else:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('ERROR Wallet incorrect!'))  

# 7 - Create token
def createToken():
    print(colorsPython.escribirVerdeOpacidad('Creating the token the amount 0.001 ERG of fee will be sent.'))
    inputName = input(colorsPython.escribirAmarillo('→ → Enter token name: '))
    inputDescription = input(colorsPython.escribirAmarillo('→ → Enter token description: '))
    inputAmount = int(input(colorsPython.escribirAmarillo('→ → Enter token amount: ')))
    inputDecimals = int(input(colorsPython.escribirAmarillo('→ → Enter token decimals: ')))
    validoCreacion = input(colorsPython.escribirAmarillo('You are about to create a token on the Ergo blockchain, review the data. Are they correct? (Y/n): '))
    if validoCreacion == 'Y':
        try:
            print(colorsPython.escribirVerde('Transaction ↓') + '\033[2;32m')
            print(helperMethods.createToken(ergo=ergo, tokenName=inputName, description=inputDescription, tokenAmount=inputAmount, tokenDecimals=inputDecimals, walletMnemonic=walletMnemonic))
            print('\033[2;32m' + colorsPython.escribirVerde('Token created correctly ↓'))
            print(colorsPython.escribirVerdeOpacidad('Name: ') + colorsPython.escribirVerdeOpacidad(str(inputName)))
            print(colorsPython.escribirVerdeOpacidad('Description: ') + colorsPython.escribirVerdeOpacidad(str(inputDescription)))
            print(colorsPython.escribirVerdeOpacidad('Amount: ') + colorsPython.escribirVerdeOpacidad(str(inputAmount)))
            print(colorsPython.escribirVerdeOpacidad('Decimals: ') + colorsPython.escribirVerdeOpacidad(str(inputDecimals)))
        except:
            print(colorsPython.borraLaPantalla())
            colorsPython.cargoCabecera()
            colorsPython.cargoMenu(0)
            print(colorsPython.escribirRojo('ERROR creating token!'))
    else:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(7)
        createToken()

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

# 11 - Info Token
def infoToken():
    inputidToken = input(colorsPython.escribirAmarillo('→ → Enter token Id: '))
    if requests.get('https://api.ergoplatform.com/api/v0/assets/' + inputidToken + '/issuingBox').status_code == 200:
        dataToken = requests.get('https://api.ergoplatform.com/api/v0/assets/' + inputidToken + '/issuingBox')
        dataToken = dataToken.json()
        nameToken = str(dataToken[0]['assets'][0]['name'])
        amountToken = str(dataToken[0]['assets'][0]['amount'])
        descriptionToken = toUtf8String(dataToken[0]['additionalRegisters']['R5'])[2:]
        
        # Detect NFT
        try:
            tokenNFT = dataToken[0]['additionalRegisters']['R7']
        except:
            tokenNFT = ''

        # Detect NFT type
        if tokenNFT == '0e020101':
            try:
                urlArchivo = resolveIpfs(toUtf8String(dataToken[0]['additionalRegisters']['R9'])[2:])
            except:
                urlArchivo = 'No URL available in R9'
        elif tokenNFT == '0e020102':
            url1ArchivoAudio = resolveIpfsAudio(toUtf8String(dataToken[0]['additionalRegisters']['R9'])[4:])
            url2ArchivoAudio = resolveIpfsAudio2(toUtf8String(dataToken[0]['additionalRegisters']['R9'])[4:])
        elif tokenNFT == '0e020103':
            urlArchivo = resolveIpfs(toUtf8String(dataToken[0]['additionalRegisters']['R9'])[2:])
        else:
            urlArchivo = 'No NFT'
            print('No NFT')
        
        # Muestro datos
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirVerde('Token Info ↓'))
        print(colorsPython.escribirVerdeOpacidad('Id token: ' + inputidToken))
        print(colorsPython.escribirVerdeOpacidad('Name: ' + nameToken))
        print(colorsPython.escribirVerdeOpacidad('Description: ' + descriptionToken))
        print(colorsPython.escribirVerdeOpacidad('Amount: ' + amountToken))
        
        if tokenNFT == '0e020102':
            print(colorsPython.escribirVerdeOpacidad('URL-1: ' + url1ArchivoAudio))    
            print(colorsPython.escribirVerdeOpacidad('URL-2: ' + url2ArchivoAudio))
        else: 
            print(colorsPython.escribirVerdeOpacidad('URL: ' + urlArchivo))


    else:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('ERROR Id token incorrect!'))


def elegirOpciones(opcion):
    if opcion == '1':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(1)
        configWallet()
    elif opcion == '2':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(2)
        sendErg()
    elif opcion == '3':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(3)
        sendErgRandom()
    elif opcion == '4':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(4)
        sendNftWallet()
    elif opcion == '5':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(5)
        sendNftRandomWallet()
    elif opcion == '6':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(6)
        sendRandomNftWallet()
    elif opcion == '7':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(7)
        createToken()
    elif opcion == '9':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(9)
        infoErgo()
    elif opcion == '10':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(10)
        infoWallet()
    elif opcion == '11':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(11)
        infoToken()
    elif opcion == '12':
        print(' ')
        print('Bye!')
        print(' ')
        exit()
    else:
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('Sorry, that option is incorrect!'))
        print(colorsPython.escribirVerdeOpacidad('Select option (1-12)'))
        

# Menu
colorsPython.cargoCabecera()
colorsPython.cargoMenu(0)
while True:
    opcionInput = input('\033[0;m' + colorsPython.escribirAmarillo('→ Enter option: '))
    elegirOpciones(opcionInput)