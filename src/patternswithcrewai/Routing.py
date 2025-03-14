from crewai.flow.flow import Flow, start, listen, or_, and_, router # Import necessary modules from crewai

class Routing(Flow): # Define a class RouteFlow that inherits from Flow

    @start() # Decorator to mark the entry point of the flow
    def In(self): # Define the In method
        print("Receiving Input...") # Print a message indicating input reception

    @listen(In) # Decorator to listen to the In method
    def llm_call_router(self): # Define the llm_call_router method
        print("Routing LLM Calls...") # Print a message indicating LLM call routing

    @listen(llm_call_router) # Decorator to listen to the llm_call_router method
    def llm_call_1(self): # Define the llm_call_1 method
        print("Processing in LLM Call 1...") # Print a message indicating processing in LLM Call 1

    @router(and_(llm_call_router)) # Decorator to route based on llm_call_router
    def llm_call_2(self): # Define the llm_call_2 method
        return "Optional Out" # Return a string "Optional Out"

    @router(and_(llm_call_router)) # Decorator to route based on llm_call_router
    def llm_call_3(self): # Define the llm_call_3 method
        return "Optional Out" # Return a string "Optional Out"

    @listen(or_(llm_call_1, "Optional Out")) # Decorator to listen to either llm_call_1 or "Optional Out"
    def Out(self): # Define the Out method
        print("Final Output Generated...") # Print a message indicating final output generation

def Run(): # Define a function Run
    obj = Routing() # Create an instance of RouteFlow
    obj.kickoff() # Start the flow

def Plot(): # Define a function Plot
    obj = Routing() # Create an instance of RouteFlow
    obj.plot() # Plot the flow
# uv run RRun
# uv run RPlot


# # from crewai.flow.flow import Flow, listen, start, or_

# # class RouteFlow(Flow):
# #     @start()
# #     def In(self):
# #         """Handles input processing."""
# #         print("🔹 Assalam-O-Alaikum! Receiving Input...")

# #     @listen(In)
# #     def llm_call_router(self):
# #         #"""LLM processes the input."""
# #         print("🤖 Processing input using LLM...")
# #         #return "process_complete"

# #     @listen(llm_call_router)
# #     def llm_call_1(self, query):
# #         """LLM Call 1 node"""
# #         print(f"🤖 LLM Call 1: Processing query '{query}' using LLM model 1...")
# #     @listen(llm_call_router)
# #     def llm_call_2(self):
# #         """LLM Call 2 node"""
# #         print("🤖 LLM Call 2: Processing query using LLM model 2...")
# #     @listen(llm_call_router)
# #     def llm_call_3(self):
# #         """LLM Call 3 node"""
# #         print("🤖 LLM Call 3: Processing query using LLM model 3...")

# #     @listen(or_("llm_call_1", "llm_call_2", "llm_call_3"))
   

# #     def Out(self):
# #         #"""Handles output."""
# #         print("✅ Generating final output...")

# # def kickoff():
# #     obj = RouteFlow()
# #     obj.kickoff()

# # def plot7():
# #     obj = RouteFlow()
# #     obj.plot()

# from crewai.flow.flow import Flow, listen, start, or_, and_
# class RouteFlow(Flow):
#     @start()
#     def In(self):
#         print("Receiving Input...")
#     @listen(In)
#     def llm_call_router(self):
#         print("Performing...")
#     @listen(or_(llm_call_router))#...
#     @listen(llm_call_router)
#     def llm_call_1(self):
#         print("Processing...")#....
#     @listen(and_(llm_call_router))#1...
#     @listen(llm_call_router)
#     def llm_call_2(self):
#         print("Processing ...")#1..
#     @listen(and_(llm_call_router))#2..
#     @listen(llm_call_router)
#     def llm_call_3(self):
#         print("Processing ...")#2...
#     # #
#     @listen(llm_call_2)
#     def Out(self):
#         print("Processing ...")
#     @listen(llm_call_3)
#     def Out(self):
#         print("Processing ...")

#     #@listen(and_(llm_call_1, or_(llm_call_2, llm_call_3)))
    

    
    
#     @listen(and_(llm_call_2, llm_call_3))
#     # @listen(or_(llm_call_1))#///
#     @listen(llm_call_1)
#     def Out(self):
#         print("Generating...")#////
    
# def kickoff():
#     obj = RouteFlow()
#     obj.kickoff()

# def plot7():
#     obj = RouteFlow()
#     obj.plot()