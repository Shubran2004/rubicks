
import copy

class State:

    def __init__(self, state=None):
        if isinstance(state, State):
            self.__cost = state.__cost + 1
        else:
            self.__cost = 0

        self.__parent = None
        if isinstance(state, State):
            self.__parent = state
            self.__state = copy.copy(state.__state)
        else:
            self.__state = copy.copy(state)

    def __call__(self, *args, **kwargs):
        return self.__state.__call__(*args, **kwargs)

    def __lt__(self, other):
        if isinstance(other, State):
            return self.__cost < other.__cost

    def __le__(self, other):
        if isinstance(other, State):
            return self.__cost <= other.__cost
          # return comparison
    def __eq__(self, other):
        if isinstance(other, State):
            return self.__cost == other.__cost

    def __ne__(self, other):
        if isinstance(other, State):
            return self.__cost != other.__cost

    def __gt__(self, other):
        if isinstance(other, State):
            return self.__cost > other.__cost

    def __ge__(self, other):
        if isinstance(other, State):
            return self.__cost >= other.__cost

    def get(self):
        return self.__state

    @property
    def cost(self):
        return self.__cost

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state
