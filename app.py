import gradio as gr
from env import EcommerceEnv
from models import Action
import random

def simulate():
    env = EcommerceEnv()
    obs = env.reset()

    log = ""
    total_reward = 0
    steps = 0
    clicks = 0
    purchases = 0

    done = False

    while not done:
        # simple agent
        action = Action(recommended_product=random.randint(1, 3))

        obs, reward, done, _ = env.step(action)

        steps += 1
        total_reward += reward.score

        if reward.score == 1.0:
            purchases += 1
        elif reward.score > 0:
            clicks += 1

        log += f"Step {steps} → Recommended: {action.recommended_product} | Reward: {reward.score}\n"

    # Metrics
    ctr = clicks / steps if steps else 0
    conversion = purchases / steps if steps else 0

    log += "\n--- SESSION SUMMARY ---\n"
    log += f"Total Steps: {steps}\n"
    log += f"Total Reward: {round(total_reward,2)}\n"
    log += f"Clicks: {clicks}\n"
    log += f"Purchases: {purchases}\n"
    log += f"CTR: {round(ctr,2)}\n"
    log += f"Conversion Rate: {round(conversion,2)}\n"

    return log


gr.Interface(
    fn=simulate,
    inputs=[],
    outputs="text",
    title="🛒 AI E-commerce Recommendation Simulator",
    description="Simulates how an AI agent recommends products and optimizes user engagement & conversions."
).launch(share=True)