items = {}

def main():
    while True:
        try:
            new_item = input("")
            new_item = new_item.upper()
            # si se repite el new item el valor se suma +1
            if not new_item in items:
                items[new_item] = 1
            else:
                items[new_item] += 1
        
        
            #se ignora el EOFError y se imprime items en mayusculas con su valor al inicio de cada linea
        except EOFError:
            print()
            for item in sorted(items.keys(), key=str.casefold):
                print(str(items[item]), item, sep=" ")
            # print(sorted(items.keys(), key=str.casefold), sep="/n")
            break
            
            

main()