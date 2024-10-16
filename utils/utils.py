def categorize_activity(activity):
    if 'museos' in activity.lower() or 'exposiciones' in activity.lower() or 'galerías de arte' in activity.lower():
        return 'Museos y exposiciones'
    elif 'monumentos' in activity.lower() or 'yacimientos' in activity.lower():
        return 'Monumentos y yacimientos'
    elif 'biblioteca' in activity.lower() or 'archivos' in activity.lower():
        return 'Archivos y bibliotecas'
    elif 'libros' in activity.lower() or 'lectores' in activity.lower():
        return 'Lectura'
    elif 'teatro' in activity.lower() or 'ópera' in activity.lower() or 'zarzuela' in activity.lower() or \
         'ballet' in activity.lower() or 'danza' in activity.lower() or 'circo' in activity.lower():
        return 'Artes escénicas'
    elif 'conciertos' in activity.lower():
        return 'Música'
    elif 'cine' in activity.lower():
        return 'Cine'
    else:
        return 'Otras actividades'

def identificar_grupo_actividad(organismo):
    grupos = {
        'Museos y exposiciones': ['Condeduque', 'Conde Duque', 'Matadero', 'Naves del Español en Matadero', 'Naves Matadero'],
        'Monumentos y yacimientos': ['Convenios'],
        'Archivos y bibliotecas': [],
        'Lectura': [],
        'Artes escénicas': ['Circo Price', 'Teatro Español', 'Teatro Circo Price', 'Teatro Fernán Gómez. Centro Cultural de la Villa', 'Fernán Gómez', 'Naves del Español', 'Veranos de la Villa'],
        'Música': [],
        'Cine': ['Cineteca']
    }
    
    for grupo, organismos in grupos.items():
        if organismo in organismos:
            return grupo
    return 'Desconocido'

def autolabel(rects):
    """Añadir etiquetas encima de las barras."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',  # Formato con dos decimales
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # Desplazamiento en píxeles
                    textcoords="offset points",
                    ha='center', va='bottom')
        
def color_variations(base_color, n_variations):

    base_color = np.array(mcolors.to_rgb(base_color))  # Convertir a RGB
    variations = [mcolors.to_hex(base_color * (1 - i * 0.15)) for i in range(n_variations)]  # Variaciones
    return variations

