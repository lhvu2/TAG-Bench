from lotus.models import LM
import lotus

lm = lotus.models.LM(model="gpt-4o")
# lm = LM(model="together/deepseek-ai/DeepSeek-R1", api_key=api_key)
lotus.settings.configure(lm=lm)
pass
