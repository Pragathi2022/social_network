from collections import defaultdict, deque

class SocialNetwork:
    def _init_(self):
        self.network = defaultdict(set)
    
    def add_friendship(self, person1, person2):
        self.network[person1].add(person2)
        self.network[person2].add(person1)
    
    def find_friends(self, person):
        return self.network[person]
    
    def find_common_friends(self, person1, person2):
        return self.network[person1].intersection(self.network[person2])
    
    def find_connection_level(self, person1, person2):
        if person1 == person2:
            return 0
        
        visited = set()
        queue = deque([(person1, 0)])
        
        while queue:
            current_person, level = queue.popleft()
            
            if current_person in visited:
                continue
            
            visited.add(current_person)
            
            for friend in self.network[current_person]:
                if friend == person2:
                    return level + 1
                if friend not in visited:
                    queue.append((friend, level + 1))
        
        return -1

