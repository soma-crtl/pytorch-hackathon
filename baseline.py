from env import EcommerceEnv
from models import Action
import random

env = EcommerceEnv()

total_reward = 0
episodes = 3

for ep in range(episodes):
    obs = env.reset()
    done = False

    print(f"\nEpisode {ep+1}")

    while not done:
        # Simple agent (random recommendation)
        action = Action(recommended_product=random.randint(1, 3))

        obs, reward, done, _ = env.step(action)

        print(f"Recommended: {action.recommended_product}, Reward: {reward.score}")

        total_reward += reward.score

print("\nFinal Total Reward:", total_reward)