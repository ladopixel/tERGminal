def borraLaPantalla():
    return '\033[2J\033[1;1f'

def escribirNegro(texto):
    return '\033[1;30m' + texto + '\033[0;m'

def escribirRojo(texto):
    return '\033[1;31m' + texto + '\033[0;m'
def escribirRojoOpacidad(texto):
    return '\033[2;31m' + texto + '\033[0;m'

def escribirVerde(texto):
    return '\033[1;32m' + texto + '\033[0;m'
def escribirVerdeOpacidad(texto):
    return '\033[2;32m' + texto + '\033[0;m'

def escribirAmarillo(texto):
    return '\033[1;33m' + texto + '\033[0;m'
def escribirAmarilloOpacidad(texto):
    return '\033[2;33m' + texto + '\033[0;m'

def escribirAzul(texto):
    return '\033[1;34m' + texto + '\033[0;m'
def escribirAzulOpacidad(texto):
    return '\033[2;34m' + texto + '\033[0;m'

def escribirMorado(texto):
    return '\033[1;35m' + texto + '\033[0;m'
def escribirMoradoOpacidad(texto):
    return '\033[2;35m' + texto + '\033[0;m'

def escribirCian(texto):
    return '\033[1;36m' + texto + '\033[0;m'
def escribirCianOpacidad(texto):
    return '\033[2;36m' + texto + '\033[0;m'

def escribirBlanco(texto):
    return '\033[1;37m' + texto + '\033[0;m'
def escribirBlancoOpacidad(texto):
    return '\033[2;37m' + texto + '\033[0;m'

def finColor():
    return '\033[0;m'

def cargoCabecera():
    print(borraLaPantalla())
    print(escribirAmarilloOpacidad('┌──────────────────────────────────────────────────┐'))
    print(escribirAmarilloOpacidad('│                                                  │'))
    print(escribirAmarilloOpacidad('│') + escribirCianOpacidad('    ▓▓▓▓▓▓▓▓▓') + escribirAmarilloOpacidad('                                     │'))
    print(escribirAmarilloOpacidad('│') + escribirCianOpacidad('    ▓▓') + escribirAmarilloOpacidad('                                            │'))
    print(escribirAmarilloOpacidad('│') + escribirCianOpacidad('      ▓▓') + escribirAmarilloOpacidad('                                          │'))
    print(escribirAmarilloOpacidad('│') + escribirCianOpacidad('        ▓▓') + escribirAmarilloOpacidad('                                        │'))
    print(escribirAmarilloOpacidad('│') + escribirCianOpacidad('      ▓▓') + escribirAmarilloOpacidad('                                          │'))
    print(escribirAmarilloOpacidad('│') + escribirCianOpacidad('    ▓▓') + escribirBlancoOpacidad('        Playing with python + blockchain') + escribirAmarilloOpacidad('    │'))
    print(escribirAmarilloOpacidad('│') + escribirCianOpacidad('    ▓▓▓▓▓▓▓▓▓') + escribirBlanco(' ERGOPLATFORM.ORG') + escribirAmarilloOpacidad('                    │'))
    print(escribirAmarilloOpacidad('│                                                  │'))
    print(escribirAmarilloOpacidad('└──────────────────────────────────────────────────┘'))

def cargoMenu(wallet):
    print(escribirAmarilloOpacidad('┌──────────────────────────────────────────────────┐'))
    print(escribirAmarilloOpacidad('│                                                  │'))
    print(escribirAmarilloOpacidad('│') + escribirCian('    tERGminal') + escribirAmarilloOpacidad('                                     │'))
    print(escribirAmarilloOpacidad('│                                                  │'))
    if wallet == 1:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('1') + escribirAmarillo('   Configure wallet.                         ') + escribirAmarilloOpacidad('│'))
    else:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('1') + escribirAmarilloOpacidad('   Configure wallet.                         │'))
    if wallet == 2:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('2') + escribirAmarillo('   Send ERG to a wallet.                     ') + escribirAmarilloOpacidad('│'))
    else: 
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('2') + escribirAmarilloOpacidad('   Send ERG to a wallet.                     │'))
    if wallet == 3:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('3') + escribirAmarillo('   Send ERG to a random wallet.              ') + escribirAmarilloOpacidad('│'))
    else:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('3') + escribirAmarilloOpacidad('   Send ERG to a random wallet.              │'))
    if wallet == 4:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('4') + escribirAmarillo('   Send NFT to wallet.                       ') + escribirAmarilloOpacidad('│'))
    else:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('4') + escribirAmarilloOpacidad('   Send NFT to wallet.                       │'))
    if wallet == 5:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('5') + escribirAmarillo('   Send NFT to a random wallet.              ') + escribirAmarilloOpacidad('│'))
    else:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('5') + escribirAmarilloOpacidad('   Send NFT to a random wallet.              │'))
    if wallet == 6:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('6') + escribirAmarillo('   Send NFT random to a wallet.              ') + escribirAmarilloOpacidad('│'))
    else:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('6') + escribirAmarilloOpacidad('   Send NFT random to a wallet.              │'))
    if wallet == 7:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('7') + escribirAmarillo('   Create token.                             ') + escribirAmarilloOpacidad('│'))
    else:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('7') + escribirAmarilloOpacidad('   Create token.                             │'))
    if wallet == 8:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('8') + escribirAmarillo('   Create NFT.                               ') + escribirAmarilloOpacidad('│'))
    else:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('8') + escribirAmarilloOpacidad('   Create NFT.                               │'))
    if wallet == 9:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('9') + escribirAmarillo('   Info Ergo.                                ') + escribirAmarilloOpacidad('│'))
    else:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('9') + escribirAmarilloOpacidad('   Info Ergo.                                │'))
    if wallet == 10:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('10') + escribirAmarillo('  Info Wallet.                              ') + escribirAmarilloOpacidad('│'))
    else:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('10') + escribirAmarilloOpacidad('  Info Wallet.                              │'))
    if wallet == 11:
         print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('11') + escribirAmarillo('  Info Token.                               ') + escribirAmarilloOpacidad('│'))
    else:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('11') + escribirAmarilloOpacidad('  Info Token.                               │'))
    if wallet == 12:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('12') + escribirAmarillo('  Info Transaction.                         ') + escribirAmarilloOpacidad('│'))
    else:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('12') + escribirAmarilloOpacidad('  Info Transaction.                         │'))
    if wallet == 13:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('13') + escribirAmarillo('  Send tokens to multiple addresses.        ') + escribirAmarilloOpacidad('│'))
    else:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('13') + escribirAmarilloOpacidad('  Send tokens to multiple addresses.        │'))
    if wallet == 14:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('14') + escribirAmarillo('  Send multiple tokens to addresses.        ') + escribirAmarilloOpacidad('│'))
    else:
        print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('14') + escribirAmarilloOpacidad('  Send multiple tokens to addresses.        │'))
    
    print(escribirAmarilloOpacidad('│    ') + escribirAmarillo('0') + escribirAmarilloOpacidad('  Exit.                                      │'))
    print(escribirAmarilloOpacidad('│                                                  │'))
    print(escribirAmarilloOpacidad('└──────────────────────────────────────────────────┘'))
    print(' ')