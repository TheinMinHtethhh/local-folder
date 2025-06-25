class Car:
    def __init__(self) -> None:
        self.__car_price = 0
    
    @property
    def car_price(self):
        return self.__car_price
    
    @car_price.setter
    def car_price(self,price):
        if price < 0:
            raise ValueError('price cannot be negative')
        self.__car_price = price

    def installment_plan(self,amount):
        times_to_pay = 0
        remainder_to_pay = 0
        times_time = ''
        if amount <= self.__car_price:
            times=self.__car_price//amount
            remainder = self.__car_price%amount
            times_to_pay += times
            remainder_to_pay += remainder
            if times == 1:
                times_time += 'time'
            else:
                times_time += 'times'
        return times_to_pay,remainder_to_pay,times_time
    
    def show_times_to_pay(self,amount):
        times_to_pay,remainder_to_pay,times_time = self.installment_plan(amount)
        if remainder_to_pay > 0:
            print(f'you need to pay {times_to_pay} {times_time} and {remainder_to_pay}$ in cash')

        else:
            print(f'you need to pay {times_to_pay} {times_time}')
            

lamborghini = Car()
lamborghini.car_price = int(input('set the new car price : '))
print(f'the car\'s new update price is {lamborghini.car_price}')
lamborghini.show_times_to_pay(int(input('set your installment plan : ')))



        
        



        
