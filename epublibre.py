import pandas as pd

output = open("enlaces.sh", "w+")

# Cargamos el CSV con los datos

data = pd.read_csv('epublibre.csv')

# Filtramos solo los libros que están en Español

data_esp = data.loc[(data['Idioma'] == 'Español')]

# Extraemos la fecha de la columna Publicado

fecha_raw = data_esp.assign(Fecha=data_esp['Publicado'].str[2:])

# Convertimos la nueva columna en formato fecha

fecha_raw['Fecha'] = pd.to_datetime(fecha_raw['Fecha'], format='%d-%m-%Y')

# Se pregunta al usuario por la fecha hasta la que hay que llegar

fecha_limite = input('Introduce la fecha limite (yyyy-mm-dd): ')

# Se devuelven los enlaces hasta esa fecha

final = fecha_raw.loc[(fecha_raw['Fecha'] >= fecha_limite), [
    'Título', 'Autor', 'Enlace(s)', 'Fecha']]

final.to_csv('ep2.csv')

enlaces_raw = pd.Series.tolist(final['Enlace(s)'])

for enlace in enlaces_raw:
    if ', ' in enlace:
        temp_list = enlace.split(', ')
        for temp in temp_list:
            output.write('transmission-gtk magnet:?xt=urn:btih:' + temp + '\n')
    else:
        output.write('transmission-gtk magnet:?xt=urn:btih:' + enlace + '\n')

output.close()

#
