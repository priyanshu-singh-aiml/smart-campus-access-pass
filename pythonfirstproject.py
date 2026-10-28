print("="*64)
print(" "*8,"SMARTCAMPUS UTILITY & ACCESS PASS GENERATOR"," "*8)
print("="*64)
category=(input("Select User Category(1.Student,2:Faculty/Staff): "))
if category in ["student","Student"]:
    sub_category=(input("Enter Sub-Category(UG/PG): "))
    if sub_category in ["ug","UG","PG","pg"]:
        student_cgpa=(float(input("Enter Student CGPA: ")))
        if student_cgpa>=8.5:
            if sub_category=="ug"or"UG":
                base_fee=500
                merit_discount=200
            elif sub_category=="pg"or"PG":
                base_fee=350
                merit_discount=200

        elif student_cgpa>7.5:
             if sub_category=="ug"or"UG":
                base_fee=500
                merit_discount=100
             elif sub_category=="pg"or"PG":
                base_fee=350
                merit_discount=100
        else:
            if sub_category=="ug"or"UG":
                base_fee=500
                merit_discount=0
            elif sub_category=="pg"or"PG":
                base_fee=350
                merit_discount=0
elif category in["faculty","Faculty","staff","Staff"]:
    sub_category=(input("Enter Sub-Category(Resident faculty/Visting): "))
    if sub_category in ["Resident faculty","Visting","resident faculty","visting"]:
        serviced_year=(int(input("Enter your serviced year: ")))
        if serviced_year>10:
            if sub_category=="Resident faculty":
                base_fee=800
                merit_discount=150
            elif sub_category=="Visting":
                base_fee=1200
                merit_discount=150          
        else:
           if sub_category=="Resident faculty":
            base_fee=800
            merit_discount=0
           elif sub_category=="Visting":
            base_fee=1200
            merit_discount=0
else:
    print("worng ") 
        
if category in  ["student","Student"]:
    student_peak=150
else:
    student_peak=0

vichle_type=(int(input("Selecting Parking permit(0.None,2:Two-wheeler,4:four wheeler): ")))
if vichle_type==2:
    vichle_price=200
elif vichle_type==4 and category=="student":
    vichle_price=600-student_peak
elif vichle_type==4:
    vichle_price=600
elif vichle_type==0:
    vichle_price=0
else:
    print("wrong chocie")


if category=="student" or vichle_type=="0":
    student_peak=0

electricity_unit=(int(input("Enter Monthly Electricity Consumption(in kWh): ")))
if electricity_unit<101:
    electricity_bill=(electricity_unit*3) + 50
elif electricity_unit<301:
    electricity_bill=(electricity_unit*5) + 100
elif electricity_unit<500:
    electricity_bill=(electricity_unit*7.50) + 150
elif electricity_unit>500:
    electricity_bill=(electricity_unit*10) + 250
else:
    print("NONE")
print("-"*64)
print(" "*8,"CALCULATED INVOICE BREAKDOWN"," "*8)
print("-"*64)
print("Base Access Pass Fee : ₹",base_fee)
print("Merit Discount: ₹",merit_discount)
print("Parking Fee: ₹",vichle_price)
if category in ["student","Student"]:
    print("Student Peak Surcharge: ₹",student_peak)
print("Net Pass & Parking Total: ₹",vichle_price+base_fee+student_peak-merit_discount)
print("-"*64)
print("Electricity Bill: ₹",electricity_bill)
print("-"*64)
print("TOTAL MONTHLY PAYBLE: ₹",base_fee-merit_discount+vichle_price+student_peak+electricity_bill)