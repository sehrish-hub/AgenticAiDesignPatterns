from crewai.flow.flow import Flow, listen, start, or_, and_, router

class AgentFlow(Flow):
    @start()
    def Human(self):
        print("Start")

    @listen(or_(Human, "Env Method"))
    def llm_call(self):
        print("something")
    
    @router(llm_call)
    def Environment(self):
        return "Env Method"

    @listen(and_(llm_call))
    def Stop(self):
        print("stop")
def Run():
    obj = AgentFlow()
    obj.kickoff()

def Plot():
    obj = AgentFlow()
    obj.plot()
# uv run ARun 
# uv run APlot

   
    # @start()
    # def Human(self):
    #     print("HELLO, WORLD...")

    # @listen(Human)
    # def llm_call(self):
    #     print("HELLO, WORLD FROM LLM Call 1...")

    # @listen(llm_call)
    # def Environment(self):
    #     print("HELLO, WORLD FROM LLM Call 2...")
    
    # @listen(llm_call)
    # def Stop(self):
    #     print("HELLO, WORLD FROM LLM Call 3...")

    # @start()
    # def Human(self):
    #     print("Start")
    # @listen(and_(Human))
    # def llm_call(self):
    #     print("Llm Call")
    # @listen(and_(llm_call))
    # def Stop(self):
    #     print("stop")
    # @listen(llm_call)
    # def Environment(self):
    #     print("HELLO")
    
#     import streamlit as st
# from crewai.flow.flow import Flow, listen, start, or_, and_, router

# # Define CrewAI Flow
# class AgentFlow(Flow):
#     @start()
#     def Human(self):
#         print("Start")

#     @listen(or_(Human, "Env Method"))
#     def llm_call(self):
#         print("something")

#     @router(llm_call)
#     def Environment(self):
#         return "Env Method"

#     @listen(and_(llm_call))
#     def Stop(self):
#         print("stop")

# # Streamlit UI
# st.title("🤖 CrewAI Flow Deployment in Streamlit")

# # Initialize session state
# if "flow" not in st.session_state:
#     st.session_state.flow = AgentFlow()

# # Buttons for execution
# col1, col2 = st.columns(2)

# with col1:
#     if st.button("Run Flow"):
#         st.write("🚀 Running CrewAI Flow...")
#         st.session_state.flow.kickoff()
#         st.success("✅ CrewAI Flow Execution Completed!")

# with col2:
#     if st.button("Plot Flow"):
#         st.write("📊 Generating Flow Diagram...")
        
#         # Save flow diagram as HTML
#         diagram_path = "crewai_flow.html"
#         st.session_state.flow.plot(diagram_path)
        
#         # Display HTML in Streamlit
#         with open(diagram_path, "r", encoding="utf-8") as f:
#             html_content = f.read()
#         st.components.v1.html(html_content, height=600, scrolling=True)
        
#         st.success("✅ CrewAI Flow Diagram Displayed!")

# st.info("Press 'Run Flow' to start execution and 'Plot Flow' to see the graph.")
# streamlit run src/patternswithcrewai/Agents.py