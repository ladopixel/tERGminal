import random
import os
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

if os.name == 'posix':
    os.system ('clear')
elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
    os.system ('cls')


# Varias funciones para datos
def to_utf8_string(hex):
    valor_utf8 = '' 
    aux = ''
    contador = 0
    for i in hex:
        contador = contador + 1
        if contador < 3:
            aux = aux + i
        if contador == 2:
            valor_utf8 = valor_utf8 + str(chr(int(aux, 16)))
            contador = 0
            aux = ''
    return valor_utf8

def resolve_ipfs(url):
    ipfs_prefix = 'ipfs://'
    if url[0:7:1] != ipfs_prefix:
        return url
    else:
        print(url.replace(ipfs_prefix, 'https://cloudflare-ipfs.com/ipfs/'))
        return url.replace(ipfs_prefix, 'https://cloudflare-ipfs.com/ipfs/')

def resolve_ipfs_audio(urls):
    ipfs_prefix = 'ipfs://'
    posicion = urls.find('B')
    if urls[0:7:1] != ipfs_prefix:
        return urls
    else:
        url1 = urls[0:posicion:1]
        url1 = url1.replace(ipfs_prefix, 'https://cloudflare-ipfs.com/ipfs/')
        print(url1.replace(ipfs_prefix, 'https://cloudflare-ipfs.com/ipfs/'))
    return str(url1)

def resolve_ipfs_audio2(urls):
    ipfs_prefix = 'ipfs://'
    posicion = urls.find('B')
    if urls[0:7:1] != ipfs_prefix:
        return urls
    else:
        url2 = urls[posicion+1:]
        url2 = url2.replace(ipfs_prefix, 'https://cloudflare-ipfs.com/ipfs/')
        print(url2.replace(ipfs_prefix, 'https://cloudflare-ipfs.com/ipfs/'))
    return str(url2)

# 1 - Config wallet
def config_wallet():
    global wallet_mnemonic
    input_semilla = input(colorsPython.escribirAmarillo('→ → Enter seed phrase: '))
    wallet_mnemonic = input_semilla
    print(colorsPython.borraLaPantalla())
    colorsPython.cargoCabecera()
    colorsPython.cargoMenu(0)
    print(colorsPython.escribirVerde('wallet ok!'))

# 2 - Send ERG
def send_erg():
    input_send_erg = float(input(colorsPython.escribirAmarillo('→ → Enter amount to send: ')))
    input_send_erg_wallet = input(colorsPython.escribirAmarillo('→ → Enter wallet to send: '))
    amount = [input_send_erg]
    receiver_addresses = [input_send_erg_wallet]
    try:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirVerde('Transaction ↓') + '\033[2;32m')
        print(helper_functions.simple_send(ergo=ergo, amount=amount, wallet_mnemonic=wallet_mnemonic, receiver_addresses=receiver_addresses))
        print(colorsPython.escribirVerde('Send OK ↓'))
        print(colorsPython.escribirVerdeOpacidad('Send ' + str(amount) + ' ERG to the wallet ' + str(input_send_erg_wallet)))
    except:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('ERROR Transaction!'))

# 3 - Send ERG random
def send_erg_random():
    input_send_erg = float(input(colorsPython.escribirAmarillo('→ → Enter amount to send: ')))
    array_wallets = whiteList.getWhiteList()
    winner = random.randint(0, len(array_wallets)-1)
    ganador = array_wallets[winner]
    receiver_addresses = [ganador]
    amount = [input_send_erg]
    try:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirVerde('Wallet winner ↓'))
        print(colorsPython.escribirVerdeOpacidad(ganador))
        print(colorsPython.escribirVerde('Transaction ↓') + '\033[2;32m')
        print(helper_functions.simple_send(ergo=ergo, amount=amount, wallet_mnemonic=wallet_mnemonic, receiver_addresses=receiver_addresses))
        print(colorsPython.escribirVerde('Send OK ↓'))
        print(colorsPython.escribirVerdeOpacidad('Send ' + str(amount) + ' ERG to the wallet ' + str(ganador)))
    except:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('ERROR Transaction!'))

# 4 - Send NFT wallet
def send_nft_wallet():
    print(colorsPython.escribirVerdeOpacidad('With your NFT the amount of 0.01 ERG + fee will be sent.'))
    input_nft_id = input(colorsPython.escribirAmarillo('→ → Enter NFT Id to send: '))
    input_send_erg_wallet = input(colorsPython.escribirAmarillo('→ → Enter wallet to send: '))
    amount = [0.01]
    receiver_addresses = [input_send_erg_wallet]
    token_para_enviar = [input_nft_id]
    tokens = [token_para_enviar]
    try:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirVerde('Transaction ↓') + '\033[2;32m')
        print(helper_functions.send_token(ergo=ergo, amount=amount, receiver_addresses=receiver_addresses, tokens=tokens, wallet_mnemonic=wallet_mnemonic))
        print('\033[2;32m' + colorsPython.escribirVerde('Send OK ↓'))
        print(colorsPython.escribirVerdeOpacidad('Send NFT with ID ' + str(input_nft_id) + ' to the wallet ' + str(input_send_erg_wallet)))
    except:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('ERROR Transaction!'))

# 5 - Send NFT random wallet
def send_nft_random_wallet():
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
def send_random_nft_wallet():
    print(colorsPython.escribirVerdeOpacidad('With your NFT the amount of 0.01 ERG + fee will be sent.'))
    input_info_wallet = input(colorsPython.escribirAmarillo('→ → Enter you wallet address: '))
    
    if requests.get('https://api.ergoplatform.com/api/v1/addresses/' + input_info_wallet + '/balance/confirmed').status_code == 200:
        data_Wallet = requests.get('https://api.ergoplatform.com/api/v1/addresses/' + input_info_wallet + '/balance/confirmed')
        data_Wallet = data_Wallet.json()
        array_tokens = data_Wallet['tokens']
        winner_token = random.randint(0, len(array_tokens)-1)
        ganador_token = array_tokens[winner_token]['tokenId']
        tokens = [ganador_token]
        tokens_para_enviar = [tokens]
        amount = [0.01]

        print(colorsPython.escribirAmarillo('→ → → Token List ↓'))
        
        for token in array_tokens:
            if token['tokenId'] != ganador_token:
                print('      ' + colorsPython.escribirAmarilloOpacidad(token['name']) + colorsPython.escribirAmarillo(' → ') + colorsPython.escribirAmarilloOpacidad(token['tokenId']))
            else:
                print('      ' + colorsPython.escribirVerde(token['name']) + colorsPython.escribirVerde(' → ') + colorsPython.escribirVerdeOpacidad(token['tokenId']))
        input_send_wallet = input(colorsPython.escribirAmarillo('→ → Enter wallet address to send token ' + colorsPython.escribirAmarilloOpacidad(ganador_token) + ': '))
        receiver_addresses = [input_send_wallet]
        if requests.get('https://api.ergoplatform.com/api/v1/addresses/' + input_info_wallet + '/balance/confirmed').status_code == 200:    
            try:
                print(colorsPython.escribirVerde('Transaction ↓') + '\033[2;32m')
                print(helper_functions.send_token(ergo=ergo, amount=amount, receiver_addresses=receiver_addresses, tokens=tokens_para_enviar, wallet_mnemonic=wallet_mnemonic))
                print('\033[2;32m' + colorsPython.escribirVerde('Send OK ↓'))
                print(colorsPython.escribirVerdeOpacidad('Send NFT with ID ' + str(tokens) + ' to the wallet ' + str(receiver_addresses)))
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
def create_token():
    print(colorsPython.escribirVerdeOpacidad('Creating the token the amount 0.001 ERG of fee will be sent.'))
    input_name = input(colorsPython.escribirAmarillo('→ → Enter token name: '))
    input_description = input(colorsPython.escribirAmarillo('→ → Enter token description: '))
    input_amount = int(input(colorsPython.escribirAmarillo('→ → Enter token amount: ')))
    input_decimals = int(input(colorsPython.escribirAmarillo('→ → Enter token decimals: ')))
    valido_creacion = input(colorsPython.escribirAmarillo('You are about to create a token on the Ergo blockchain, review the data. Are they correct? (Y/n): '))
    if valido_creacion == 'Y':
        try:
            print(colorsPython.escribirVerde('Transaction ↓') + '\033[2;32m')
            print(helper_functions.create_token(ergo=ergo, token_name=input_name, description=input_description, token_amount=input_amount, token_decimals=input_decimals, wallet_mnemonic=wallet_mnemonic))
            print('\033[2;32m' + colorsPython.escribirVerde('Token created correctly ↓'))
            print(colorsPython.escribirVerdeOpacidad('Name: ') + colorsPython.escribirVerdeOpacidad(str(input_name)))
            print(colorsPython.escribirVerdeOpacidad('Description: ') + colorsPython.escribirVerdeOpacidad(str(input_description)))
            print(colorsPython.escribirVerdeOpacidad('Amount: ') + colorsPython.escribirVerdeOpacidad(str(input_amount)))
            print(colorsPython.escribirVerdeOpacidad('Decimals: ') + colorsPython.escribirVerdeOpacidad(str(input_decimals)))
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
def create_nft():
    print(colorsPython.escribirVerdeOpacidad('Creating the NFT the amount 0.001 ERG of fee will be sent.'))
    input_nft_name = input(colorsPython.escribirAmarillo('→ → Enter NFT name: '))
    nft_name = input_nft_name
    input_description = input(colorsPython.escribirAmarillo('→ → Enter NFT description: '))
    description = input_description
    input_image_link = input(colorsPython.escribirAmarillo('→ → Enter NFT link (IPFS): '))
    image_link = input_image_link
    input_ruta_local_imagen = input(colorsPython.escribirAmarillo('→ → Enter Image local directory path: '))
    imagen = input_ruta_local_imagen
    with open(imagen, 'rb') as f:    
            bytes = f.read()
            hash_local_image = hashlib.sha256(bytes).hexdigest()
            image_hash = appkit.sha256caster(hash_local_image)
    try:
        print(colorsPython.escribirVerde('Transaction ↓') + '\033[2;32m')
        print(helper_functions.create_nft(ergo=ergo, nft_name=nft_name, description=description, image_link=image_link, image_hash=image_hash, wallet_mnemonic=wallet_mnemonic))

        print('\033[2;32m' + colorsPython.escribirVerde('NFT created correctly ↓'))
        print(colorsPython.escribirVerdeOpacidad('Name: ') + colorsPython.escribirVerdeOpacidad(str(nft_name)))
        print(colorsPython.escribirVerdeOpacidad('Description: ') + colorsPython.escribirVerdeOpacidad(str(description)))
        print(colorsPython.escribirVerdeOpacidad('SHA: ') + colorsPython.escribirVerdeOpacidad(str(hash_local_image)))
    except:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('ERROR create NFT!'))

# 9 - Info Ergo
def info_ergo():
    url_height = 'https://api.ergoplatform.com/api/v1/networkState'
    url_precio = 'https://api.nanopool.org/v1/ergo/prices'
    url_hashrate = 'https://api.ergoplatform.com/api/v0/info'

    data = requests.get(url_height) 
    data = data.json()
    altura = str(data['height'])

    data_precio = requests.get(url_precio)
    data_precio = data_precio.json()
    precio_eur = str(data_precio['data']['price_eur'])
    precio_usd = str(data_precio['data']['price_usd'])
    precio_btc = str(data_precio['data']['price_btc'])

    dataHashRate = requests.get(url_hashrate) 
    dataHashRate = dataHashRate.json()
    hashrate = str('{0:.2f}'.format(dataHashRate['hashRate']/1000000000000))
    supply = str('{0:.0f}'.format(dataHashRate['supply']/1000000000))

    try:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirVerde('Info Ergo ↓'))
        print(colorsPython.escribirVerdeOpacidad('Height: ' + altura))
        print(colorsPython.escribirVerdeOpacidad('Supply: ' + supply + ' → 97739924 ERG' ))
        print(colorsPython.escribirVerdeOpacidad('Price: ' + precio_eur + '€ → ' +  precio_usd + '$ → ' + precio_btc + '₿'))
        print(colorsPython.escribirVerdeOpacidad('Hashrate: ' + hashrate + 'TH/s'))
    except:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('ERROR Info!'))

# 10 - Info Wallet
def info_wallet():
    input_info_wallet = input(colorsPython.escribirAmarillo('→ → Enter wallet address: '))
    if requests.get('https://api.ergoplatform.com/api/v1/addresses/' + input_info_wallet + '/balance/confirmed').status_code == 200:
        data_Wallet = requests.get('https://api.ergoplatform.com/api/v1/addresses/' + input_info_wallet + '/balance/confirmed')
        data_Wallet = data_Wallet.json()
        total_wallet = str(data_Wallet['nanoErgs']/1000000000)
        total_tokens = str(len(data_Wallet['tokens']))
        try:
            print(colorsPython.borraLaPantalla())
            colorsPython.cargoCabecera()
            colorsPython.cargoMenu(0)
            print(colorsPython.escribirVerde('Info Wallet ↓'))
            print(colorsPython.escribirVerdeOpacidad('Total ERG: ' + str(total_wallet)))
            print(colorsPython.escribirVerdeOpacidad('Total tokens: ' + str(total_tokens)))
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
def info_token():
    input_id_token = input(colorsPython.escribirAmarillo('→ → Enter token Id: '))
    if requests.get('https://api.ergoplatform.com/api/v0/assets/' + input_id_token + '/issuingBox').status_code == 200:
        data_token = requests.get('https://api.ergoplatform.com/api/v0/assets/' + input_id_token + '/issuingBox')
        data_token = data_token.json()
        name_token = str(data_token[0]['assets'][0]['name'])
        amount_token = str(data_token[0]['assets'][0]['amount'])
        description_token = to_utf8_string(data_token[0]['additionalRegisters']['R5'])[2:]
        
        # Detect NFT
        try:
            token_nft = data_token[0]['additionalRegisters']['R7']
        except:
            token_nft = ''

        # Detect NFT type
        if token_nft == '0e020101':
            try:
                url_archivo = resolve_ipfs(to_utf8_string(data_token[0]['additionalRegisters']['R9'])[2:])
            except:
                url_archivo = 'No URL available in R9'
        elif token_nft == '0e020102':
            url1_archivo_audio = resolve_ipfs_audio(to_utf8_string(data_token[0]['additionalRegisters']['R9'])[4:])
            url2_archivo_audio = resolve_ipfs_audio2(to_utf8_string(data_token[0]['additionalRegisters']['R9'])[4:])
        elif token_nft == '0e020103':
            url_archivo = resolve_ipfs(to_utf8_string(data_token[0]['additionalRegisters']['R9'])[2:])
        else:
            url_archivo = 'No NFT'
            print('No NFT')
        
        # Muestro datos
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirVerde('Token Info ↓'))
        print(colorsPython.escribirVerdeOpacidad('Id token: ' + input_id_token))
        print(colorsPython.escribirVerdeOpacidad('Name: ' + name_token))
        print(colorsPython.escribirVerdeOpacidad('Description: ' + description_token))
        print(colorsPython.escribirVerdeOpacidad('Amount: ' + amount_token))
        
        if token_nft == '0e020102':
            print(colorsPython.escribirVerdeOpacidad('URL-1: ' + url1_archivo_audio))    
            print(colorsPython.escribirVerdeOpacidad('URL-2: ' + url2_archivo_audio))
        else: 
            print(colorsPython.escribirVerdeOpacidad('URL: ' + url_archivo))


    else:
        print(colorsPython.borraLaPantalla())
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(0)
        print(colorsPython.escribirRojo('ERROR Id token incorrect!'))

# 12 Info Transaction example: 3704f28826aff29296965951295fe3aa59eef6aa4442c6ca1fcbdbbe1fc7ecae
def info_transaction():
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
def send_tokens_multiple_address():
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


# 14  Send multiple tokens to addresses.
def send_multiple_tokens_address():
    print(colorsPython.escribirVerde('Working... ') + '\033[2;32m')


def elegir_opciones(opcion):
    if opcion == '1':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(1)
        config_wallet()
    elif opcion == '2':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(2)
        send_erg()
    elif opcion == '3':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(3)
        send_erg_random()
    elif opcion == '4':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(4)
        send_nft_wallet()
    elif opcion == '5':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(5)
        send_nft_random_wallet()
    elif opcion == '6':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(6)
        send_random_nft_wallet()
    elif opcion == '7':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(7)
        create_token()
    elif opcion == '8':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(8)
        create_nft()
    elif opcion == '9':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(9)
        info_ergo()
    elif opcion == '10':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(10)
        info_wallet()
    elif opcion == '11':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(11)
        info_token()
    elif opcion == '12':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(12)
        info_transaction()
    elif opcion == '13':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(13)
        send_tokens_multiple_address()
    elif opcion == '14':
        colorsPython.cargoCabecera()
        colorsPython.cargoMenu(14)
        send_multiple_tokens_address()
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
    opcion_input = input('\033[0;m' + colorsPython.escribirAmarillo('→ Enter option: '))
    elegir_opciones(opcion_input)