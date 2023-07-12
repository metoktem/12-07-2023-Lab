## TODO APP

### Django ORM (Object Relational Mapping) - veri tabani islemleri
- title
- desc
- is_active
- created_at
- updated_at

#### Shell Calismasi
from todo.models import Todo

select
Todo.objects.all()

count
Todo.objects.all().count()

create
Todo.objects.create(title='Shell uzerinden olusan kayit')

filter
Todo.objects.filter(is_active=True)