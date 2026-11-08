def define_env(env):
    env.variables["trip"] = "Meadow walk"

    @env.macro
    def greeting(name):
        return f"Welcome to the trail, {name}!"
