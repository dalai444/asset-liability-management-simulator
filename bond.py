# Bond class
# In its own file since I wanted the database file to focus purely on sql

class Bond:
    def __init__(self, id, name, face, coupon, maturity):
        self.id = id
        self.name = name
        self.face = face
        self.coupon = coupon
        self.maturity = maturity
