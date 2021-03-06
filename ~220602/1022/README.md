# PJT 07

## π λͺ©ν

β λ°μ΄ν°μ λν CRUDκΈ°λ₯μ λ€λ£° μ μλ `Web application` μ μ

β `Django Web Framework` λ₯Ό ν΅ν λ°μ΄ν° μ‘°μ

β `Authentication` μ λν μ΄ν΄

β Database `1:N`  `M:N`  κ΄κ³μ μ΄ν΄μ λ°μ΄ν° κ΄κ³ μ€μ 



## β μμνκΈ° μ  μκ°

π μκ³ λ¦¬μ¦μ λ§μΉκ³  λ€μ λ§λ³΄λ DJango νλ‘μ νΈμΈλ° μ΄μ μ μμλ λ΄μ©μ κΉλ¨Ήμ§ μμμκΉ κ±±μ μ΄ λλ€.

π λ€μ΄μ΄κ·Έλ¨μΌλ‘ λͺ¨λΈμ κ΅¬μ‘°λ₯Ό μμλ΄€λλ° ν‘μ¬ μκ³ λ¦¬μ¦μ λ³΄λ λ― νλ€.

π 1:N, M:N κ΄κ³κ° μκ°λ³΄λ€ κΈλ°© μ΅νμ§μ§ μμμ νλ‘μ νΈλ₯Ό μ§ννλ©΄μ κ°μ μ‘μμΌ ν  κ² κ°λ€.



### A. νλ‘μ νΈ κ΅¬μ‘°

β νλ‘μ νΈ κ΅¬μ‘° μ΄ν΄νκΈ°

π― `venv` ,  `django`  λ±μ μ΄μ©ν΄ νλ‘μ νΈ κΈ°λ³Έ κ΅¬μ‘° λ§λ€κΈ°

```bash
# κ°μνκ²½ ν΄λ μμ±
python -m venv venv

# κ°μνκ²½ νμ±ν
source venv/Scripts/activate

# django μ€μΉ
pip install django

# νλ‘μ νΈ μμ± (ν΄λΉ νλ‘μ νΈμμλ νΈμμ configλ‘ μμ±νμ΅λλ€.)
django-admin startproject pjt07 .

# μ΄νλ¦¬μΌμ΄μ μμ±
python manage.py startapp community
python manage.py startapp accounts
# μ΄ν settings.py - 'INSTALLED_APPS'μ 'community', 'accounts', μμ±

# settings.py μμ 'auth_User'μΈ λν΄νΈκ°μ 'accounts_User'λ‘ μ€μ 
AUTH_USER_MODEL = 'accounts.User'
```

β startapp λͺλ Ήμ΄λ₯Ό μ¬μ©ν  λ `django-admin` μΈμ§ `python manage.py` μΈμ§ νΌλμ΄ μμλ€.

β μμ μμ±ν κ² μ²λΌ `settings.py` μμ μ»€μ€ν μ μ  λͺ¨λΈμ μΆκ°μ μΌλ‘ μ€μ νλ€.



### B. Signup / Login

β μ¬μ©μ μΈμ¦ κ΄λ¦¬

π― μλ²λ₯Ό μ΄μ©νκΈ° μν νμκ°μ / λ‘κ·ΈμΈ-μμ κ΅¬μ±

```python
@require_http_methods(['GET', 'POST'])
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('community:index')
        else:
            form = CustomUserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('community:index')


@require_http_methods(['GET', 'POST'])
def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                # user = form.save()
                auth_login(request, form.get_user())
                return redirect(request.GET.get('next') or 'community:index')
        else:
            form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('community:index')
```

β `signup` κ³Ό `login` μ ν° νμ λΉμ·ν΄μ λ€λ₯Έ λΆλΆμ λΉν΄ μμ μκ°μ΄ μ μλ€.

β `views.login` μμ auth_login~return κ΅¬λ¬Έμμ μ°©μ€κ° μμ΄ μ κ² μ€κ°μ λ‘κ·ΈμΈμ΄ μλλ νμμ΄ μμλ€.



### C. Profile

β `Django ORM queryset` μ΄ν΄

π― νλ‘μ° κΈ°λ₯ κ΅¬ν 

```python
def follow(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    if person.followers.filter(pk=request.user.pk).exists():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
```

β ORM μΏΌλ¦¬μμ κ°λ§μ μ¬μ©ν΄λ΄€λλ° μ΅μνμ§κ° μμμ κ·Έλ°μ§ λ°λ‘λ°λ‘ μκ°μ΄ λμ§ μμλ€.

β νλ‘ν νλ©΄μ κ΅¬μ±ν΄λκ³  ν΄λΉ λ§ν¬λ₯Ό κ±Έμ΄λμ§ μμ μ£Όμμ°½μ μ§μ  μ£Όμλ₯Ό μμ± ν΄μΌλ§ νλ‘νμ λ³Ό μ μλ μΌμ’μ ν΄νλμ΄ μμλ€.



### D. Index

β Bootstrap νμ©

π― `card` λ₯Ό μ΄μ©ν μΈλ±μ€ μ λ ¬

```python
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)
```

β κΈ°μ‘΄μλ μΆκ°μ μΈ μ€νμΌλ§ μμ΄ forλ¬Έμ μ΄μ©ν΄ μ λ ¬μ νμλλ° μ΄λ²μλ λΆνΈμ€νΈλ©μ μΉ΄λμ κ·Έλ¦¬λλ₯Ό μ΄μ©ν΄ μ€νμΌλ§μ ν΄λ΄€λ€.

β μΉ΄λμ ν¬κΈ°λ₯Ό μ ν΄λμ κ²μ΄ μλμ¬μ μμ λͺ©μ΄ μλ λ¦¬λ·°μ κ²½μ° ν¬κΈ°κ° μμμ Έ λ³΄κΈ°μ λΆνΈν κ°μ΄ μμ§μμ μμλ€.

<img src="README.assets/image-20211022172453523.png" alt="image-20211022172453523" style="zoom:80%;" />



### E. Create

β `Create` κΈ°λ₯ μ΄ν΄

π― μλ‘μ΄ λ¦¬λ·° μμ± νμ΄μ§ κ΅¬μ±

```python
@require_http_methods(['GET', 'POST'])
@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)
```

β `commit=False` κ΅¬λ¬Έμ λ£μ§ μμ `IntegrityError` κ° λ¬μλ€.

<img src="README.assets/image-20211022213233479.png" alt="image-20211022213233479" style="zoom: 50%;" />



### F. Detail

β pkμ λν μ΄ν΄

π― μμΈ λ¦¬λ·° ν­λͺ© μμ±

```python
@require_safe
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)
```

<img src="README.assets/image-20211022173230363.png" alt="image-20211022173230363" style="zoom: 33%;" />

<img src="README.assets/image-20211022173302138.png" alt="image-20211022173302138" style="zoom: 33%;" />



## π μκ° μ§λ¨

β μ€κ° μ κ²μ νλ©΄μ μλ¬λ₯Ό ν΄κ²°νλ μλλ μ λ³΄λ€ λΉ¨λΌμ‘μ§λ§, μμ§ μ²μ μμ±νλ λμ μ¬μν λΆλΆμ λμΉλ κ²½μ°κ° λ§μλ€.

β μ΄λ²μλ μκ°μ΄ μΌλ§ μλ¨μμ΄λ μ‘°κΈμ΄λΌλ μ€νμΌλ§μ ν΄λ³΄λ €κ³  μλν΄λ΄€λλ°, κ²°κ³Όμ μΌλ‘ μ’μ κ²°κ³Όκ° λμλ€. μ­μ μΌλ¨ κ±΄λλ €λΌλ λ³΄λ κ²μ΄ λμμ΄ λ§μ΄ λλ κ² κ°λ€.

β PJTλ₯Ό νκΈ° μ  νΌμ μ½λλ₯Ό κ±΄λλ¦΄ λλ `NoReverseMatch` μλ¬κ° μλ μμ΄ λ΄λλ° μ€λμ νλ²λ λ³΄μ΄μ§ μμμ λλ¦ κΈ°λΆμ΄ μ’μλ€.



## πΎ μΆκ° html μ½λ

```html
{% comment %} detail.html {% endcomment %}
<form action="{% url 'community:like' review.pk %}" method='POST'>
  {% csrf_token %}
  <span>{{ review.like_users.all|length }}</span>
  {% if user in review.like_users.all %}
    <button><i class="fas fa-heart" style='color: red'></i>  {{review.like_users.all|length}}</button>
    {% else %}
    <button><i class="fas fa-heart"></i>  {{review.like_users.all|length}}</button>
  {% endif %}
</form>
<h3>λκΈ</h3>
{% if comments %}
  <p>{{ comments|length }}κ°μ λκΈμ΄ μμ΅λλ€.</p>
{% endif %}
<ul>
  {% for comment in comments %}
    <li>{{ comment.user }}: {{ comment.content }}</li>
  {% endfor %}
</ul>
<hr>
{% if request.user.is_authenticated %}
  <form action="{% url 'community:comment_create' review.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
{% else %}
  <a href="{% url 'accounts:login' %}">login</a>
{% endif %}
{% endblock %}
```

