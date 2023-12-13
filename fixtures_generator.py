from django.contrib.auth.models import User
from django.utils.text import slugify
import json
from faker import Faker

# Initialize faker module
fake = Faker()

# Define the base data
names = ['Health', 'Nutrition', 'Exercise', 'Mental Health', 'Wellness']
users = ['John', 'Jane', 'Doe', 'Ann', 'Mia']

# Initialize the list to store all data
data = []

# Create users
for i in range(1, 6):
    first_name: str = fake.first_name()
    last_name: str = fake.last_name()
    username = '@%s%s' % (first_name.lower(), last_name.lower())

    user = User.objects.create(username=username, first_name=first_name, last_name=last_name)
    user.save()

# Create authors
for i in range(1, 6):
    data.append({
        "model": "author.author",
        "pk": i,
        "fields": {
            "user": i,
            "about": f"I'm author number {i}",
        }
    })

# Create categories
for i in range(6, 11):
    data.append({
        "model": "category.category",
        "pk": i,
        "fields": {
            "name": names[i - 6] + f" {i}",
            "slug": names[i - 6].lower() + f"-{i}",
        }
    })

# Create posts
for i, j, k in zip(range(11, 26), [6, 7, 8, 9, 10] * 3, [1, 2, 3, 4, 5] * 3):
    
    content = ''
    for _ in range(5):
        content = f"{content}//n/n{fake.paragraph(5)}"

    title = fake.sentence(12)
    slug = slugify(title)

    data.append({
        "model": "post.post",
        "pk": i,
        "fields": {
            "title": title,
            "slug": slug,
            "subtitle": fake.sentence(15),
            "content": content,
            "reading_duration": i % 10 + 1,
            "extra_content": fake.sentence(15),
            "image_url": fake.url(),
            "category": j,
            "author": k,
        }
    })

# Write to the fixture file
with open('fixtures.json', 'w') as f:
    f.write(json.dumps(data))