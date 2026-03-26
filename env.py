import random
from models import Observation, Action, Reward

class EcommerceEnv:
    def __init__(self):
        self.sessions = [
            {"history": [1,2], "target": 3},
            {"history": [2,3], "target": 1},
            {"history": [1,3], "target": 2},
        ]
        self.max_steps = 5

    def reset(self):
        self.current_session = random.choice(self.sessions)
        self.steps = 0
        self.done = False
        return self._get_obs()

    def _get_obs(self):
        return Observation(
            user_id=1,
            history=self.current_session["history"]
        )

    def step(self, action: Action):
        self.steps += 1

        target = self.current_session["target"]

        # Reward shaping (IMPORTANT)
        if action.recommended_product == target:
            reward = 1.0   # purchase
            self.done = True
        elif action.recommended_product in self.current_session["history"]:
            reward = 0.3   # click
        else:
            reward = -0.2  # irrelevant

        if self.steps >= self.max_steps:
            self.done = True

        return self._get_obs(), Reward(score=reward), self.done, {}

    def state(self):
        return {
            "steps": self.steps,
            "target": self.current_session["target"]
        }