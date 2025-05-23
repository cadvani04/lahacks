from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
from mnemonic import Mnemonic

 
from uagents import Agent, Context
 
agent = Agent(name="alice", seed="secret_seed_phrase", port=8000, endpoint=["http://localhost:8000/submit"])
 
@agent.on_event("startup")
async def introduce_agent(ctx: Context):
    ctx.logger.info(f"Hello, I'm agent {agent.name} and my address is {agent.address}.")
 
if __name__ == "__main__":
    agent.run()