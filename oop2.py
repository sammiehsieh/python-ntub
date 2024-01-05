class Daddy():
    def company(self):
        return 20000
    
class Me(Daddy):
    def company(self):
        daddy_company  = super().company()
        return 5000 + daddy_company
    
m = Me()
print(m.company()) # 25000