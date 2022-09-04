__version__ = '0.0.1'

class Introduction:
    pass

class Authentication:
    pass

class Requests:
    pass

class Responses:
    pass

class Chat:
    def Add_Participants():
        pass

    def Turn_On_Notifications():
        pass

    def Clear_Chat_History():
        pass

    def Create_Group_Chat():
        pass

    def Get_Chat():
        pass

    def Delete_Chat():
        pass

    def Update_Chat():
        pass

    def Edit_Message():
        pass

    def Turn_Off_Notifications():
        pass

    def Forward_Messages():
        pass

    def Search_Attachments():
        pass

    def Get_Messages():
        pass

    def Get_Messages_Changes():
        pass

    def Get_User_Starred_Messages():
        pass

    def Get_Muted_Chats():
        pass

    def Get_P2P_Chat():
        pass

    def Get_Chats():
        pass

    def Search_Chats():
        pass

    def Remove_Message():
        pass

    def Remove_Message_Attachment():
        pass

    def Remove_Messages():
        pass

    def Remove_Participants():
        pass

    def Send_Audio_Message():
        pass

    def Send_Message():
        pass

    def Turn_On_Off_Notifications_From_User():
        pass

    def Star_Messages():
        pass

    def Notify_About_Typing():
        pass

    def Unstar_Messages():
        pass

    def Update_Participant():
        pass

    def Notify_About_Read():
        pass

class Chat_Call:
    def Get_Call():
        pass

    def Join_Call():
        pass

    def Leave_Call():
        pass

    def Change_Media_State():
        pass

    def Start_Screen_Sharing():
        pass

    def Stop_Screen_Sharing():
        pass

class Conference:
    def Create_Conference():
        pass

    def Delete_Conference():
        pass

    def Respond_On_Invitation():
        pass

    def Quick_Start_Conference():
        pass

    def Create_Room():
        pass

class Conference_Session:
    def Get_Conference_Session_Public_Info_By_Id():
        pass

    def Get_Conference_Session_Public_Info_By_Parameters():
        pass

    def Get_Conference_Join_Info():
        pass

    def Get_Conference_Session_Personal_Info():
        pass

    def Delete_Conference_Session():
        pass

    def Update_Conference_Session():
        pass

    def Find_Conference_Sessions_Deprecated():
        pass

    def Find_Rooms():
        pass

    def Find_Conference_Sessions():
        pass

    def Get_Conference_Sessions_Join_Data():
        pass

    def Get_Periodical_Conference_Session_Personal_Info():
        pass

    def Join_Conference_Session():
        pass

    def Leave_Conference_Session():
        pass

    def Respond_On_Invitation():
        pass

    def Start_Conference_Session():
        pass

    def Start_Recording():
        pass

    def Start_Transcription():
        pass

    def Stop_Conference_Session():
        pass

    def Stop_Recording():
        pass

    def Stop_Transcription():
        pass

class Conference_Media:
    def Get_Conference_Media_Info():
        pass

    def Get_Conference_Media_Info_Deprecated():
        pass

    def Report_Media_State():
        pass

    def Report_Participant_Media_Equipment():
        pass

    def Set_Broadcast_Language():
        pass

    def Set_Layout_Of_Mixed_Main_Content_Stream():
        pass

    def Set_Quality_Of_Mixed_Main_Content_Stream():
        pass

    def Set_Translation_Direction():
        pass

class Conference_Participants:
    def Add_Participants():
        pass

    def Cancel_Outgoing_Call():
        pass

    def Disconnect_Participants():
        pass

    def Hand_Down():
        pass

    def Hand_Up():
        pass

    def Find_Participants():
        pass

    def Get_Participant():
        pass

    def Remove_Participants():
        pass

    def Start_Outgoing_Call():
        pass

    def Update_Participant():
        pass

class Conference_Lobby:
    def Approve_Request():
        pass

    def Approve_All_Requests():
        pass

    def Get_Lobby_Participants():
        pass

    def Join_Conference_Session_Lobby():
        pass

    def Leave_Conference_Lobby():
        pass

    def Reject_Request():
        pass

    def Reject_All_Request():
        pass

class Conference_Documents:
    def Create_Document():
        pass

    def Delete_Document():
        pass

    def Update_Document():
        pass

    def Check_The_Ability_To_Upload_A_Document():
        pass

    def List_Pages_For_The_Document():
        pass

    def List_Documents():
        pass

    def Pause_Video_Demonstration():
        pass

    def Play_Video_Demonstration():
        pass

    def Set_Video_Position():
        pass

    def Start_Document_Demonstration():
        pass

    def Start_Video_Demonstration():
        pass

    def Stop_Document_Demonstration():
        pass

    def Stop_Video_Demonstration():
        pass

    def Update_Demonstration_Cursor_State():
        pass

    def Update_Demonstration_State():
        pass

class Conference_Chat:
    def Edit_Message():
        pass

    def Get_Messages():
        pass

    def Get_Private_Messages_Interlocutors():
        pass

    def Moderate_Message():
        pass

    def Remove_All_Conference_Session_Messages():
        pass

    def Remove_All_Participant_Messages():
        pass

    def Remove_Message():
        pass

    def Send_Message():
        pass

    def Notify_About_Typing():
        pass

class Whiteboard:
    def Start_Demonstration():
        pass

    def Stop_Demonstration():
        pass

    def Update_Demonstration_Cursor_State():
        pass

    def Update_Demonstration_State():
        pass

    def Get_Whiteboard():
        pass

class Screenshare:
    def Start_Remote_Screen_Demonstration():
        pass

    def Start_Local_Screen_Demonstration():
        pass

    def Stop_Screen_Demonstration():
        pass

class Conference_Templates:
    def Find_Conference_Template():
        pass

    def List_Conference_Templates():
        pass

class Conference_Statistics:
    def Export_Participants_Statistics():
        pass

    def Get_Conference_Session_Participants_Statistics():
        pass

    def Get_Participant_Statistics():
        pass

    def Get_Participants_Activity():
        pass

    def Export_Conference_Sessions_Statistics():
        pass

    def Export_User_Participation_Statistics():
        pass

    def Get_Conference_Session_Statistics():
        pass

    def Get_Participants_Activity():
        pass

    def Get_Conference_Sessions_Statistics_Slice():
        pass

    def Get_Conference_Sessions_Statistics_Aggregation():
        pass

    def Get_Aggregated_Statistics_Of_User_Participation():
        pass

    def Get_User_Participation_Statistics_Slice():
        pass

class User_Session:
    def Get_User_Session_Information():
        pass

    def Login():
        pass

    def Login_With_Token():
        pass

    def Login_As_Guest():
        pass

    def Logout():
        pass

class Profile:
    def Get_Password_Recovery_Info():
        pass

    def Get_Profile_Info():
        pass

    def Update_Profile():
        pass

    def Request_Password_Recovery():
        pass

    def Update_Password():
        pass

    def Update_Password_During_Recovery():
        pass

class Interlocutors:
    def Get_Interlocutor_By_Contact():
        pass

    def Get_Interlocutor_By_Ldap_User():
        pass

    def Get_Interlocutor_By_Profile():
        pass

    def Find_Interlocutors():
        pass

    def Get_Available_Interlocutors_Types():
        pass

class Contacts:
    def Create_Note_Contact():
        pass

    def Get_Contacts_Changes():
        pass

    def Get_Contacts():
        pass

    def Get_Contacts_Presences():
        pass

    def Get_Contact_Invitations():
        pass

    def Get_User_Tags():
        pass

    def Get_Profiles_Presences():
        pass

    def Invite_To_Contacts():
        pass

    def Reject_Contact_Invitations():
        pass

    def Remove_Contact():
        pass

    def Update_Contact():
        pass

    def Remove_Contacts():
        pass

class File_Resources:
    def Create_Resource():
        pass

    def Download_File():
        pass

    def Upload_File():
        pass

class System:
    def Confirm_Delayed_Sms():
        pass

    def Get_System_Broadcast_Notification():
        pass

    def Get_System_Information():
        pass

    def Get_System_Media_Information():
        pass

    def Send_App_Crash_Report():
        pass

    def Send_EMail_To_Support():
        pass

class Client_Applications:
    def Get_Client_Applications():
        pass

class Events_Subscription:
    def Subscribe_To_Event_Channel():
        pass

class Chat_Events:
    def Chat_Call_Events():
        pass

    def Chat_Events():
        pass

class Conference_Events:
    def Common_Events():
        pass

    def Invitation_Events():
        pass

class Active_Conference_Events:
    def Chat_Events():
        pass

    def Common_Events():
        pass

    def Media_Events():
        pass

    def Participants_Events():
        pass

    def Presentation_Events():
        pass

    def Resource_Events():
        pass

class Profile_Events:
    def Profile_Events():
        pass

class Contact_Events:
    def Contact_Events():
        pass
