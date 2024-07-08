
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación:

tipo_pizza = input('Ingrese el tipo de pizza (vegetariana / no vegetariana): ')

if(tipo_pizza == "vegetariana" or tipo_pizza == "VEGETARIANA" ):
    print(f'Ingredientes vegetarianos: Pimiento y tofu.')
elif (tipo_pizza == "no vegetariana" or tipo_pizza == "NO VEGETARIANA"):
    print(f'Ingredientes no vegetarianos: Peperoni, Jamón y Salmón')
else:
    print('no existe el tipo de pizza')