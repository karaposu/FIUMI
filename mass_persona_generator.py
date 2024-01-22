
import pandas as pd 
from persona_genarator import 
df = pd.DataFrame(columns=list(features.keys()) + ['Description'])

# Generating and saving a set number of personas
num_personas = 10  # Set the number of personas you want to generate
for _ in range(num_personas):
    random_persona = create_feature_set()
    description = generate_persona_description(random_persona)
    random_persona['Description'] = description
    df = df.append(random_persona, ignore_index=True)

print(df)
