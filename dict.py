favorite_movies = {}
template=[]
recommended_movies = {
    'Хенкок': {'rating': 4.5, 'review': 'Смотреть можно'},
    'Матрица': {'rating': 4.7, 'review': 'Фильм крут'},
    'Кибер': {'rating': 2.5, 'review': 'Так себе киношечка'},
    'Трон': {'rating': 3.8, 'review': 'Так себе киношечка'},
    'Мстители': {'rating': 4.7, 'review': 'Фильм крут'},
    'Хакеры':  {'rating': 4.5, 'review': 'Смотреть можно'}
}
for name_film, info in recommended_movies.items():                        
    if info['rating']<4.0:
        print(f'Фильм {name_film} не интересен: {info["review"]}. Фильм удален из рекомендаций')
        template.append(name_film)
    else:
        print(f'У фильма {name_film} хороший отзыв: {info["review"]}. Фильм добавлен в избранное')
        favorite_movies[name_film]=info

for key in template:
    del recommended_movies[key]
        

        
        
            

        

print(favorite_movies)
print(recommended_movies)