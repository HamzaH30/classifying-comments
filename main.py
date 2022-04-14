import json

def return_total_comments():
    sum = 0

    # Opening the comments.json file
    with open("comments.json", mode="r", encoding="utf8") as comments:
        data = json.load(comments)
        
        sum += len(data)
        
        for comment_value in data:
            sum += len(comment_value["replies"])
            
    return sum

# Lists that will be holding dictionaries.
fake_comments = []
real_comments = []

iteration = 0

# Opening the comments.json file
with open("comments.json", mode="r", encoding="utf8") as comments:
    # reading the data and saving it in a variable
    data = json.load(comments)
    
    # Looping through every dictionary element in data variable (comments.json)
    for comment_dict in data:
        comment = comment_dict["message"]
        comment_user = comment_dict["username"]
        comment_replies = comment_dict["replies"]


        # Asking user if this is a fake comment
        print(f"User: {comment_user}\nComment: {comment}\n")
        answered = False
        while answered is False:
            fake_or_real = input("Is this a fake comment (Y/N): ").lower()
            if (fake_or_real != "y") and (fake_or_real != "n"):
                answered = False
            else:
                answered = True
        
        # Did the user said it's fake or real?
        if fake_or_real == "y":
            # If it's fake, add it to the fake_comments list
            fake_comments.append({"username": comment_user, "comment": comment})
        else:
            # If it's real, add it to the real_comments list
            real_comments.append({"username": comment_user, "comment": comment})
        
        iteration += 1
        print(f"You have done {iteration} comments so far. You have {return_total_comments() - iteration} comments left. \n\n")
        
        # Loop through elements in the replies of the comment
        for reply_dict in comment_replies:
            
            
            reply = reply_dict["message"]
            reply_user = reply_dict["username"]
            
            # Ask user if this is a fake reply (comment)
            print(f"\nUser: {reply_user}\nComment (this is a reply): {reply}\n")
            answered = False
            while answered is False:
                fake_or_real = input("Is this a fake comment (Y/N): ").lower()
                if (fake_or_real != "y") and (fake_or_real != "n"):
                    answered = False
                else:
                    answered = True
            
            # Did the user say it's fake or real?
            if fake_or_real == "y":
                # If it's fake, add it to the fake_comments list
                fake_comments.append({"username": reply_user, "comment": reply})
            else:
                # If it's real, add it to the real_comments list
                real_comments.append({"username": reply_user, "comment": reply})
                
            iteration += 1
                
            print(f"You have done {iteration} comments so far. You have {return_total_comments() - iteration} comments left. \n\n")

## Print the fake and real comments list     
# print(f"Fake Comments list:\n{fake_comments}\n")
# print(f"Real Comments list:\n{real_comments}\n")

# save the fake and real comments lists as JSON files
with open("fake_comments.json", mode="w") as fake_comments_file:
    fake_comments_json = json.dumps(fake_comments)
    fake_comments_file.write(fake_comments_json)

with open("real_comments.json", mode="w") as real_comments_file:
    real_comments_json = json.dumps(real_comments)
    real_comments_file.write(real_comments_json)