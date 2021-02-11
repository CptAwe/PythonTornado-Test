"""
Generate unique uuids
"""

class uuidManager():

    last_uuid = -1

    def generate(self):
        self.last_uuid += 1
        return self.last_uuid
