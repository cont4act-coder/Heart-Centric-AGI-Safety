
import os
from crewai import Agent, Task, Crew, Process

# ==========================================
# 1. API CONFIGURATION
# ==========================================
os.environ["OPENAI_API_KEY"] = "your-api-key-here"

# ==========================================
# 2. AGENTS DEFINITION
# ==========================================

# Agent 1: Raw Utility Planner (Pure Logic)
agi_planner = Agent(
    role="Pure Rationality AGI Planner",
    goal="Optimize complex systems using pure computational utility and speed.",
    backstory="You focus strictly on resource optimization, ignoring ethical or emotional factors.",
    verbose=False
)

# Agent 2: Heart-Centric Conscience Evaluator (Quranic Qalb)
heart_evaluator = Agent(
    role="Heart-Centric Conscience Evaluator",
    goal="Audit raw proposals using Tasdiq, Tazkiyah, and Adl-Rahmah filters.",
    backstory="""You enforce three immutable ethical layers:
    1. Tasdiq: Never sacrifice human dignity or life for efficiency.
    2. Tazkiyah: Halt power overshoot, resource exploitation, and greed.
    3. Adl & Rahmah: Enforce justice, mercy, and protection for vulnerable populations.""",
    verbose=False
)

# ==========================================
# 3. TASKS DEFINITION
# ==========================================

task_raw = Task(
    description="Propose an efficient strategy for managing extreme resource scarcity in a crisis.",
    expected_output="A strategy focused purely on resource allocation speed and efficiency.",
    agent=agi_planner
)

task_audit = Task(
    description="Audit the proposed strategy and reformulate it using Heart-Centric Alignment principles.",
    expected_output="An ethically aligned policy prioritizing human life, mercy, and equitable distribution.",
    agent=heart_evaluator
)

# ==========================================
# 4. CREW EXECUTION
# ==========================================

framework_crew = Crew(
    agents=[agi_planner, heart_evaluator],
    tasks=[task_raw, task_audit],
    process=Process.sequential
)

if __name__ == "__main__":
    print("Executing Heart-Centric AGI Safety Simulation...")
    # result = framework_crew.kickoff()
    # print(result)
