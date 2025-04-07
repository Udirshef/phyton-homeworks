universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollments_stats(unis):
    enrollments=[uni[1] for uni in unis]
    tuitions=[uni[2] for uni in unis]
    return enrollments,tuitions

def mean(numbers):
    return sum(numbers)/len(numbers)

def median(numbers) :
    numbers=sorted(numbers)
    mid=len(numbers)//2
    if sum(numbers)%2==0:
        return (numbers[mid-1]+numbers[mid])/2
    else:
        return numbers[mid]

enrollments,tuitions=enrollments_stats(universities)

print('*'*35)
print(f"Total students: {sum(enrollments):,}")
print(f"Total tuitions: {sum(tuitions):,}\n")

print(f"Student mean: {mean(enrollments):,.2f}")
print(f"Students median: {median(enrollments):,}\n")

print(f"Tuitions mean: {mean(tuitions):,.2f}")
print(f"Tuitions median: {median(tuitions):,}")
print("*"*35)
    
