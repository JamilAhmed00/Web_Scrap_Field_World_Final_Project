from fastapi import FastAPI
from scraper import scrape_news
import requests
from bs4 import BeautifulSoup
from database import get_database_connection
import openai

  # Set your OpenAI API key here

app = FastAPI()

def generate_summary_with_gpt(news_details):
    
    prompt = f"Summarize the following news article into a short summary:\n\n{news_details}"

    response = openai.Completion.create(
        model="gpt-4o-3",  
        prompt=prompt,
        max_tokens=100000,  
        temperature=0.5
    )

    summary = response.choices[0].text.strip()
    return summary


@app.get("/news")
def get_news():
    news = scrape_news()
    return news

@app.get("/details")
def get_details_and_save(link: str):
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

      
        article_tag = soup.find('article', id='main-single-post')

        if article_tag:
           
            paragraphs = article_tag.find_all('p')
            full_content = " ".join(p.get_text(strip=True) for p in paragraphs)

           
            summary = generate_summary_with_gpt(full_content)

            
            heading_tag = soup.find('h1') or soup.find('h3')
            heading = heading_tag.get_text(strip=True) if heading_tag else "No Heading Found"

            conn = get_database_connection()
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO news (news_heading, news_details, details_summary) VALUES (%s, %s, %s)",
                    (heading, full_content, summary)
                )
                conn.commit()
                return {
                    "message": "Details and summary saved to the database successfully!",
                    "link": link,
                    "news_heading": heading,
                    "news_details": full_content,
                    "details_summary": summary
                }
            except Exception as e:
                conn.rollback()
                return {"message": f"Failed to save details and summary to the database. Error: {str(e)}"}
            finally:
                cursor.close()
                conn.close()
        else:
            return {"message": "Article content not found.", "link": link}
    else:
        return {"message": f"Failed to fetch the page. Status code: {response.status_code}", "link": link}




