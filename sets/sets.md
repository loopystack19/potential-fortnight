**sets**-A collection of unique elements , no dublicates

**creation of a set**- fruits={}

my_fruits={"apples", "bananas","mangoes"}

**to create an empty set you need the set constructor**

my_empty_set=set()

**Adding an element to a set**

my_set={1,2,3,4}

my_set.add(5)

print(my_set)

**output**->{1, 2, 3, 4, 5}

**removing an element in a set**

my_set={1,2,3,4}

my_set.remove(4)

print(my_set)

**output**->{1,2,3}

my_set.pop()->removes an element from the set

my_set.clear()->removes all the elements from the set

**my_set{}- is immutable meaning that once its initialized the values cannot be changed, inability to modify in place