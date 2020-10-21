from django.http import Http404
class Post():

    POSTS = [
        {'id': 1, 'title': 'Fist Post', 'body': 'This is my first Post'},
        {'id': 2, 'title': 'Second Post', 'body': 'This is my first Post'},
        {'id': 3, 'title': 'Third Post', 'body': 'This is my third Post'},
    ]

    @classmethod
    def all(cls):
        return cls.POSTS

    @classmethod
    def find(cls, id):
        try:
            return cls.POSTS[int(id) - 1]
        except:
            raise Http404('Sorry, Post #{} not found.'.format(id))
