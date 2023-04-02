import itertools

class Person:
    id_counter = 0 # unique identifier 
    def __init__(self, name:str, phone:str, degree:str='', interests:list=[]):
        self.name = name
        self.phone = phone
        self.degree = degree
        self.interests = interests
        global people # access people database
        self.matches = Matches(self)
        # generate unique identifier
        self.id= Person.id_counter
        Person.id_counter += 1

    def __str__(self):
        return self.name

    def get_matches(self):
        return print(self.matches)

people:list[Person] = [] # people database

# get person via id
def get_person(id:int):
    global people # access people database
    for person in people:
        if person.id == id: return person

class Matches:
    def __init__(self, person:Person):
        self.person = person
        
    # generate top three matches
    def generate_matches(self):
        global people # access people database
        # get scores for each person
        scores = {}
        for current_person in people: # compare to all people
            if current_person.id == self.person.id: continue # skip if the same person
            score = 0
            # add points for similarities
            if (self.person.degree != '') & (current_person.degree == self.person.degree): score += 50 # if same degree, add 50 points
            if (self.person.interests != []): score += (sum(x == y for x, y in zip(self.person.interests, current_person.interests)) / len(self.person.interests)) * 50 # if same interests, add points in relation to overlap (up to 50) (reference: https://www.geeksforgeeks.org/python-count-of-common-elements-in-the-lists/)
            scores.update({current_person.id: score}) # add to res with score
        # get actual matches
        matches = dict(filter(lambda val: val[1] > 25.0, scores.items())) # remove with score below 25 (reference: https://thispointer.com/python-filter-a-dictionary-by-conditions-on-keys-or-values/)
        top_matches = dict(itertools.islice(matches.items(),3)) # get top three (reference: https://theprogrammingexpert.com/slice-dictionary-python/)
        sorted_matches = {val[0]:val[1] for val in sorted(top_matches.items(), key = lambda x : (-x[1], x[0]))} # sort by score (https://www.geeksforgeeks.org/python-sort-dictionary-by-values-and-keys/)
        return sorted_matches
    
    # get matches as list
    def get_matches(self):
        matches_dict = self.generate_matches().keys()
        matches:list[Person] = []
        for match in matches_dict:
            matches.append(get_person(match))
        return matches