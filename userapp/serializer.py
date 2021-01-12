from rest_framework.serializers import ModelSerializer

from userapp.models import Book, Press, Author


class PressModelSerializer(ModelSerializer):
    class Meta:
        model = Press
        fields = ('id', 'press_name', 'address',)




class BookModelSerializer(ModelSerializer):
    publish=PressModelSerializer()

    class Meta:
        model = Book
        fields = ('id','book_name', 'price','publish_name','author_list', 'publish_address','create_time','publish')
        extra_kwargs={
            'publish':{
                'write_only':True
            },
            'authors':{
                'write_only':True
            },
            'publish_name':{
                'read_only':True
            },
            'publish_address':{
                'read_only':True
            }
        }

class BookDeModelSerializer(ModelSerializer):
    class Meta:
        model=Book
        fields=('book_name', 'price', 'publish', 'authors')
        extra_kwargs={
            'book_name':{
                "min_length":4,
                "max_length":20,
                'required':True,
                'error_messages':{
                    'max_length':'字段不能超过20个字符',
                    'min_length':'字段不能小于4个字符'
                },

            },
            "price": {
                'max_digits': 5,
                'decimal_places': 2
            },
        }
