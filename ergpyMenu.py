import random
from platform import node
from ergpy import helper_functions, appkit
import colorsPython
import whiteList
import requests
import hashlib
from datetime import datetime

node_url: str = "http://159.65.11.55:9053/" 
ergo = appkit.ErgoAppKit(node_url=node_url)

wallet_mnemonic = ''

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
    global wallet_mnemonic
    inputSemilla = input(colorsPython.escribirAmarillo('→ → Enter seed phrase: '))
    wallet_mnemonic = inputSemilla
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
        print(helper_functions.simple_send(ergo=ergo, amount=amount, wallet_mnemonic=wallet_mnemonic, receiver_addresses=receiverAddresses))
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
        print(helper_functions.simple_send(ergo=ergo, amount=amount, wallet_mnemonic=wallet_mnemonic, receiver_addresses=receiverAddresses))
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
        print(helper_functions.send_token(ergo=ergo, amount=amount, receiver_addresses=receiverAddresses, tokens=tokens, wallet_mnemonic=wallet_mnemonic))
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
        print(helper_functions.send_token(ergo=ergo, amount=amount, receiver_addresses=receiverAddresses, tokens=tokens, wallet_mnemonic=wallet_mnemonic))
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
                print(helper_functions.send_token(ergo=ergo, amount=amount, receiver_addresses=receiverAddresses, tokens=tokensParaEnviar, wallet_mnemonic=wallet_mnemonic))
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
            print(helper_functions.create_token(ergo=ergo, token_name=inputName, description=inputDescription, token_amount=inputAmount, token_decimals=inputDecimals, wallet_mnemonic=wallet_mnemonic))
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

# 8 - Create NFT
def createNft():
    print(colorsPython.escribirVerdeOpacidad('Creating the NFT the amount 0.001 ERG of fee will be sent.'))
    inputNftName = input(colorsPython.escribirAmarillo('→ → Enter NFT name: '))
    nftName = inputNftName
    inputDescription = input(colorsPython.escribirAmarillo('→ → Enter NFT description: '))
    description = inputDescription
    inputImageLink = input(colorsPython.escribirAmarillo('→ → Enter NFT link (IPFS): '))
    image_link = inputImageLink
    inputRutaLocalImagen = input(colorsPython.escribirAmarillo('→ → Enter Image local directory path: '))
    imagen = inputRutaLocalImagen
    with open(imagen, 'rb') as f:    
            bytes = f.read()
            hashLocalImage = hashlib.sha256(bytes).hexdigest()
            image_hash = appkit.sha256caster(hashLocalImage)
    try:
        print(colorsPython.escribirVerde('Transaction ↓') + '\033[2;32m')
        print(helper_functions.create_nft(ergo=ergo, nft_name=nftName, description=description, image_link=image_link, image_hash=image_hash, wallet_mnemonic=wallet_mnemonic))

        print('\033[2;32m' + colorsPython.escribirVerde('NFT created correctly ↓'))
        print(colorsPython.escribirVerdeOpacidad('Name: ') + colorsPython.escribirVerdeOpacidad(str(nftName)))
        print(colorsPython.escribirVerdeOpacidad('Description: ') + colorsPython.escribirVerdeOpacidad(str(description)))
        print(colorsPython.escribirVerdeOpacidad('SHA: ') + colorsPython.escribirVerdeOpacidad(str(hashLocalImage)))
    except:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('ERROR create NFT!'))

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

# 12 Info Transaction example: 3704f28826aff29296965951295fe3aa59eef6aa4442c6ca1fcbdbbe1fc7ecae
def infoTransaction():
    input_info_transaction = input(colorsPython.escribirAmarillo('→ → Enter transaction id: '))
    if requests.get('https://api.ergoplatform.com/api/v1/transactions/' + input_info_transaction).status_code == 200:
        dato_transaction = requests.get('https://api.ergoplatform.com/api/v1/transactions/' + input_info_transaction)
        dato_transaction = dato_transaction.json()
        try:
            print(colorsPython.borraLaPantalla())
            colorsPython.cargoCabecera()
            colorsPython.cargoMenu(0)
            print(colorsPython.escribirVerde('Info Transaction ↓'))
            print(colorsPython.escribirNegro('Transaction id: ') + colorsPython.escribirVerdeOpacidad(str(dato_transaction['id'])))
            print(colorsPython.escribirNegro('Block id: ') + colorsPython.escribirVerdeOpacidad(str(dato_transaction['blockId'])))
            print(colorsPython.escribirNegro('Inclusion Height: ') + colorsPython.escribirVerdeOpacidad(str(dato_transaction['inclusionHeight'])))
            print(colorsPython.escribirNegro('Confirmations: ') + colorsPython.escribirVerdeOpacidad(str(dato_transaction['numConfirmations'])))
            print(colorsPython.escribirNegro('Index: ') + colorsPython.escribirVerdeOpacidad(str(dato_transaction['index'])))
            print(colorsPython.escribirNegro('Global index: ') + colorsPython.escribirVerdeOpacidad(str(dato_transaction['globalIndex'])))
            # Divide by 1000 to go from js ts to python ts
            ts = dato_transaction['timestamp']/1000
            dt = datetime.fromtimestamp(ts)
            print(colorsPython.escribirNegro('Received Time: ') + colorsPython.escribirVerdeOpacidad(str(dt)))

            size_kB = dato_transaction['size']/1024
            size_kB_round = round(size_kB, 2)
            print(colorsPython.escribirNegro('Size: ') + colorsPython.escribirVerdeOpacidad(str(size_kB_round) + ' kB'))
            
            print(' ')
            print(colorsPython.escribirVerde('Inputs ↓'))
            dato_inputs = dato_transaction['inputs']
            for item_input in dato_inputs:
                print(colorsPython.escribirAmarillo('→ ' + colorsPython.escribirVerdeOpacidad(str(item_input))))
            
            print(' ')
            print(colorsPython.escribirVerde('Data Inputs ↓'))
            item_data_input = dato_transaction['dataInputs']
            for item_data_input in item_data_input:
                print(colorsPython.escribirAmarillo('→ ' + colorsPython.escribirVerdeOpacidad(str(item_data_input))))
                print(' ')
            
            print(' ')
            print(colorsPython.escribirVerde('Outputs ↓'))
            dato_output = dato_transaction['outputs']
            for item_output in dato_output:
                print(colorsPython.escribirAmarillo('→ ' + colorsPython.escribirVerdeOpacidad(str(item_output))))
                print(' ')

        except:
            print(colorsPython.borraLaPantalla())
            colorsPython.cargoCabecera()
            colorsPython.cargoMenu(0)
            print(colorsPython.escribirRojo('ERROR info transaction!'))
    else:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('ERROR transaction id incorrect!'))

# 13  Send tokens to multiple addresses.
def sendTokensMultipleAddress():
    print(colorsPython.escribirVerdeOpacidad('To each address the amount of 0.002 ERG will be added in the sending of the token.'))
    input_nft_id = input(colorsPython.escribirAmarillo('→ → Enter Token Id to send: '))
    receiver_addresses = whiteList.getWhiteList()
    token_para_enviar = []
    amount = []
    
    # To generate ID and amounts for each Wallet
    for i in receiver_addresses:
        token_para_enviar.append([input_nft_id])
        amount.append(0.002)
    
    tokens = token_para_enviar

    total_pagar = 0.002 * len(receiver_addresses)
    price_ok = input(colorsPython.escribirAmarillo('Sending the token to ' + str(len(receiver_addresses)) + ' addresses costs you ' + str(total_pagar) + ' ERG. Are you sure? (Y/n): '))
    if price_ok == 'Y':
        try:
            print(colorsPython.borraLaPantalla())
            colorsPython.cargoCabecera()
            colorsPython.cargoMenu(0)
            print(colorsPython.escribirVerde('Transaction ↓') + '\033[2;32m')
            print(helper_functions.send_token(ergo=ergo, amount=amount, receiver_addresses=receiver_addresses, tokens=tokens, wallet_mnemonic=wallet_mnemonic))
            print('\033[2;32m' + colorsPython.escribirVerde('Send OK ↓'))
            print(colorsPython.escribirVerdeOpacidad('Send NFT with ID ' + str(tokens) + ' to the wallets:'))
            print(colorsPython.escribirVerdeOpacidad(str(receiver_addresses)))
        except:
            print(colorsPython.borraLaPantalla())
            colorsPython.cargoCabecera()
            colorsPython.cargoMenu(0)
            print(colorsPython.escribirRojo('ERROR Transaction!'))
    else:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)

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
    elif opcion == '8':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(8)
        createNft()
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
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(12)
        infoTransaction()
    elif opcion == '13':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(13)
        sendTokensMultipleAddress()
    elif opcion == '0':
        print(' ')
        print('Bye!')
        print(' ')
        exit()
    else:
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('Sorry, that option is incorrect!'))
        print(colorsPython.escribirVerdeOpacidad('Select option (0-12)'))
        

# Menu
colorsPython.cargoCabecera()
colorsPython.cargoMenu(0)
while True:
    opcionInput = input('\033[0;m' + colorsPython.escribirAmarillo('→ Enter option: '))
    elegirOpciones(opcionInput)