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
    for index, name in enumerate(names, start=1):
        room_message = f"Hello, {name}! You'll be assigned to room {index}!"
        MESSAGES.append(room_message)  # Add the message to the list
    return MESSAGES


assigned_messages = assign_rooms(["Collin, Pharell", "Jerry", "Brenda"])
for message in assigned_messages:
    print(message)


def printer(names):
    # Generating the messages using the batch_badge_creator() first
    badge_messages = batch_badge_creator(names)

    room_assign_messages = assign_rooms(names)

    for a_badge_message in badge_messages:
        print(a_badge_message)

    for a_room_message in room_assign_messages:
        print(a_room_message)


print(printer(["Collin, Pharell", "Jerry", "Brenda"]))
