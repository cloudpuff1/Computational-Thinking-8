# Create varibles
cat_points=0
dog_points=0


# questions
answer=input("When faced with a challenge, you prefer to A) Tackle it head-on with a clear strategy or B) Take a step back and think about it before diving in.")
if answer=="A":
    dog_points+=1
elif answer=="B":
    cat_points+=1


answer=input("How do you usually spend your weekends? A)  Relaxing at home, reading, or watching movies or B) Exploring new activities or meeting friends.Relaxing at home, reading, or watching movies.")
if answer=="A":
    cat_points+=1
elif answer=="B":
    dog_points+=1


answer=input("How do you feel about large social gatherings? A) I prefer small groups or one-on-one conversations or B) I enjoy them and thrive in the energy of the crowd")


if answer=="A":
    cat_points+=1
elif answer=="B":
    dog_points+=1


answer=input("When making decisions, you tend to A) Trust your instincts and go with what feels right or B) Analyze all the options before making a choice.")
if answer=="A":
    dog_points+=1
elif answer=="B":
    cat_points+=1


answer=input(" Which statement resonates with you the most? A) I like to observe and offer support when needed or B) I like to lead and take charge of situations.")
if answer=="A":
    cat_points+=1
elif answer=="B":
    dog_points+=1


# end of quiz:
if dog_points>1:
   print(" You have a Dynamic and Assertive Personality. You’re action-oriented, confident, and tend to take charge in situations. You’re energized by new experiences and challenges.")
elif cat_points>1:
    print("You have a Calm and Reflective Personality. You prefer to think things through, find balance, and enjoy peaceful moments. You thrive in more intimate or quieter environments and are a great listener")

