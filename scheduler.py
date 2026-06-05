import heapq
import logging

class PriorityHeapOrchestrator:
    """Implements a Min-Heap queue to extract high-urgency fields in O(log n) time."""
    def __init__(self):
        self.priority_heap = []
        logging.info("PriorityHeapOrchestrator structure instanced.")

    def inject_plot_into_queue(self, dynamic_urgency_score, plot_object):
        """Pushes data elements onto the structural min-heap vector tuple."""
        heapq.heappush(self.priority_heap, (dynamic_urgency_score, plot_object.id, plot_object.crop))
        logging.debug(f"Plot {plot_object.id} queued at current urgency: {dynamic_urgency_score:.2f}")

    def extract_optimal_target(self):
        """Pulls the highest-urgency plot out of the heap."""
        if self.priority_heap:
            return heapq.heappop(self.priority_heap)
        return None
