import json

class State:
    def __init__(self) -> None:
        self.state = {
            'temperature' : 0,
            'humidity': 0,
            'bed_wet': False,
            'baby_outbed': False,
            
        }
        self.deep_state = 0 
    
    def sensor_in(self, text):
        self.state = json.loads(text)
        self.state['deep_state'] = self.deep_state
        
        
    def state_out(self):
        return json.dumps(self.state)

state = State()

