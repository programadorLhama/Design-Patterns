from factorys import UseCaseFactory

usecase = UseCaseFactory.create()

response = usecase.do_something(True)
print(response)
