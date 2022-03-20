from random import randrange, randint
from time import time


códigos_para_símbolos = {111: '0', 112: '1', 113: '2', 114: '3', 115: '4',
116: '5', 117: '6', 118: '7', 119: '8', 121: '9', 122: '=', 123: '+',
124: '-', 125: '/', 126: '*', 127: 'a', 128: 'b', 129: 'c', 131: 'd',
132: 'e', 133: 'f', 134: 'g', 135: 'h', 136: 'i', 137: 'j', 138: 'k',
139: 'l', 141: 'm', 142: 'n', 143: 'o', 144: 'p', 145: 'q', 146: 'r',
147: 's', 148: 't', 149: 'u', 151: 'v', 152: 'w', 153: 'x', 154: 'y',
155: 'z', 156: 'á', 157: 'à', 158: 'â', 159: 'ã', 161: 'é', 162: 'ê',
163: 'í', 164: 'ó', 165: 'ô', 166: 'õ', 167: 'ú', 168: 'ç', 169: 'A',
171: 'B', 172: 'C', 173: 'D', 174: 'E', 175: 'F', 176: 'G', 177: 'H',
178: 'I', 179: 'J', 181: 'K', 182: 'L', 183: 'M', 184: 'N', 185: 'O',
186: 'P', 187: 'Q', 188: 'R', 189: 'S', 191: 'T', 192: 'U', 193: 'V',
194: 'W', 195: 'X', 196: 'Y', 197: 'Z', 198: 'Á', 199: 'À', 211: 'Â',
212: 'Ã', 213: 'É', 214: 'Ê', 215: 'Í', 216: 'Ó', 217: 'Ô', 218: 'Õ',
219: 'Ú', 221: 'Ç', 222: ',', 223: '.', 224: '!', 225: '?', 226: ';',
227: ':', 228: '_', 229: '(', 231: ')', 232: '"', 233: '#', 234: '$',
235: '%', 236: '@', 237: ' ', 238: '\n'}

símbolos_para_códigos = {'0': 111, '1': 112, '2': 113, '3': 114, '4': 115,
'5': 116, '6': 117, '7': 118, '8': 119, '9': 121, '=': 122, '+': 123,
'-': 124, '/': 125, '*': 126, 'a': 127, 'b': 128, 'c': 129, 'd': 131,
'e': 132, 'f': 133, 'g': 134, 'h': 135, 'i': 136, 'j': 137, 'k': 138,
'l': 139, 'm': 141, 'n': 142, 'o': 143, 'p': 144, 'q': 145, 'r': 146,
's': 147, 't': 148, 'u': 149, 'v': 151, 'w': 152, 'x': 153, 'y': 154,
'z': 155, 'á': 156, 'à': 157, 'â': 158, 'ã': 159, 'é': 161, 'ê': 162,
'í': 163, 'ó': 164, 'ô': 165, 'õ': 166, 'ú': 167, 'ç': 168, 'A': 169,
'B': 171, 'C': 172, 'D': 173, 'E': 174, 'F': 175, 'G': 176, 'H': 177,
'I': 178, 'J': 179, 'K': 181, 'L': 182, 'M': 183, 'N': 184, 'O': 185,
'P': 186, 'Q': 187, 'R': 188, 'S': 189, 'T': 191, 'U': 192, 'V': 193,
'W': 194, 'X': 195, 'Y': 196, 'Z': 197, 'Á': 198, 'À': 199, 'Â': 211,
'Ã': 212, 'É': 213, 'Ê': 214, 'Í': 215, 'Ó': 216, 'Ô': 217, 'Õ': 218,
'Ú': 219, 'Ç': 221, ',': 222, '.': 223, '!': 224, '?': 225, ';': 226,
':': 227, '_': 228, '(': 229, ')': 231, '"': 232, '#': 233, '$': 234,
'%': 235, '@': 236, ' ': 237, '\n': 238}


def achaPrimo(n):
    """
    Essa função recebe um int 'n' e gera um número primo 'p' realizando testes de Miller-Rabin;
    int -> int;
    """
    x = 1
    while x == 1:
        p = randrange(10**(n), 10**(n+2))
    
        if p % 2 == 0:
            if p == 2:
                return p
            p = randrange(10**(n), 10**(n+2))  # Como o único primo par é o 2, p será sorteado até ser ímpar
    
        q = (p - 1)  # Sabendo que p é ímpar, (p-1) é par
        k = 0
    
        while q % 2 == 0:
            q //= (2**k)
            k += 1
        
        for i in range(10):  # Para cada primo sorteado, executa 10 testes de Miller-Rabin
            b = randrange(2, p-1) # Em cada laço, sorteia uma base 'b'
            r = pow(b, q, p)  # b**q (mod p)
            if r == 1 or r == q:
                x = 0
            
            for j in range(1, k+1):
                r = pow(r, 2, p)
                if r == p-1:
                    break
    return p


def mdc(a, b):
    """
    Essa função recebe os inteiros 'a' e 'b', retornando o mdc(a,b);
    int, int -> int
    """
    while a != 0:
        a, b = b % a, a
    return b


def Euclides_estendido(a,b):
    """
    Retirado do código da aula 33 do professor Hugo Nobrega;
    """
    if a == 0:
        return b, 0, 1
    if b == 0:
        return a, 1, 0

    x_anterior = 1
    x_atual = 0
    y_anterior = 0
    y_atual = 1
    Dividendo, Divisor = a, b

    while True:
        Quociente, Resto = divmod(Dividendo, Divisor)
        x_anterior, x_atual = x_atual, (x_anterior - x_atual*Quociente)
        y_anterior, y_atual = y_atual, (y_anterior - y_atual*Quociente)
        if Resto == 0:
            return x_anterior
        Dividendo, Divisor = Divisor, Resto


def gera_chaves():
    """
    Essa função chama achaPrimos() para encontrar valores int 'p', 'q' e calcula o expoente público
    'e', a chave de decriptação 'd', os módulos 'n' e 'phi' e as ferramentas necessárias para a implementação do 
    Teorema Chinês dos Restos, são elas: 'inv_p_mod_q', 'inv_q_mod_p', 'd_mod_p_menos_1' e 'd_mod_q_menos_1'.
        -> int (todos)
    """
    p = achaPrimo(75)
    q = achaPrimo(75)
    n = p*q
    phi = (p-1)*(q-1)
    
    while True:  # Vai sortear 'e' até que 'e' e 'phi' sejam coprimos
        e = randrange(2, 30)
        if mdc(e, phi) == 1:
            break
    
    d = Euclides_estendido(e, phi) % phi
    
    # As informações abaixo serão usadas na implementação do Teorema Chinês dos Restos
    inv_p_mod_q = Euclides_estendido(p, q) % q
    inv_q_mod_p = Euclides_estendido(q, p) % p
    d_mod_p_menos_1 = d % (p-1)
    d_mod_q_menos_1 = d % (q-1)
    
    return n, e, d, p, q, inv_p_mod_q, inv_q_mod_p, d_mod_p_menos_1, d_mod_q_menos_1


def encriptar(texto, n, e):
    """
    Essa função recebe a str 'texto' e os ints 'n','e', retornando blocos encriptados;
    str, int, int -> list
    """
    listaCodigos = []
    
    for letra in texto:
        listaCodigos.append(str(símbolos_para_códigos[letra])) # Converte os símbolos para códigos do dicionário
    strCodigos = ''.join(listaCodigos)
    
    for i in range(len(strCodigos)):
        intervalo = randint(7, len(str(p))-1)  # Sorteia o intervalo dos blocos para dificultar a decriptação
        mensagemCodigos = [int(strCodigos[i:i+intervalo]) for i in range(0, len(strCodigos), intervalo)]  # Separa os códigos em blocos

    blocos = [pow(mensagemCodigos[i], e, n) for i in range(len(mensagemCodigos))]  # Realiza encriptação
    
    return blocos


def descriptar(blocos, n, d):
    """
    Essa função recebe a lista 'blocos' e os ints 'n' e 'd', retornando a mensagem descriptada
    através do Teorema Chinês dos Restos;
    list, int, int -> str
    """
    descriptarStr = ""
    blocosDescript = []
    
    q_elevado_p_menos_1_modN = pow(q, p-1, n)  # (q ** (p-1)) (mod n)
    p_elevado_p_menos_1_modN = pow(p, q-1, n)  # (p ** (q-1)) (mod n)
    
    for bloco in blocos:
        # Usando Teorema Chinês dos Restos (TCR)
        congruenciaP = pow(bloco, d_mod_p_menos_1, p)  # (bloco ** d_mod_p_menos_1) (mod p)
        congruenciaQ = pow(bloco, d_mod_q_menos_1, q)  # (bloco ** d_mod_q_menos_1) (mod q)
        
        produtoNoModuloP = congruenciaP * q_elevado_p_menos_1_modN 

        produtoNoModuloQ = congruenciaQ * p_elevado_p_menos_1_modN
        
        soma = produtoNoModuloP + produtoNoModuloQ
        
        resultado = str(pow(soma, 1, n))
        blocosDescript.append(resultado)
    
    for codigo in blocosDescript:
        descriptarStr += str(codigo)
    
    separarIntervalos = [int(descriptarStr[i:i+3]) for i in range(0, len(descriptarStr), 3)]
    
    mensagemDescriptada = ""
    
    for codigo in separarIntervalos:
        mensagemDescriptada += (códigos_para_símbolos[codigo])
    
    return mensagemDescriptada


texto = input("Insira a mensagem: ")

t0 = time()

n, e, d, p, q, inv_p_mod_q, inv_q_mod_p, d_mod_p_menos_1, d_mod_q_menos_1 = gera_chaves()
blocos = encriptar(texto, n, e)

mensagemDescriptada = descriptar(blocos,n,d)

t1 = time() - t0  # Calcula tempo de execução do código

print(f"\nMensagem Encriptada = {blocos}\n")
print(f"Mensagem Descriptada = {mensagemDescriptada}\n")
print(f"d = {d}\n")
print(f"e = {e}\n")
print(f"Módulo = {n}")

print(f"\nTempo de Execução do Código = {t1} s")