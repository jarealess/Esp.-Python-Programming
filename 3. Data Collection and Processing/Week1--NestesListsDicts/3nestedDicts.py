###### DICCIONARIOS ANIDADOS ###############3
info = {'personal_data':
            {'name': 'Lauren',
            'age':20,
            'major': 'Information science',
            'physical_features':
                    {'color':{'eye':'blue',
                            'hair':'brown'},
                    'height': "5'8"
                    },
            'other':
                    {'favorite_colors': ['purple','green','blue'],
                    'interested_in':['social media', 'copyright', 'music', 'books']
                    }
                }
        }

### queremos imprimir favorite color
print(info['personal_data']['other']['favorite_colors'])