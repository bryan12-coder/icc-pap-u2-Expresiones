def main():
    runEjemplo1()
    runEjemplo2()
    runEjemplo3()

import re

def runEjemplo1():
    patron = r"ab*"
    palabras =[ "a" , "ab" , "abbb" , "abab" , "b" ,""]

    for palabra in palabras:
        res = re.match(patron, palabra)
        print(f"{palabra}  =>  {res}")
    

def runEjemplo2():
    patron = "[TO][0-9]{3}"
    lista = ["T001", "O120", "T01", "X001", "T0001"]

    for palabra in lista:
        res = re.match(patron, palabra)
        print(f"{palabra}  =>  {res}")

def runEjemplo3():
    texto= "Sensores: T001 reporta 23.5 C; O001 reporta 12 PERSONAS; T002 reporta -2 C."
    patron= r"[TO][0-9]{3}"

    for res in re.finditer(patron, texto):
        print(f"Encontrado: {res.group()}, posición: {res.start()}")


    pass

if __name__ == "__main__":
    main()