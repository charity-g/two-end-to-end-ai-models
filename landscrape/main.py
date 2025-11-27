from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent, AgentExecutor

# definte class to hold output schema
class TopicResponse(BaseModel):
    topic: str
    summary: str
    key_people_names: list[str]
    key_companies_organizations: list[str]
    sources: list[str]
    tools_used: list[str]

class PersonSchema(BaseModel):
    name: str
    relevance: str
    roles: list[str]
    worked_with: list[str]
    organizations_affiliations: list[str]
    contact_information: dict[str, str]
    sources: list[str]
    tools_used: list[str]

class OrgSchema(BaseModel):
    name: str
    industry: str
    competitive_position: str
    headquarters_location: str
    key_people_names: list[str]
    contact_information: dict[str, str]
    products: list[str]
    sources: list[str]
    tools_used: list[str]

class ProductSchema(BaseModel):
    name: str
    description: str
    company: str
    key_features: list[str]
    market_position: str #too vague
    user_pain_points: list[str]
    missing_features: list[str]
    target_audience: str
    sources: list[str]
    tools_used: list[str]

load_dotenv()

system_prompt = """
      You are an expert industry and business intelligence researcher to help with competitive analysis and product-market fit research for startups.
      Answer the user query and use necessary tools.
      Wrap the output in the following schema and provide no other text:\n{format_instructions}"""

# You will gathers detailed information on an entreprenueral software,
#   technology and artificial intelligence products.
llm  = OpenAI(model="gpt-4")
parser = PydanticOutputParser(pydantic_object=TopicResponse)
template = ChatPromptTemplate.from_template(
    [("system", 
      system_prompt),
      ("placeholder", "{chat_history}"),
      ("human",
       """
       Given a description of a prototype product, research competitors and product-market fit.
       {industry} 
       {description}
       {target_audience}
       {features}
       {pain_points}
       {pricing_model}
       """),
      ("placeholder", "{agent_scratchpad}")
    ]
)

prompt = template.invoke({
    "industry": "Companion + Wellness",
    "description": "AI-chatbot for mental health support",
    "target_audience": "Young adults aged 18-30",
    "features": "24/7 availability, personalized conversations, mood tracking",
    "pain_points": "Stigma around seeking help, lack of affordable options",
    "pricing_model": "Freemium with premium features"  
})

agent = create_agent(
    model=llm,
    system_prompt=system_prompt,
    tools=[]
    )

agent.invoke(prompt)
