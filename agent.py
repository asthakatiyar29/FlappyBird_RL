import time
import flappy_bird_gym


env = flappy_bird_gym.make("FlappyBird-v0", render_mode="human")

state, _ = env.reset()
while True:
    # Next action:
    # (feed the observation to your agent here)
    action = ...  # env.action_space.sample() for a random action

    # Processing: terminated => done
    next_state, reward, done, _, _ = env.step(action)

    # Checking if the player is still alive
    if done:
        break

env.close()