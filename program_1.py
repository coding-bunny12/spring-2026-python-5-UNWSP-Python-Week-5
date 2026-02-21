# Abrielle Nyei
# Kilometer Converter
# 2/21/26
# Function to convert kilometers to miles
def kilometers_to_miles(kilometers):
    miles = kilometers * 0.6214
    return miles

# Main program
def main():
    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers_to_miles(kilometers)
    print("Distance in miles:", miles)

main()
