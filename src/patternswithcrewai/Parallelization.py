from crewai.flow.flow import Flow, start, listen, router, or_, and_

class ParallelizationFlow(Flow):
    @start()
    def In(self):
        print("Start")

    @listen(In)
    def LlmCall1(self):
        print("LlmCall1")

    @listen(In)
    def LlmCall2(self):
        print("LlmCall2")

    @listen(In)
    def LlmCall3(self):
        print("LlmCall3")

    @listen(or_(LlmCall1, LlmCall2, LlmCall3))
    def Aggregator(self):
        print("Aggregator")

    @listen(Aggregator)
    def Out(self):
        print("Out")


def Run():
    flow = ParallelizationFlow()
    flow.kickoff()

def Plot():
    flow = ParallelizationFlow()
    flow.plot() 
# uv run PRun
# uv run PPlot

# @start()
#     def In(self):
#         print("HELLO, WORLD...")

#     @listen(In)
#     def llm_call_1(self):
#         print("HELLO, WORLD FROM LLM Call 1...")

#     @listen(In)
#     def llm_call_2(self):
#         print("HELLO, WORLD FROM LLM Call 2...")
    
#     @listen(In)
#     def llm_call_3(self):
#         print("HELLO, WORLD FROM LLM Call 3...")

#     @listen(or_("llm_call_1", "llm_call_2", "llm_call_3"))
#     def Aggregator(self):
#         print("This is Aggregator")
    
#     @listen("Aggregator")
#     def Out(self):
#         print("This is Output...")
# import random
# class RouteFlow(Flow):
#     @start()
#     def In(self):
#         print("Input...")
#         return "LLM Call Router"

#     @listen(In)
#     def llm_call_1(self):
#         print("LLM Call 1...")
#         return "Output"

#     @listen(In)
#     def llm_call_2(self):
#         print("LLM Call 2...")
#         return "Output"
    
#     @listen(In)
#     def llm_call_3(self):
#         print("LLM Call 3...")
#         return "Output"

#     @listen(or_("llm_call_1", "llm_call_2", "llm_call_3"))
#     def Aggregator(self):
#         llm_calls =["LLM_Call_1", "LLM_Call_2", "LLM_Call_3"]
#         selected_call = random.choice(llm_calls)
#         print(f"Routing to: (selected_call)")
#         return selected_call
    
#     @listen(and_("llm_call_1", "llm_call_2", "llm_call_3"))
#     def Aggregator(self):
#         print("Aggregrate")
#     @listen("Aggregator")

#     def Out(self):
#         print("Generating final output...")