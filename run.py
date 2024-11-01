import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'swarm'))

from dotenv import load_dotenv
load_dotenv() 

from swarm.repl import run_demo_loop
from sql_agents import sql_router_agent

if __name__ == "__main__":
    run_demo_loop(sql_router_agent)