from .manager import Manager


class EventManager(Manager):
    """
    An event bus that publishes events to subscribers.
    """

    def _init(self):
        """
        Initialize a dictionary that maps events to their handlers.
        """
        self.subscribers = {}

    def subscribe(self, event_types, handler):
        """
        Subscribe to a set of event types. Event types should be a set of pygame events.
        """
        for event_type in event_types:
            if event_type not in self.subscribers:
                self.subscribers[event_type] = []
            self.subscribers[event_type].append(handler)

    def unsubscribe(self, event_types, handler):
        """
        Unsubscribe from an event type. Event types should be a set of pygame events.
        """
        for event_type in event_types:
            if event_type in self.subscribers:
                self.subscribers[event_type].remove(handler)
                if not self.subscribers[event_type]:
                    del self.subscribers[event_type]

    def publish(self, event):
        """
        Publish events to their subscribers if they are active.
        """
        for handler in self.subscribers.get(event.type, []):
            handler(event)
