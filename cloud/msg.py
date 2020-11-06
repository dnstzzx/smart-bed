import threading

msg_lock = threading.Lock()
msgs = {
    'esp':[],
    'app':[],
    'cloud': []
}

def msg_count(role):
    with msg_lock:
        return len(msgs[role])

def pop_msg(role):
    with msg_lock:
        msg = msgs[role].pop()
    return msg

def pop_msgs(role):
    with msg_lock:
        result = msgs[role]
        msgs[role] = []
    return result

def add_msg(role, msg):
    if role == 'cloud':
        print(msg);
        return None;
    with msg_lock:
        msgs[role].append(msg)
