def decorator(funcao):
    def wrapper(*arg, **kwargs):
        print('Ola Mundo')
        print(arg[1])
        print(kwargs)
        funcao(*arg, **kwargs) # print('Estou na minha classe')

    return wrapper


class minha_classe:

    @decorator
    def metodo(self, num):
        print('Estou na minha classe')



cl = minha_classe()
cl.metodo(4)
