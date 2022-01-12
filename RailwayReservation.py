class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getStatus(self):
        print('------------------------------')
        print(f'The name of the train is {self.name}')
        print(f'The seats available in the train is {self.seats}')
        print('-------------------------------')
    def fareInfo(self):
        
        print(f'The price of the ticket is {self.fare}')

    def bookTicket(self):
        if self.seats>0:
            
            print(f'your seat is booked and your seat number is {self.seats}')
            self.seats=self.seats-1
        else:
            print('Sorry this train if full')
    def cancelTicket(self):
        print('Your seat is canceled!')
        self.seats=self.seats+1

intercity=Train('Intercity Express',90,300)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket()
intercity.getStatus()