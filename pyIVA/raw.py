Add participants
Adds specified participants to chat (available for chat creator only).

As a result, server event ChatRoomUsersChangedEvent is sent to all chat room participants and new system message is created and sent to all chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
REQUEST BODY SCHEMA: application/json
Array ()
Any of ArbitraryInterlocutorDTOContactInterlocutorDTOProfileInterlocutorDTO
email
string
phone
string
name
string
Responses
204 Success
POST
/chats/{chatRoomId}/participants/add
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
[
{
"email": "string",
"phone": "string",
"name": "string"
}
]

Chat events
Chat events
Responses
200 Subscribed
Callbacks
POST
ChatRoomMessageEventPOST
ChatRoomChangedEventPOST
ChatRoomMessageRemoveEventPOST
ChatRoomClearHistoryEventPOST
ChatRoomDeleteEventPOST
ChatRoomMessageEditEventPOST
ChatRoomMessageMarkEventPOST
ChatRoomUsersChangedEventPOST
ChatRoomLastReadAtChangeEventPOST
ChatRoomUserMessageStatusDateChangeEventPOST
ChatRoomTypingEvent
GET
/websocket/chat
Callback payload samples
Callback
POST: ChatRoomMessageEvent

Turn on notifications
Turns on visual and sound notifications about any changes in specified chat.

As a result, server event ChatRoomUsersChangedEvent is sent to all chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
Responses
204 Success
POST
/chats/{chatRoomId}/allow-notifications

Clear chat history
Removes all messages and attachments from the chat.
Operation is allowed for participants of peer-to-peer chats and for chat owners in group chats.

As a result, server event ChatRoomClearHistoryEvent is sent to all chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room id
Responses
204 Success
POST
/chats/{chatRoomId}/clear-history

Create group chat
Creates group chat with specified users.

As a result, system message is created and sent to all chat participants.
AUTHORIZATIONS:
IvcsAuthSession
REQUEST BODY SCHEMA: application/json
Array ()
Any of ArbitraryInterlocutorDTOContactInterlocutorDTOProfileInterlocutorDTO
email
string
phone
string
name
string
Responses
200 Chat room
POST
/chats/create-group-chat
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
[
{
"email": "string",
"phone": "string",
"name": "string"
}
]
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
"createdBy": "25a02396-1048-48f9-bf93-102d2fb7895e",
"createdAt": 0,
"historyStartFrom": 0,
"name": "string",
"lastMessageAt": 0,
"lastMessageUpdatedAt": 0,
"isGroupChat": true,
"chatAvatar": "b3dfff2c-fdb5-4692-8552-065b82e6b6d2",
"isChatHistoryAccessLimited": true,
"users": 
[
{
}
],
"call": 
{
"callId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"chatRoomId": "3ac3ce06-23ce-422a-a7b2-bab25934bb58",
"state": "INACTIVE",
"createdAt": 0,
"startedAt": 0,
"createdBy": "941396ff-e89b-44c5-9f30-6fd1b0a533ef"
}
}

Get chat
Returns information about chat room with or without number of unread messages.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
QUERY PARAMETERS
withUnreadCount
required
boolean
Include number of unread messages in response
Responses
200 Chat room
GET
/chats/{chatRoomId}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
"createdBy": "25a02396-1048-48f9-bf93-102d2fb7895e",
"createdAt": 0,
"historyStartFrom": 0,
"name": "string",
"lastMessageAt": 0,
"lastMessageUpdatedAt": 0,
"isGroupChat": true,
"chatAvatar": "b3dfff2c-fdb5-4692-8552-065b82e6b6d2",
"isChatHistoryAccessLimited": true,
"users": 
[
{
}
],
"call": 
{
"callId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"chatRoomId": "3ac3ce06-23ce-422a-a7b2-bab25934bb58",
"state": "INACTIVE",
"createdAt": 0,
"startedAt": 0,
"createdBy": "941396ff-e89b-44c5-9f30-6fd1b0a533ef"
},
"unreadMessagesCount": 0
}

Delete chat
Deletes chat room for all participants.
Operation is allowed for participants of peer-to-peer chats and for chat owners in group chats.

As a result, server event ChatRoomDeleteEvent is sent to all chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room id
Responses
204 Success
DELETE
/chats/{chatRoomId}

Update chat
Updates parameters of specified chat room (available for chat creator only).

As a result, server event ChatRoomUpdatedEvent is sent to all chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room id
REQUEST BODY SCHEMA: application/json
Chat room update parameters
name
string
isChatHistoryAccessLimited
boolean
chatAvatar
string <uuid>
Responses
204 Success
PATCH
/chats/{chatRoomId}
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"name": "string",
"isChatHistoryAccessLimited": true,
"chatAvatar": "b3dfff2c-fdb5-4692-8552-065b82e6b6d2"
}

Edit message
Edits specified message. Message can be edited by its owner only within 1 hour after sending it.

As a result, server event ChatRoomMessageEditEvent is sent to all chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
id
required
string <uuid>
Message ID
REQUEST BODY SCHEMA: application/json
Message data
message
required
string
Responses
204 Success
PATCH
/chats/{chatRoomId}/messages/{id}
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string"
}

Turn off notifications
Turns off visual and sound notifications about any changes in specified chat.

As a result, server event ChatRoomUsersChangedEvent is sent to all chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
Responses
204 Success
POST
/chats/{chatRoomId}/forbid-notifications

Forward messages
Forwards messages to specified chat rooms.

As a result, server event ChatRoomMessageEvent is sent to all chat room participants and push notification ChatRoomMessagePayload is sent to all registered devices of chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
REQUEST BODY SCHEMA: application/json
List of messages and chats
forwardMessageIds
Array of strings <uuid>
toChatRoomIds
Array of strings <uuid>
Responses
200 Created message
POST
/chats/forward-messages
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"forwardMessageIds": 
[
"497f6eca-6276-4993-bfeb-53cbbbba6f08"
],
"toChatRoomIds": 
[
"497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
[
{
"id": "08e3e69b-acf4-442e-8dcd-76f750451118",
"type": "SYSTEM",
"chatRoomId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"author": "08e3e69b-acf4-442e-8dcd-76f750451118",
"authorName": "string",
"authorAvatar": "08e3e69b-acf4-442e-8dcd-76f750451118",
"createdAt": 0,
"updatedAt": 0,
"message": "string",
"attachment": 
{
},
"isGroupChat": true,
"chatRoomName": "string",
"deleted": true,
"edited": true,
"forwardMessageAuthor": "08e3e69b-acf4-442e-8dcd-76f750451118",
"forwardMessageAuthorName": "string",
"forwardMessageCreatedAt": 0,
"systemMessageInfo": 
{
},
"repliedOn": 
{
},
"starred": true
}
]

Search attachments
Returns attachments by specified search criteria.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
REQUEST BODY SCHEMA: application/json
size
integer <int32>
Default: 50
searchCriteria
string
mimeTypes
Array of strings
excludeMimeTypes
boolean
offset
integer <int64> >= 0
Date (UNIX time in ms)
Responses
200 Requested messages attachments
POST
/chats/{chatRoomId}/chat-attachments/find-by-criteria
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"size": 50,
"searchCriteria": "string",
"mimeTypes": 
[
"string"
],
"excludeMimeTypes": true,
"offset": 0
}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

Get messages
Returns chat room messages by specified parameters. It can be used for searching messages.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
QUERY PARAMETERS
textContains
string
Search criteria
dateFrom
integer <int64>
Date from (UNIX time in ms)
dateTo
integer <int64>
Date to (UNIX time in ms)
size
integer <int32>
Default: 50
Result page size
orderAsc
boolean
Default: false
Order ascendancy
Responses
200 Requested messages
GET
/chats/{chatRoomId}/messages
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

Get messages changes
Returns chat room messages changes. If onlyChanged parameter is true that returns only changed messages.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
QUERY PARAMETERS
dateFrom
required
integer <int64>
Date from (UNIX time in ms)
size
integer <int32>
Default: 50
Result page size
onlyChanged
boolean
Default: false
Only changed
Responses
200 Requested messages changes
GET
/chats/{chatRoomId}/messages/changes
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

Get user starred messages
Returns chat room messages that were starred by user.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
QUERY PARAMETERS
textContains
string
Search criteria
dateFrom
integer <int64> >= 0
Date from (UNIX time in ms)
size
integer <int32> [ 1 .. 200 ]
Default: 50
Result slice limit. Should be more then 0.
Responses
200 Requested messages
404 Not found
GET
/chats/{chatRoomId}/messages/starred
Response samples
200404
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

Get muted chats
Returns chats for which notifications are muted.
AUTHORIZATIONS:
IvcsAuthSession
Responses
200 IDs of muted chats
GET
/chats/muted-chat-ids
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
[
"497f6eca-6276-4993-bfeb-53cbbbba6f08"
]

Get P2P chat
Returns or creates (if it doesn't exist) p2p chat with specified user. A user can be defined by 3 ways: contact ID, user profile ID or user contact data - name, email, phone (at least on field should be set).
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
contactId
string <uuid>
Contract ID
profileId
string <uuid>
Profile ID
name
string
User name
email
string
User email
phone
string
User phone
Responses
200 Chat room
GET
/chats/p2p
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
"createdBy": "25a02396-1048-48f9-bf93-102d2fb7895e",
"createdAt": 0,
"historyStartFrom": 0,
"name": "string",
"lastMessageAt": 0,
"lastMessageUpdatedAt": 0,
"isGroupChat": true,
"chatAvatar": "b3dfff2c-fdb5-4692-8552-065b82e6b6d2",
"isChatHistoryAccessLimited": true,
"users": 
[
{
}
],
"call": 
{
"callId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"chatRoomId": "3ac3ce06-23ce-422a-a7b2-bab25934bb58",
"state": "INACTIVE",
"createdAt": 0,
"startedAt": 0,
"createdBy": "941396ff-e89b-44c5-9f30-6fd1b0a533ef"
},
"unreadMessagesCount": 0
}

Get chats
Returns chat rooms with last message is less than specified date. Result is sorted in descending order by last message date.
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
olderThan
required
integer <int64>
Criteria date (UNIX time in ms)
size
integer <int32>
Default: 50
Result page size
Responses
200 Requested chats
GET
/chats
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true
}

Search chats
Returns chat rooms that contain specified search criteria in name. Result is sorted in descending order by last message date.
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
size
integer <int32>
Default: 50
Result page size
page
integer <int32>
Default: 0
Page number
searchCriteria
required
string
Search criteria
Responses
200 Found chats
GET
/chats/search
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true
}

Remove message
Removes specified message. Any chat participant can remove own message whereas chat owner can remove any message.

As a result, server event ChatRoomMessageRemoveEvent is sent to all chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
messageId
required
string <uuid>
Message ID
Responses
204 Success
DELETE
/chats/{chatRoomId}/messages/{messageId}

Remove message attachment
Removes message attachment with related message. Any chat participant can remove own message whereas chat owner can remove any message.

As a result, server event ChatRoomMessageRemoveEvent is sent to all chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
id
required
string <uuid>
Attachment ID
Responses
204 Success
DELETE
/chats/{chatRoomId}/chat-attachments/{id}

Remove messages
Removes specified messages. Any chat participant can remove own message whereas chat owner can remove any message.

As a result, server events ChatRoomMessageRemoveEvent for each message are sent to all chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
REQUEST BODY SCHEMA: application/json
Array ()
string <uuid>
Responses
204 Success
POST
/chats/{chatRoomId}/messages/remove
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
[
"497f6eca-6276-4993-bfeb-53cbbbba6f08"
]

Remove participants
Removes specified participants from chat (available for chat creator only).

As a result, server event ChatRoomUsersChangedEvent is sent to all chat room participants and new system message is created and sent to all chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
REQUEST BODY SCHEMA: application/json
Array ()
string <uuid>
Responses
204 Success
POST
/chats/{chatRoomId}/participants/remove
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
[
"497f6eca-6276-4993-bfeb-53cbbbba6f08"
]

Send audio message
Sends new audio message to chat room. This method can be also used for replying on another message. Audio attachment should be uploaded to the server before as usual file upload.
Following codecs for audio file are supported: g711, g722, aac, opus, speex, mp3.

As a result, server event ChatRoomMessageEvent is sent to all chat room participants and push notification ChatRoomMessagePayload is sent to all registered devices of chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
REQUEST BODY SCHEMA: application/json
Message data
replyOn
string <uuid>
attachmentId
required
string <uuid>
Responses
200 Created message
POST
/chats/{chatRoomId}/send-audio-message
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"replyOn": "49d10892-579c-4689-85f2-0a39915c45c2",
"attachmentId": "96b9bbac-86d3-4497-9e0c-1f8e3803eddb"
}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"id": "08e3e69b-acf4-442e-8dcd-76f750451118",
"type": "SYSTEM",
"chatRoomId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"author": "08e3e69b-acf4-442e-8dcd-76f750451118",
"authorName": "string",
"authorAvatar": "08e3e69b-acf4-442e-8dcd-76f750451118",
"createdAt": 0,
"updatedAt": 0,
"message": "string",
"attachment": 
{
"id": "08e3e69b-acf4-442e-8dcd-76f750451118",
"resourceId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"name": "string",
"createdOn": 0,
"format": "PDF",
"metaData": 
{
},
"mimeType": "string",
"fileSize": 0,
"convertingProgress": 0,
"conversionState": "NOT_SUPPORTED",
"ownerId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"ownerName": "string",
"messageId": "08e3e69b-acf4-442e-8dcd-76f750451118"
},
"isGroupChat": true,
"chatRoomName": "string",
"deleted": true,
"edited": true,
"forwardMessageAuthor": "08e3e69b-acf4-442e-8dcd-76f750451118",
"forwardMessageAuthorName": "string",
"forwardMessageCreatedAt": 0,
"systemMessageInfo": 
{
"messageType": "NONE",
"author": 
{
},
"users": 
[
],
"callDuration": 0
},
"repliedOn": 
{
"id": "08e3e69b-acf4-442e-8dcd-76f750451118",
"type": "SYSTEM",
"chatRoomId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"author": "08e3e69b-acf4-442e-8dcd-76f750451118",
"authorName": "string",
"authorAvatar": "08e3e69b-acf4-442e-8dcd-76f750451118",
"createdAt": 0,
"updatedAt": 0,
"message": "string",
"attachment": 
{
},
"isGroupChat": true,
"chatRoomName": "string",
"deleted": true,
"edited": true,
"forwardMessageAuthor": "08e3e69b-acf4-442e-8dcd-76f750451118",
"forwardMessageAuthorName": "string",
"forwardMessageCreatedAt": 0,
"systemMessageInfo": 
{
}
},
"starred": true
}

Send message
Sends new message to chat room. This method can be also used for replying on another message. If message are sent with attachment that the one should be uploaded to the server before.

As a result, server event ChatRoomMessageEvent is sent to all chat room participants and push notification ChatRoomMessagePayload is sent to all registered devices of chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
REQUEST BODY SCHEMA: application/json
Message data
message
string
replyOn
string <uuid>
attachmentId
string <uuid>
Responses
200 Created message
POST
/chats/{chatRoomId}/send-message
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"replyOn": "49d10892-579c-4689-85f2-0a39915c45c2",
"attachmentId": "96b9bbac-86d3-4497-9e0c-1f8e3803eddb"
}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"id": "08e3e69b-acf4-442e-8dcd-76f750451118",
"type": "SYSTEM",
"chatRoomId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"author": "08e3e69b-acf4-442e-8dcd-76f750451118",
"authorName": "string",
"authorAvatar": "08e3e69b-acf4-442e-8dcd-76f750451118",
"createdAt": 0,
"updatedAt": 0,
"message": "string",
"attachment": 
{
"id": "08e3e69b-acf4-442e-8dcd-76f750451118",
"resourceId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"name": "string",
"createdOn": 0,
"format": "PDF",
"metaData": 
{
},
"mimeType": "string",
"fileSize": 0,
"convertingProgress": 0,
"conversionState": "NOT_SUPPORTED",
"ownerId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"ownerName": "string",
"messageId": "08e3e69b-acf4-442e-8dcd-76f750451118"
},
"isGroupChat": true,
"chatRoomName": "string",
"deleted": true,
"edited": true,
"forwardMessageAuthor": "08e3e69b-acf4-442e-8dcd-76f750451118",
"forwardMessageAuthorName": "string",
"forwardMessageCreatedAt": 0,
"systemMessageInfo": 
{
"messageType": "NONE",
"author": 
{
},
"users": 
[
],
"callDuration": 0
},
"repliedOn": 
{
"id": "08e3e69b-acf4-442e-8dcd-76f750451118",
"type": "SYSTEM",
"chatRoomId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"author": "08e3e69b-acf4-442e-8dcd-76f750451118",
"authorName": "string",
"authorAvatar": "08e3e69b-acf4-442e-8dcd-76f750451118",
"createdAt": 0,
"updatedAt": 0,
"message": "string",
"attachment": 
{
},
"isGroupChat": true,
"chatRoomName": "string",
"deleted": true,
"edited": true,
"forwardMessageAuthor": "08e3e69b-acf4-442e-8dcd-76f750451118",
"forwardMessageAuthorName": "string",
"forwardMessageCreatedAt": 0,
"systemMessageInfo": 
{
}
},
"starred": true
}

Turn on/off notifications from user
Turns on/off visual and sound notifications about any changes in p2p chat with specified user.

As a result, server events ChatRoomUsersChangedEvent for each mesages are sent to all chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
REQUEST BODY SCHEMA: application/json
interlocutor
ProfileInterlocutorDTO (object) or ContactInterlocutorDTO (object) or ArbitraryInterlocutorDTO (object) (InterlocutorDTO)
allowNotifications
boolean
Responses
204 Success
POST
/chats/p2p-chat-notifications
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"interlocutor": 
{
"profileId": "faebe71b-2bf8-4bdb-9b67-258e4d6aa00a"
},
"allowNotifications": true
}

Star messages
Stars chat room messages for current user.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
REQUEST BODY SCHEMA: application/json
IDs of messages
Array ()
string <uuid>
Responses
204 Success
404 Not found
POST
/chats/{chatRoomId}/star-messages
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
[
"497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
Response samples
404
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Notify about typing
Notifies about typing message process in chat room.

Recommended behavior: Each client notifies the server about the process of entering text in the message input field in the chat every 4.5 seconds, and the server sends this event to the rest of the chat participants.
When a corresponding event is received, each client graphically displays this process for 5.2 seconds, and if no new event was received, then hides the corresponding graphical display.

As a result, server event ChatRoomTypingEvent are sent to all chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
Responses
204 Success
POST
/chats/{chatRoomId}/typing

Unstar messages
Unstars chat room messages for current user.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
REQUEST BODY SCHEMA: application/json
IDs of messages
Array ()
string <uuid>
Responses
204 Success
404 Not found
POST
/chats/{chatRoomId}/unstar-messages
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
[
"497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
Response samples
404
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Update participant
Updates participant properties. Only chat owner can perform this action.

As a result, server event ChatRoomUsersChangedEvent is sent to all chat room participants
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
profileId
required
string <uuid>
Profile ID
REQUEST BODY SCHEMA: application/json
role
required
string
Enum: "OWNER" "ADMIN" "REGULAR"
Responses
204 Success
PATCH
/chats/{chatRoomId}/participants/{profileId}
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"role": "OWNER"
}

Notify about read
Notifies about read messages which have date less or equal than specified date.

As a result, server event ChatRoomLastReadAtChangeEvent and push notification ChatRoomLastReadAtChangedPayload is sent to all another devices of current user and ChatRoomUserMessageStatusDateChangeEvent is sent to all chat room participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
REQUEST BODY SCHEMA: application/json
lastReadAt
integer <int64> >= 0
UNIX time
Responses
204 Success
POST
/chats/{chatRoomId}/last-read-at
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"lastReadAt": 0
}

Get call
Returns existed call in given chat with participants in DIALING and CONNECTED sates.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
Responses
200 Chat call info
GET
/chat-calls/{chatRoomId}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"callId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"chatRoomId": "3ac3ce06-23ce-422a-a7b2-bab25934bb58",
"state": "INACTIVE",
"createdAt": 0,
"startedAt": 0,
"createdBy": "941396ff-e89b-44c5-9f30-6fd1b0a533ef",
"participants": 
[
{
}
],
"presentation": 
{
"ownerId": "4d206909-730f-409a-88f6-dcfaa8fc28cc",
"dataSubscribeUri": "string"
}
}

Join call
Starts new call or/and joins current user to existing one in specified chat.

In case of new call server event ChatRoomCallInvitationEvent and push notification ChatRoomCallPayload are sent to all chat participants.
In case of joining existing call server event ChatRoomCallParticipantJoinEvent is sent to all call participants and push notification ChatRoomCallAnsweredPayload is sent to registered devices of currently joined participant.
If call state is changed during joining process (for instance, from DIALING to ACTIVE) that server event ChatRoomCallStateChangeEvent is sent to all chat participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
REQUEST BODY SCHEMA: application/json
Join initial data
mediaState
required
string
Enum: "NONE" "AUDIO" "VIDEO" "AUDIO_VIDEO"
Initial participant media state
eventBusId
required
string
Comet event bus id
tokenId
string
Some unique token that represents current device in call
Responses
200 Chat call join info
POST
/chat-calls/{chatRoomId}/join
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"mediaState": "NONE",
"eventBusId": "string",
"tokenId": "string"
}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"chatRoom": 
{
"id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
"createdBy": "25a02396-1048-48f9-bf93-102d2fb7895e",
"createdAt": 0,
"historyStartFrom": 0,
"name": "string",
"lastMessageAt": 0,
"lastMessageUpdatedAt": 0,
"isGroupChat": true,
"chatAvatar": "b3dfff2c-fdb5-4692-8552-065b82e6b6d2",
"isChatHistoryAccessLimited": true,
"users": 
[
],
"call": 
{
}
},
"participants": 
[
{
}
],
"presentation": 
{
"ownerId": "4d206909-730f-409a-88f6-dcfaa8fc28cc",
"dataSubscribeUri": "string"
},
"publishUrl": "string"
}

Chat call events
Chat call events
Responses
200 Subscribed
Callbacks
POST
ChatRoomCallInvitationEventPOST
ChatRoomCallParticipantJoinEventPOST
ChatRoomCallParticipantLeaveEventPOST
ChatRoomCallParticipantMediaStateChangeEventPOST
ChatRoomCallStateChangeEventPOST
ChatRoomCallTransferredEventPOST
ChatRoomCallPresentationStateChangeEvent
GET
/websockets/chatCallEvents
Callback payload samples
Callback
POST: ChatRoomCallInvitationEvent

Leave call
Removes current user from active call in specified chat.

As a result, server event ChatRoomCallParticipantLeaveEvent is sent to all call participants and push notification ChatRoomCallAnsweredPayload is sent to registered devices of currently left participant.
If call state is changed during leaving process (for instance, from ACTIVE to INACTIVE) that server event ChatRoomCallStateChangeEvent is sent to all chat participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
Responses
204 Success
POST
/chat-calls/{chatRoomId}/leave

Change media state
Change media state of own outgoing media stream.

As a result, server event ChatRoomCallParticipantMediaStateChangeEvent is sent to all call participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
REQUEST BODY SCHEMA: application/json
mediaState
required
string
Enum: "NONE" "AUDIO" "VIDEO" "AUDIO_VIDEO"
Responses
204 Success
POST
/chat-calls/{chatRoomId}/media-state
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"mediaState": "NONE"
}

Start screen sharing
Starts secondary stream for screen sharing content of current participant.

If there was any other screen demonstration it would be replaced be this one.
Each new participant on join to call will get information about existence and state of this presentation.

As a result, server event ChatRoomCallPresentationStateChangeEvent is sent to all call participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
Responses
204 Success
POST
/chat-calls/{chatRoomId}/demonstration/screenshare/start

Stop screen sharing
Stops secondary stream for screen sharing content of current participant.

As a result, server event ChatRoomCallPresentationStateChangeEvent is sent to all call participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
chatRoomId
required
string <uuid>
Chat room ID
Responses
204 Success
POST
/chat-calls/{chatRoomId}/demonstration/screenshare/stop

Create conference
Creates conference planned in specified time.

As a result, server event ConferenceCreatedEvent is sent to owner and ConferenceInvitationEvent is sent to rest invited participants.
AUTHORIZATIONS:
IvcsAuthSession
REQUEST BODY SCHEMA: application/json
description
string <= 2048 characters
conferenceTemplateId
string <uuid>
Conference template ID. If it is empty that system default conference template is used.
settings
object (ConferenceCreateSettingsRestDTO)
Conference settings. These settings overrides corresponding settings from specified conference template.
subscriptionId
string <uuid>
User subscription ID. If it is empty that first suitable active user subscription is used.
participants
Array of objects (ConferenceParticipantInvitationRestDTO)
Participants of planned conference. Participant for owner is added by default on server side.
guestPasscode
string [ 4 .. 8 ] characters
Passcode for guest entrance by link. Only digits are allowed.
speakerPasscode
string [ 4 .. 8 ] characters
Passcode for speaker entrance by link. Only digits are allowed.
name
required
string <= 1024 characters
startDate
required
integer <int64> >= 0
Conference start date (UNIX time in ms)
duration
integer <int64> [ 300000 .. 86400000 ]
Default: 3600000
Conference duration (in ms)
schedule
object (ScheduleRestDTO)
Schedule for periodical conference
Responses
200 First conference session
POST
/conferences
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"description": "string",
"conferenceTemplateId": "4e39ad17-49b4-47f1-8776-29503b5f83be",
"settings": 
{
"runType": "AUTO",
"features": 
[
],
"joinRestriction": "ANYONE",
"attendeePermissions": 
[
],
"attendeeMediaState": "NONE"
},
"subscriptionId": "d079718b-ff63-45dd-947b-4950c023750f",
"participants": 
[
{
}
],
"guestPasscode": "string",
"speakerPasscode": "string",
"name": "string",
"startDate": 0,
"duration": 3600000,
"schedule": 
{
"periodicityType": "DAILY",
"daysOfWeek": 
[
],
"dayNumber": 1,
"weekNumber": 1,
"monthNumber": 1
}
}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"conferenceSessionId": "2df2d749-63a9-4bdf-8d0c-33caa5c48e90",
"conferenceId": "5dda8c14-0f3e-4e73-ba90-c90721c159fe",
"name": "string",
"description": "string",
"createDate": 0,
"updateDate": 0,
"lastMediaSessionStartDate": 0,
"actualStartDate": 0,
"state": "NO_STARTED",
"room": true,
"deleted": true,
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"ownerName": "string",
"ownerAvatarId": "eb58ab5a-1793-408a-87e5-27c981e508d7",
"conferenceNumber": 0,
"settings": 
{
"runType": "AUTO",
"conferenceType": "EQUITABLE_CONVERSATION",
"attendeeSubscribeLimit": "NONE",
"sharingLevel": "ALL_PARTICIPANTS",
"features": 
[
]
},
"isAdHocEvent": true,
"participantsCount": 0,
"onlineParticipantsCount": 0,
"participants": 
[
{
}
],
"startDate": 0,
"duration": 0,
"schedule": 
{
"periodicityType": "DAILY",
"daysOfWeek": 
[
],
"dayNumber": 1,
"weekNumber": 1,
"monthNumber": 1
},
"sessionNumber": 0
}

Common events
Common events
Responses
200 Subscribed
Callbacks
POST
ConferenceCreatedEventPOST
ConferenceChangedEventPOST
ConferenceSessionChangedEventPOST
ConferenceSessionOnlineParticipantsCountChangeEventPOST
ConferenceRemovedEventPOST
ConferenceSessionRemovedEvent
GET
/websocket/commonConferenceEvents

Invitation events
Invitation events
Responses
200 Subscribed
Callbacks
POST
ConferenceInvitationEventPOST
ConferenceSessionInvitationEventPOST
ConferenceParticipantRemovedNotificationEventPOST
ConferenceSessionParticipantRemovedNotificationEventPOST
ConferenceParticipantInvitationResponseEventPOST
ConferenceSessionParticipantInvitationResponseEvent
GET
/websocket/conferenceInvitationEvents

Delete conference
Deletes given conference with all child sessions (in case of conference is periodical). User should be either moderator.
If domain setting prohibits to delete conference records then sessions without records will be deleted and others left as is.
If conference has active session then ConferenceSessionFinishedEvent is sent to its participants.
After removal either ConferenceRemovedEvent (if all conference session will be removed) or ConferenceSessionRemovedEvent (if specified conference sessions will be removed) will be sent to all participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceId
required
string <uuid>
Responses
204 Success
400 reason = DELETED, type = ConferenceEditException - if conference has already been deleted
DELETE
/conferences/{conferenceId}

Common events
Common events
Responses
200 Subscribed
Callbacks
POST
ConferenceSessionJoinDataChangedEventPOST
ActiveConferenceSessionChangedEventPOST
PublishPresetsChangedEventPOST
ConferenceSessionRecordingStateChangedEventPOST
ConferenceSessionTranscriptionStateChangedEventPOST
ForwardToAnotherConferenceSessionEventPOST
ConferenceSessionFinishedEvent
GET
/websocket/commonActiveConferenceEvents

Respond on invitation
Responds on invitation to conference. If it is periodical conference that response belongs to all sessions of conference.

As a result, server event ConferenceSessionParticipantInvitationResponseEvent is sent to current user for all (created) conference sessions.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceId
required
string <uuid>
Conference ID
REQUEST BODY SCHEMA: application/json
Invitation response
response
required
string
Enum: "NONE" "APPROVE" "REJECT" "MAYBE"
Responses
204 Success
POST
/conferences/{conferenceId}/respond-on-invitation
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"response": "NONE"
}

Quick start conference
Creates non periodical conference and starts it now (i.e. changes it state to ACTIVE).

As a result, server event ConferenceCreatedEvent is sent to owner and ConferenceSessionChangedEvent is sent to all invited participants.
AUTHORIZATIONS:
IvcsAuthSession
REQUEST BODY SCHEMA: application/json
description
string <= 2048 characters
conferenceTemplateId
string <uuid>
Conference template ID. If it is empty that system default conference template is used.
settings
object (ConferenceCreateSettingsRestDTO)
Conference settings. These settings overrides corresponding settings from specified conference template.
subscriptionId
string <uuid>
User subscription ID. If it is empty that first suitable active user subscription is used.
participants
Array of objects (ConferenceParticipantInvitationRestDTO)
Participants of planned conference. Participant for owner is added by default on server side.
guestPasscode
string [ 4 .. 8 ] characters
Passcode for guest entrance by link. Only digits are allowed.
speakerPasscode
string [ 4 .. 8 ] characters
Passcode for speaker entrance by link. Only digits are allowed.
name
string <= 1024 characters
duration
integer <int64> [ 300000 .. 86400000 ]
Default: 3600000
Conference duration (in ms)
Responses
200 Created conference session
POST
/conferences/start-now
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"description": "string",
"conferenceTemplateId": "4e39ad17-49b4-47f1-8776-29503b5f83be",
"settings": 
{
"runType": "AUTO",
"features": 
[
],
"joinRestriction": "ANYONE",
"attendeePermissions": 
[
],
"attendeeMediaState": "NONE"
},
"subscriptionId": "d079718b-ff63-45dd-947b-4950c023750f",
"participants": 
[
{
}
],
"guestPasscode": "string",
"speakerPasscode": "string",
"name": "string",
"duration": 3600000
}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"conferenceSessionId": "2df2d749-63a9-4bdf-8d0c-33caa5c48e90",
"conferenceId": "5dda8c14-0f3e-4e73-ba90-c90721c159fe",
"name": "string",
"description": "string",
"createDate": 0,
"updateDate": 0,
"lastMediaSessionStartDate": 0,
"actualStartDate": 0,
"state": "NO_STARTED",
"room": true,
"deleted": true,
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"ownerName": "string",
"ownerAvatarId": "eb58ab5a-1793-408a-87e5-27c981e508d7",
"conferenceNumber": 0,
"settings": 
{
"runType": "AUTO",
"conferenceType": "EQUITABLE_CONVERSATION",
"attendeeSubscribeLimit": "NONE",
"sharingLevel": "ALL_PARTICIPANTS",
"features": 
[
]
},
"isAdHocEvent": true,
"participantsCount": 0,
"onlineParticipantsCount": 0,
"participants": 
[
{
}
],
"startDate": 0,
"duration": 0,
"schedule": 
{
"periodicityType": "DAILY",
"daysOfWeek": 
[
],
"dayNumber": 1,
"weekNumber": 1,
"monthNumber": 1
},
"sessionNumber": 0
}

Create room
Creates virtual conference room (room is a conference session without start and end).

As a result, server event ConferenceCreatedEvent is sent to owner and ConferenceInvitationEvent is sent to rest invited participants.
AUTHORIZATIONS:
IvcsAuthSession
REQUEST BODY SCHEMA: application/json
description
string <= 2048 characters
conferenceTemplateId
string <uuid>
Conference template ID. If it is empty that system default conference template is used.
settings
object (ConferenceCreateSettingsRestDTO)
Conference settings. These settings overrides corresponding settings from specified conference template.
subscriptionId
string <uuid>
User subscription ID. If it is empty that first suitable active user subscription is used.
participants
Array of objects (ConferenceParticipantInvitationRestDTO)
Participants of planned conference. Participant for owner is added by default on server side.
guestPasscode
string [ 4 .. 8 ] characters
Passcode for guest entrance by link. Only digits are allowed.
speakerPasscode
string [ 4 .. 8 ] characters
Passcode for speaker entrance by link. Only digits are allowed.
name
required
string <= 1024 characters
Responses
200 Created room
POST
/rooms
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"description": "string",
"conferenceTemplateId": "4e39ad17-49b4-47f1-8776-29503b5f83be",
"settings": 
{
"runType": "AUTO",
"features": 
[
],
"joinRestriction": "ANYONE",
"attendeePermissions": 
[
],
"attendeeMediaState": "NONE"
},
"subscriptionId": "d079718b-ff63-45dd-947b-4950c023750f",
"participants": 
[
{
}
],
"guestPasscode": "string",
"speakerPasscode": "string",
"name": "string"
}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"conferenceSessionId": "2df2d749-63a9-4bdf-8d0c-33caa5c48e90",
"conferenceId": "5dda8c14-0f3e-4e73-ba90-c90721c159fe",
"name": "string",
"description": "string",
"createDate": 0,
"updateDate": 0,
"lastMediaSessionStartDate": 0,
"actualStartDate": 0,
"state": "NO_STARTED",
"room": true,
"deleted": true,
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"ownerName": "string",
"ownerAvatarId": "eb58ab5a-1793-408a-87e5-27c981e508d7",
"conferenceNumber": 0,
"settings": 
{
"runType": "AUTO",
"conferenceType": "EQUITABLE_CONVERSATION",
"attendeeSubscribeLimit": "NONE",
"sharingLevel": "ALL_PARTICIPANTS",
"features": 
[
]
},
"isAdHocEvent": true,
"participantsCount": 0,
"onlineParticipantsCount": 0,
"participants": 
[
{
}
]
}

Get conference session public info by ID
Returns public information about conference session by it's ID.
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session Id.
Responses
200 Conference session information
404 Conference session is not found
GET
/public/conference-sessions/{conferenceSessionId}
Response samples
200404
Content type
application/json
Copy
Expand all Collapse all
{
"conferenceSessionId": "2df2d749-63a9-4bdf-8d0c-33caa5c48e90",
"runType": "AUTO",
"conferenceId": "5dda8c14-0f3e-4e73-ba90-c90721c159fe",
"name": "string",
"description": "string",
"conferenceNumber": 0,
"createDate": 0,
"updateDate": 0,
"lastMediaSessionStartDate": 0,
"startDate": 0,
"duration": 0,
"schedule": 
{
"periodicityType": "DAILY",
"daysOfWeek": 
[
],
"dayNumber": 0,
"weekNumber": 0,
"monthNumber": 0
},
"ownerName": "string",
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"ownerAvatarId": "eb58ab5a-1793-408a-87e5-27c981e508d7",
"currentUserRoles": 
[
"ATTENDEE"
],
"isAllowRecordAccess": true,
"isAllowUploadDocumentAccess": true,
"countUsers": 0,
"countOnlineUsers": 0,
"periodical": true,
"sessionNumber": 0,
"moderators": 
[
{
}
],
"onlySessionModerator": true,
"allSessionsParticipant": true,
"state": "NO_STARTED",
"inviteResponseType": "NONE",
"hasQuestionnaire": true,
"hasFinishedInquiry": true,
"hasRecords": true,
"hasAttachments": true,
"actualStartDate": 0,
"roomStartDate": 0,
"hidePoll": true,
"deleted": true,
"room": true,
"selfRegistrationEnabled": true,
"selfRegistrationActive": true,
"subscriptionActive": true,
"guestAllowed": true,
"isPasscodeRequired": true,
"conferenceType": "EQUITABLE_CONVERSATION",
"sharingLevel": "ALL_PARTICIPANTS",
"attendeeSubscribeLimit": "NONE",
"hasVVoIPSupport": true,
"canBeRestored": true,
"timeIntervalForRestore": 0,
"isAdHocEvent": true
}

Get conference session public info by parameters
Returns public information about conference session by it's ticket token (it can be useful during entering to event by ticket link).
Or returns information about conference session by it's planned conference id and session number.
QUERY PARAMETERS
token
string
Conference session ticket token
conferenceId
string <uuid>
Conference Id
sessionNumber
integer <int32>
Default: 1
Session number
Responses
200 Conference session information
404 Conference session is not found
GET
/public/conference-sessions
Response samples
200404
Content type
application/json
Copy
Expand all Collapse all
{
"conferenceSessionId": "2df2d749-63a9-4bdf-8d0c-33caa5c48e90",
"runType": "AUTO",
"conferenceId": "5dda8c14-0f3e-4e73-ba90-c90721c159fe",
"name": "string",
"description": "string",
"conferenceNumber": 0,
"createDate": 0,
"updateDate": 0,
"lastMediaSessionStartDate": 0,
"startDate": 0,
"duration": 0,
"schedule": 
{
"periodicityType": "DAILY",
"daysOfWeek": 
[
],
"dayNumber": 0,
"weekNumber": 0,
"monthNumber": 0
},
"ownerName": "string",
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"ownerAvatarId": "eb58ab5a-1793-408a-87e5-27c981e508d7",
"currentUserRoles": 
[
"ATTENDEE"
],
"isAllowRecordAccess": true,
"isAllowUploadDocumentAccess": true,
"countUsers": 0,
"countOnlineUsers": 0,
"periodical": true,
"sessionNumber": 0,
"moderators": 
[
{
}
],
"onlySessionModerator": true,
"allSessionsParticipant": true,
"state": "NO_STARTED",
"inviteResponseType": "NONE",
"hasQuestionnaire": true,
"hasFinishedInquiry": true,
"hasRecords": true,
"hasAttachments": true,
"actualStartDate": 0,
"roomStartDate": 0,
"hidePoll": true,
"deleted": true,
"room": true,
"selfRegistrationEnabled": true,
"selfRegistrationActive": true,
"subscriptionActive": true,
"guestAllowed": true,
"isPasscodeRequired": true,
"conferenceType": "EQUITABLE_CONVERSATION",
"sharingLevel": "ALL_PARTICIPANTS",
"attendeeSubscribeLimit": "NONE",
"hasVVoIPSupport": true,
"canBeRestored": true,
"timeIntervalForRestore": 0,
"isAdHocEvent": true
}

Get conference join info
Returns conference session information for following join by it's short ID.
QUERY PARAMETERS
conferenceNumber
required
integer <int64>
Short conference ID
Responses
200 Conference session information for following join
404 Conference session is not found
GET
/public/conference-sessions/join-info
Response samples
200404
Content type
application/json
Copy
Expand all Collapse all
{
"conferenceSessionInfo": 
{
"conferenceSessionId": "2df2d749-63a9-4bdf-8d0c-33caa5c48e90",
"runType": "AUTO",
"conferenceId": "5dda8c14-0f3e-4e73-ba90-c90721c159fe",
"name": "string",
"description": "string",
"conferenceNumber": 0,
"createDate": 0,
"updateDate": 0,
"lastMediaSessionStartDate": 0,
"startDate": 0,
"duration": 0,
"schedule": 
{
},
"ownerName": "string",
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"ownerAvatarId": "eb58ab5a-1793-408a-87e5-27c981e508d7",
"currentUserRoles": 
[
],
"isAllowRecordAccess": true,
"isAllowUploadDocumentAccess": true,
"countUsers": 0,
"countOnlineUsers": 0,
"periodical": true,
"sessionNumber": 0,
"moderators": 
[
],
"onlySessionModerator": true,
"allSessionsParticipant": true,
"state": "NO_STARTED",
"inviteResponseType": "NONE",
"hasQuestionnaire": true,
"hasFinishedInquiry": true,
"hasRecords": true,
"hasAttachments": true,
"actualStartDate": 0,
"roomStartDate": 0,
"hidePoll": true,
"deleted": true,
"room": true,
"selfRegistrationEnabled": true,
"selfRegistrationActive": true,
"subscriptionActive": true,
"guestAllowed": true,
"isPasscodeRequired": true,
"conferenceType": "EQUITABLE_CONVERSATION",
"sharingLevel": "ALL_PARTICIPANTS",
"attendeeSubscribeLimit": "NONE",
"hasVVoIPSupport": true,
"canBeRestored": true,
"timeIntervalForRestore": 0,
"isAdHocEvent": true
},
"conferenceSystemToken": "string",
"conferenceNumber": 0
}

Get conference session personal info
Returns conference session info including personal participation data.

Method is available only for invited or connected participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
Responses
200 Found conference session
400 Bad request
500 Internal server error
GET
/conference-sessions/{conferenceSessionId}
Response samples
200400500
Content type
application/json
Example
ConferenceSessionPersonalSummaryInfoRestDTO
Copy
Expand all Collapse all
{
"conferenceSessionId": "2df2d749-63a9-4bdf-8d0c-33caa5c48e90",
"conferenceId": "5dda8c14-0f3e-4e73-ba90-c90721c159fe",
"name": "string",
"description": "string",
"createDate": 0,
"updateDate": 0,
"lastMediaSessionStartDate": 0,
"actualStartDate": 0,
"state": "NO_STARTED",
"room": true,
"deleted": true,
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"ownerName": "string",
"ownerAvatarId": "eb58ab5a-1793-408a-87e5-27c981e508d7",
"settings": 
{
"runType": "AUTO",
"conferenceType": "EQUITABLE_CONVERSATION",
"attendeeSubscribeLimit": "NONE",
"sharingLevel": "ALL_PARTICIPANTS",
"features": 
[
]
},
"invitedParticipantsCount": 0,
"onlineParticipantsCount": 0,
"conferenceNumber": 0,
"personalParticipationInfo": 
{
"conferenceSessionParticipantId": "13159501-abd3-4d37-abef-2c526afe320a",
"conferenceSessionRoles": 
[
],
"conferenceSessionInviteResponse": "NONE",
"conferenceParticipantId": "452fe6b7-3e3b-4e4b-afff-342002752acc",
"conferenceRoles": 
[
],
"conferenceInviteResponse": "NONE"
},
"startDate": 0,
"duration": 0,
"schedule": 
{
"periodicityType": "DAILY",
"daysOfWeek": 
[
],
"dayNumber": 1,
"weekNumber": 1,
"monthNumber": 1
},
"sessionNumber": 0
}

Delete conference session
Deletes given conference session. If conference is periodical then rest sessions of conference are not changed.
User should have moderator role.
If conference session is active then ConferenceSessionFinishedEvent is sent to its participants.
After removal ConferenceSessionRemovedEvent will be sent to all conference participants.
If conference is not periodical then ConferenceRemovedEvent also will be sent to all conference participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Responses
204 Success
400 reason = DELETED, type = ConferenceEditException - if conference has been already deleted
reason = CAN_NOT_DELETE_SESSION_WITH_RECORD, type = ConferenceEditException - if conference has records which are not allowed to be deleted
DELETE
/conference-sessions/{conferenceSessionId}

Update conference session
Updates specified parameters of conference session. Only moderators can update conference session parameters.

As a result, following server events are sent depending on the parameters being changed:
- ConferenceSessionChangedEvent;
- ActiveConferenceSessionChangedEvent;
- ConferenceSessionJoinDataChangedEvent;
- ConferenceSessionParticipantPermissionsChangeEvent;
- MediaParticipantStateChangedEvent;
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
REQUEST BODY SCHEMA: application/json
Set of parameters to be updated for specified conference session. Absence of particular parameter means that this property is not updated.
name
string [ 1 .. 1024 ] characters
New name for conference session
description
object (NullableParameterDescription) <= 2048 characters
New description for conference session
regenerateConferenceNumber
boolean
Specify true to regenerate conference number (short ID)
regenerateJoinLinks
Array of strings
Items Enum: "ATTENDEE" "INTERPRETER" "SPEAKER" "MODERATOR"
Specify participant role types to regenerate specified join links
passcodes
object (SystemTicketPasscodesRestDTO)
Passcodes for guest and speaker links are updated at the same time, i.e. absence one of the passcodes means that the passcode for given link will be cleared.
features
Array of objects (MapEntryRestDTOConferenceFeatureTypeBoolean)
List of conference features to enable/disable (supported features for edit: LOBBY_ROOM, MUTE_EXTERNAL_NOTIFICATIONS, CLEAR_ROOM_RESOURCES_AFTER_PARTICIPANTS_EXIT (for rooms only))
attendeePermissions
Array of strings
Items Enum: "SPEAKER_OTHER" "RECORD_ACCESS" "DOWNLOAD_DOCUMENTS" "UPLOAD_DOCUMENT" "BOARD_DRAWING" "CHAT_SEND_WITHOUT_PREMODERATION" "POLLING_CREATION" "INVITING_PARTICIPANTS" "MODERATOR_OTHER" "SEND_REQUEST_REMOTE_ACCESS" "DEMONSTRATE_DOCUMENTS" "PUBLISH_HTTP_REFERENCE_IN_CHAT" "PUBLISH_MESSAGES_IN_CHAT" "DOWNLOAD_RECORD" "RECEIVE_MEDIA"
Attendee permissions
attendeeMediaState
string
Enum: "NONE" "AUDIO" "VIDEO" "AUDIO_VIDEO"
Attendee publish media permissions
activePreset
string
Enum: "LOWEST" "LOW" "NORMAL" "FINE" "FINEST"
Publish video quality preset (actually, publish video quality limit) for all participant
joinRestriction
string
Enum: "ANYONE" "INVITED_OR_REGISTERED" "INVITED"
Join restrictions for conference
sharingLevel
string
Enum: "ALL_PARTICIPANTS" "ONLY_MODERATORS"
Sharing level for links
duration
integer <int64> [ 300000 .. 86400000 ]
Duration of conference session (in ms)
startDate
integer <int64> >= 0
Date of conference session start. Should not be less than current time.
participants
object (ConferenceSessionParticipantsUpdateRestDTO)
Changes for invited participants
Responses
204 Success
PATCH
/conference-sessions/{conferenceSessionId}
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"name": "string",
"description": 
{
"value": "string"
},
"regenerateConferenceNumber": true,
"regenerateJoinLinks": 
[
"ATTENDEE"
],
"passcodes": 
{
"guestPasscode": "string",
"speakerPasscode": "string"
},
"features": 
[
{
}
],
"attendeePermissions": 
[
"SPEAKER_OTHER"
],
"attendeeMediaState": "NONE",
"activePreset": "LOWEST",
"joinRestriction": "ANYONE",
"sharingLevel": "ALL_PARTICIPANTS",
"duration": 300000,
"startDate": 0,
"participants": 
{
"addedParticipants": 
[
],
"changedParticipants": 
[
],
"removedParticipants": 
[
]
}
}

Participants events
Participants events
Responses
200 Subscribed
Callbacks
POST
ConferenceSessionParticipantDataChangeEventPOST
OwnConferenceSessionParticipantMediaSettingsChangeEventPOST
ConferenceSessionParticipantJoinEventPOST
ConferenceSessionParticipantLeaveEventPOST
ConferenceSessionParticipantsAddEventPOST
ConferenceSessionParticipantsRemoveEventPOST
ConferenceSessionParticipantPermissionsChangeEventPOST
ConferenceSessionParticipantBroadcastLangChangeEventPOST
ConferenceSessionParticipantInterpretationLangPairChangeEventPOST
ConferenceSessionParticipantTranslationDirectionChangeEventPOST
ConferenceParticipantRoleChangeEventPOST
ParticipantChangeRoleEventPOST
ParticipantHandStateChangedEventPOST
ConferenceLobbyParticipantJoinEventPOST
ConferenceLobbyParticipantLeaveEventPOST
ConferenceLobbyParticipantApproveEventPOST
ConferenceLobbyParticipantRejectEventPOST
ParticipantCallRequestEvent
GET
/websocket/participantActiveConferenceEvents

Media events
Media events
Responses
200 Subscribed
Callbacks
POST
ConferenceSessionMediaPublicationChangedEventPOST
ConferenceSessionLayoutChangedEventPOST
MediaParticipantStateChangedEventPOST
MediaRoomStreamChangedEvent
GET
/websocket/mediaActiveConferenceEvents

Find conference sessions Deprecated
Use Find conference sessions instead

Find conference session with current user participation by parameters
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
nameContains
string
Conference name contains...
dateFrom
integer <int64> >= 0
Conference session date from
dateTo
integer <int64> >= 0
Conference date to
offset
integer <int32> >= 0
Default: 0
Offset in result set
limit
integer <int32> [ 1 .. 100 ]
Default: 20
Limit of result set
orderAsc
boolean
Default: true
Result set sort order
state
string
Default: "ALL"
Enum: "ALL" "TODAY" "OLD"
State of conference session
conferenceId
string <uuid>
Search by conference id
Responses
200 Found conference sessions
400 Bad request
500 Internal server error
GET
/conference-sessions
Response samples
200400500
Content type
application/json
Copy
Expand all Collapse all
[
{
"conferenceSessionId": "2df2d749-63a9-4bdf-8d0c-33caa5c48e90",
"runType": "AUTO",
"conferenceId": "5dda8c14-0f3e-4e73-ba90-c90721c159fe",
"name": "string",
"description": "string",
"conferenceNumber": 0,
"createDate": 0,
"updateDate": 0,
"lastMediaSessionStartDate": 0,
"startDate": 0,
"duration": 0,
"schedule": 
{
},
"ownerName": "string",
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"ownerAvatarId": "eb58ab5a-1793-408a-87e5-27c981e508d7",
"currentUserRoles": 
[
],
"isAllowRecordAccess": true,
"isAllowUploadDocumentAccess": true,
"countUsers": 0,
"countOnlineUsers": 0,
"periodical": true,
"sessionNumber": 0,
"moderators": 
[
],
"onlySessionModerator": true,
"allSessionsParticipant": true,
"state": "NO_STARTED",
"inviteResponseType": "NONE",
"hasQuestionnaire": true,
"hasFinishedInquiry": true,
"hasRecords": true,
"hasAttachments": true,
"actualStartDate": 0,
"roomStartDate": 0,
"hidePoll": true,
"deleted": true,
"room": true,
"selfRegistrationEnabled": true,
"selfRegistrationActive": true,
"subscriptionActive": true,
"guestAllowed": true,
"isPasscodeRequired": true,
"conferenceType": "EQUITABLE_CONVERSATION",
"sharingLevel": "ALL_PARTICIPANTS",
"attendeeSubscribeLimit": "NONE",
"hasVVoIPSupport": true,
"canBeRestored": true,
"timeIntervalForRestore": 0,
"isAdHocEvent": true
}
]

Find conference sessions
Find conference session with current user participation by parameters
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
nameContains
string
Conference name contains...
dateFrom
integer <int64> >= 0
Filter by startDate FROM specified date depending on ordering. For [orderAsc = true] fromDate should be less than toDate, otherwise - fromDate should be more than toDate
dateTo
integer <int64> >= 0
Filter by startDate TO specified date depending on ordering. For [orderAsc = true] toDate should be more than fromDate, otherwise - toDate should be less than fromDate
limit
integer <int32> [ 1 .. 100 ]
Default: 20
Limit of result set
orderAsc
boolean
Default: true
Result set sort order by date ascending
conferenceId
string <uuid>
Search by conference id
Responses
200 Found conference sessions
400 Bad request
500 Internal server error
GET
/conference-sessions/sessions
Response samples
200400500
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true
}

Find rooms
Find rooms with current user participation by parameters
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
nameContains
string
Room name contains...
includeArchiveRooms
boolean
Default: false
Whether include archive rooms
offset
integer <int32> >= 0
Default: 0
Offset in result set
limit
integer <int32> [ 1 .. 200 ]
Default: 30
Limit of result set
Responses
200 Found rooms
400 Bad request
500 Internal server error
GET
/conference-sessions/rooms
Response samples
200400500
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true
}

Get conference sessions join data
Returns conference session join data (links to connect, some connection info, etc.) depending on current participant rights and conference session sharing settings
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
Responses
200 Conference session join data
GET
/conference-sessions/{conferenceSessionId}/join-data
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"conferenceNumber": 0,
"previousConferenceNumber": 0,
"joinByIdLink": "string",
"guestLink": "string",
"speakerLink": "string",
"moderatorLink": "string",
"guestPasscode": "string",
"speakerPasscode": "string",
"frameLink": "string",
"selfRegistrationUrl": "string",
"phoneNumber": "string",
"vvoipAddress": "string"
}

Get periodical conference session personal info
Returns conference session info (for periodical conference) including personal participation data by it's planned conference ID and session number.

Method is available only for invited or connected participants.
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
conferenceId
required
string <uuid>
Conference ID
sessionNumber
required
integer <int32>
Default: 1
Session number
Responses
200 Found conference session
400 Bad request
500 Internal server error
GET
/conference-sessions/periodical
Response samples
200400500
Content type
application/json
Example
ConferenceSessionPersonalSummaryInfoRestDTO
Copy
Expand all Collapse all
{
"conferenceSessionId": "2df2d749-63a9-4bdf-8d0c-33caa5c48e90",
"conferenceId": "5dda8c14-0f3e-4e73-ba90-c90721c159fe",
"name": "string",
"description": "string",
"createDate": 0,
"updateDate": 0,
"lastMediaSessionStartDate": 0,
"actualStartDate": 0,
"state": "NO_STARTED",
"room": true,
"deleted": true,
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"ownerName": "string",
"ownerAvatarId": "eb58ab5a-1793-408a-87e5-27c981e508d7",
"settings": 
{
"runType": "AUTO",
"conferenceType": "EQUITABLE_CONVERSATION",
"attendeeSubscribeLimit": "NONE",
"sharingLevel": "ALL_PARTICIPANTS",
"features": 
[
]
},
"invitedParticipantsCount": 0,
"onlineParticipantsCount": 0,
"conferenceNumber": 0,
"personalParticipationInfo": 
{
"conferenceSessionParticipantId": "13159501-abd3-4d37-abef-2c526afe320a",
"conferenceSessionRoles": 
[
],
"conferenceSessionInviteResponse": "NONE",
"conferenceParticipantId": "452fe6b7-3e3b-4e4b-afff-342002752acc",
"conferenceRoles": 
[
],
"conferenceInviteResponse": "NONE"
},
"startDate": 0,
"duration": 0,
"schedule": 
{
"periodicityType": "DAILY",
"daysOfWeek": 
[
],
"dayNumber": 1,
"weekNumber": 1,
"monthNumber": 1
},
"sessionNumber": 0
}

Join conference session
The general method to join the conference session.
1. If you are invited then just join by conference session ID
2. If you are not invited then join by invitation ticket

As a result, server event ParticipantSessionStartedEvent is sent to all online conference participants and ConferenceSessionOnlineParticipantsCountChangedEvent to all invited conference participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session Id.
REQUEST BODY SCHEMA: application/json
Conference session join configuration info
ticketInfo
object (BindTicketRestDTO)
Information about the ticket
supportedProtocols
required
Array of strings
Items Enum: "RTMP" "WEBRTC" "SIP" "H323" "S4B" "RTSP" "VNC"
List of client available protocols
tokenId
string
Some unique token that represents current device in call
eventBusId
required
string
Comet event bus id
Responses
200 Conference session join response info
400 Bad request
500 Internal server error
POST
/conference-sessions/{conferenceSessionId}/join
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"ticketInfo": 
{
"ticketLink": "string",
"passcode": "string"
},
"supportedProtocols": 
[
"RTMP"
],
"tokenId": "string",
"eventBusId": "string"
}
Response samples
200400500
Content type
application/json
Copy
Expand all Collapse all
{
"conferenceSessionId": "2df2d749-63a9-4bdf-8d0c-33caa5c48e90",
"participantId": "9f6624b5-5f99-42b6-899f-30f2b369cbd7",
"alreadyJoined": true,
"isAudioOnlyMode": true
}

Leave conference session
Leaves the conference session.

As a result, server event ParticipantSessionFinishedEvent is sent to all online conference participants and ConferenceSessionOnlineParticipantsCountChangedEvent to all invited conference participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session Id
Responses
204 Success
400 Bad request
500 Internal server error
POST
/conference-sessions/{conferenceSessionId}/leave
Response samples
400500
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Respond on invitation
Responds on invitation to conference session.

As a result, server event ConferenceSessionParticipantInvitationResponseEvent is sent to current user.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
REQUEST BODY SCHEMA: application/json
Invitation response
response
required
string
Enum: "NONE" "APPROVE" "REJECT" "MAYBE"
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/respond-on-invitation
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"response": "NONE"
}

Start conference session
Starts the conference session by id.
User should have moderator role and planned start time should be not more than 30 minutes later.

As a result, server events are sent:
- ActiveConferenceSessionChangedEvent to all online conference participants;
- ConferenceSessionChangedEvent to all conference participants which are not connected to conference.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Responses
204 Success
400 reason = ACTIVE_CONFERENCE_SESSIONS_EXIST, type = ConferenceSessionStateChangeException - if conference already have active session
reason = TOO_EARLY_TO_START, type = ConferenceSessionStateChangeException - if conference session starts in more than 30 minutes
reason = ALREADY_STOPPED, type = ConferenceSessionStateChangeException - if conference session already stopped
403 User not in conference session or haven't moderator role
POST
/conference-sessions/{conferenceSessionId}/start

Start recording
Starts recording of media data in conference.

As a result, server event ConferenceSessionRecordingStateChangedEvent is sent to all online conference participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/record/start

Start transcription
Starts transcription of audio data in conference.
User should have moderator role.
As a result, server event ConferenceSessionTranscriptionStateChangedEvent is sent to all online conference participants
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
Responses
204 Success
400 reason = SYSTEM_CONFIGURATION_TRANSCRIPTION_ERROR, type = IvcsAccessControlException - if speech recognition settings have invalid fields
reason = FS_LIMIT_RESTRICTION, type = IvcsAccessControlException - if user does not have enough file storage space
500 Internal server error
POST
/conference-sessions/{conferenceSessionId}/transcription/start
Response samples
500
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Stop conference session
Stops the conference session by id.
User should have moderator role.

As a result, server event ConferenceSessionFinishedEvent is sent to all conference participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Responses
204 Success
400 reason = NOT_ACTIVE, type = ConferenceSessionStateChangeException - if conference session not in active state
403 User not in conference session or haven't moderator role
POST
/conference-sessions/{conferenceSessionId}/stop

Stop recording
Stops recording of media data in conference.

As a result, server event ConferenceSessionRecordingStateChangedEvent is sent to all online conference participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/record/stop

Stop transcription
Stops transcription of audio data in conference.
As a result, server event ConferenceSessionTranscriptionStateChangedEvent is sent to all online conference participants
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
Responses
204 Success
400 Bad request
500 Internal server error
POST
/conference-sessions/{conferenceSessionId}/transcription/stop
Response samples
400500
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Get conference media info
Returns current media information about an conference, including connected participants, active demonstrations, active cascading connections, etc. This information is usually requested when joining an event. Subsequent update and synchronization is performed using the received server events:
- ActiveConferenceSessionChangedEvent - update conference session settings;
- ConferenceSessionFinishedEvent - finish particular conference session;
- ForwardToAnotherConferenceSessionEvent - automatic forwarding current participant to another conference session;
- PublishPresetsChangedEvent - update publish quality preset;
- ConferenceSessionJoinDataChangedEvent - update join data;
- MediaParticipantStateChangedEvent - update allowed participant media state;
- ConferenceSessionLayoutChangedEvent - update conference session layout;
- MediaRoomStreamChangedEvent - update participant real media state;
- ConferenceSessionMediaPublicationChangedEvent - update participant real media state;
- ParticipantChangeRoleEvent - update participant roles;
- ConferenceSessionParticipantPermissionsChangeEvent - update participant permissions;
- ConferenceSessionParticipantJoinEvent - enter new participant in the event;
- ConferenceSessionParticipantLeaveEvent - leave participant from the event;
- ConferenceSessionPresentationChangeEvent - start/end of additional content demonstration;
- ConferenceSessionPresentationStateChangeEvent - update state of additional content demonstration (document, whiteboard);
- ConferenceSessionPresentationPointerChangeEvent - update pointer position in additional content demonstration (document, whiteboard);
- to be continued...
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session Id
Responses
200 Conference session media info
GET
/conference-sessions/{conferenceSessionId}/media/info
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"participantId": "9f6624b5-5f99-42b6-899f-30f2b369cbd7",
"ownParticipantData": 
{
"speakerStreamPublishUrl": "string",
"screenShareStreamPublishUrl": "string",
"subscribeLimit": "NONE",
"layout": 
{
},
"maxMediaProfile": 0,
"outputAudioGain": 0,
"inputAudioGain": 0
},
"conferenceSession": 
{
"conferenceSessionId": "2df2d749-63a9-4bdf-8d0c-33caa5c48e90",
"conferenceId": "5dda8c14-0f3e-4e73-ba90-c90721c159fe",
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"ownerName": "string",
"ownerAvatarId": "eb58ab5a-1793-408a-87e5-27c981e508d7",
"conferenceType": "EQUITABLE_CONVERSATION",
"runType": "AUTO",
"name": "string",
"description": "string",
"startDate": 0,
"actualStartDate": 0,
"lastMediaSessionStartDate": 0,
"duration": 0,
"state": "NO_STARTED",
"periodical": true,
"schedule": 
{
},
"room": true,
"attendeeSubscribeLimit": "NONE",
"participantsCount": 0,
"recording": true,
"transcribing": true,
"rootFolderId": "3d36bbdf-3fbe-4ea3-93a2-f59dba43c294",
"features": 
[
],
"hasVVoIPSupport": true,
"isAudioOnlyMode": true,
"sharingLevel": "ALL_PARTICIPANTS",
"layout": 
{
},
"joinRestriction": "ANYONE",
"moderatorPermissions": 
[
],
"speakerPermissions": 
[
],
"interpreterPermissions": 
[
],
"interpreterMediaState": "NONE",
"attendeePermissions": 
[
],
"attendeeMediaState": "NONE",
"availableInterpretationLanguages": 
[
]
},
"presentation": 
{
"presentationId": "e1fc6bcc-f902-4bce-8b40-504b99e58d26",
"ownerParticipantId": "00cd9a07-cc52-4503-a1ca-9dd633f57032",
"cursorLeft": 0,
"cursorTop": 0,
"cursorVisible": true,
"document": 
{
},
"state": 
{
}
},
"mediaConferenceId": "b1ff732b-4bd7-484b-8620-600b810caf52",
"participants": 
[
{
}
],
"interconnections": 
[
{
}
],
"demonstrationState": "DEFAULT",
"onlineParticipantsCount": 0,
"onlineFramesCount": 0,
"protocol": "RTMP",
"qualityPreset": "LOWEST",
"alertNotifications": 
[
{
}
],
"webinarTranslationInfo": 
{
"mainContentUrl": "string",
"additionalContentUrl": "string",
"flvMainContentUrl": "string",
"flvAdditionalContentUrl": "string"
}
}

Presentation events
Presentation events
Responses
200 Subscribed
Callbacks
POST
ConferenceSessionPresentationChangeEventPOST
ConferenceSessionPresentationStateChangeEventPOST
ConferenceSessionPresentationPointerChangeEventPOST
PresentationInterruptedEvent
GET
/websocket/presentationActiveConferenceEvents

Get conference media info Deprecated
Use Get system media information instead

Returns current media information about an conference, including connected participants, active demonstrations, active cascading connections, etc. This information is usually requested when joining an event. Subsequent update and synchronization is performed using the received server events:
- LiveConferenceSessionChangedEvent - update conference session settings;
- ConferenceSessionFinishedEvent - finish particular conference session;
- MediaParticipantStateChangedEvent - update allowed participant media state;
- MediaRoomStreamChangedEvent - update participant real media state;
- ParticipantChangeRoleEvent - update participant roles;
- ParticipantChangePermissionsEvent - update participant permissions;
- ParticipantSessionStartedEvent - enter new participant in the event;
- ParticipantSessionFinishedEvent - leave participant from the event;
- MediaRoomStateChangedEvent - start/end of additional content demonstration;
- PresentationStateChangedEvent - update state of additional content demonstration (document, whiteboard);
- PresentationPointerStateChangedEvent - update pointer position in additional content demonstration (document, whiteboard);
- to be continued...
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session Id
Responses
200 Conference session media info
GET
/conference-sessions/{conferenceSessionId}/media/room-info
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"currentConferenceSessionParticipantId": "644cfd9c-504e-4da0-8846-26afca704722",
"mediaConferenceId": "b1ff732b-4bd7-484b-8620-600b810caf52",
"participants": 
[
{
}
],
"interconnections": 
[
{
}
],
"currentRoomState": "DEFAULT",
"presentation": 
{
"ownerId": "4d206909-730f-409a-88f6-dcfaa8fc28cc",
"cursorX": 0,
"cursorY": 0,
"cursorLeft": 0,
"cursorTop": 0,
"cursorVisible": true,
"id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
"state": 
{
},
"subscribeUri": "string",
"isRemote": true,
"vncServerAddress": "string",
"vncPassword": "string"
},
"currentSession": 
{
"id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
"name": "string",
"description": "string",
"conferenceId": "5dda8c14-0f3e-4e73-ba90-c90721c159fe",
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"ownerName": "string",
"ownerAvatarId": "eb58ab5a-1793-408a-87e5-27c981e508d7",
"recording": true,
"transcribing": true,
"startDate": 0,
"actualStartDate": 0,
"duration": 0,
"state": "NO_STARTED",
"periodical": true,
"schedule": 
{
},
"rootFolderId": "3d36bbdf-3fbe-4ea3-93a2-f59dba43c294",
"features": 
[
],
"hasVVoIPSupport": true,
"isAudioOnlyMode": true,
"conferenceType": "EQUITABLE_CONVERSATION",
"attendeeSubscribeLimit": "NONE",
"room": true,
"subscription": 
{
},
"conferenceNumber": 0,
"previousConferenceNumber": 0,
"sharingLevel": "ALL_PARTICIPANTS",
"eventStyle": 
{
},
"guestLink": "string",
"selfRegistrationLink": "string",
"autoStartStop": true,
"layout": 
{
},
"joinRestriction": "ANYONE"
},
"inquiriesActive": true,
"permissions": 
[
"SPEAKER_OTHER"
],
"privateRoomInfo": 
{
"frameLink": "string",
"selfRegistrationUrl": "string",
"mediaPublication": 
{
},
"vncPublication": 
{
},
"speakerLink": "string",
"moderatorLink": "string",
"guestPasscode": "string",
"speakerPasscode": "string"
},
"participantCount": 0,
"frameCount": 0,
"speakerStreamPublishUrl": "string",
"screenShareStreamPublishUrl": "string",
"protocol": "RTMP",
"activePreset": "LOWEST",
"subscribeLimit": "NONE",
"conferenceAlertNotifications": 
[
{
}
],
"webinarTranslationInfo": 
{
"mainContentUrl": "string",
"additionalContentUrl": "string",
"flvMainContentUrl": "string",
"flvAdditionalContentUrl": "string"
}
}

Report media state
Reports the state of audio / video broadcasting of the current participant in specified conference. In fact, this method only changes the broadcasting state of the participant in the conference, which is a "trigger" for updating the media from this participant in the media streams of the server mosaic and from the rest of the event participants. Direct change of the media broadcast state from the participant is carried out using the WebRTC JS API.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session Id
REQUEST BODY SCHEMA: application/json
Media state of specified stream
mediaState
string
Enum: "NONE" "AUDIO" "VIDEO" "AUDIO_VIDEO"
streamType
string
Enum: "SPEAKER" "SCREENSHARE"
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/media/media-state
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"mediaState": "NONE",
"streamType": "SPEAKER"
}

Report participant media equipment
Reports to the system about the change of equipment used by the participant (camera, microphone, speakers) in the conference. The method should be called every time the equipment used in the broadcast changes.

This information is used in the administrative interface to control and manage the event and its participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session Id
REQUEST BODY SCHEMA: application/json
Participant equipment
camera
string
microphone
string
speakers
string
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/media/equipment
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"camera": "string",
"microphone": "string",
"speakers": "string"
}

Set broadcast language
Sets participant's broadcast language.

As a result, following server events are sent:
- ConferenceSessionParticipantBroadcastLangChangeEvent;
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session Id
REQUEST BODY SCHEMA: application/json
language
string
Enum: "RUSSIAN" "ENGLISH" "FRENCH" "DEUTSCH" "SPANISH" "PORTUGUESE" "ITALIAN" "TURKISH" "ARABIC" "HEBREW" "HINDI" "CHINESE" "JAPANESE" "KOREAN"
Participant's broadcast language
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/media/broadcast-language
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"language": "RUSSIAN"
}

Set layout of mixed main content stream
Sets personal layout of mixed main content stream.

Layout installation can be done in two ways:
- By choosing a specific layout by specifying the 'layoutId' field (the list of layouts available in the system can be found in the system media information (see Get system media information) with the ability to control the display of names in the layout;
- By choosing one of the preset layouts in the system - layoutPreset.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session Id
REQUEST BODY SCHEMA: application/json
Desired layout settings
layout
object (LayoutRestDTO)
layoutPreset
string
Enum: "DEFAULT" "ALTERNATIVE1" "ALTERNATIVE2"
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/media/layout
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"layout": 
{
"layoutId": 0,
"showNames": true
},
"layoutPreset": "DEFAULT"
}

Get system media information
Returns system media information for particular domain.
Responses
200 System media information
GET
/public/system/media-info
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"mediaProfiles": 
[
{
}
],
"mediaServerAddressMap": 
[
{
}
],
"conferencePresets": 
[
{
}
],
"screenSharePresets": 
[
{
}
],
"iceServers": 
[
{
}
],
"mosaicLayoutHolder": 
{
"mosaicLayouts": 
[
]
},
"layoutPresets": 
[
{
}
]
}

Set quality of mixed main content stream
Sets personal quality of mixed main content stream by specifying index of predefined media quality profile. The list of media qualities profiles available in the system can be found in the system media information (see Get system media information).
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session Id
REQUEST BODY SCHEMA: application/json
Desired media quality
profileIndex
integer <int32>
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/media/media-profile
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"profileIndex": 0
}

Set translation direction
Sets interpreter's translation direction.

As a result, following server events are sent:
- ConferenceSessionParticipantTranslationDirectionChangeEvent;
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session Id
REQUEST BODY SCHEMA: application/json
language
required
string
Enum: "RUSSIAN" "ENGLISH" "FRENCH" "DEUTSCH" "SPANISH" "PORTUGUESE" "ITALIAN" "TURKISH" "ARABIC" "HEBREW" "HINDI" "CHINESE" "JAPANESE" "KOREAN"
Interpreter's translation direction language
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/media/translation-direction
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"language": "RUSSIAN"
}

Add participants
Adds participants to specified conference.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
REQUEST BODY SCHEMA: application/json
Users for participation in conference
invitations
Array of ProfileInterlocutorDTO (object) or ContactInterlocutorDTO (object) or ArbitraryInterlocutorDTO (object) (InterlocutorDTO) non-empty
performOutgoingCall
boolean
Default: false
notifyBySms
boolean
Default: false
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/participants/add
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"invitations": 
[
{
}
],
"performOutgoingCall": false,
"notifyBySms": false
}

Cancel outgoing call
Cancels outgoing call to specified participant.

As a result, following server events are sent:
- ParticipantCallRequestEvent;
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
participantId
required
string <uuid>
Conference session participant ID
Responses
400 Bad request
500 Internal server error
POST
/conference-sessions/{conferenceSessionId}/participants/{participantId}/cancel-outgoing-call
Response samples
400500
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Disconnect participants
Disconnects participants from specified conference session.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
REQUEST BODY SCHEMA: application/json
Array ()
string <uuid>
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/participants/disconnect
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
[
"497f6eca-6276-4993-bfeb-53cbbbba6f08"
]

Hand down
Makes participant hand down.
It is available for the participant himself or conference session moderator

As a result, server event ParticipantHandStateChangedEvent is sent to all online conference participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
participantId
required
string <uuid>
Conference session participant ID
Responses
204 Success
403 User is not the participant or moderator
POST
/conference-sessions/{conferenceSessionId}/participants/{participantId}/hand-down

Hand up
Makes participant hand up.
It is available for the participant himself or conference session moderator

As a result, server event ParticipantHandStateChangedEvent is sent to all online conference participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
participantId
required
string <uuid>
Conference session participant ID
Responses
204 Success
403 User is not the participant or moderator
POST
/conference-sessions/{conferenceSessionId}/participants/{participantId}/hand-up

Find participants
Find participants by parameters. Not invited users or regular participants in webinars do not have access to NOT_CONNECTED and INVITED filters.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
QUERY PARAMETERS
participantFilterType
string
Default: "SPEAKER_OR_MODERATOR"
Enum: "INVITED" "SPEAKER_OR_MODERATOR" "NOT_CONNECTED"
Participant filter type
sortField
string
Default: "NAME"
Enum: "ROLE" "NAME"
Participant sort field
orderAsc
boolean
Default: true
Result set sort order
offset
integer <int32>
Default: 0
Offset. Starts from 0.
limit
integer <int32> <= 200
Default: 50
Records Limit. Should be more then 0.
Responses
200 Success
GET
/conference-sessions/{conferenceSessionId}/participants/find
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

Get participant
Get participant info
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
participantId
required
string <uuid>
Conference session participant ID
Responses
200 Success
404 Something goes wrong
GET
/conference-sessions/{conferenceSessionId}/participants/{participantId}
Response samples
200404
Content type
application/json
Copy
Expand all Collapse all
{
"participantId": "9f6624b5-5f99-42b6-899f-30f2b369cbd7",
"profileId": "faebe71b-2bf8-4bdb-9b67-258e4d6aa00a",
"name": "string",
"avatarResourceId": "bc84249e-8ad6-4649-8b59-04125098a24d",
"roles": 
[
"ATTENDEE"
],
"isInvited": true,
"inviteResponseType": "NONE",
"inviteResponseDate": 0,
"isRegisteredUser": true,
"settings": 
{
"interpreterLanguagesPair": 
[
],
"broadcastLanguage": "RUSSIAN",
"mediaState": "NONE",
"permissions": 
[
]
},
"callRequest": 
{
"status": "STARTED",
"started": 0
},
"interlocutorInfo": 
{
"name": "string",
"email": "string",
"phone": "string",
"interlocutorType": "FOREIGN_CONTACT",
"contact": 
{
},
"profile": 
{
},
"ldapUser": 
{
}
}
}

Remove participants
Removes participants from specified conference session.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
REQUEST BODY SCHEMA: application/json
Array ()
string <uuid>
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/participants/remove
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
[
"497f6eca-6276-4993-bfeb-53cbbbba6f08"
]

Start outgoing call
Starts outgoing call to specified participant.

As a result, following server events are sent:
- ParticipantCallRequestEvent;
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
participantId
required
string <uuid>
Conference session participant ID
Responses
200 Success
204 Call wasn't started for some reason
400 Bad request
500 Internal server error
POST
/conference-sessions/{conferenceSessionId}/participants/{participantId}/start-outgoing-call
Response samples
200400500
Content type
application/json
Copy
Expand all Collapse all
{
"status": "STARTED",
"started": 0
}

Update participant
Updates particular parameters for specified participant. Only moderators can update participant parameters.

As a result, following server events are sent depending on the parameters being changed:
- MediaParticipantStateChangedEvent;
- ParticipantChangeRoleEvent;
- ConferenceSessionParticipantPermissionsChangeEvent;
- ConferenceSessionJoinDataChangedEvent;
- OwnConferenceSessionParticipantMediaSettingsChangeEvent;
- ConferenceSessionParticipantBroadcastLangChangeEvent;
- ConferenceSessionParticipantInterpretationLangPairChangeEvent;
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
participantId
required
string <uuid>
Conference session participant ID
REQUEST BODY SCHEMA: application/json
Set of parameters to be updated for specified participant. Absence of particular parameter means that this property is not updated.
name
string [ 1 .. 255 ] characters
New participant name (name can be updated only for users that is not registered in the system)
mediaState
object (MediaStateParameterValueRestDTO)
Custom allowed media state for participant
permissions
object (PermissionParameterValueRestDTO)
Custom participant permissions
roles
Array of strings
Items Enum: "ATTENDEE" "INTERPRETER" "SPEAKER" "MODERATOR"
Participant roles
interpreterLanguagesPair
Array of strings
Items Enum: "RUSSIAN" "ENGLISH" "FRENCH" "DEUTSCH" "SPANISH" "PORTUGUESE" "ITALIAN" "TURKISH" "ARABIC" "HEBREW" "HINDI" "CHINESE" "JAPANESE" "KOREAN"
Interpreter's translation language pair (for conferences with simultaneous interpretation feature). Acceptable values: empty set or set with two values.
broadcastLanguage
object (NullableParameterValueRestDTOTranslationLanguageType)
Broadcast language (for conferences with simultaneous interpretation feature)
Responses
204 Success
400 reason = GIVEN_BROADCAST_LANGUAGE_IS_ABSENT, type = ParticipantEditException - if selected broadcast language is not listed in available interpreter languages
PATCH
/conference-sessions/{conferenceSessionId}/participants/{participantId}/settings
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"name": "string",
"mediaState": 
{
"value": "NONE"
},
"permissions": 
{
"value": 
[
]
},
"roles": 
[
"ATTENDEE"
],
"interpreterLanguagesPair": 
[
"RUSSIAN"
],
"broadcastLanguage": 
{
"value": "RUSSIAN"
}
}

Approve request
Approves the lobby participant's request and allows to join conference session
The lobby participant will be removed and a conference session participant will be created instead.
As a result, server event LobbyParticipantApproveEvent is sent to the lobby participant and to all online conference moderators.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
profileId
required
string <uuid>
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/lobby/participants/{profileId}/approve

Approve all requests
Approves all lobby participant's request and allows to join conference session
All of lobby participants will be removed and a conference session participants will be created instead.
As a result, server events LobbyParticipantApproveEvent are sent for each lobby participants to the participant himself and to all online conference moderators.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/lobby/approve-all

Get lobby participants
Returns batch of lobby participants with given size and offset for conference session

AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
QUERY PARAMETERS
offset
integer <int32>
Default: 0
size
integer <int32>
Default: 50
Responses
200 Lobby participants
GET
/conference-sessions/{conferenceSessionId}/lobby/participants
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

Join conference session lobby
Forwards not invited user to wait in lobby while it would be allowed to join conference session.
As a result, server event LobbyParticipantJoinEvent is sent to all online conference moderators.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
REQUEST BODY SCHEMA: application/json
Conference session join configuration info
ticketInfo
required
object (BindTicketRestDTO)
Information about the ticket
eventBusId
required
string
Comet event bus id
Responses
200 Conference session info
POST
/conference-sessions/{conferenceSessionId}/lobby/join
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"ticketInfo": 
{
"ticketLink": "string",
"passcode": "string"
},
"eventBusId": "string"
}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"conferenceSessionId": "2df2d749-63a9-4bdf-8d0c-33caa5c48e90",
"conferenceId": "5dda8c14-0f3e-4e73-ba90-c90721c159fe",
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"ownerName": "string",
"ownerAvatarId": "eb58ab5a-1793-408a-87e5-27c981e508d7",
"conferenceType": "EQUITABLE_CONVERSATION",
"runType": "AUTO",
"name": "string",
"description": "string",
"startDate": 0,
"actualStartDate": 0,
"lastMediaSessionStartDate": 0,
"duration": 0,
"state": "NO_STARTED",
"periodical": true,
"schedule": 
{
"periodicityType": "DAILY",
"daysOfWeek": 
[
],
"dayNumber": 1,
"weekNumber": 1,
"monthNumber": 1
},
"room": true,
"attendeeSubscribeLimit": "NONE"
}

Leave conference lobby
Removes not invited user from lobby of conference session
As a result, server event LobbyParticipantLeaveEvent is sent to all online conference moderators.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/lobby/leave

Reject request
Rejects the lobby participant's request to join conference session.
The lobby participant will be removed.
As a result, server event LobbyParticipantRejectEvent is sent to the lobby participant and to all online conference moderators.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
profileId
required
string <uuid>
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/lobby/participants/{profileId}/reject

Reject all request
Rejects all lobby participant's requests to join conference session.
All of lobby participants will be removed.
As a result, server events LobbyParticipantRejectEvent are sent for each lobby participants to the participant himself and to all online conference moderators.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/lobby/reject-all

Create document
Creates document in conference and returns created one. Current user should be in conference and directory in which document is created should also be in conference. User must have permission to upload document.

As a result, ConferenceSessionDocumentCreateEvent is sent to all connected conference participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
directoryId
required
string <uuid>
Parent folder to create document in
resourceId
required
string <uuid>
Resource id for document to create
Responses
200 Created document
400 Bad request
500 Internal server error
POST
/conference-sessions/{conferenceSessionId}/documents/{directoryId}/create-document-for/{resourceId}
Response samples
200400500
Content type
application/json
Copy
Expand all Collapse all
{
"name": "string",
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"modified": 0,
"created": 0,
"nodeId": "959356e3-6168-4a92-b4a5-b9d462be6177",
"parentFolderId": "530e31ab-f9ca-43ae-a4fe-193336bc6bd0",
"authorName": "string",
"type": "DOCUMENT",
"isPublic": true,
"storageDate": 0,
"resource": 
{
"resourceId": "026d60bb-63a8-407e-bf67-01dcfc6022e6",
"name": "string",
"size": 0,
"mimeType": "string",
"createdDate": 0,
"metadata": 
{
},
"objectInnerType": "DOCUMENT",
"objectType": "DOCUMENT",
"securityLevel": "UNCLASSIFIED"
},
"conversionProgress": 0,
"conversionState": "NOT_SUPPORTED"
}

Delete document
Deletes document in conference. Current user should be in conference as well as document to remove.
Following users can delete documents:
- owner of the document,
- conference moderator,
- Ivcs admin or operator.
In case document is being demonstrated it cannot be removed.

After removal ConferenceSessionDocumentDeleteEvent is sent to all connected conference participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
documentId
required
string <uuid>
Document to delete
Responses
204 Success
DELETE
/conference-sessions/{conferenceSessionId}/documents/{documentId}

Update document
Updates document in conference. Current user should be in conference as well as document.Following users can rename documents:
- document owner,
- conference moderator.

After updating ConferenceSessionDocumentUpdateEvent is sent to all connected conference participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
documentId
required
string <uuid>
Document id
REQUEST BODY SCHEMA: application/json
name
string [ 1 .. 255 ] characters
New name for document
Responses
204 Success
PATCH
/conference-sessions/{conferenceSessionId}/documents/{documentId}
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"name": "string"
}

Check the ability to upload a document
Checks if user can upload a document of exact size to event.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
QUERY PARAMETERS
size
required
integer <int64>
Size of a document in bytes
Responses
200 An Information about the result of check
400 Bad request
500 Internal server error
GET
/conference-sessions/{conferenceSessionId}/documents/can-upload
Response samples
200400500
Content type
application/json
Copy
Expand all Collapse all
{
"canUpload": true
}

List pages for the document
Returns converted pages for the given document with paging support. User should be invited or connected to conference and document should belong to conference. Conversion status doesn't exist for all the documents.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
documentId
required
string <uuid>
Document id
QUERY PARAMETERS
offset
integer <int32> >= 0
Default: 0
Offset in result set
limit
integer <int32> [ 1 .. 100 ]
Default: 20
Limit of result set
Responses
200 Pages info of the document
GET
/conference-sessions/{conferenceSessionId}/documents/{documentId}/pages
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

List documents
Returns list of documents in a given folder with paging support. User should be invited or connected to conference and searching directory should belong to conference.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
directoryId
required
string <uuid>
ID of directory for which files are listed
QUERY PARAMETERS
orderAsc
boolean
Default: true
Result set sort order
sortField
string
Default: "NAME"
Enum: "NAME" "SIZE" "CHANGED_DATE"
Sort result set by field
offset
integer <int32> >= 0
Default: 0
Offset in result set
limit
integer <int32> [ 1 .. 100 ]
Default: 20
Limit of result set
Responses
200 Found conference session documents
400 Bad request
500 Internal server error
GET
/conference-sessions/{conferenceSessionId}/documents/{directoryId}
Response samples
200400500
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

Pause video demonstration
Pauses video document demonstration in conference.
As a result, server event ConferenceSessionPresentationStateChangeEvent is sent to all online session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
Responses
204 Success
400 reason = NOT_IN_PRESENTATION, type = IvcsAccessControlException - if current participant does not have active video document demonstration.
500 Internal server error
POST
/conference-sessions/{conferenceSessionId}/demonstration/video-document/pause
Response samples
500
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Play video demonstration
Plays video document demonstration in conference.
As a result, server event ConferenceSessionPresentationStateChangeEvent is sent to all online session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
Responses
204 Success
400 reason = NOT_IN_PRESENTATION, type = IvcsAccessControlException - if current participant does not have active video document demonstration.
500 Internal server error
POST
/conference-sessions/{conferenceSessionId}/demonstration/video-document/play
Response samples
500
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Set video position
Sets video document demonstration position.
As a result, server event ConferenceSessionPresentationStateChangeEvent is sent to all online session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
REQUEST BODY SCHEMA: application/json
position
required
number <double> >= 0
Video demonstration position (in seconds from zero point position)
Responses
204 Success
400 reason = NOT_IN_PRESENTATION, type = IvcsAccessControlException - if current participant does not have active video document demonstration.
500 Internal server error
POST
/conference-sessions/{conferenceSessionId}/demonstration/video-document/position
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"position": 0
}
Response samples
500
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Start document demonstration
Starts document demonstration in a given conference.

User should participate in a given conference. As a result, server event ConferenceSessionPresentationChangeEvent is sent to all online session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
REQUEST BODY SCHEMA: application/json
left
required
integer <int32>
top
required
integer <int32>
pageIndex
required
integer <int32> >= 1
Page number to display
right
required
integer <int32> >= 0
Right should be more than left
bottom
required
integer <int32> >= 0
Bottom should be more than top
documentId
required
string <uuid>
Demonstrated document
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/demonstration/document/start
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"left": 0,
"top": 0,
"pageIndex": 1,
"right": 0,
"bottom": 0,
"documentId": "4704590c-004e-410d-adf7-acb7ca0a7052"
}

Start video demonstration
Starts video document demonstration in conference.
As a result, server events:
- ConferenceSessionPresentationChangeEvent is sent to all online session participants.
- PresentationInterruptedEvent is sent to previous demonstration owner if there was active demonstration that is interrupted by new one and owners are not matched.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
REQUEST BODY SCHEMA: application/json
documentId
required
string <uuid>
Demonstrated document
Responses
204 Success
400 Bad request
500 Internal server error
POST
/conference-sessions/{conferenceSessionId}/demonstration/video-document/start
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"documentId": "4704590c-004e-410d-adf7-acb7ca0a7052"
}
Response samples
400500
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Stop document demonstration
Stops current document demonstration in a given conference.

As a result, server event ConferenceSessionPresentationChangeEvent is sent to all online session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/demonstration/document/stop

Stop video demonstration
Stops video demonstration in conference.
As a result, server event ConferenceSessionPresentationChangeEvent is sent to all online session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
Responses
204 Success
400 Bad request
500 Internal server error
POST
/conference-sessions/{conferenceSessionId}/demonstration/video-document/stop
Response samples
400500
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Update demonstration cursor state
Updates current demonstration cursor state.As a result, server event ConferenceSessionPresentationPointerChangeEvent is sent to all online session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
REQUEST BODY SCHEMA: application/json
cursorTop
integer <int32> >= 0
Cursor top position in a presentation
cursorLeft
integer <int32> >= 0
Cursor left position in a presentation
cursorVisible
required
boolean
Responses
204 Success
PATCH
/conference-sessions/{conferenceSessionId}/demonstration/document/cursor
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"cursorTop": 0,
"cursorLeft": 0,
"cursorVisible": true
}

Update demonstration state
Updates current demonstration state. As a result, server event ConferenceSessionPresentationStateChangeEvent is sent to all online session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
REQUEST BODY SCHEMA: */*
left
required
integer <int32>
top
required
integer <int32>
pageIndex
required
integer <int32> >= 1
Page number to display
right
required
integer <int32> >= 0
Right should be more than left
bottom
required
integer <int32> >= 0
Bottom should be more than top
Responses
204 Success
PATCH
/conference-sessions/{conferenceSessionId}/demonstration/document/state

Edit message
Edits specified message. Message can be edited by its owner only within 1 hour after sending it. Message can be edited only if chat moderation is off.

As a result, server event ConferenceChatMessageUpdatedEvent is sent to all online conference session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
id
required
string <uuid>
Message ID
REQUEST BODY SCHEMA: application/json
Message data
message
string
Responses
204 Success
PATCH
/conference-sessions/{conferenceSessionId}/messages/{id}
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string"
}

Get messages
Returns conference session chat messages by specified parameters. It can be used for searching messages.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
QUERY PARAMETERS
moderationStatuses
required
Array of strings
Items Enum: "NOT_MODERATED" "APPROVED" "REJECTED"
Moderation statuses
target
string
Default: "ALL"
Enum: "ALL" "COMMON" "Target participant id as string <uuid>"
Message target
textContains
string
Search criteria
dateFrom
integer <int64>
Date from (UNIX time in ms)
dateTo
integer <int64>
Date to (UNIX time in ms)
relateToModeratedAt
boolean
Default: true
Sort and filter messages by moderatedAt or createdAt date
onlyMyModeration
boolean
Default: true
Actual only for moderators: whether show only self not moderated or rejected messages
size
integer <int32>
Default: 50
Result page size
orderAsc
boolean
Default: false
Order ascendancy
Responses
200 Requested messages
GET
/conference-sessions/{conferenceSessionId}/messages
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

Get private messages interlocutors
Returns all interlocutors of existed private messages in the conference session.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
Responses
200 Private messages interlocutors
GET
/conference-sessions/{conferenceSessionId}/messages/participant-targets
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
[
{
"participantId": "5d930c6c-83a7-4aae-bd98-78b67d01215b",
"profileId": "0da3ca13-95fc-4e58-8a81-3f904778c719",
"name": "string",
"avatarId": "2ed65e16-5450-4f50-ba21-e83e248277b3",
"lastMessageAt": 0,
"totalMessagesCount": 0
}
]

Moderate message
Moderates specified message by conference session moderators.

As a result, server event ConferenceChatMessageEvent is sent to all online conference session participants if it is approved or online speakers and moderators and author only if it is rejected.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
REQUEST BODY SCHEMA: application/json
Message moderation data
messageIds
Array of strings <uuid>
approve
boolean
Responses
204 Success
400 reason = MESSAGE_ALREADY_MODERATED, type = ChatMessageEditException - if message already moderated by another moderator with another answer.
500 Internal server error
POST
/conference-sessions/{conferenceSessionId}/messages/moderate
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"messageIds": 
[
"497f6eca-6276-4993-bfeb-53cbbbba6f08"
],
"approve": true
}
Response samples
500
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Remove all conference session messages
Removes all messages in specified conference session or in all sessions of periodical conference.

As a result, server event ConferenceChatClearedEvent is sent to all online conference session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
REQUEST BODY SCHEMA: application/json
Scope of messages removal
deleteInAllConferenceSessions
boolean
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/messages/remove-all
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"deleteInAllConferenceSessions": true
}

Remove all participant messages
Removes all messages of specified participant.

As a result, server event ConferenceChatParticipantMessagesRemovedEvent is sent to all online conference session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
REQUEST BODY SCHEMA: application/json
Messages removing details
authorParticipantId
string <uuid>
Author participant ID
prohibitMessaging
boolean
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/messages/remove-all-for-participant
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"authorParticipantId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"prohibitMessaging": true
}

Remove message
Removes specified messages. Any conference participant can remove own message whereas conference session moderators can remove any message.

As a result, server event ConferenceChatMessageRemovedEvent is sent to all online conference session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
REQUEST BODY SCHEMA: application/json
Array ()
string <uuid>
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/messages/remove
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
[
"497f6eca-6276-4993-bfeb-53cbbbba6f08"
]

Send message
Sends new message to conference session chat. This method can be also used for replying on another message. If message are sent with attachment that the one should be uploaded to the server before.

As a result, server event ConferenceChatMessageEvent is sent to all online conference session participants if moderation is offotherwise - online speakers and moderators.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
REQUEST BODY SCHEMA: application/json
Message data
message
string
replyOn
string <uuid>
attachmentId
string <uuid>
targetParticipantId
string <uuid>
Responses
200 Created message
400 reason = HTTP_REFERENCE_NOT_ALLOWED, type = ChatMessageSentException - if the user not allowed to send http references in chat.
reason = RELATED_MESSAGE_DELETED, type = ChatMessageSentException - if the user message addressed to a message to has been deleted.
reason = RELATED_MESSAGE_NOT_MODERATED, type = ChatMessageSentException - if the user message addressed to a message to has not been moderated.
500 Internal server error
POST
/conference-sessions/{conferenceSessionId}/messages/send
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"replyOn": "49d10892-579c-4689-85f2-0a39915c45c2",
"attachmentId": "96b9bbac-86d3-4497-9e0c-1f8e3803eddb",
"targetParticipantId": "37ed336b-6dc3-48ac-b51e-e2b5fe0c8d1d"
}
Response samples
200500
Content type
application/json
Copy
Expand all Collapse all
{
"messageId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"conferenceSessionId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"authorParticipantId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"authorProfileId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"authorName": "string",
"authorAvatarId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"targetParticipantId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"targetProfileId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"targetName": "string",
"message": "string",
"attachment": 
{
"id": "08e3e69b-acf4-442e-8dcd-76f750451118",
"resourceId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"name": "string",
"createdOn": 0,
"format": "PDF",
"metaData": 
{
},
"mimeType": "string",
"fileSize": 0,
"convertingProgress": 0,
"conversionState": "NOT_SUPPORTED"
},
"edited": true,
"createdAt": 0,
"moderatedAt": 0,
"updatedAt": 0,
"moderationStatus": "NOT_MODERATED",
"repliedOn": 
{
"messageId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"conferenceSessionId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"authorParticipantId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"authorProfileId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"authorName": "string",
"authorAvatarId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"targetParticipantId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"targetProfileId": "08e3e69b-acf4-442e-8dcd-76f750451118",
"targetName": "string",
"message": "string",
"attachment": 
{
},
"edited": true,
"createdAt": 0,
"moderatedAt": 0,
"updatedAt": 0,
"moderationStatus": "NOT_MODERATED"
}
}

Notify about typing
Notifies about typing message process in conference session chat or single participant if message is private.

Recommended behavior: Each client notifies the server about the process of entering text in the message input field in the chat every 4.5 seconds, and the server sends this event to the rest of the chat participants.
When a corresponding event is received, each client graphically displays this process for 5.2 seconds, and if no new event was received, then hides the corresponding graphical display.

As a result, if participantId of private message interlocutor is not specified than server events ConferenceChatTypingEvent are sent to all online conference session participants or online speakers and moderators if chat moderation is enabled else if target participantId is specified and moderation is not enabled than event is sent to exact participant.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
REQUEST BODY SCHEMA: application/json
The identifier of target participant
id
string <uuid>
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/messages/typing
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
}

Start demonstration
Starts whiteboard demonstration in the conference session.

As a result, server event MediaRoomStateChangedEvent is sent to all online conference session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
REQUEST BODY SCHEMA: application/json
Whiteboard demonstration state data
bookIndex
required
integer <int32>
pageIndex
required
integer <int32>
left
required
integer <int32>
right
required
integer <int32>
top
required
integer <int32>
bottom
required
integer <int32>
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/demonstration/whiteboard/start
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"bookIndex": 0,
"pageIndex": 0,
"left": 0,
"right": 0,
"top": 0,
"bottom": 0
}

Stop demonstration
Stops current whiteboard demonstration in the conference session.

As a result, server event MediaRoomStateChangedEvent is sent to all online conference session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/demonstration/whiteboard/stop

Update demonstration cursor state
Updates cursor state in current whiteboard demonstration in the conference session.

As a result, server event PresentationPointerStateChangedEvent is sent to all online conference session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
REQUEST BODY SCHEMA: application/json
Demonstration cursor state data
cursorTop
integer <int32> >= 0
Cursor top position in a presentation
cursorLeft
integer <int32> >= 0
Cursor left position in a presentation
cursorVisible
required
boolean
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/demonstration/whiteboard/cursor
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"cursorTop": 0,
"cursorLeft": 0,
"cursorVisible": true
}

Update demonstration state
Updates current whiteboard demonstration state in the conference session.

As a result, server event PresentationStateChangedEvent is sent to all online conference session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
REQUEST BODY SCHEMA: application/json
Whiteboard demonstration state data
bookIndex
required
integer <int32>
pageIndex
required
integer <int32>
left
required
integer <int32>
right
required
integer <int32>
top
required
integer <int32>
bottom
required
integer <int32>
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/demonstration/whiteboard/state
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"bookIndex": 0,
"pageIndex": 0,
"left": 0,
"right": 0,
"top": 0,
"bottom": 0
}

Get whiteboard
Returns information about whiteboard.Book and page index parameters should start from 1.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
QUERY PARAMETERS
bookIndex
integer <int64>
Book index
pageIndex
integer <int64>
Page index
Responses
200 Whiteboard
GET
/conference-sessions/{conferenceSessionId}/whiteboard
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"bookDTO": 
[
{
}
],
"bookCount": 0
}

Start remote screen demonstration
Starts remote (VNC) screen share demonstration in the conference session.

As a result, server event MediaRoomStateChangedEvent is sent to all online conference session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
REQUEST BODY SCHEMA: application/json
Remote screen demonstration data
remoteAddress
required
string
password
required
string
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/demonstration/screenshare/start-vnc
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"remoteAddress": "string",
"password": "string"
}

Start local screen demonstration
Starts local screen share demonstration in the conference session. In additional, demonstration owner should change media state of SCREENSHARE stream via (see Report media state) after starting real media streaming.

As a result, server event MediaRoomStateChangedEvent is sent to all online conference session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/demonstration/screenshare/start

Stop screen demonstration
Stops current screen share demonstration in the conference session. As a result, server event MediaRoomStateChangedEvent is sent to all online conference session participants.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session id
Responses
204 Success
POST
/conference-sessions/{conferenceSessionId}/demonstration/screenshare/stop

Find conference template
Finds conference template by id.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceTemplateId
required
string <uuid>
Responses
200 Conference template
GET
/conference-templates/{conferenceTemplateId}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"conferenceTemplateId": "4e39ad17-49b4-47f1-8776-29503b5f83be",
"name": "string",
"description": "string",
"conferenceType": "EQUITABLE_CONVERSATION",
"attendeeSubscribeLimit": "NONE",
"isDefault": true,
"features": 
[
"HIDE_HAND_UP"
]
}

List conference templates
Lists conference templates which are available for the current user
AUTHORIZATIONS:
IvcsAuthSession
Responses
200 Conference templates
GET
/conference-templates
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
[
{
"conferenceTemplateId": "4e39ad17-49b4-47f1-8776-29503b5f83be",
"name": "string",
"description": "string",
"conferenceType": "EQUITABLE_CONVERSATION",
"attendeeSubscribeLimit": "NONE",
"isDefault": true,
"features": 
[
]
}
]

Export participants statistics
Exports statistics of conference session participants to CSV file.
It is available for domain or system admin, operator and conference session moderator.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
QUERY PARAMETERS
wasOnConference
boolean
Whether the participant joined
fileName
string
File name
language
string
Enum: "RU" "EN"
Language
Responses
200 Conference session participants statistics
400 Bad request
404 Not Found
500 Internal server error
GET
/conference-sessions/{conferenceSessionId}/participants/statistics/export
Response samples
400404500
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Get conference session participants statistics
Returns conference session participants statistics slice.
It is available for domain or system admin, operator and conference session moderator.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
QUERY PARAMETERS
wasOnConference
boolean
Whether the participant joined
offset
integer <int32> >= 0
Default: 0
Slice offset
limit
integer <int32> [ 1 .. 100 ]
Default: 20
Slice size
Responses
200 Conference session participants slice statistics
400 Bad request
404 Not Found
500 Internal server error
GET
/conference-sessions/{conferenceSessionId}/participants/statistics
Response samples
200400404500
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

Get participant statistics
Returns statistics slice of the conference session participant.
It is available for domain or system admin, operator and conference session moderator.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
participantId
required
string <uuid>
Conference session participant ID
QUERY PARAMETERS
dateFrom
integer <int64> >= 0
Start of range
dateTo
integer <int64> >= 0
End of range
offset
integer <int32> >= 0
Default: 0
Slice offset
limit
integer <int32> [ 1 .. 100 ]
Default: 20
Slice size
Responses
200 Participant statistics
400 Bad request
404 Not Found
500 Internal server error
GET
/conference-sessions/{conferenceSessionId}/participants/{participantId}/statistics
Response samples
200400404500
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

Get participants activity
Returns conference participants presence statistics map in conference session.
Result contains map with date as key, and array with statistics data at this moment as value (array content legend: 1-st element - maximum participants presence).
Result map does not contain intervals with empty statistics data. Date intervals starts from specified "dateFrom" parameter and continues with step that specified in "stepInMinutes" parameter.
Result data should contain less than 1000 timeslots including empty ticks.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
QUERY PARAMETERS
dateFrom
required
integer <int64> >= 0
Date offset for data slice
dateTo
required
integer <int64> >= 0
Date limit for data slice
stepInMinutes
integer <int32> >= 1
Default: 1
Step in minutes. Starts from 1.
Responses
200 Success
400 Bad request
404 Not Found
500 Internal server error
GET
/conference-sessions/{conferenceSessionId}/participants/statistics/activity
Response samples
200400404500
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
{
"property1": 
[
],
"property2": 
[
]
}
}

Export conference sessions statistics
Exports conference sessions statistics to CSV file.
It is available for domain or system admin, operator and conference session moderator.
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
dateFrom
required
integer <int64> >= 0
Date offset for data slice
dateTo
required
integer <int64> >= 0
Date limit for data slice
searchCriteria
string
Search criteria
ownerId
string <uuid>
Owner id
conferenceType
string
Enum: "EQUITABLE_CONVERSATION" "WEBINAR"
Type of conference
fileName
string
File name
language
string
Enum: "RU" "EN"
Language
Responses
200 Conference session statistics
400 Bad request
500 Internal server error
GET
/conference-sessions/statistics/export
Response samples
400500
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Export user participation statistics
Returns CSV file of statistics of user participation in conference sessions.
It is available for domain or system admin, operator and conference session moderator.
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
profileId
required
string <uuid>
searchCriteria
string
Search criteria
dateFrom
required
integer <int64> >= 0
Date (UNIX time in ms)
dateTo
required
integer <int64> >= 0
Date (UNIX time in ms)
ownerId
string <uuid>
conferenceType
string
Enum: "EQUITABLE_CONVERSATION" "WEBINAR"
fileName
string
File name
language
string
Enum: "RU" "EN"
Language
Responses
200 User participation statistics
400 Bad request
500 Internal server error
GET
/conference-sessions/statistics/user-participation/export
Response samples
400500
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Get conference session statistics
Returns conference session statistics.
It is available for domain or system admin, operator and conference session moderator.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
conferenceSessionId
required
string <uuid>
Conference session ID
Responses
200 Conference session statistics
400 Bad request
404 Not Found
500 Internal server error
GET
/conference-sessions/{conferenceSessionId}/statistics/aggregation
Response samples
200400404500
Content type
application/json
Copy
Expand all Collapse all
{
"name": "string",
"conferenceSessionId": "2df2d749-63a9-4bdf-8d0c-33caa5c48e90",
"startDate": 0,
"endDate": 0,
"duration": 0,
"conferenceType": "EQUITABLE_CONVERSATION",
"invitedParticipantsCount": 0,
"invitedAndVisitedParticipantsCount": 0,
"registeredParticipantsCount": 0,
"registeredAndVisitedParticipantsCount": 0,
"guestParticipantsCount": 0,
"visitedParticipantsCount": 0,
"engagement": 0,
"userAgentsCounts": 
[
{
}
],
"pastAllPollsParticipantsCount": 0
}

Get participants activity
Returns conference session participants presence statistics map in specified set of conference sessions.
Date range should be less or equal one month (31 days).
Result contains map with date as key, and array with statistics data at this moment as value (array content legend: 1-st element - maximum participants presence).
Result map does not contain intervals with empty statistics data. Date intervals starts from specified "dateFrom" parameter and continues with step that specified in "stepInMinutes" parameter.
Result data should contain less than 1000 timeslots including empty ticks.
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
dateFrom
required
integer <int64> >= 0
Date offset for data slice
dateTo
required
integer <int64> >= 0
Date limit for data slice
stepsInMinutes
integer <int32> >= 1
Default: 1
Step in minutes. Starts from 1.
searchCriteria
string
Search criteria
ownerId
string <uuid>
Owner id
conferenceType
string
Enum: "EQUITABLE_CONVERSATION" "WEBINAR"
Type of conference
Responses
200 Conference session statistics
400 Bad request
500 Internal server error
GET
/conference-sessions/statistics/participation-activity
Response samples
200400500
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
{
"property1": 
[
],
"property2": 
[
]
}
}

Get conference sessions statistics slice
Returns conference sessions statistics slice.
It is available for domain or system admin, operator and conference session moderator.
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
dateFrom
required
integer <int64> >= 0
Date offset for data slice
dateTo
required
integer <int64> >= 0
Date limit for data slice
searchCriteria
string
Search criteria
ownerId
string <uuid>
Owner id
conferenceType
string
Enum: "EQUITABLE_CONVERSATION" "WEBINAR"
Type of conference
offset
integer <int32> >= 0
Default: 0
Slice offset
limit
integer <int32> [ 1 .. 100 ]
Default: 20
Slice size
Responses
200 Conference session statistics
400 Bad request
500 Internal server error
GET
/conference-sessions/statistics
Response samples
200400500
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

Get conference sessions statistics aggregation
Returns conference sessions statistics aggregation.
It is available for domain or system admin, operator and conference session moderator.
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
dateFrom
required
integer <int64> >= 0
Date offset for data slice
dateTo
required
integer <int64> >= 0
Date limit for data slice
searchCriteria
string
Search criteria
ownerId
string <uuid>
Owner id
conferenceType
string
Enum: "EQUITABLE_CONVERSATION" "WEBINAR"
Type of conferene
Responses
200 Conference session statistics
400 Bad request
500 Internal server error
GET
/conference-sessions/statistics/aggregation
Response samples
200400500
Content type
application/json
Copy
Expand all Collapse all
{
"totalCount": 0,
"averageVisitedParticipantsCount": 0,
"invitedAndVisitedParticipantsRatio": 0,
"registeredAndVisitedParticipantsRatio": 0,
"guestParticipantsRatio": 0,
"engagement": 0,
"userAgentsCounts": 
[
{
}
]
}

Get aggregated statistics of user participation.
Returns aggregated statistics of user participation in conference sessions.
It is available for domain or system admin, operator and conference session moderator.
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
profileId
required
string <uuid>
dateFrom
required
integer <int64> >= 0
Date (UNIX time in ms)
dateTo
required
integer <int64> >= 0
Date (UNIX time in ms)
ownerId
string <uuid>
conferenceType
string
Enum: "EQUITABLE_CONVERSATION" "WEBINAR"
Responses
200 Aggregation of user participation statistics
400 Bad request
500 Internal server error
GET
/conference-sessions/statistics/user-participation/aggregation
Response samples
200400500
Content type
application/json
Copy
Expand all Collapse all
{
"profileId": "faebe71b-2bf8-4bdb-9b67-258e4d6aa00a",
"participationRatio": 0,
"engagement": 0
}

Get user participation statistics slice
Returns slice of statistics of user participation in conference sessions.
It is available for domain or system admin, operator and conference session moderator.
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
profileId
required
string <uuid>
dateFrom
required
integer <int64> >= 0
Date (UNIX time in ms)
dateTo
required
integer <int64> >= 0
Date (UNIX time in ms)
ownerId
string <uuid>
conferenceType
string
Enum: "EQUITABLE_CONVERSATION" "WEBINAR"
offset
integer <int32> >= 0
Default: 0
Slice offset
limit
integer <int32> [ 1 .. 100 ]
Default: 20
Slice size
Responses
200 User participation statistics
400 Bad request
500 Internal server error
GET
/conference-sessions/statistics/user-participation
Response samples
200400500
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

Get user session information
Returns current user session information that are bind to session header.
AUTHORIZATIONS:
IvcsAuthSession
Responses
200 User session information
GET
/session/info
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"sessionId": "f6567dd8-e069-418e-8893-7d22fcf12459",
"loginToken": "d95d1f7e-d72b-4289-9318-75df183f28c1",
"user": 
{
"profileId": "faebe71b-2bf8-4bdb-9b67-258e4d6aa00a",
"login": "string",
"userType": "ADMIN",
"securityLevel": "UNCLASSIFIED",
"avatarResourceId": "bc84249e-8ad6-4649-8b59-04125098a24d",
"name": "string",
"email": 
{
},
"phone": 
{
},
"additionalContact": 
{
},
"aboutSelf": "string",
"isRegisteredUser": true,
"companyId": "8bb73d03-06b4-47c7-80c7-59301f770eda",
"companyName": "string",
"isConferenceCreationEnabled": true,
"locale": "RU",
"timeZone": "string",
"isTimeZoneAutoSelection": true,
"ldapInfo": 
{
}
},
"diskUtilizationInfo": 
{
"diskSpaceLimit": 0,
"diskSpaceUsage": 0
},
"clientIp": "string",
"hasAdminAccess": true,
"timestamp": 0
}

Login
Login to the system with user credentials (login/password).
REQUEST BODY SCHEMA: application/json
User credentials
login
required
string
password
required
string
rememberMe
boolean
Default: false
Responses
200 User session information
POST
/login
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"login": "string",
"password": "string",
"rememberMe": false
}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"sessionId": "f6567dd8-e069-418e-8893-7d22fcf12459",
"loginToken": "d95d1f7e-d72b-4289-9318-75df183f28c1",
"user": 
{
"profileId": "faebe71b-2bf8-4bdb-9b67-258e4d6aa00a",
"login": "string",
"userType": "ADMIN",
"securityLevel": "UNCLASSIFIED",
"avatarResourceId": "bc84249e-8ad6-4649-8b59-04125098a24d",
"name": "string",
"email": 
{
},
"phone": 
{
},
"additionalContact": 
{
},
"aboutSelf": "string",
"isRegisteredUser": true,
"companyId": "8bb73d03-06b4-47c7-80c7-59301f770eda",
"companyName": "string",
"isConferenceCreationEnabled": true,
"locale": "RU",
"timeZone": "string",
"isTimeZoneAutoSelection": true,
"ldapInfo": 
{
}
},
"diskUtilizationInfo": 
{
"diskSpaceLimit": 0,
"diskSpaceUsage": 0
},
"clientIp": "string",
"hasAdminAccess": true,
"timestamp": 0
}

Login with token
Login to the system with token that are assigned to particular user session.
REQUEST BODY SCHEMA: application/json
Login token
token
string
Login token of a user
Responses
200 User session information
POST
/login-with-token
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"token": "string"
}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"sessionId": "f6567dd8-e069-418e-8893-7d22fcf12459",
"loginToken": "d95d1f7e-d72b-4289-9318-75df183f28c1",
"user": 
{
"profileId": "faebe71b-2bf8-4bdb-9b67-258e4d6aa00a",
"login": "string",
"userType": "ADMIN",
"securityLevel": "UNCLASSIFIED",
"avatarResourceId": "bc84249e-8ad6-4649-8b59-04125098a24d",
"name": "string",
"email": 
{
},
"phone": 
{
},
"additionalContact": 
{
},
"aboutSelf": "string",
"isRegisteredUser": true,
"companyId": "8bb73d03-06b4-47c7-80c7-59301f770eda",
"companyName": "string",
"isConferenceCreationEnabled": true,
"locale": "RU",
"timeZone": "string",
"isTimeZoneAutoSelection": true,
"ldapInfo": 
{
}
},
"diskUtilizationInfo": 
{
"diskSpaceLimit": 0,
"diskSpaceUsage": 0
},
"clientIp": "string",
"hasAdminAccess": true,
"timestamp": 0
}

Login as guest
Login as guest by ticket link.
REQUEST BODY SCHEMA: application/json
User credentials
guestName
required
string
Displayed name of guest
guestDescription
string
Displayed description of guest
ticketLink
required
string
Ticket link
Responses
200 User session information
POST
/login-as-guest
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"guestName": "string",
"guestDescription": "string",
"ticketLink": "string"
}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"sessionId": "f6567dd8-e069-418e-8893-7d22fcf12459",
"loginToken": "d95d1f7e-d72b-4289-9318-75df183f28c1",
"user": 
{
"profileId": "faebe71b-2bf8-4bdb-9b67-258e4d6aa00a",
"login": "string",
"userType": "ADMIN",
"securityLevel": "UNCLASSIFIED",
"avatarResourceId": "bc84249e-8ad6-4649-8b59-04125098a24d",
"name": "string",
"email": 
{
},
"phone": 
{
},
"additionalContact": 
{
},
"aboutSelf": "string",
"isRegisteredUser": true,
"companyId": "8bb73d03-06b4-47c7-80c7-59301f770eda",
"companyName": "string",
"isConferenceCreationEnabled": true,
"locale": "RU",
"timeZone": "string",
"isTimeZoneAutoSelection": true,
"ldapInfo": 
{
}
},
"diskUtilizationInfo": 
{
"diskSpaceLimit": 0,
"diskSpaceUsage": 0
},
"clientIp": "string",
"hasAdminAccess": true,
"timestamp": 0
}

Logout
Logout from the system.
AUTHORIZATIONS:
IvcsAuthSession
Responses
204 Success
POST
/logout

Get password recovery info
Returns password recovery info
PATH PARAMETERS
recoveryTokenId
required
string <uuid>
Recovery token identifier
Responses
200 Password recovery info
404 Recovery token not found
GET
/public/profiles/password-recovery/{recoveryTokenId}
Response samples
200404
Content type
application/json
Copy
Expand all Collapse all
{
"name": "string",
"login": "string",
"email": "string",
"recoveryTokenCreatedAt": 0
}

Get profile info
Returns profile info
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
profileId
required
string <uuid>
Profile ID
Responses
200 User profile info
404 User profile is not found
GET
/profiles/{profileId}
Response samples
200404
Content type
application/json
Copy
Expand all Collapse all
{
"profileId": "faebe71b-2bf8-4bdb-9b67-258e4d6aa00a",
"login": "string",
"userType": "ADMIN",
"securityLevel": "UNCLASSIFIED",
"avatarResourceId": "bc84249e-8ad6-4649-8b59-04125098a24d",
"name": "string",
"email": 
{
"value": "string",
"privacy": "PUBLIC"
},
"phone": 
{
"value": "string",
"privacy": "PUBLIC"
},
"additionalContact": 
{
"value": "string",
"privacy": "PUBLIC"
},
"aboutSelf": "string",
"isRegisteredUser": true,
"companyId": "8bb73d03-06b4-47c7-80c7-59301f770eda",
"companyName": "string",
"isConferenceCreationEnabled": true,
"locale": "RU",
"timeZone": "string",
"isTimeZoneAutoSelection": true,
"ldapInfo": 
{
"ldapUserId": "string"
}
}

Update profile
Updates specified parameters of self profile.

As a result, server event server event ProfileChangedEvent is sent to current user.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
profileId
required
string <uuid>
Profile ID
REQUEST BODY SCHEMA: application/json
Set of parameters to be updated for profile. Absence of particular parameter means that this property is not updated.
name
string [ 1 .. 255 ] characters
avatarResourceId
object (NullableParameterId)
emailPrivacy
string
Enum: "PUBLIC" "AUTHORIZED" "NOBODY"
phone
object (NullablePhone) <= 512 characters
Phone in form of E164 phone format or valid SIP, H323, RTSP, S4B address
phonePrivacy
string
Enum: "PUBLIC" "AUTHORIZED" "NOBODY"
additionalContact
object (NullableParameterContact) <= 255 characters
Any contact data in free form
additionalContactPrivacy
string
Enum: "PUBLIC" "AUTHORIZED" "NOBODY"
aboutSelf
object (NullableParameterNote) <= 2000 characters
Some information about user in free form
locale
string
Enum: "RU" "EN"
Locale of user's clients applications
timeZone
string
Specified time zone for the user account. Value is public TZ database name (for example: Europe/Moscow)
isTimeZoneAutoSelection
boolean
Time zone selection depends on user's OS time zone
Responses
204 Success
PATCH
/profiles/{profileId}
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"name": "string",
"avatarResourceId": 
{
"value": "a860a344-d7b2-406e-828e-8d442f23f344"
},
"emailPrivacy": "PUBLIC",
"phone": 
{
"value": "string"
},
"phonePrivacy": "PUBLIC",
"additionalContact": 
{
"value": "string"
},
"additionalContactPrivacy": "PUBLIC",
"aboutSelf": 
{
"value": "string"
},
"locale": "RU",
"timeZone": "string",
"isTimeZoneAutoSelection": true
}

Profile events
Events of changing profile states and data
Responses
200 Subscribed
Callbacks
POST
ProfileChangedEventPOST
LogoutRequestEvent
GET
/websocket/profileEvents

Request password recovery
Sends link to recover current user's password via email
REQUEST BODY SCHEMA: application/json
Password recovery request
userIdentifier
required
string
User's identifier. Email or login is allowed.
Responses
200 Password recovery info
POST
/public/profiles/password-recovery/request-recovery
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"userIdentifier": "string"
}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"name": "string",
"login": "string",
"email": "string",
"recoveryTokenCreatedAt": 0
}

Update password
Updates self profile password
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
profileId
required
string <uuid>
Profile ID
REQUEST BODY SCHEMA: application/json
Update password request
oldPassword
required
string
Old user password
newPassword
required
string <= 32 characters
New user password (min length is defined by system setting)
Responses
204 Success
POST
/profiles/{profileId}/change-password
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"oldPassword": "string",
"newPassword": "string"
}

Update password during recovery
Changes user's password by recovery token
PATH PARAMETERS
recoveryTokenId
required
string <uuid>
Recovery token identifier
REQUEST BODY SCHEMA: application/json
Password change request
newPassword
required
string
New user's password
Responses
204 Success
POST
/public/profiles/password-recovery/{recoveryTokenId}/change-password
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"newPassword": "string"
}

Get interlocutor by contact
Returns interlocutor information by user contact ID.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
contactId
required
string <uuid>
Contact ID
Responses
200 Interlocutor info
404 Interlocutor is not found
GET
/interlocutors/contact/{contactId}
Response samples
200404
Content type
application/json
Copy
Expand all Collapse all
{
"name": "string",
"email": "string",
"phone": "string",
"interlocutorType": "FOREIGN_CONTACT",
"contact": 
{
"contactId": "b5ec5d98-4bee-4da1-ad24-dde86346cb1d",
"type": "FOREIGN",
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"createdAt": 0,
"updatedAt": 0,
"note": "string",
"tags": 
[
]
},
"profile": 
{
"profileId": "faebe71b-2bf8-4bdb-9b67-258e4d6aa00a",
"login": "string",
"userType": "ADMIN",
"avatarResourceId": "bc84249e-8ad6-4649-8b59-04125098a24d",
"additionalContact": "string",
"aboutSelf": "string",
"isGuest": true,
"companyId": "8bb73d03-06b4-47c7-80c7-59301f770eda",
"companyName": "string",
"parameters": 
[
]
},
"ldapUser": 
{
"ldapUserId": "string",
"parameters": 
[
]
}
}

Get interlocutor by ldap user
Returns interlocutor information by ldap user ID.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
userId
required
string
Ldap user ID
Responses
200 Interlocutor info
404 Interlocutor is not found
GET
/interlocutors/ldap/{userId}
Response samples
200404
Content type
application/json
Copy
Expand all Collapse all
{
"name": "string",
"email": "string",
"phone": "string",
"interlocutorType": "FOREIGN_CONTACT",
"contact": 
{
"contactId": "b5ec5d98-4bee-4da1-ad24-dde86346cb1d",
"type": "FOREIGN",
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"createdAt": 0,
"updatedAt": 0,
"note": "string",
"tags": 
[
]
},
"profile": 
{
"profileId": "faebe71b-2bf8-4bdb-9b67-258e4d6aa00a",
"login": "string",
"userType": "ADMIN",
"avatarResourceId": "bc84249e-8ad6-4649-8b59-04125098a24d",
"additionalContact": "string",
"aboutSelf": "string",
"isGuest": true,
"companyId": "8bb73d03-06b4-47c7-80c7-59301f770eda",
"companyName": "string",
"parameters": 
[
]
},
"ldapUser": 
{
"ldapUserId": "string",
"parameters": 
[
]
}
}

Get interlocutor by profile
Returns interlocutor information by user profile ID.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
profileId
required
string <uuid>
Profile ID
Responses
200 Interlocutor info
404 Interlocutor is not found
GET
/interlocutors/profile/{profileId}
Response samples
200404
Content type
application/json
Copy
Expand all Collapse all
{
"name": "string",
"email": "string",
"phone": "string",
"interlocutorType": "FOREIGN_CONTACT",
"contact": 
{
"contactId": "b5ec5d98-4bee-4da1-ad24-dde86346cb1d",
"type": "FOREIGN",
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"createdAt": 0,
"updatedAt": 0,
"note": "string",
"tags": 
[
]
},
"profile": 
{
"profileId": "faebe71b-2bf8-4bdb-9b67-258e4d6aa00a",
"login": "string",
"userType": "ADMIN",
"avatarResourceId": "bc84249e-8ad6-4649-8b59-04125098a24d",
"additionalContact": "string",
"aboutSelf": "string",
"isGuest": true,
"companyId": "8bb73d03-06b4-47c7-80c7-59301f770eda",
"companyName": "string",
"parameters": 
[
]
},
"ldapUser": 
{
"ldapUserId": "string",
"parameters": 
[
]
}
}

Find interlocutors
Searches and returns interlocutors by search criteria in specified sources.

Offset for next page request should be built as sum of previous offset and previous result count for particular interlocutor source.
AUTHORIZATIONS:
IvcsAuthSession
REQUEST BODY SCHEMA: application/json
Search interlocutors request
searchCriteria
string
sources
required
Array of objects (InterlocutorSourceRequestDTO)
searchContext
object (InterlocutorSearchContextDTO)
Context for which interlocutors are searched (for instance, conference session or chat room)
limit
integer <int32> <= 200
Default: 50
Responses
200 Founded interlocutors
POST
/interlocutors/find
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"searchCriteria": "string",
"sources": 
[
{
}
],
"searchContext": 
{
"contextType": "CONFERENCE_SESSION",
"contextId": "84451116-c600-49e2-9c60-5b6b34fae0d6"
},
"limit": 50
}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"sources": 
[
{
}
]
}

Get available interlocutors types
Returns available for search interlocutors types for current user. Available types depend on system settings and current user data state.
AUTHORIZATIONS:
IvcsAuthSession
Responses
200 Available interlocutor types
GET
/interlocutors/types
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
[
"FOREIGN_CONTACT"
]

Create note contact
Creates new note contact and add it to personal contact list. Returns created contact.

Sends an ContactAddedEvent to current user
AUTHORIZATIONS:
IvcsAuthSession
REQUEST BODY SCHEMA: application/json
A set of parameters for a new contact. Phone or email fields must be filled.
name
string [ 1 .. 255 ] characters
email
string (Email) <= 255 characters
Email for note contact
phone
string (Phone) <= 512 characters
Phone in form of E164 phone format or valid SIP, H323, RTSP, S4B, VNC, RTMP address
note
string (Note) <= 2000 characters
Some information about user in free form
tags
Array of strings (Tags)
Set of tags assigned to a contact
Responses
200 Contact invitations slice
POST
/contacts/create-note
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"name": "string",
"email": "string",
"phone": "string",
"note": "string",
"tags": 
[
"string"
]
}
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"name": "string",
"email": "string",
"phone": "string",
"interlocutorType": "FOREIGN_CONTACT",
"contact": 
{
"contactId": "b5ec5d98-4bee-4da1-ad24-dde86346cb1d",
"type": "FOREIGN",
"ownerProfileId": "c89cb221-d0cc-4aba-977c-75836e8307b5",
"createdAt": 0,
"updatedAt": 0,
"note": "string",
"tags": 
[
]
},
"profile": 
{
"profileId": "faebe71b-2bf8-4bdb-9b67-258e4d6aa00a",
"login": "string",
"userType": "ADMIN",
"avatarResourceId": "bc84249e-8ad6-4649-8b59-04125098a24d",
"additionalContact": "string",
"aboutSelf": "string",
"isGuest": true,
"companyId": "8bb73d03-06b4-47c7-80c7-59301f770eda",
"companyName": "string",
"parameters": 
[
]
},
"ldapUser": 
{
"ldapUserId": "string",
"parameters": 
[
]
}
}

Contact events
Events of changing contacts list
Responses
200 Subscribed
Callbacks
POST
ContactAddedEventPOST
ContactChangedEventPOST
ContactBlockedEventPOST
ContactUnblockedEventPOST
ContactRemovedEventPOST
ContactOnlineEventPOST
ContactInvitationCreatedEventPOST
ContactInvitationRemovedEvent
GET
/websocket/contactEvents

Get contacts changes
Returns contacts changes of current user from specified date.
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
dateFrom
integer <int64> >= 0
Date offset for contact updatedAt field (exclude)
limit
integer <int32> [ 1 .. 200 ]
Default: 50
Result slice limit. Should be more then 0.
Responses
200 Success
GET
/contacts/changes
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

Get contacts
Returns contacts of current user by parameters.
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
searchCriteria
string
Search criteria (by fields: name, email, phone, tags)
offset
integer <int32> >= 0
Default: 0
Result slice offset. Starts from 0.
limit
integer <int32> [ 1 .. 200 ]
Default: 50
Result slice limit. Should be more then 0.
orderAsc
boolean
Default: true
Result slice sort order (by contact name)
Responses
200 Success
GET
/contacts
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

Get contacts presences
Returns presence statuses for users from personal contacts list. Result contains only ONLINE and OFFLINE statuses, other users from contacts list has status UNKNOWN. Real presence status is available for authorized (there is backward contact) contacts only.
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
offset
integer <int32> >= 0
Default: 0
Result slice offset. Starts from 0.
limit
integer <int32> [ 1 .. 1000 ]
Default: 1000
Result slice limit. Should be more then 0.
Responses
200 Contacts presence statuses
GET
/contacts/presences
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

Get contact invitations
Returns current user contact invitations.
AUTHORIZATIONS:
IvcsAuthSession
QUERY PARAMETERS
searchCriteria
string
Additional search criteria (by fields: name, email, phone)
offset
integer <int32> >= 0
Default: 0
Result slice offset. Starts from 0.
limit
integer <int32> [ 1 .. 200 ]
Default: 50
Result slice limit. Should be more then 0.
sortField
string
Default: "DATE"
Enum: "DATE" "NAME"
Sort result set by field (default - by date)
orderAsc
boolean
Default: true
Result slice sort order
Responses
200 Contact invitations slice
GET
/contacts/invitations
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"data": 
[
{
}
],
"hasNext": true,
"totalCount": 0
}

Get user tags
Returns the tags previously used by the user for contacts.
AUTHORIZATIONS:
IvcsAuthSession
Responses
200 List of tags
GET
/contacts/tags
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
[
"string"
]

Get profiles presences
Returns presence statuses for specified users. Real presence status is available for authorized (there is backward contact) contacts only.
AUTHORIZATIONS:
IvcsAuthSession
REQUEST BODY SCHEMA: */*
Set of profile ids. Maximum allowed size of set for requested profiles is 1000.
Array ()
string <uuid>
Responses
200 Profiles presence statuses
POST
/contacts/presences/find-for-users
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
[
{
"profileId": "faebe71b-2bf8-4bdb-9b67-258e4d6aa00a",
"presenceStatus": "ONLINE"
}
]

Invite to contacts
Invites users to personal contact list of current user.

As a result following server events are sent:
- ContactAddedEvent to current user.
- ContactInvitationCreatedEvent to invited users if they do not have contact to current user
- ContactOnlineEvent to current and invited users if this is a mutual add to contacts
AUTHORIZATIONS:
IvcsAuthSession
REQUEST BODY SCHEMA: */*
Set of profile ids. Maximum allowed size of set for requested profiles is 100.
Array ()
string <uuid>
Responses
204 Success
400 reason = PROFILE_BLOCKED_OR_DELETED, type = ContactInvitationException - if invited profile is deleted or blocked.
500 Internal server error
POST
/contacts/invite
Response samples
500
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Reject contact invitations
Rejects contact invitations.

As a result following server event is sent:
- ContactInvitationRemovedEvent to invitation's owner.
AUTHORIZATIONS:
IvcsAuthSession
REQUEST BODY SCHEMA: */*
Set of profile ids. Maximum allowed size of set for requested profiles is 100.
Array ()
string <uuid>
Responses
204 Success
400 reason = INVITATION_NOT_FOUND, type = ContactInvitationException - if invitation from requested user is not found.
500 Internal server error
POST
/contacts/invitations/reject
Response samples
500
Content type
application/json
Copy
Expand all Collapse all
{
"message": "string",
"reason": "string",
"type": "string"
}

Remove contact
Remove the specified contact from user contact list.

As a result following server events is sent:
- ContactRemovedEvent to current user.
If contact is foreign:
- ContactInvitationRemovedEvent to contact user, if current user did not respond to the invitation.
- ContactOnlineEvent to contact user.
- ContactChangedEvent to contact user.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
id
required
string <uuid>
Contact id
Responses
204 Success
DELETE
/contacts/{id}

Update contact
Updates the specified contact data.

As a result following server events is sent:
- ContactChangedEvent to current user.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
id
required
string <uuid>
Contact id
REQUEST BODY SCHEMA: application/json
Set of parameters to be updated for specified contact. Absence of particular parameter means that this property is not updated.
name
string [ 1 .. 255 ] characters
email
object (NullableEmail) <= 255 characters
Email for note contact
phone
object (NullablePhone) <= 512 characters
Phone in form of E164 phone format or valid SIP, H323, RTSP, S4B address
note
object (NullableNote) <= 2000 characters
Some information about user in free form
tags
object (NullableTags)
Set of tags assigned to a contact
Responses
204 Success
PATCH
/contacts/{id}
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"name": "string",
"email": 
{
"value": "string"
},
"phone": 
{
"value": "string"
},
"note": 
{
"value": "string"
},
"tags": 
{
"value": 
[
]
}
}

Remove contacts
Remove specified contacts from user contact list.

As a result following server events is sent:
- ContactRemovedEvent to current user.
If contact is foreign:
- ContactInvitationRemovedEvent to contact user, if current user did not respond to the invitation.
- ContactOnlineEvent to contact user.
- ContactChangedEvent to contact user.
AUTHORIZATIONS:
IvcsAuthSession
REQUEST BODY SCHEMA: */*
Set of contact ids.
Array ()
string <uuid>
Responses
204 Success
POST
/contacts/remove

Create resource
Creates a file representation to bind with the file to be uploaded
AUTHORIZATIONS:
IvcsAuthSession
REQUEST BODY SCHEMA: */*
A name of the resource
name
required
string
A name of resource
Responses
200 An identifier of the resource
POST
/resources/create
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
"497f6eca-6276-4993-bfeb-53cbbbba6f08"

Download file
Downloads specified resource file from server. Inside we compose the URL and redirect user to this URL.Optionally one can add width and height parameters in order to resize image resource to given size.
PATH PARAMETERS
resourceId
required
string <uuid>
Resource id to upload
QUERY PARAMETERS
contentDisposition
string
Default: "ATTACHMENT"
Enum: "INLINE" "ATTACHMENT"
Specifies Content-Disposition header value of response either INLINE or ATTACHMENT.
It is ATTACHMENT by default.
fileName
string
Desired resource file name including extension. Can be used to set a name of file.
width
integer <int64> >= 1
Desired resource width. Can be used to set image resource size.
height
integer <int64> >= 1
Desired resource height. Can be used to set image resource size.
Responses
200 Success
GET
/resources/{resourceId}

Upload file
Uploads file on server. Place raw file inside HTTP POST body and specify headers: resourceSize, chunkBegin and chunkEnd.
They define the offset of a transmitted part relative to original file in bytes.
It means that if you have a big file then you can upload it in parts with multiple http requests.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
resourceId
required
string <uuid>
An id of the resource that should be bound with uploading file
HEADER PARAMETERS
chunkBegin
required
integer <int64>
An index into the File indicating the first byte to include in the Chunk.
chunkEnd
required
integer <int64>
An index into the File indicating the first byte that will not be included in the new Chunk
resourceSize
required
integer <int64>
A size of the file in bytes
REQUEST BODY SCHEMA: application/octet-stream
Responses
204 The chunk was successfully written
POST
/resources/{resourceId}

Confirm delayed sms
Confirms delayed sms that need to be approved by sim-account owner. It is configured by system administrator.
AUTHORIZATIONS:
IvcsAuthSession
REQUEST BODY SCHEMA: application/json
Sms confirmation info
approved
Array of strings <uuid>
rejected
Array of strings <uuid>
Responses
204 Success
POST
/system/sms-approval
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"approved": 
[
"497f6eca-6276-4993-bfeb-53cbbbba6f08"
],
"rejected": 
[
"497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
}

Get system broadcast notification
Returns system broadcast notification if any that are set by system administrator (usually it is notification about scheduled work on server).
AUTHORIZATIONS:
IvcsAuthSession
Responses
200 System broadcast information
GET
/public/system/broadcast-notification
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"text": 
[
{
}
],
"id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
}

Get system information
Returns system information for particular domain.
Responses
200 System information
GET
/public/system/info
Response samples
200
Content type
application/json
Copy
Expand all Collapse all
{
"domain": 
{
"id": "string",
"name": "string",
"fullName": "string",
"copyright": "string",
"supportEmail": "string",
"supportPhone": "string",
"supportUrl": "string",
"logo": "3c06f846-1ab1-40a9-8645-a19a9fdeae85",
"bigLogo": "2f21491a-8ad2-4726-8858-a3be0d99fa00",
"eventLogo": "7df23114-d7ec-4b63-bde6-6e427d0fb105",
"frameLogo": "410954a8-149e-4e7f-859f-e87acad50129",
"registrationAvailable": true,
"passwordModification": true,
"externalLoginUrl": "string",
"privateOfficeUrl": "string",
"googleAnalyticsAccount": "string",
"hostUrl": "string",
"registrationUrl": "string",
"promoSiteUrl": "string",
"userAgreementLink": "string",
"bwCheckerLink": "string",
"frameLinkAvailable": true,
"outgoingCallAvailable": true,
"minPhoneLength": 0,
"maxPhoneLength": 0,
"conferenceReferenceHost": "string",
"avaibleConnectionConfiguration": true,
"features": 
[
],
"notificationBySmsAvailable": true,
"notifyAboutSendingSmsEnabled": true,
"smsTariffUrl": "string",
"recordDeletionEnabled": true,
"fixedLocale": "RU",
"leaveConferenceRedirectUrl": "string",
"defaultSenderEmail": "string",
"autoRecord": true,
"calendarOrganizerEmail": "string",
"recordLiveIntervalInDays": 0,
"ivcsBilling": true,
"externalBilling": true,
"theme": "string",
"externalContactsUrl": "string",
"sendMissedNotification": true,
"sendThirdpartyNotification": true,
"sendSmsFromOwner": true,
"emailToSendSms": "string",
"deleted": true
},
"systemSettings": 
[
{
}
],
"licenseInfo": 
{
"domains": 
[
],
"notAfter": 0,
"notBefore": 0,
"vcsServerInstanceId": "string",
"isExpired": true,
"isValidForVCSServerInstance": true,
"isValidForDomain": true,
"licenseId": "string",
"issued": 0,
"licenseIssuer": "string",
"licenseHolder": "string",
"maxRecordCount": 0,
"isMultiServerInstallation": true,
"isSupport4K": true,
"universalConnectionsLimit": 0,
"universalWebRTCConnectionsLimit": 0,
"universalConnectionsInConferencesLimit": 0,
"webRTCConnectionsInConferencesLimit": 0,
"additionalWebRTCSpeakersInWebinarsLimit": 0,
"webRTCConnectionsInWebinarsLimit": 0
},
"systemInstallationType": "LIVE_CD",
"securityInstallationType": "NONE",
"apiVersion": "string"
}

Send app crash report
Commits application crash report attachment to server side for following collecting and analyzing. The attachment should be uploaded to server as resource before performing commit.
AUTHORIZATIONS:
IvcsAuthSession
PATH PARAMETERS
fileId
required
string <uuid>
Crash report resource ID
Responses
204 Success
POST
/system/crash-report/{fileId}

Send e-mail to support
Sends e-mail to system support.
AUTHORIZATIONS:
IvcsAuthSession
REQUEST BODY SCHEMA: application/json
E-mail data
subject
string
body
string
fromEmail
string
context
string
attachments
Array of strings
Responses
204 Success
POST
/system/mail-to-support
Request samples
Payload
Content type
application/json
Copy
Expand all Collapse all
{
"subject": "string",
"body": "string",
"fromEmail": "string",
"context": "string",
"attachments": 
[
"string"
]
}

Get client applications
Returns available client application versions
QUERY PARAMETERS
appName
string
Enum: "IVCS_MEETING_ANDROID" "IVCS_MEETING_IOS" "IVCS_MESSENGER_ANDROID" "IVCS_MESSENGER_IOS" "IVCS_MESSENGER_DESKTOP" "IVCS_ROOM_DESKTOP" "IVCS_OUTLOOK_PLUGIN"
Client app name
appType
string
Enum: "IVCS_MEETING" "IVCS_MESSENGER" "IVCS_ROOM" "IVCS_OUTLOOK"
Client app type
assemblyType
string
Default: "ENTERPRISE"
Enum: "ENTERPRISE" "STORE"
Client assembly type
osType
string
Enum: "WINDOWS" "MAC_OS" "ASTRA_LINUX" "IOS" "ANDROID"
Operation system type
lastVersion
boolean
Default: true
Search only for last versions
Responses
200 Available client applications
400 Bad request
500 Internal server error
GET
/public/applications
Response samples
200400500
Content type
application/json
Copy
Expand all Collapse all
[
{
"name": "string",
"appName": "IVCS_MEETING_ANDROID",
"appType": "IVCS_MEETING",
"osType": "WINDOWS",
"assemblyType": "ENTERPRISE",
"version": "string",
"downloadUrl": "string",
"extension": "string",
"size": 0,
"date": 0
}
]

Subscribe to event channel
Subscribe to event channel is using by WebSocket protocol.

First, connect to this url over websocket protocol. After connecting you will be able to receive events from server.

In order to check if channel is alive heartbeat messages should be used. If channel is empty for 30 seconds then connection is closed by the server. It is the client responsibility to ping the server. To ping send the text message ping-[ping_number] where [ping_number] is any unique identifier. In response server will send you back pong-[ping_number] where [ping_number] is the identifier you used to send ping. One approach for ping number is a simple integer counter.

Other reasons why connection could be closed are the following: user session has expired, I\O error on a network channel, user has logged out.

All server events are wrapped into so called NumberedMessage which us used for controlling the sequence of receiving messages and possible message losses:
{
    "sequenceNumber": 410,
    "message": ..., // server message
    "_class": "NumberedMessage"
}
In its turn NumberedMessage can be wrapped up into BulkMessage if multiple messages are being sent at once:
{
    "events": [...], // list of server events
    "_class": "BulkMessage"
}

Message sequence integrity control
In order to check for potential server message losses you need to save sequnceNumber of the last received NumberedMessage. This number should be reset to -1 during each new websocket connection (after successful reconnection attempts, when there are no message losses sequenceNumber should not be reset).

During each connection/reconnection server sends sync message where "message" is absent. It is used for checking current sequenceNumber in this channel. For a new channel connection sequenceNumber is 0, after reconnecting it is equal to the number of the last sent message to this channel. If after reconnecting client sequenceNumber is less then server sequenceNumber then is a sign of messages lost on a client side.

In other cases client should check it sequenceNumber with the one in message
serverSequenceNumber > clientSequenceNumber + 1, means server events lost - needs refresh
serverSequenceNumber = clientSequenceNumber + 1, means no losses - message can be used
serverSequenceNumber < clientSequenceNumber + 1, received duplicated events - message should be filtered out
PATH PARAMETERS
sessionId
required
string <uuid>
User session id. In order to get it you need to be authenticated.
busId
required
string <uuid>
Random uuid which represents your websockets connection id
serializer
required
string
Default: "json"
Payload serializer
Responses
200 Subscribed
GET
/websocket/eventbus/{sessionId}/{busId}/{serializer}

Chat events
Chat events
Responses
200 Subscribed
Callbacks
POST
ConferenceChatClearedEventPOST
ConferenceChatTypingEventPOST
ConferenceChatMessageEventPOST
ConferenceChatMessageUpdatedEventPOST
ConferenceChatMessageRemovedEventPOST
ConferenceChatParticipantMessagesRemovedEvent
GET
/websocket/chatActiveConferenceEvents

Resource events
Events of changing states of some conference session resources: records, documents, etc
Responses
200 Subscribed
Callbacks
POST
ConferenceSessionDocumentCreateEventPOST
ConferenceSessionDocumentUpdateEventPOST
ConferenceSessionDocumentDeleteEvent
GET
/websocket/resourcesActiveConferenceEvents

