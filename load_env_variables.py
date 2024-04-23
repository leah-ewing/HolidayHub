from dotenv import load_dotenv
import os

production_secrets = ".env.production"

load_dotenv(production_secrets)

print(os.environ['DEVELOPER']) 