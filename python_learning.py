def who_is_online(friends: list) -> dict:
    status_list = {}

    for friend in friends:
        username = friend["username"]                                       # variable to define a username
        group = "online"                                                    # standard group is set to online
        if friend["status"] == "online" and friend["lastActivity"] > 10:    # then we check if the user is online or away
            group = "away"                                                  # if so - we change the group
        elif friend["status"] == "offline":                                 # if he's not away, we check if he is offline
            group = "offline"                                               # if so - change the group

        if group not in status_list:                                        # if nothing has changed - the user is online
            status_list[group] = [username]                                 # if there is no such a group, we add one and add the user as a list
        else:
            status_list[group].append(username)                             # if the user has the status of the existing group, we add him to that group
    return status_list

print(who_is_online([{
  "username": "Alice",
  "status": "online",
  "lastActivity": 10
}, {
  "username": "Lucy",
  "status": "offline",
  "lastActivity": 22
}, {
  "username": "Bob",
  "status": "online",
  "lastActivity": 104
}]))