
#importação de bibliotecas
import re

#Declaração dos tokens
tokens = [

('def', r'shein'), #PALAVRA RESERVADA def
('return', r'uber'), #PALAVRA RESERVADA return
('if', r'seara'), #PALAVRA RESERVADA if
('else', r'casasbahia'), #PALAVRA RESERVADA else
('elif', r'anvisa'), #PALAVRA RESERVADA elif
('while', r'whatsapp'), #PALAVRA RESERVADA while
('for', r'ford'), #PALAVRA RESERVADA for
('in', r'intel'), #PALAVRA RESERVADA in
('break', r'kitkat'), #PALAVRA RESERVADA break
('continue', r'correios'), #PALAVRA RESERVADA continue
('pass', r'gamepass'), #PALAVRA RESERVADA pass
('True', r'original'), #PALAVRA RESERVADA True
('False', r'pirata'), #PALAVRA RESERVADA False
('none', r'bompreço'), #PALAVRA RESERVADA none
('and', r'andy'), #PALAVRA RESERVADA and
('or', r'oreo'), #PALAVRA RESERVADA or
('not', r'notas'), #PALAVRA RESERVADA not
('is', r'google'), #PALAVRA RESERVADA is
(',', r'virgula'), #vírgula
(':', r'doispontos'), #dois pontos
('(', r'abreparenteses'), #abre parênteses
(')', r'fechaparenteses'), #fecha parênteses
('[', r'abrecolchetes'), #abre colchetes
(']', r'fechacolchetes'), #fecha colchetes
('{', r'abrechaves'), #abre chaves
('}', r'fechachaves'), #fecha chaves
('.', r'ponto'), #ponto
(';', r'pontoevirgula'), #ponto e vírgula
('@', r'arroba'), #arroba
('=', r'igual'), #igual
('->', r'flecha'), #flecha
('+=', r'adicao'), #adicao
('-=', r'subtracao'), #subtracao
('*=', r'multiplicacao'), #multiplicacao
('/=', r'divisao'), #divisao
('//=', r'divisaointeira'), #divisaointeira
('%=', r'resto'), #resto
('@=', r'concatenacao'), #concatenacao
('&=', r'andbit'), #andbit
('|=', r'orbit'), #orbit
('^=', r'xorbit'), #xorbit
('>>=', r'rightshift'), #rightshift
('<<=', r'leftshift'), #leftshift
('**=', r'exponenciacao'), #exponenciacao
('==', r'igualigual'), #igualigual
('!=', r'diferente'), #diferente
('<', r'menor'), #menor
('>', r'maior'), #maior
('<=', r'menorigual'), #menorigual
('>=', r'maiorigual'), #maiorigual
(':', r'doisdoispontos'), #doisdoispontos

]

#Cria o analisador léxico
def lex():
    #Le o arquivo
    arquivo = open("programa.capitalista", "r")
    
    #Lê cada linha
    for linha in arquivo:
        #Remove caracteres especiais e espaços
        linha = linha.strip()
        #Separa a linha em tokens
        tokens = linha.split()
        #Cria um vetor para os lexemas
        lexemas = [

        ]
        
        #Percorre os tokens
        for token in tokens:
            if re.match(r'shein',token):
                lexemas.append('PALAVRA RESERVADA DEF')
            elif re.match(r'uber',token):
                lexemas.append('PALAVRA RESERVADA RETURN')
            elif re.match(r'seara',token):
                lexemas.append('PALAVRA RESERVADA IF')
            elif re.match(r'casasbahia',token):
                lexemas.append('PALAVRA RESERVADA ELSE')
            elif re.match(r'anvisa',token):
                lexemas.append('PALAVRA RESERVADA ELIF')
            elif re.match(r'whatsapp',token):
                lexemas.append('PALAVRA RESERVADA WHILE')
            elif re.match(r'ford',token):
                lexemas.append('PALAVRA RESERVADA FOR')
            elif re.match(r'intel',token):
                lexemas.append('PALAVRA RESERVADA IN')
            elif re.match(r'kitkat',token):
                lexemas.append('PALAVRA RESERVADA BREAK')
            elif re.match(r'correios',token):
                lexemas.append('PALAVRA RESERVADA CONTINUE')
            elif re.match(r'gamepass',token):
                lexemas.append('PALAVRA RESERVADA PASS')
            elif re.match(r'original',token):
                lexemas.append('PALAVRA RESERVADA TRUE')
            elif re.match(r'pirata',token):
                lexemas.append('PALAVRA RESERVADA FALSE')
            elif re.match(r'none',token):
                lexemas.append('PALAVRA RESERVADA NONE')
            elif re.match(r'google',token):
                lexemas.append('PALAVRA RESERVADA PRINT')
            elif re.match(r'facebook',token):
                lexemas.append('PALAVRA RESERVADA INPUT')
            elif re.match(r'abreparenteses',token):
                lexemas.append('DELIMITADOR ABRE PARENTESES')
            elif re.match(r'fechaparenteses',token):
                lexemas.append('DELIMITADOR FECHA PARENTESES')
            elif re.match(r'abrecolchetes',token):
                lexemas.append('DELIMITADOR ABRE COLCHETES')
            elif re.match(r'fechacolchetes',token):
                lexemas.append('DELIMITADOR FECHA COLCHETES')
            elif re.match(r'abrechaves',token):
                lexemas.append('DELIMITADOR ABRE CHAVES')
            elif re.match(r'fechachaves',token):
                lexemas.append('DELIMITADOR FECHA CHAVES')
            elif re.match(r'igual',token):
                lexemas.append('OPERADOR IGUAL')
            elif re.match(r'igualigual',token):
                lexemas.append('OPERADOR IGUAL IGUAL')
            elif re.match(r'diferente',token):
                lexemas.append('OPERADOR DIFERENTE')
            elif re.match(r'maior',token):
                lexemas.append('OPERADOR MAIOR')
            elif re.match(r'menor',token):
                lexemas.append('OPERADOR MENOR')
            elif re.match(r'maiorigual',token):
                lexemas.append('OPERADOR MAIOR IGUAL')
            elif re.match(r'menorigual',token):
                lexemas.append('OPERADOR MENOR IGUAL')
            elif re.match(r'andy',token):
                lexemas.append('PALAVRA RESERVADA AND')
            elif re.match(r'or',token):
                lexemas.append('PALAVRA RESERVADA OR')
            elif re.match(r'not',token):
                lexemas.append('PALAVRA RESERVADA NOT')
            elif re.match(r'mais',token):
                lexemas.append('OPERADOR MAIS')
            elif re.match(r'menos',token):
                lexemas.append('PALAVRA RESERVADA MENOS')
            elif re.match(r'mult',token):
                lexemas.append('PALAVRA RESERVADA MULT')
            elif re.match(r'div',token):
                lexemas.append('PALAVRA RESERVADA DIV')
            elif re.match(r'pot',token):
                lexemas.append('PALAVRA RESERVADA POT')
            elif re.match(r'ponto',token):
                lexemas.append('OPERADORPONTO')
            elif re.match(r'pontovirgula',token):
                lexemas.append('OPERADOR PONTO E VIRGULA')
            elif re.match(r'virgula',token):
                lexemas.append('OPERADOR VIRGULA')
            elif re.match(r'pontoexclamacao',token):
                lexemas.append('OPERADOR PONTO DE EXCLAMAÇÃO')
            elif re.match(r'pontointerrogacao',token):
                lexemas.append('OPERADOR PONTO DE INTERROGAÇÃO')
            elif re.match(r'pontoe',token):
                lexemas.append('OPERADOR PONTO E')
            elif re.match(r'pontou',token):
                lexemas.append('PALAVRA RESERVADA PONTO OU')
            elif re.match(r'pontov',token):
                lexemas.append('PALAVRA RESERVADA PONTO V')
            elif re.match(r'pontovv',token):
                lexemas.append('PALAVRA RESERVADA PONTO VV')
            elif re.match(r'pontovvv',token):
                lexemas.append('PALAVRA RESERVADA PONTO VVV')
            elif re.match(r'pontovvvv',token):
                lexemas.append('PALAVRA RESERVADA PONTO VVVV')
            elif re.match(r'doispontos',token):
                lexemas.append('OPERADOR DOIS PONTOS')
            #identifica número negativo:
            elif re.match(r'^-\d*\d$',token):
                lexemas.append('NUMERO INTEIRO NEGATIVO')
            elif re.match(r'\d*',token):
                lexemas.append('NUMERO INTEIRO')
            else:
                lexemas.append('ERRO. TOKEN OU IMPRESSÃO NÃO RECONHECIDA')
                        
        #Imprime o vetor de lexemas
        print(tokens, lexemas)

#Chama a função lex
lex()