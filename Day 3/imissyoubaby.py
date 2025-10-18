import time
import os

# Optional: Clear screen for each line (works on Windows, Mac, Linux)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Song title
print("Now playing: All i ask by Adele(yearning time!)")
time.sleep(2)

# Lyrics (you can replace these with any song)
lyrics = [
    "I will leave my heart at the door",
    "I won't say a word",
    "They've all been said before, you know",
    "So why don't we just play pretend",
    "Like we're not scared of what is coming next",
    "Or scared of having nothing left",
   " Look, don't get me wrong",
    "I know there is no tomorrow",
    "All I ask is",
   " If this is my last night with you",
    "Hold me like I'm more than just a friend",
   " Give me a memory I can use",
    "Take me by the hand while we do what lovers do",
    "It matters how this ends",
   " Cause what if I never love again?",
    "I don't need your honesty",
   " It's already in your eyes",
    "And I'm sure my eyes, they speak for me",
    "No one knows me like you do",
    "And since you're the only one that matters",
    "Tell me who do I run to?",
    "Look, don't get me wrong",
   " I know there is no tomorrow",
    "All I ask is",
   " If this is my last night with you",
    "Hold me like I'm more than just a friend",
    "Give me a memory I can use",
    "Take me by the hand while we do what lovers do",
    "It matters how this ends",
    "Cause what if I never love again?",
    "Let this be our lesson in love",
    "Let this be the way we remember us",
    "I don't wanna be cruel or vicious",
    "And I ain't asking for forgiveness",
    "All I ask is",
    "If this is my last night with you",
    "Hold me like I'm more than just a friend",
    "Give me a memory I can use",
   " Take me by the hand while we do what lovers do",
    "It matters how this ends",
    "Cause what if I never love again?",
]

# Loop through the lyrics and display them one at a time
for line in lyrics:
    clear_screen()          # Clears screen before showing next line
    print(line)
    time.sleep(5)           # Delay 2 seconds per line

print("\n🎶 End of song! 🎶")