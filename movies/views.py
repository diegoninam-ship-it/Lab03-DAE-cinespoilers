from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Movie, Genre  
from .serializers import MovieSerializer, GenreSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=False, methods=['get'], url_path='search')
    def search_by_name(self, request):
        """
        Buscar películas por nombre (parcial)
        Ej: /api/movies/search/?name=incep
        """
        name = request.query_params.get('name', '')
        movies = Movie.objects.filter(title__icontains=name)
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)

    # NUEVO
    @action(detail=False, methods=['get'], url_path='active')
    def get_active_movies(self, request):
        """
        Obtener solo películas activas
        Ej: /api/movies/active/
        """
        movies = Movie.objects.filter(is_active=True)
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)

    # NUEVO
    @action(detail=False, methods=['get'], url_path='by-genre')
    def get_by_genre(self, request):
        """
        Filtrar películas por género
        Ej: /api/movies/by-genre/?genre_id=1
        """
        genre_id = request.query_params.get('genre_id')

        if not genre_id:
            return Response(
                {"error": "Debe proporcionar genre_id"},
                status=400
            )

        movies = Movie.objects.filter(genres__id=genre_id)
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


    @action(detail=False, methods=['get'], url_path='buscar-por-id/(?P<id>[0-9]+)')
    def buscar_por_id(self, request, id=None):
        try:
            genre = Genre.objects.get(id=id)
            serializer = self.get_serializer(genre)
            return Response(serializer.data)
        except Genre.DoesNotExist:
            return Response({'error': 'Género no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'], url_path='peliculas')
    def buscar_peliculas(self, request, pk=None):
        genre = self.get_object()
        movies = genre.movies.all() # Relación ManyToMany de Diego
        serializer = MovieSerializer(movies, many=True)
        return Response({
            'genero': genre.name,
            'total': movies.count(),
            'peliculas': serializer.data
        })