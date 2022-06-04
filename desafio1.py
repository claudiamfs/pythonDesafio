# Menu Principal
#principal=print ("Menú Principal:\n"+"1 - Clientes\n"+"2 - Produtos\n"+"3 - Faturas\n")
menu_principal = {
    1: 'Clientes',
    2: 'Produtos',
    3: 'Faturas',
    4: 'Sair',
    
    
}


def print_menu():
    for key in menu_principal.keys():
        print (key, '--', menu_principal[key] )

    

menu_cliente= {
    1: 'Listar',
    2: 'Procurar',
    3: 'Inserir',
    4: 'Eliminar',
    9: 'Voltar ao menú principal'
       
    }
def print_menu_cliente():
    for key in menu_cliente.keys():
             print (key, '--', menu_cliente[key] )
    

menu_produto= {
    1: 'Listar',
    2: 'Procurar',
    3: 'Inserir',
    4: 'Eliminar',
    9: 'Voltar ao menú principal'
       
}

def print_menu_produto():
    for key in menu_produto.keys():
             print (key, '--', menu_produto[key] )

menu_fatura= {
    1: 'Listar',
    2: 'Procurar',
    3: 'Inserir',
    4: 'Eliminar',
    9: 'Voltar ao menú principal'
       
}

def print_menu_fatura():
    for key in menu_fatura.keys():
             print (key, '--', menu_fatura[key] )




if __name__=='__main__':
    print ("Menú Principal")
    print_menu()
    while(True):
        
        option = ''
        try:
            option = int(input('Escolha uma opção: '))
        except:
            print('Opção invalida. Por favor selecione un número ...')
       
        if option == 1:
            print ("Menú Cliente")
            print_menu_cliente()
            
            i=True
            while(i):
                option_cliente = ''
                try:
                    option_cliente = int(input('Escolha uma opção: '))
                except:
                    print('Opção invalida. Por favor selecione un número ...')
                if option_cliente  == 1:
                    print("opção Listar")
                elif option_cliente  == 2:
                    print("opção Procurar")
                elif option_cliente  == 3:
                    print("opção inserir")
                elif option_cliente  == 4:
                    print("opção eliminar")
                elif option_cliente  == 9:
                    print_menu()
                    i=False
                                
                
        elif option == 2:
            print ("Menú Produto")
            print_menu_produto()

            i=True
            while(i):
                option_produto = ''
                try:
                    option_produto = int(input('Escolha uma opção: '))
                except:
                    print('Opção invalida. Por favor selecione un número ...')
                if option_produto == 1:
                    print("opção Listar")
                elif option_produto  == 2:
                    print("opção Procurar")
                elif option_produto  == 3:
                    print("opção inserir")
                elif option_produto  == 4:
                    print("opção eliminar")
                elif option_produto  == 9:
                    print_menu()
                    i=False
       
       
        elif option == 3:
            print ("Menú Fatura")
            print_menu_fatura()

            i=True
            while(i):
                option_fatura = ''
                try:
                    option_fatura= int(input('Escolha uma opção: '))
                except:
                    print('Opção invalida. Por favor selecione un número ...')
                if option_fatura == 1:
                    print("opção Listar")
                elif option_fatura == 2:
                    print("opção Procurar")
                elif option_fatura  == 3:
                    print("opção inserir")
                elif option_fatura  == 4:
                    print("opção eliminar")
                elif option_fatura  == 9:
                    print_menu()
                    i=False


        elif option == 4:
            print('Obrigado por usar a nossa aplicação')
            exit()
        else:
            print('Opção invalida')



