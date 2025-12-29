'''
Implement a class Time to represent and manipulate quantities of time stored in 
hours (non-negative integer-valued) and minutes (non-negative real-valued).
The number of minutes should always be less than 60.
  
The variables, inside the class, storing hours and minutes should be declared private.

Implement a constructor taking no argument, meant to initialize the times to 0 hours and 0 minutes.
When this is called, it should print out “Default Constructor called”.

Implement a constructor taking two arguments meant to initialize the hours and minutes values.
When this is called, it should print out “Constructor with two arguments called for (hours,minutes)”
where hours and minutes should actually show the values and not letters.

Implement the destructor, which should output a message, i.e, when this is called,
it should print out “Destructor called for (hours,minutes)” where hours and minutes should actually show the real values (not the letters).

Implement overloaded operators + and - to perform, respectively, addition and subtraction.
If a larger quantity of time is being subtracted from a smaller quantity of time, then the result should be 0 hours and 0 minutes.
The overloaded operators should work when:
both the operands are of the type of the time object;
the second operand is an integer (indicating minutes).

Implement overloaded operators * and / to perform multiplication and division with a positive scalar.

Implement an overloaded operator = to perform assignment when the right hand side is an object of type Time and also when the right hand side is an integer (indicating minutes).

Implement overloaded operators ==, <, > to perform comparisons and return a value of type bool. In this case, the second operand can either be an object of type Time or an integer (indicating minutes).

Implement a counter variable (count) within the class that keeps a track of the number of objects that are existing i.e. with memory allocated at any point in the program.

Instructions for usage:

Do not modify the main function, comment out some parts for debugging or testing purposes if needed.

Only modify the class Time in the TODO sections. Remove the pass statement before adding your code.

Run `python3 autograder.py` to check the output of your code.


'''


class Time:
    
    count = 0 # static variable to keep track of the number of objects

    def __str__(self):
        #Implement string representation here
        #TODO
        return f"{self.__hours} hours, {float(self.__minutes)} minutes"

    def __init__(self, hours=0, minutes=0):
        #Implement constructor here
        #TODO
        self.__hours = hours
        self.__minutes = minutes
        if hours == 0 and minutes == 0:
            print("Default Constructor called")
        else:
            print(f"Constructor with two arguments called for ({hours},{float(minutes)})")
        Time.count += 1
        pass    

    def __del__(self):
        #Implement destructor here
        #TODO
        print(f"Destructor called for ({self.__hours},{float(self.__minutes)})")
        Time.count -= 1
        pass

    def __add__(self, other):
        #Implement addition overload here
        #TODO
        try:
            other=int(other)
            total_minutes=self.__hours*60+self.__minutes+other
            h=int(total_minutes//60)
            m=total_minutes%60
            return Time(h,m)
        except:
            h=self.__hours + other._Time__hours
            m=self.__minutes + other._Time__minutes
            if m>=60:
                h+=m//60
                m=m%60
            return Time(h,m)

    def __sub__(self, other):
        #Implement subtraction overload here
        #TODO
        try:
            other=int(other)
            total_minutes=self.__hours*60+self.__minutes-other
            if total_minutes<0:
                return Time(0,0)
            h=int(total_minutes//60)
            m=total_minutes%60
            return Time(h,m)
        except:
            if self.__hours>other._Time__hours:
                h=self.__hours-other._Time__hours
                m=self.__minutes-other._Time__minutes
                if m<0:
                    h-=1
                    m+=60
                return Time(h,m)
            elif self.__hours==other._Time__hours and self.__minutes>=other._Time__minutes:
                h=self.__hours-other._Time__hours
                m=self.__minutes-other._Time__minutes
                return Time(h,m)
            else:
                return Time(0,0)

    def __mul__(self, scalar):
        #Implement multiplication overload here
        #TODO
        total_minutes=self.__hours*60+self.__minutes
        total_minutes*=scalar
        h=int(total_minutes//60)
        m=total_minutes%60
        return Time(h,m)
    def __truediv__(self, scalar):
        #Implement division overload here
        #TODO
        total_minutes=self.__hours*60+self.__minutes
        total_minutes/=scalar
        h=int(total_minutes//60)
        m=total_minutes % 60
        return Time(h,m)
    def __eq__(self, other):
        #Implement equal overload here
        #TODO
        return self.__minutes==other._Time__minutes and self.__hours==other._Time__hours

    def __lt__(self, other):
        #Implement less than overload here
        #TODO
        try:
            other=int(other)
            tmself=self.__hours*60+self.__minutes
            return tmself<other
        except:
            tmself=self.__hours*60+self.__minutes
            tmother=other._Time__hours*60+other._Time__minutes
            return tmself<tmother

    def __gt__(self, other):
        #Implement greater than overload here
        #TODO
        try:
            other=int(other)
            tmself=self.__hours*60+self.__minutes
            return tmself>other
        except:
            tmself=self.__hours*60+self.__minutes
            tmother=other._Time__hours*60+other._Time__minutes
            return tmself>tmother

    def __assign__(self, other):
        #Implement assignment overload here
        #TODO
        h=int(other//60)
        m=other%60
        self.__hours=h
        self.__minutes=m
def main():
    print(f"current count: {Time.count}")
    

    t1 = Time(7, 4.5)
    t2 = Time(3, 30)
    scalar = 5

    print(f"t1 = {t1}")
    print(f"t2 = {t2}")
    print(f"current count: {Time.count}")

    sum_time = t1 + t2
    print(f"t1 + t2 = {sum_time}")

    difference = t1 - t2
    print(f"t1 - t2 = {difference}")

    product = t1 * scalar
    print(f"t1 * scalar = {product}")
    print(f"current count: {Time.count}")

    divided = t2 / scalar
    print(f"t2 / scalar = {divided}")

    t3 = Time()
    t3.__assign__(100.5)
    
    print(f"t3 = {t3}")

    t3 = t3 + 100
    print(f"t3 += 100: {t3}")
    print(f"current count: {Time.count}")

    t3 = t3 - 70
    print(f"t3 -= 70: {t3}")

    if t3 < 100:
        print("t3 is less than 100")
    else:
        print("t3 is not less than 100")

    if t3 > 100:
        print("t3 is greater than 100")
    else:
        print("t3 is not greater than 100")

    if t1 < t2:
        print("t1 is less than t2")
    else:
        print("t1 is not less than t2")

    if t3 > t2:
        print("t3 is greater than t2")
    else:
        print("t3 is not greater than t2")

    if t1 == t3:
        print("t1 is equal to t3")
    else:
        print("t1 is not equal to t3")

    print(f"current count: {Time.count}")

if __name__ == "__main__":
    main()