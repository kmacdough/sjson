from collections import defaultdict
import itertools


class FSM(object):
    """
    A finite state machine
    """

    def __init__(self, *, alphabet=None):
        self.states = {}
        self.start_state = None
        self.final_states = []

    def add_state(self, name, edges=None, default=None,
                  *, start=False, final=False):
        """
        Add a state to this FSM
        :param name: state name
        :type edges: str
        :param edges: edge dict
        :type edges: dict (char -> state)
        :param default: state to transition to by default
        :type default: srt
        :param start: True if this state is the start state
        :type start: bool
        :param final: True if this state is a final state
        :type final: bool
        :return: None
        """
        edges = {} if edges is None else edges
        if default is None:
            self.states[name] = edges
        else:
            self.states[name] = defaultdict(lambda: default, edges)
        if start:
            self.start_state = name
        if final:
            self.final_states.append(name)

    def run(self, char_stream, *, limit=None):
        state = self.start_stat
        counter = itertools.count() if limit is None else range(limit)
        for i in counter:
            cur_char = char_stream.cur_char()
            state = self.states[state[cur_char]]
            if state in self.final_states:
                return state



