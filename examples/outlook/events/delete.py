"""

"""

from office365.graph_client import GraphClient
from office365.outlook.calendar.events.event import Event
from tests.graph_case import acquire_token_by_username_password

client = GraphClient(acquire_token_by_username_password)
event_id = '--event id goes here--'
event_to_del = client.me.calendar.events[event_id]  # type: Event
event_to_del.delete_object().execute_query()
