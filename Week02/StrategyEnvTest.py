import gym
from time import sleep

env = gym.make('StrategyEnv-v3')
env.reset()

#策略评估和策略改善
not_changed_count = 0
for _ in range(10000):
    env.env.policy_evaluate()
    changed = env.env.policy_improve()
    if changed:
        not_changed_count = 0
    else:
        not_changed_count += 1
    if not_changed_count == 10: #超过10次策略没有再更新，说明策略已经稳定了
        break

env.reset()

for _ in range(1000):
    env.render()
    if env.env.states_policy_action[env.env.current_state] is not None:
        observation,reward,done,info = env.step(env.env.states_policy_action[env.env.current_state])
    else:
        done = True
    print(_)
    if done:
        sleep(0.5)
        env.render()
        env.reset()
        print("reset")
    sleep(0.5)
env.close()


