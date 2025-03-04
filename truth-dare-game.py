import streamlit as st
import random
# Custom CSS to hide the footer
hide_footer = """
    <style>
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_footer, unsafe_allow_html=True
# Define truths and dares for couples
truths_couples = [
    "Have you ever had a sexy dream about me? Tell me what it was like.",
    "How many people have you kissed?",
    "How many people have you slept with?",
    "Would you rather be the person doing the spanking or be spanked yourself?",
    "What’s something I do that unintentionally turns you on a lot?",
    "What’s something I do in bed that turns you on a lot?",
    "What’s something in bed that you would like me to try?",
    "What’s a position you want to try?",
    "Do you have anything you fear sexually?",
    "How often do you pleasure yourself a week?",
    "Have you ever watched porn? What’s your go-to category?",
    "Where is the craziest place you’ve ever masturbated?",
    "Where is the craziest place you’ve ever had sex?",
    "What’s an odd fetish that you would try out?",
    "What’s the record amount of times you’ve had sex in one day?",
    "Do you like to be the dominant one in bed? Or do you prefer me to be?",
    "Have you ever had sex while other people were in the room without them knowing?",
    "What non-sexual part of your body gets you horny when I touch it?",
    "Are you a fan of foreplay?",
    "Are you a fan of shower sex?",
    "What’s something you like in bed that I can do more of or improve on?",
    "When’s the last time you pleasured yourself?",
    "Do you enjoy receiving nudes?",
    "What’s your favorite nude I’ve ever sent?",
    "What’s your favorite body part of mine?",
    "What’s a secret fantasy you’ve always kept hidden from me?",
    "Tell me something kinky you want to try in bed.",
    "What’s your favorite outfit on me and why?",
    "What’s your favorite sexual memory of me or us?",
    "Do you think we’ve improved in bed over time or is there something you miss that we used to do more?",
    "What do you love about me the most?",
    "What sexual adventure would you be willing to try if we get bored way down the line?",
    "What’s something sexual I’ve done that you didn’t expect of me when we first got together?",
    "Give me a sexy nightclub dancer name.",
    "Have you ever been to a strip club? If not, would you like to go?",
    "Have you ever wanted to try role play?",
    "Have you ever masturbated with something weird?",
    "How old were you when you first watched porn?",
    "Have you ever wanted to try bondage?",
    "When was the first time you were attracted to me?",
    "Have you ever received a lap dance?",
    "What’s your favorite fantasy to pleasure yourself to?",
    "What sex act have you done that you never want to do again?",
    "Have you ever faked an orgasm with me?",
    "Tell me about the best orgasm you’ve ever had.",
    "Have you ever had a crazy one-night stand? Tell me about it.",
    "If you woke up as the opposite sex, what’s the first thing you would explore about yourself?",
    "Do you like listening to music while having sex?",
    "What’s the longest you’ve gone without having sex?",
    "What’s something sexy I say that you love?",
    "Have you ever thought about experimenting with someone of the same sex?",
    "Have you ever watched or wanted to watch another couple have sex?",
    "Lights off or lights on during sex?",
    "Where is your favorite place to have sex?",
    "Does dirty talk get you horny?",
    "Would you rather give or receive pleasure?",
    "What’s a sexual act that you never want to try?",
    "What’s the dirtiest thing you’ve ever been caught doing or almost been caught doing?",
    "What’s something you’ve fantasized about your partner that’s made you finish when pleasuring yourself before?",
    "Tell me about a time you’ve been embarrassed in bed.",
    "Do you like sex to be rough or sensual?",
    "Have you ever been friend-zoned?",
    "Have you ever paid for porn or sexual pleasure in any way?",
    "What’s the quickest way to get you into bed?",
    "What’s the quickest way I’ve turned you on before?",
    "What’s the sexiest underwear I have?",
    "Do you prefer a little hair or smooth-shaven?",
    "What’s the least sexual thing your partner has done that’s gotten you aroused somehow?"
]


dares_couples = [
    "Give over your phone to your partner and let them decide on a sex toy you two can try together.",
    "Have your partner read through your browsing history in a sexy voice.",
    "Make a sexy song playlist with your partner.",
    "Sexily wash your partner’s feet.",
    "Be blindfolded and tickled or lightly touched for one minute.",
    "Have your partner close their eyes and try to turn them on only using sounds.",
    "Try to turn on your partner by blowing on the back of their neck, alternating between cold and hot.",
    "Place a hand in your partner’s underwear for the next round and try to arouse them.",
    "Draw something on your partner’s back. If they guess correctly, they get a special favor of their choosing, if not, you get one.",
    "Your partner gets to dress you up in their clothes and take a photo.",
    "Call the parents of your partner and express to them how much you adore your partner.",
    "Give your partner a hot lap dance.",
    "Whisper something not sexy into your partner’s ear but try to make it sound hot.",
    "Describe your partner’s naked body in intense, erotic detail.",
    "Wear handcuffs or have your hands tied for a few turns.",
    "Trade clothes with your partner.",
    "Take a body shot off your partner.",
    "Show your partner your go-to porn video.",
    "Give your partner a sexy full-body massage.",
    "Give your phone to your partner and let them order something hot for you to wear.",
    "Turn on your partner by only touching their arms and hands.",
    "Lick something yummy off your partner’s body part of choice.",
    "Take off a piece of your partner’s clothing, only using your teeth.",
    "Trace your partner’s body with an ice cube that’s being held in your mouth.",
    "Beg your partner to do naughty things to you. It better be convincing!",
    "Give your partner head with their clothes on.",
    "Do whatever your partner says for one minute.",
    "Put on the hottest song you know and try to seduce your partner with it.",
    "Make your best orgasm face and let your partner take a photo of it. This is your lock screen for the next 24 hours.",
    "Become a sexy chef while teaching your partner how to make a fun late night snack while just wearing an apron.",
    "Find an old photograph and try to recreate it together.",
    "Have your partner ask 3 questions about themselves that you should know the answers to. If you get them right, you get a reward. If you get them wrong, you get punished.",
    "Have your partner take a picture of you looking naughty.",
    "Give your partner a massage without using your hands.",
    "Act out how you remember your first date in 30 seconds.",
    "Lick your partner’s feet for 15 seconds.",
    "Set a timer and try to make your partner orgasm in 5 minutes.",
    "Set a timer for 2 minutes and try not to get turned on by whatever your partner decides to do to you.",
    "Watch porn together and try to imitate what you see on the screen.",
    "Perform a strip tease for your partner.",
    "Lick your partner’s nipples.",
    "Kiss your partner in the sexiest place and sexiest way possible.",
    "Undress your partner with one hand.",
    "Suck on your partner's finger like you’re giving them head.",
    "Send a naughty text message to your partner.",
    "Become a sexy chef and spank your partner sexily with an item from the kitchen.",
    "Arouse your partner by only using your tongue.",
    "Attempt to make a sex tape with your partner.",
    "Let your partner blindfold you and do what they want to you for a minute.",
    "Bend your partner over your knee and spank them while telling them they’re a bad boy/girl.",
    "Sexily perform good foreplay on your partner’s ear to get them aroused.",
    "Dress up in something your partner would find sexy.",
    "Turn on your partner by sexily sucking on their finger.",
    "Have your partner lay down and kiss them upside down the best you can.",
    "Give your partner a lesson on giving head to them with an object from the kitchen.",
    "Have your partner spank you as hard as they can.",
    "Whisper a sexy name in my ear that you’ve never called me but have thought about trying.",
    "Use a sex toy to try and get your partner in the mood.",
    "Have your partner blindfold you and touch you with a part of their body. If you guess what part of their body they’re touching you with, you get a special reward.",
    "Seduce your partner in a room where you have never had sex before."
]


# Define truths and dares for group
truths_group = [
    "If you had to make out with anyone in this room, who would it be and why?",
    "Play 'fuck, marry, kill' with three people in the room.",
    "Where is the craziest place you’ve ever had sex?",
    "Tell the group about a sexual fantasy you have.",
    "Who was the worst you’ve ever had and the best you’ve ever had?",
    "Read us your best sexting line in a sexy accent.",
    "What’s the kinkiest thing you’ve ever done in bed?",
    "What’s the most adventurous thing you want to try in bed?",
    "Would you rather have sex with someone 20 years older or 20 years younger?",
    "What’s the biggest lie you’ve told someone to get them into bed with you?",
    "How old were you when you lost your virginity and how did it go?",
    "Who was your first kiss?",
    "What’s a popular fetish that you would never want to try?",
    "Do you remember the first time you experienced an orgasm? Tell us about it.",
    "What’s your favorite body part on your body?",
    "If you could have one sexual superpower, what would it be?",
    "Would you sleep with your boss if you could?",
    "What’s the least amount of time you’ve gone between having sex with two different people?",
    "What’s the most amount of people you’ve kissed in one night?",
    "Have you ever been tempted to cheat on your significant other?",
    "What’s your body count?",
    "What’s your favorite position?",
    "What’s the smallest amount of time you’ve known someone before sleeping with them?",
    "Have you ever been caught having sex?",
    "What position is popular that you think is overrated?",
    "Do you prefer sex when you’re in love or when it’s a hot hookup?",
    "Do you think virginity is special?",
    "Who is the oddest person you’ve ever had a sexual fantasy about?",
    "Do you think there’s an age where someone becomes 'too old' to be a virgin?",
    "Who in the room do you think has slept with the most people?",
    "Do you think there should be a limit on the amount of people you sleep with in your lifetime or do you think that doesn’t matter?",
    "Have you ever had sex and immediately gotten up and left?",
    "Have you ever called someone 'Daddy' or been called 'Daddy' while having sex?",
    "What do you wish you had learned about sex way earlier than you did?",
    "What fictional character have you or could you have sexual fantasies about?"
]


dares_group = [
    "Message something bold to someone hot you’ve been wanting to get to know.",
    "Kiss someone in the room that you’re attracted to.",
    "Fake your best orgasm in front of the group.",
    "Leave a sexy voicemail for your ex to listen to.",
    "Pick a position and imitate it with the person to your right.",
    "Sexily lick the food of your choice off the finger of the person to your left.",
    "Do a naked lap around the neighborhood.",
    "Find a position online that you’ve never tried and act it out on furniture that’s in the room.",
    "Prank call someone and pretend to be a sex ad.",
    "Trace the lips of someone here and whisper something sexy.",
    "Do a mini strip tease by taking off some of your clothing in front of the group.",
    "For the next round, you have to keep your hand on the inner thigh of the person to your left.",
    "Post something raunchy on your preferred social media app and you can’t remove it until the next round is over.",
    "Give someone else in the group a sexy massage while talking dirty.",
    "If there’s water nearby, it’s time to go skinny dipping!",
    "Time to play spin the bottle! Kiss whoever the bottle lands on.",
    "Close your eyes while a few members of the group stand across from you. Walk with your hands open until you touch one of them, then kiss them wherever your hand touched.",
    "Give the person to your left an eskimo kiss.",
    "You’ve been naughty, time to be put in time out on someone’s lap for the next round.",
    "Pick something small to sexily feed someone else in the group.",
    "Leave the room while everyone in the group pours a shot. When you come back, pick a shot to take. Whoever poured that shot, you have to kiss.",
    "Talk in a raunchy accent until your next turn.",
    "Scroll blindly through your contacts and whoever you land on, say one sexy thing about them.",
    "Give your best impression of a naughty cop who’s trying to arrest someone for being too sexy.",
    "Give the person to your right a butterfly kiss.",
    "Wink and do your best sexy face for the group.",
    "Pretend to have awful sex with the person to your right.",
    "Send a bold, dirty message to someone you’ve hooked up with before.",
    "Call a phone sex line and pretend to have an odd fetish.",
    "Take a pen and paper and draw your penis or vagina.",
    "Facetime an old hookup. If they pick up, say something raunchy before hanging up.",
    "Fake a blowjob on a bottle.",
    "Describe your favorite position in detail but without saying what it is. See if the group can guess it!",
    "Perform a motorboat on someone. If you’re a girl, have someone do it to you."
]


# Initialize session state
if 'used_truths' not in st.session_state:
    st.session_state.used_truths = []
if 'used_dares' not in st.session_state:
    st.session_state.used_dares = []

st.title("💋 Spicy Night")

# Game mode selection
mode = st.radio("Are you playing as a couple or in a group?", ("Couple", "Group"))

# Options for Truth, Dare, or Both
option = st.radio("Do you want only Truth, only Dare, or Both?", ("Truth", "Dare", "Both"))

# Define appropriate lists
if mode == "Couple":
    truths = truths_couples
    dares = dares_couples
else:
    truths = truths_group
    dares = dares_group

# Button to generate truth or dare
if st.button("Generate!"):
    result = ""
    if option == "Truth":
        available_truths = list(set(truths) - set(st.session_state.used_truths))
        if available_truths:
            result = random.choice(available_truths)
            st.session_state.used_truths.append(result)
        else:
            result = "No more truths left! Reset to play again."
    elif option == "Dare":
        available_dares = list(set(dares) - set(st.session_state.used_dares))
        if available_dares:
            result = random.choice(available_dares)
            st.session_state.used_dares.append(result)
        else:
            result = "No more dares left! Reset to play again."
    else:  # Both
        available_truths = list(set(truths) - set(st.session_state.used_truths))
        available_dares = list(set(dares) - set(st.session_state.used_dares))
        if available_truths or available_dares:
            if random.choice([True, False]):
                if available_truths:
                    result = random.choice(available_truths)
                    st.session_state.used_truths.append(result)
                else:
                    result = random.choice(available_dares)
                    st.session_state.used_dares.append(result)
            else:
                if available_dares:
                    result = random.choice(available_dares)
                    st.session_state.used_dares.append(result)
                else:
                    result = random.choice(available_truths)
                    st.session_state.used_truths.append(result)
        else:
            result = "No more truths or dares left! Reset to play again."

    st.markdown(f"<h2 style='text-align: center; color: red;'>{result}</h2>", unsafe_allow_html=True)

# Reset button
if st.button("Reset Game"):
    st.session_state.used_truths = []
    st.session_state.used_dares = []
    st.write("Game has been reset!")
