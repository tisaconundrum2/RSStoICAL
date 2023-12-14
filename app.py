from flask import Flask, Response, render_template
import feedparser
from icalendar import Calendar, Event
from datetime import datetime
import urllib.parse

app = Flask(__name__)

@app.route('/<path:rss_url>')
def convert_rss_to_ical(rss_url):
    try:
        # Decode the URL
        rss_url = urllib.parse.unquote(rss_url)

        # Parse the RSS feed
        feed = feedparser.parse(rss_url)

        # Create an iCalendar (ICS) object
        ical = Calendar()

        # Iterate through the RSS feed items and convert them to ICS events
        for item in feed.entries:
            event = Event()
            event.add('summary', item.title)
            event.add('description', item.description)

            # Convert the RSS date format to a datetime object
            rss_date = datetime.strptime(item.published, '%a, %d %b %Y %H:%M:%S %Z')

            # Set the start and end time for the event (assuming it's a single-day event)
            event.add('dtstart', rss_date)
            event.add('dtend', rss_date)

            # Add the event to the ICS calendar
            ical.add_component(event)

        # Generate the ICS data as a string
        ical_data = ical.to_ical()

        # Create a Flask response with the ICS data
        response = Response(ical_data, content_type='text/calendar')
        return response

    except Exception as e:
        return str(e), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
