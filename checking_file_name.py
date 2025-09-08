import os

unprocessed_files = ['/Users/Supreeth/cisco-codes/gen-ai-ingestion-pipeline/data/input/dataset/course_files\\course_00aa1c79-97bb-48e4-89b9-09f4d4ae1bc0.json',
                     '/Users/Supreeth/cisco-codes/gen-ai-ingestion-pipeline/data/input/dataset/course_files\\tc-ai-langchain-pyats.json',
                     '/Users/Supreeth/cisco-codes/gen-ai-ingestion-pipeline/data/input/dataset/course_files\\tc-appd-apis.json',
                     '/Users/Supreeth/cisco-codes/gen-ai-ingestion-pipeline/data/input/dataset/course_files\\tc-ccna-intro-acl.json',
                     '/Users/Supreeth/cisco-codes/gen-ai-ingestion-pipeline/data/input/dataset/course_files\\tc-python-imports.json']

unprocessed_files = [
                f for f in unprocessed_files if not os.path.basename(f).startswith("tc")
            ]
print(unprocessed_files)