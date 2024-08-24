months = [ 
    "January",
    "Febrary",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#prompt user for a date in format MM/DD/YYYY or September 8, 1636, the month in it has to be in months
def main():
    while True:
        date_given = input("Date: ")
        if "/" in date_given:
            month, day, year = date_given.split("/")
            try:
                year = year.strip()
                month = month.strip()
                month_int = int(month)
                day = day.strip()
                day_int = int(day)
                if not month_int > 12 and not day_int > 31:
                    print(year, "-", formato_month(month), "-", formato_0(day), sep="")
                    break
                else:
                    pass
            except ValueError: pass
        elif "," in date_given:
            month_day, year = date_given.split(",")
            month, day = month_day.split(" ")
            year = year.strip()
            try:
                day_int = int(day)
                if not day_int > 31:
                    print(year, "-", formato_month(month), "-", formato_0(day), sep="")
                    break
            except ValueError: pass
        else:
            pass

def formato_month(num):
    if num.isalpha():
        if num.title() in months:
            # index num position in months
            return f"{months.index(num) + 1:02}"
    if num.isdigit():
        num_int = int(num.strip())
        if num_int < 10:
            return f"{num_int:02}"
        else:
            return num_int
    
def formato_0(num):
    num_int = int(num)
    if num_int < 10:
        return f"{num_int:02}"
    else:
        return num_int
#output a formatted date in format YYYY-MM-DD adding a 0 where is only one number... every month has no more 31 days.
main()