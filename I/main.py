from __future__ import division

users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]

friendship = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user['friends'] = []

for i,j in friendship:
    users[i]['friends'].append(j)     
    users[j]['friends'].append(i) 


def numberOfFriends (user):
    '''quantos amigos o usuario tem'''
    return len(user['friends'])  #tamanho da lista!

totalConnections = sum(numberOfFriends(user) for user in users)


numUsers = len(users)
avgConnections = totalConnections / numUsers

#criar lista com (userId, numberOfFriends)
numFriendsById = [(user['id'], numberOfFriends(user)) for user in users] 
sorted(numFriendsById, key = lambda (userId, numberOfFriends): numberOfFriends, reverse = True)


    