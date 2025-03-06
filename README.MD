# Queries

```python
from django.db.models import Count
from djangotask.models import AppUser, Discussion, Comment

# 1. All users with non-empty e-mail
AppUser.objects.exclude(email="")

# 2. All discussions with more than 10 comments
Discussion.objects.annotate(comment_count=Count("comments")).filter(
    comment_count__gt=10
)

# 3. All comments whose author has non-empty metadata.
Comment.objects.exclude(app_user__metadata={})
```
# To install app
### Create venv

```shell
  python3.11 -m venv venv
```

### Activate venv

```shell
  source venv/bin/activate
```

### Install dependencies

```shell
  pip install -r requirements.txt
```

