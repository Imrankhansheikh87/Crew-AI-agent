from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class BilingualAiAgentWithAmericanAccentAndRealTimeInteractionCrew():
    """BilingualAiAgentWithAmericanAccentAndRealTimeInteraction crew"""

    @agent
    def language_processing_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['language_processing_expert'],
            tools=[SerperDevTool()],
        )

    @agent
    def speech_synthesis_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['speech_synthesis_expert'],
            tools=[SerperDevTool()],
        )

    @agent
    def dispatch_coordination_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['dispatch_coordination_expert'],
            tools=[SerperDevTool()],
        )

    @agent
    def location_tracking_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['location_tracking_expert'],
            tools=[SerperDevTool()],
        )


    @task
    def query_understanding_task(self) -> Task:
        return Task(
            config=self.tasks_config['query_understanding_task'],
            
        )

    @task
    def response_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['response_generation_task'],
            
        )

    @task
    def speech_conversion_task(self) -> Task:
        return Task(
            config=self.tasks_config['speech_conversion_task'],
            
        )

    @task
    def dispatch_management_task(self) -> Task:
        return Task(
            config=self.tasks_config['dispatch_management_task'],
            
        )

    @task
    def location_integration_task(self) -> Task:
        return Task(
            config=self.tasks_config['location_integration_task'],
            
        )


    @crew
    def crew(self) -> Crew:
        """Creates the BilingualAiAgentWithAmericanAccentAndRealTimeInteraction crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
