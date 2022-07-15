import pywhatkit

message = "msg automatica 3"
group_id = "Fc7XkBk02sX3AGLy3psmPz"
phone_number = "+556191350143"

# pywhatkit.sendwhatmsg_instantly(phone_number, message, tab_close=True)
pywhatkit.sendwhatmsg_to_group_instantly(group_id, message, tab_close=True)
