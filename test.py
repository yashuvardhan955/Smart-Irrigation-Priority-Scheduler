from scheduler import PriorityHeapOrchestrator
from database import CultivationPlot

def test_heap_sequence_integrity():
    print("[TESTING RUNTIME] Launching data-structure validation checks...")
    
    orchestrator = PriorityHeapOrchestrator()
    dummy_plot_high = CultivationPlot(10, "DryTest1", 5.0)
    dummy_plot_low = CultivationPlot(20, "DryTest2", 0.5)
    
    orchestrator.inject_plot_into_queue(5.0, dummy_plot_high)
    orchestrator.inject_plot_into_queue(0.5, dummy_plot_low)
    
    # Verify that the min-heap returns the lower priority score first
    top_element = orchestrator.extract_optimal_target()
    assert top_element[1] == 20, "The heap sorting layout violated the Min-Heap condition."
    print(" -> Validation Step 1: Min-heap constraint sorting working correctly.")
    print("[SUCCESS] Data structure validation routines completed perfectly.")

if __name__ == "__main__":
    test_heap_sequence_integrity()
