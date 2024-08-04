import time
from django.db import connection
from django.utils.deprecation import MiddlewareMixin


class QueryCountMiddleware(MiddlewareMixin):
    '''
    Middleware для отслеживания количества запросов к 
    базе данных и времени выполнения запроса.
    '''
    
    def process_request(self, request):
        ''' Начало отслеживания времени и количества запросов. '''
        
        request._query_count_start = len(connection.queries)
        request._start_time = time.time()

    def process_response(self, request, response):
        '''Количество запросов и время выполнения запроса.'''
        
        total_queries = len(connection.queries) - request._query_count_start
        total_time = time.time() - request._start_time

        # Логирование информации
        print(f'Общее количество запросов: {total_queries}')
        print(f'Общее время: {total_time:.4f}s')

        return response
