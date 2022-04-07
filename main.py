import json

# [{username: , comment: }]
fake_comments = []
real_comments = []

with open("test1.json", mode="r", encoding="utf8") as comments:
    # Data
    data = json.load(comments)
    
    # looping through elements in the data file
    for comment_dict in data:
        comment = comment_dict["message"]
        comment_user = comment_dict["username"]
        comment_replies = comment_dict["replies"]

        print(f"User: {comment_user}\nComment: {comment}\n")
        fake_or_real = input("Is this a fake comment (Y/N): ")
        
        if fake_or_real == "y":
            fake_comments.append({"username": comment_user, "comment": comment})
        else:
            real_comments.append({"username": comment_user, "comment": comment})
        
        for reply_dict in comment_dict["replies"]:
            reply = reply_dict["message"]
            reply_user = reply_dict["username"]
            
            print(f"\nUser: {reply_user}\nComment (this is a reply): {reply}\n")
            fake_or_real = input("Is this a fake reply (Y/N): ")
            
            if fake_or_real == "y":
                fake_comments.append({"username": reply_user, "comment": reply})
            else:
                real_comments.append({"username": reply_user, "comment": reply})
            
print(f"Fake Comments list:\n{fake_comments}\n")
print(f"Real Comments list:\n{real_comments}\n")

# save the fake and real comments lists as JSON files
with open("fake_comments.json", mode="w") as fake_comments_file:
    fake_comments_json = json.dumps(fake_comments)
    fake_comments_file.write(fake_comments_json)

with open("real_comments.json", mode="w") as real_comments_file:
    real_comments_json = json.dumps(real_comments)
    real_comments_file.write(real_comments_json)