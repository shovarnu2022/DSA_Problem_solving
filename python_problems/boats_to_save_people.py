"""
Given an array people and an integer limit
People array is an array of people's weights, i-th
person had a weight people[i] and each boat can
carry at most limit

Each boat carries at most 2 people at the same time,
Given that their weight sum is at most limit.

Return the minimum number of boats to carry every
given person

What is the minimum number of boats to carry every person?

People: 1, 2
Limit: 3

Answer: 1 because 1 boat carries both 1st and 2nd person
because their weight is 1 + 2 = 3

People: 3, 2, 2, 1
Limit: 3

ans: 3, how? 1 boat carries first person.
1 boat carries second person and last person.
1 boat carries third person.

Constraint questions?

Is it guaranteed each person can be carried by a boat?

Yes, no person can be heavier than the boat limit.

People: 4, 2, 2, 1
Limit: 3 <- Not allowed

Can a person weight be zero?

No, a person weight will always be bigger than zero,
and will always be less than or equal to the limit

Do we have a limit on the number of boats we are
allowed to put people in?

No, assume you have infinite number of boats,
your question is to how to use the minimum number
of boats.

Description:

> The maximum number of people a boat can carry is 2.
> The maximum weight that a boat can carry is an input
called = limit.
> There is always an answer.

Conclusion:

> Every individual person has a weight lower than or
equal to limit

> worst case scenario is that it would take as many boats
as there are people.


Intuitive thinking:

People: 3, 2, 1, 2 Limit: 4

What is out best case scenario?
> Every 2 people take a boat, and no single person takes a
whole boat.

What is out worst case scenario?

> Every person needs a boat of its own.

What do we want to do?

> We want to maximum our best case building block (2 people
at the same boat)

How do we do this?

> Which 2 candidates do you think should match together?

if the heaviest candidate can't match with the lightest
candidate, then we know for a fact that he'll take
a seperate boat alone.

> How to do get access to the lightest and the heaviest couple?

we can do this by sorting the array, if we do, the heaviest
person will be at the last position, and the lightest
person will be at the first position.

Steps to solve this:

What will use to match the heaviest and the lightest available
people?

2 pointer technique.

People: 3, 2, 1, 2 Limit: 4

array ofter sorting: 1, 2, 2, 3

Initialize 2 pointers, left at the beginning of the sorted
array and right at the end of the sorted array,
as well as intializing the boats to 0.


numRescueBoats(people, limit){
# Loop as long as the heavy pointer is still bigger than or equal to the light pointer
    people.sort()
    heavyP = people.length() - 1
    lightP = 0
    boats = 0

    while heavyP >= lightP {
        if people[heavyP] + people[lightP] <= limit:
            boats += 1
            heavyP -= 1
            lightP += 1
        else:
            boats += 1
            heavyP -= 1
    }

    return boats
}
"""

# Implementing code


def numRescueBoats(people: list[int], limit: int) -> int:
    people.sort()
    smallest = 0
    biggest = len(people) - 1
    boats = 0
    while biggest >= smallest:
        if people[biggest] + people[smallest] <= limit:
            biggest -= 1
            smallest += 1
        else:
            biggest -= 1
        boats += 1
    return boats


people_arr = [3, 2, 1, 2]
limit = 4
print(numRescueBoats(people_arr, limit))
