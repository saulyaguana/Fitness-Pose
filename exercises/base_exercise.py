from abc import ABC, abstractmethod

class BaseExercise(ABC):
    @abstractmethod
    def process(self, body):
        pass

    @abstractmethod
    def get_metrics(self, body):
        pass
    
    @abstractmethod
    def get_repetitions(self):
        pass

    @abstractmethod
    def get_draw_config(self, body):
        pass

    @abstractmethod
    def get_summary(self):
        pass