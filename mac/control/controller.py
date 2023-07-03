from abc import ABC, abstractmethod

class Controller(ABC):
    """An abstract controller class, for other controllers
    to inherit from
    """

    # init agents and their observations
    def __init__(self, env):
        self.env = env
        self.agent_ids = self.env.get_env_agents()
    def isCentralized(self):
        pass

    def run(self, render=False, max_iteration=None):
        print("***************************")
        print("Controller - run function")
        """Runs the controller on the environment given in the init,
        with the agents given in the init

        Args:
            render (bool, optional): Whether to render while runngin. Defaults to False.
            max_iteration ([type], optional): Number of steps to run. Defaults to infinity.
        """
        done = False
        index = 0
        print("going to getobservation from env.get_env().reset()")
        observation = self.env.get_env().reset()
        print("observation recievd:")
        print(observation)
        self.total_rewards = []
        while done is not True:
            index += 1
            if max_iteration is not None and index > max_iteration:
                break

            # display environment
            if render:
                self.env.render()
            print("asserting observation is in dict form")
            # assert observation is in dict form
            print("calling env.observation_to_dict")
            observation = self.env.observation_to_dict(observation)
            print("observation as dict:")
            print(observation)

            # get actions for all agents and perform.
            print("calling get_join_action")
            joint_action = self.get_joint_action(observation)
            print("back to run method")
            print("joint action:")
            print(joint_action)
            print("calling self.perform_joint_action")
            observation, reward, done, info = self.perform_joint_action(joint_action)
            print("back to run method")
            print("new observation:")
            print(observation)
            print("new reward:")
            print(reward)
            print("done")
            print(done)
            print("info")
            print(info)

            # save rewards
            print("adding new reward to total rewards")
            self.total_rewards.append(reward)
            print("new total reward:")
            print(self.total_rewards)

            # check if all agents are done
            if all(done.values()):
                break

        if render:
            self.env.render()

    def perform_joint_action(self, joint_action):
        print("*******************")
        print("Controller - perform_join_action")
        print("env:")
        print(self.env)
        print("Calling env.step with paramater joint action:")
        print(joint_action)
        print("is Centralized value:")
        print(self._isCentralized)
        print("Caliing env.step())
        value_to_ret =  self.env.step(joint_action,self._isCentralized)
        print("back to perform_joint_action")
        print("value to return:")
        print(value_to_ret)
        return value_to_ret

    @abstractmethod
    def get_joint_action(self, observation):
        pass
