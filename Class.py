'''a=input('ведите ингредиент')
class Soda :

    def __init__(self,ingredient):
        
        if isinstance(ingredient,str):
            self.ingredient=ingredient
        else:
            self.ingredient=None
        
    def show_my_drink(self):
        if self.ingredient:
            print(f'Гозировка and {self.ingredient}')
        else:
            print("обычная гозировка")

if __name__=='__main__':
    drink=Soda(a)
    print(f'{drink.show_my_drink()}')'''

            #№2

a=int(input(''))
b=int(input(''))
c=int(input(''))
class TriengleChecker:
    def __init__(self,sides):
        self.sides=sides

    def is_triengle(self):
        if all(isinstance(side ,(int , float)) for side in self.sides):
            if all(side>0 for side in self.sides):
                sorted_sides=sorted(self.sides)
                if sorted_sides[0]+sorted_sides[1]>sorted_sides[2]:
                    return 'Cheers,you can build a triengle!'
                return 'sorry but you can not make a triengle out of this'
            return 'nothing will work with negative numbers '
        return 'you only need to enter numbers'
    
if __name__=='__main__':
    check=TriengleChecker([a,b,c])
    print(f'{check.is_triengle()}')
            


    
    