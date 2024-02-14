class Mpesa:
    def __init__(self,account_balance,phone_number):
        self.account_balance= account_balance
        self.phone_number = phone_number
    def send_money(self,amount, recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES sent to {recipient}")
        else:
            print("Insufficient amount to send money")
class PersonalMpesa(Mpesa):
    def __init__(self, account_balance, phone_number,id_no):
        super().__init__(account_balance, phone_number)
        self.id_no = id_no
    def buy_airtime(self, amount):
        self.account_balance -= amount
        print(f"{amount} KES airtime bought succesfully")
class Business_Mpesa(Mpesa):
    def __init__(self,account_balance, phone_number, business_name, business_id):
        super().__init__(account_balance, phone_number)
        self.business_name = business_name
        self.business_id =business_id
    def receive_payment(self, amount):
        self.account_balance += amount
        print(f"{amount} KES received from a customer")
personal=PersonalMpesa(2000, 727065104, 876299874)
personal.send_money(300, 727112315)
personal.buy_airtime(150)
personal=Business_Mpesa(1000, 72384949, 45367,48)
personal.receive_payment(200)







