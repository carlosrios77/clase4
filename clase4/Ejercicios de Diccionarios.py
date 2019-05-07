#1. Crear una agenda de contactos utilizando diccionario
#                   Telefono        email
#   Juan Perez      83013040        jperez@gmail.com
#   Carlos Rojas    97001030        crojas@hotmail.com
#   Ana Marin       91000130        ana@marin.com

#mi_dict={
#    'Juan_Perez' : ['Juan', 'Perez','83013040','jperez@gmail.com' ],
#    'Carlos_Rojas' : ['Carlos','Rojas', '97001030','crojas@hotmail.com'],
#    'Ana_Marin' : ['Ana','Marin','91000130','ana@marin.com']
#}


#solucion propouesta por el profesor

#agenda de contactos

agenda = {
    'juan perez' : {'telefono': 83013040,
                     'correo': 'jperez@gmail.com'},
    'carlos rojas' : {'telefono': 97001030,
                     'correo': 'crojas@hotmail.com'},
    'ana marin' : {'telefono': 91000130,
                     'correo' : 'ana@marin.com'}
}
pass

#2. Cuantas personas o contactos hay en la agenda?
#len(agenda)

#3. cuales son los nombres de los contactos?
#list(agenda.keys())

#4. Utilizando agenda imprima las informaciones de cada contacto
#for contacto in agenda.items():
#    print(contacto)

#solucion del profefor contacto, info in agenda.items():
#    print('nombre',contacto,
#          'telefono',info['telefono'],
#          'correo',info['correo'])

#5. Suponga que Juan Perez cambio de telefono, ahora tiene dos 63101111, 23333333
#agenda['juan perez']['telefono'] = ['63101111', '23333333']

#6. Hay un nuevo contacto. Sofia telefono 33333333. email sofia@gmail.com
#opcion 1
#sofia = {'telefono': 33333333,
#         'correo': 'sofia@gmail.com'}
#
#agenda['sofia castro'] = sofia

#opcion 2
#agenda.update ({'sofia alfaro': sofia})