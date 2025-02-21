class User: 
    def __init__(self, hobby, job, user_id):
        self.hobby = hobby
        self.job = job
        self.user_id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


tim = User("Guitar", "Software Engineer", "001")
Brenda = User("Piano", "Data Scientist", "002")

tim.follow(Brenda)

print(f"tim followers: {tim.followers} || tim following: {tim.following}")
print(f"Brenda followers: {Brenda.followers} || Brenda following: {Brenda.following}")
