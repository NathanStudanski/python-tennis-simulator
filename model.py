import random
class TennisPlayer:
    def __init__(self, first_serve, first_serve_points_won, second_serve_points_won, first_serve_return_points_won, second_serve_return_points_won):
        self.first_serve = first_serve
        self.first_serve_points_won = first_serve_points_won
        self.second_serve_points_won = second_serve_points_won
        self.first_serve_return_points_won = first_serve_return_points_won
        self.second_serve_return_points_won = second_serve_return_points_won
        
    def play_point(self, probability):
        if random.random() <= probability:
            return True
        
        else:
            return False
    
    def play_first_serve(self):
        return self.play_point(self.first_serve_points_won)    
    
    def play_second_serve(self):
        return self.play_point(self.second_serve_points_won)
    
    def play_first_serve_return(self):
        return self.play_point(self.first_serve_return_points_won)
    
    def play_second_serve_return(self):
        return self.play_point(self.second_serve_return_points_won) 
