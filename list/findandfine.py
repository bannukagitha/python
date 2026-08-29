def odd(self,arr,fine,total):
        for i in range(len(arr)):
            if arr[i]%2!=0:
                total+=fine[i]
        return total
def even(self,arr,fine,total):
    for i in range(len(arr)):
        if arr[i]%2==0:
            total+=fine[i]
    return total
def totalFine(self, date, car, fine):
    total=0
    if date%2==0:
        return self.odd(car,fine,total)
    else:
        return self.even(car,fine,total)