import sys
conversion_factors = {
    ('km', 'm'): 1000,
    ('m', 'km'): 0.001,
    ('km', 'mile'): 0.621371,
    ('mile', 'km'): 1.60934,
    ('m', 'mile'): 0.000621371,
    ('mile', 'm'): 1609.34
}
value=sys.argv[1]
if len(sys.argv)==4:
    from_unit=sys.argv[2].lower()
    to_unit=sys.argv[3].lower()
    key=from_unit,to_unit
    if key in conversion_factors:
        ans=conversion_factors[key]*int(value)
        print(f"{sys.argv[1]} {from_unit} = {ans:.4f} {to_unit}")
    elif from_unit == to_unit:
        print(f"{sys.argv[1]} {from_unit} = {from_unit} {to_unit}  (No Conversion")
    else:
        print(f"Invalid Input")