{
	"<USER_ID>": {

		"posts": [

			"post #1",
			"post #2",
			"post #3"

		]

	},

	"<USER_ID>": {

		"posts": [

			"post #1",
			"post #2",
			"post #3"

		]

	}
}

Simple schema for API

Grab number of users registered: 
	
```python
number_of_users_registered = len(api.keys())
```

Grab users post:
	
```python
post_by_user = api[USERNAME]["posts"]
```

Grab specific post by user (iterative example):
	
```python
for idx in len(api[USERNAME]["posts"]):
	
	post_at_idx = api[USERNAME]["posts"][idx]
```

Check if user exists already for registration purposes:

```python
return new_username in api.keys()
```

Add account customization features such as profile picture image:

```python
api[USERNAME]["profile_pic"] = "img/profile_pic_of_user.png"
```
