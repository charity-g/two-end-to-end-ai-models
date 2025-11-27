from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import OpenAI
from langchain_community.wikipedia import WikipediaAPIWrapper
from langchain.core.prompts import ChatPromptTemplate
from langchain.core.output_parsers import PydanticOutputParser

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

llm  = OpenAI(model="gpt-4")
response = llm.predict("What is the capital of France?")
print(response)

