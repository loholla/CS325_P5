from openai import OpenAI
import os

def summary(num):
  client = OpenAI()

  summaryDir = "Data/ai_summary" #data path
  articleName = "article_" + str(num) + ".txt" #article name
  articleNameFull = "article_" + str(num) + "_full.txt"
  dataPath = os.path.join(summaryDir, articleName) #the full path
  procDir = "Data/processed"
  readPath = os.path.join(procDir, articleNameFull)
  articleRead = open(readPath, "r", encoding="utf-8")
  prompt = articleRead.read()

  text1 = "Create a summary of the following article that is greater than 50 words and less than 60 words" + prompt # Generates the prompt
  article = client.chat.completions.create( # This block is what sends the prompt to the AI
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are an assistant who is skilled at summarizing articles to a word count of 50 words to 60 words."},
      {"role": "user", "content": text1}
    ]
  )
  text2 = "Can you please generate a title for this article: " + prompt # Generates the prompt
  title = client.chat.completions.create( # This block is what sends the prompt to the AI
    model = "gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
      {"role": "user", "content": text2}
    ]
  )

  # The following code writes the responses into the file
  file = open(dataPath, "w", encoding="utf-8")
  file.write(str(title.choices[0].message.content))
  file.write("\n")
  file.write(str(article.choices[0].message.content))
  file.close()