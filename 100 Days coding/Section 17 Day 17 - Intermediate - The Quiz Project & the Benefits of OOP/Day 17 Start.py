class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("001", "Hosam")
user2 = User("002", "Ahmed")
user2.follow(user1)
print(f"{user1.username} has {user1.followers} followers and {user1.following} following")
print(f"{user2.username} has {user2.followers} followers and {user2.following} following")

# user1.id = "345"
# user1.username = "Hosam"
# print(user1.username)

# user2 = User()
# user2.id = "345"
# user2.username = "Hosam"
# print(user2.username)