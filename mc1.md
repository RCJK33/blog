# Mini challenge 1

### Acceptance Criteria
1. Create a new blog project in `this` directory
2. Create the following apps:
2.1. pages
2.2. posts
2.3. accounts
3. Create an about us page for a bogus company
4. Create a home page that explains the purpose of this site
5. Create a model called post with the following attributes:
5.1. title
5.2. subtitle
5.3. author
5.4. body
5.5. created_on
6. Create migrations for your model
7. Run all migrations
8. Create the following views for your new Post model:
8.1. ListView
8.2. DetailView
8.3. CreateView
9. Create templates for all of the above
10. Create a super user account
11. Log into the admin panel and create 3 posts
12. Test everything, make sure it matches your expectations.

# Bonus
1. Add boostrap support
2. Pick a theme for your blog (sports, games, whatever hobby you have)

# Note
To create the author field, you'll need the following pieces of code:
```
# import
from django.contrib.auth import get_user_model
...
# class attribute:
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)