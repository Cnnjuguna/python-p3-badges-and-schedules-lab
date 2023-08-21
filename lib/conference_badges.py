# NAMES = ["Guido", "Edsger", "Ada", "Charles", "Alan", "Grace", "Linus", "Matz"]

# BADGES = [
#     "Hello, my name is Guido.",
#     "Hello, my name is Edsger.",
#     "Hello, my name is Ada.",
#     "Hello, my name is Charles.",
#     "Hello, my name is Alan.",
#     "Hello, my name is Grace.",
#     "Hello, my name is Linus.",
#     "Hello, my name is Matz."
#   ]

# MESSAGES = [
#     "Hello, Guido! You'll be assigned to room 1!",
#     "Hello, Edsger! You'll be assigned to room 2!",
#     "Hello, Ada! You'll be assigned to room 3!",
#     "Hello, Charles! You'll be assigned to room 4!",
#     "Hello, Alan! You'll be assigned to room 5!",
#     "Hello, Grace! You'll be assigned to room 6!",
#     "Hello, Linus! You'll be assigned to room 7!",
#     "Hello, Matz! You'll be assigned to room 8!"
# ]


def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    BADGES = []
    for name in names:
        BADGES.append(f"Hello, my name is {name}.")
        # print(BADGES)
    return BADGES


def assign_rooms(names):
    MESSAGES = []  # an empty list to store the messages
    rooms = 7
    while rooms < len(names):
        MESSAGES.append(f"Hello, {names[rooms]}! You'll be assigned to room {index}!")
    return MESSAGES


def printer(names):
    return None
