class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items
    
    #Method to calculate possible discount for more than 10 items
    def __discount_calculation(self):
        return 0.9 if self.number_items > 10 else 1
    
    #Method to add item to check
    def add_item_to_cheque(self, name):
        try:
            if len(name) == 0 or len(name) > 40:
                raise ValueError
            self.__item_price[name]
        except ValueError:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        except KeyError:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1
    
    #Method to delete item from check
    def delete_item_from_check(self, name):
        try:
            self.__name_items.remove(name)
        except ValueError:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__number_items -= 1
    
    #Method to count total price of the check positions
    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price[item])
        return sum(total) * self.__discount_calculation()
        
    #Method to count tax of the check positions of 20% tax rate, discounted if applicable
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        for item in self.__name_items:
            if self.__tax_rate.get(item) == 20:
                twenty_percent_tax.append(item)
                
        total = []
        for item in twenty_percent_tax:
            total.append(self.__item_price[item])
        return sum(total) * 0.2 * self.__discount_calculation()
          
    #Method to count tax of the check positions of 10% tax rate, discounted if applicable
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        for item in self.__name_items:
            if self.__tax_rate.get(item) == 10:
                ten_percent_tax.append(item)
      
        total = []
        for item in ten_percent_tax:
            total.append(self.__item_price[item])
        return sum(total) * 0.1 * self.__discount_calculation()
    
    #Method to count total tax of the check positions
    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()       
    
    #Method to return customer phone number
    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            number = int(telephone_number)    
            if len(str(telephone_number)) > 10:
                raise ValueError
        except ValueError:
            if not str(telephone_number).isdigit():
                raise ValueError('Необходимо ввести цифры')
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return f'+7{telephone_number}'