import os
import sys
import django
import feedparser
from datetime import datetime
import pytz

# 현재 스크립트 파일의 절대 경로 (예: /path/to/kc-news-back-service/news/crawlers/news.py)
script_path = os.path.abspath(__file__)
# 현재 스크립트가 위치한 디렉토리 (예: /path/to/kc-news-back-service/news/crawlers/)
current_dir = os.path.dirname(script_path)
# 앱 루트 디렉토리 (예: /path/to/kc-news-back-service/news/)
# news/crawlers/ 에서 news/ 로 이동
app_root = os.path.dirname(current_dir)
# 프로젝트 루트 디렉토리 (예: /path/to/kc-news-back-service/)
# news/ 에서 kc-news-back-service/ 로 이동
project_root = os.path.dirname(app_root)
# Python 모듈 검색 경로의 맨 앞에 프로젝트 루트 디렉토리를 추가합니다.
sys.path.insert(0, project_root)

# Django 설정 파일 경로 지정
# 'project'는 settings.py를 포함하는 내부 폴더 이름입니다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# Django 환경 초기화
django.setup()
# --- Django 환경 설정 끝 ---

def news_parser() :

    from news.models import NewsChannel, NewsItem

    url="https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"
    
    import feedparser
    feed = feedparser.parse(url)

    channel_info = feed['feed']
    items = feed['entries']

    channel_data = {
        "generator": channel_info.get("generator"),
        "title": channel_info.get("title"),
        "link": channel_info.get("link"),
        "language": channel_info.get("language"),
        "publisher": channel_info.get("publisher")
    }
    print("CHANNEL DATA:", channel_data)

    channel, created = NewsChannel.objects.update_or_create(
        link=channel_data['link'],
        defaults=channel_data
    )

    if created :
        print(f"채널 생성: {channel.title}")
    else :
        print(f"채널 업데이트: {channel.title}")

    for item in items :

        item_data = {
            "title": item.get("title"),
            "link": item.get("link"),
            "guid": item.get("id"),
            "description": item.get("summary"),
            "source_title": item.get("source", {}).get("title"),
            "source_url": item.get("source", {}).get("href")
        }
        print("ITEM DATA:", item_data)

        NewsItem.objects.update_or_create(
            channel=channel,
            guid=item_data['guid'],
            defaults=item_data
        )

if __name__ == "__main__" :
    news_parser()