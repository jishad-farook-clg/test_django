from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def index(request):
    if request.method == 'GET':
        people_details = {
            'people':[
                {
                'name': 'John Doe',
                'age': 30,
                'city': 'New York',
                'country':'USA', 
            },
                {
                'name': 'Jane Smith',
                'age': 25,
                'city': 'London',
                'country':'UK', 
            },
                {
                'name': 'Sam Brown',
                'age': 35,
                'city': 'Sydney',
                'country':'Australia', 
            }
        ]}
        return Response(people_details)
    elif request.method == 'POST':
        return Response({'message': 'This is a POST request'})
    elif request.method == 'PUT':
        return Response({'message': 'This is a PUT request'})
    elif request.method == 'DELETE':
        return Response({'message': 'This is a DELETE request'})

@api_view(['GET'])
def get_movies(request):
    
    mov_data = {
        'movies':[
        {
        'Title': 'The Shawshank Redemption',
        'Year': 1994,
        'Success':False,  
    },
        {
        'Title': 'The Godfather',
        'Year': 1972,
        'Summary':'Summary of the movie The Godfather goes here ', 
        'Success':True,  
    },
        {
        'Title': 'The Dark Knight',
        'Year': 2008,
        'Summary':'Summary of the movie The Dark Knight goes here ', 
        'Success':True,  
    }
    ]}
    return Response(mov_data)

def hello(request):
    mov_data = {'movies':[
        {
        'Title': 'The Shawshank Redemption',
        'Year': 1994,
        'Success':False,  
    },
        {
        'Title': 'The Godfather',
        'Year': 1972,
        'Summary':'Summary of the movie The Godfather goes here ', 
        'Success':True,  
    },
        {
        'Title': 'The Dark Knight',
        'Year': 2008,
        'Summary':'Summary of the movie The Dark Knight goes here ', 
        'Success':True,  
    },
        {
        'Title': 'Pulp Fiction',
        'Year': 1994,
        'Summary':'Summary of the movie Pulp Fiction goes here ', 
        'Success':True,  
    },
        {
        'Title': 'The Lord of the Rings: The Return of the King',
        'Year': 2003,
        'Summary':'Summary of the movie The Lord of the Rings: The Return of the King goes here ', 
        'Success':True,  
    },
        {
        'Title': 'Forrest Gump',
        'Year': 1994,
        'Summary':'Summary of the movie Forrest Gump goes here ', 
        'Success':True,  
    },
        {
        'Title': 'Inception',
        'Year': 2010,
        'Summary':'Summary of the movie Inception goes here ', 
        'Success':True,  
    },
        {
        'Title': 'The Matrix',
        'Year': 1999,
        'Summary':'Summary of the movie The Matrix goes here ', 
        'Success':True,  
    },
        {
        'Title': 'Fight Club',
        'Year': 1999,
        'Summary':'Summary of the movie Fight Club goes here ', 
        'Success':True,  
    },
        {
        'Title': 'The Empire Strikes Back',
        'Year': 1980,
        'Summary':'Summary of the movie The Empire Strikes Back goes here ', 
        'Success':True,  
    }
    ]}
    return render( request, 'hello.html',mov_data)