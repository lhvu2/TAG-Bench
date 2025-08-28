# source: https://docs.litellm.ai/docs/providers/watsonx

import os
from litellm import completion

url = os.environ["WATSONX_URL"]
key = os.environ["WATSONX_APIKEY"]
proj = os.environ["WATSONX_PROJECT_ID"]

## Call WATSONX `/text/chat` endpoint - supports function calling
response = completion(
  model="watsonx/meta-llama/llama-3-2-3b-instruct",
  messages=[{ "content": "what is your favorite colour?","role": "user"}],
  project_id=proj # or pass with os.environ["WATSONX_PROJECT_ID"]
)

## Call WATSONX `/text/generation` endpoint - not all models support /chat route. 
response = completion(
  model="watsonx/ibm/granite-3-3-8b-instruct",
  messages=[{ "content": "what is your favorite colour?","role": "user"}],
  project_id=proj
)

pass
