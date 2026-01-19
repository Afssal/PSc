from crewai import Task,Agent,Crew
import os


class Agents:

    def __init__(self,llm,goal,role,backstory,ATask,output,query):

        self.llm = llm
        self.goal = goal
        self.role = role
        self.backstory = backstory
        self.Task = ATask
        self.expected_outcome = output
        self.query = query
        self.description = self.Task + "\n User input : " + self.query

    def Builder(self):

        creator = Agent(
            role = self.role,
            goal = self.goal,
            backstory = (self.backstory),
            llm = self.llm,
            verbose = False
        )

        task = Task(
            description=(self.description),
            expected_output=self.expected_outcome,
            agent=creator
        )

        crew = Crew(
            agents=[creator],
            tasks=[task]
        )

        return crew.kickoff()

