from crewai.flow.flow import Flow, listen, or_, start


class OrExampleFlow(Flow):

    @start()
    def start_method(self):
        print("Starting flow")
        return "Hello from the method 1"

    @listen(start_method)
    def second_method(self):
        print("Second method")
        return "Hello from the method 2"

    @listen(or_(start_method, second_method))
    def logger(self, result):
        print(f"Logger: {result}")


flow = OrExampleFlow()
flow.kickoff()
