class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

user1 = User("007", "Hosam")
print(user1.id)
print(user1.username)

# user1.id = "345"
# user1.username = "Hosam"
# print(user1.username)

# user2 = User()
# user2.id = "345"
# user2.username = "Hosam"
# print(user2.username)