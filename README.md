# Diego Nina Malqui
# Jason Gomez Mancha
# Aplicación de API REST (Django REST Framework)

## Demostración de la API
![APIRest](./docs/APIRest.png)

# Lista de Movies
![Movie-List](./docs/Movie-List.png)

## Test-GET http://127.0.0.1:8000/api/movies/
![Test-GET](./docs/test-GET.png)
![Test-GET](./docs/BD-GET.png)

## Test-POST http://127.0.0.1:8000/api/movies/
![Test-POST](./docs/test-POST.png)
![Test-POST](./docs/BD-POST.png)

## Test-PUT http://127.0.0.1:8000/api/movies/2/
![Test-PUT](./docs/test-PUT.png)
![Test-POST](./docs/BD-PUT.png)

## Test-DELETE http://127.0.0.1:8000/api/movies/2/
![Test-DELETE](./docs/test-DELETE.png)
![Test-POST](./docs/BD-DELETE.png)

## Test-PATCH http://127.0.0.1:8000/api/movies/1/
![Test-PATCH](./docs/test-PATCH.png)
![Test-PATCH](./docs/BD-PATCH.png)

## PRUEBAS DE METODOS IMPLEMENTADOS
### POST Crear Género
`POST http://127.0.0.1:8000/api/genres/`

![Movie POST](./docs/movie-post.png)
---

### POST Crear Película con Género
`POST http://127.0.0.1:8000/api/movies/`
![Movie POST](./docs/movie-post.png)

---

## Movies
### GET Películas Activas
`GET http://127.0.0.1:8000/api/movies/active/`
![Movies Active](./docs/movies-active.png)

---

### GET Buscar Película por Nombre
`GET http://127.0.0.1:8000/api/movies/search/?name=inc`
![Movies Search](./docs/movies-search.png)

---

### GET Filtrar por Género
`GET http://127.0.0.1:8000/api/movies/by-genre/?genre_id=1`
![Movies By Genre](./docs/movies-by-genre.png)

---

## Genero
### GET Buscar Género por ID
`GET http://127.0.0.1:8000/api/genres/buscar-por-id/1/`
![Genre By ID](./docs/genre-by-id.png)

---

### GET Películas de un Género
`GET http://127.0.0.1:8000/api/genres/1/peliculas/`
![Genre Peliculas](./docs/genre-peliculas.png)

---
