def isint(n):
    try:
        val = int(n)
        return "int"
    except ValueError:
        try:
            val= float (n)
            return "float"
        except ValueError:
            return "none"

def lexdebug(code):
    print("-----Analizador Lexico-----\n\nAnalisis de Caracteres\n")

    tokenslist = [["print", "PRINTF"],["true","TRUE_BOOL"],['false',"FALSE_BOOL"],["0","CEROVAL"],[',',"SEPARATE"],['"',"DOUBLE_COMMIT"],[">","MAYORQ"],["<","MINORQ"],[">=","MAYANDEQUAL"],["<=","MINANDEQUAL"],["==","COMP_EQUAL"],["!=","DISTINCT"],["+","SUM"],["-","REST"],["*","MULTIPLY"],["/","DIVIDE"],["int","INTEGER"],["float","DEC_FLOAT"],["string","STRING"],["bool","BOOLEAN"],[";","ENDLINE"],["=","OPERADOR_EQUAL"],["(","BRACKOPNE"],[")","BRACKCLOSE"]] #Esta es la lista de tokens

    arreglo_espacios = []

    arreglo_saltosdelinea = code.split("\n")

    for idx,i in enumerate(arreglo_saltosdelinea):
        temp_revisiondecaracteres = list(i)

        temp_texto_nuevalinea =""
        print("\nLINEA "+str(idx+1)+":")
        for j in temp_revisiondecaracteres:
            if ord(j)<128:
                print(j+" ==> # ASCII: "+str(ord(j)))
                if(ord(j)>=33 and ord(j)<=47) or (ord(j)>=58 and ord(j)<=64) or (ord(j)>=91 and ord(j)<=96) or (ord(j)>=123 and ord(j)<=126):
                    if ord(j)==59:
                        temp_texto_nuevalinea = temp_texto_nuevalinea + " " + j
                    else:
                        temp_texto_nuevalinea = temp_texto_nuevalinea + " " + j + " "
                else:
                    temp_texto_nuevalinea = temp_texto_nuevalinea + j
            else: #ERROR
                print("Error: "+j+" ==> Caracter Invalido en la linea " + str(idx+1))
                exit() #El codigo se detiene
        
        arreglo_espacios.append(temp_texto_nuevalinea) #Este método nos permite agregar nuevos elementos a una lista

        array_final = []

        for i in arreglo_espacios:
            temp_linea = []
            temp_revisartokens= i.split()
            for j in temp_revisartokens:
                for token in tokenslist: #Compara con mi lista de tokens
                    tempchecker = False
                    if token[0] == j:
                        temp_linea.append([j,token[1]])
                        tempchecker = True
                        break
                    else:
                        tempchecker = False

                if tempchecker == False:
                    checkj = isint(j)
                    if checkj == "int":
                        temp_linea.append([j,"NUMERO_INT"])
                    elif checkj == "float":
                        temp_linea.append([j,"NUMERO_FLOAT"])
                    else:
                        temp_linea.append([j,"NOMBRE_VARIABLE"])

            array_final.append(temp_linea) #Se introducen a arreglo final, todos los arreglos guardados en temp_linea

    print("\nEn Tokens tenemos:") #A partir de aqui, se imprimen los tokens correspondientes a cada linea
    contador = 1
    for i in array_final: #en este for recorreremos cada uno de los arreglos, dentro de arreglo_final
        print("\nLINEA "+str(contador)+":")
        contador = contador + 1
        for j in i: #Se recorren cada uno de los arreglos y se imprimen los tokens uno debajo del otro
            print(j)

    print("\n")

f = open("comandos.txt", "r") #con esta instrucción, leemos la información del documento comandos.txt
lexdebug(f.read())