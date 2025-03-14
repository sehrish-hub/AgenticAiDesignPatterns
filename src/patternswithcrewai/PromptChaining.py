from crewai.flow.flow import Flow, listen, start, or_, and_
class PromptChainingFlow(Flow):
    @start()
    def In(self):
        print("Receiving Input...")
    @listen(In)
    def llm_call_1(self):
        print("Processing input using LLM...")
    @listen(llm_call_1)
    def Gate(self):
        print("Performing...")
    @listen(Gate)
    def llm_call_2(self):
        print("Processing...")
    @listen(and_(Gate))
    @listen(Gate)
    def Exit(self):
        print("Processing ...")
    @listen(llm_call_2)
    def llm_call_3(self):
        print("Generating...")
    @listen(llm_call_3)
    def Out(self):
        print("Generating Final Output...")
    # Functions to run the flow
    
def Run():
    obj = PromptChainingFlow()
    obj.kickoff()
def Plot():
    obj = PromptChainingFlow()
    obj.plot()
# uv run PCRun
# uv run PCPlot





# from crewai.flow.flow import Flow, start, listen, router
# import random

# class PromptChainingFlow(Flow):

#     @start()
#     def In(self):
#         print("Start")

#     @listen(In)
#     def LlmCall1(self):
#         # Generate a single random true or false value
#         self.state["result"] = random.choice([True, False])
#         print("LlmCall1")

#     @router(LlmCall1)
#     def Gate(self):
#         if self.state["result"]:
#             return "Pass"
#         else:
#             return "Fail"

#     @listen("Fail")
#     def Exit(self):
#         print("Exit")

#     @listen("Pass")
#     def Llmcall2(self):
#         print("Llmcall2")

#     @listen(Llmcall2)
#     def Llmcall3(self):
#         print("Llmcall3")

#     @listen(Llmcall3)
#     def Out(self):
#         print("Exit")


# def Run():
#     flow = PromptChainingFlow()
#     flow.kickoff()

# def Plot11():
#     flow = PromptChainingFlow()
#     flow.plot()//////////////////////////////////////////////////////////////////
# from crewai.flow.flow import Flow, listen, start, router, or_
# import random

# class RouteFlow(Flow):

#     @start()
#     def In(self):
#         print("Start")

    
#     @listen(In)
#     def llm_call_1(self):
#         print("Processing input")
#     @listen(llm_call_1)
#     def Gate(self):
#         return "Pass"
#     @listen("Pass")
#     def llm_call_2(self):
#         print("Processing input")
#     @listen(llm_call_2)
#     def llm_call_3(self):
#         print("Processing input")
#     @listen(llm_call_3)
#     def Out(self):
#         print("Exit")
    



# def kickoff():
#     obj = RouteFlow()
#     obj.kickoff()
# def plot11():
#     obj = RouteFlow()
#     obj.plot()//////////////////////////////////