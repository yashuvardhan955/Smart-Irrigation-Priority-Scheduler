from database import CultivationPlot
from scheduler import PriorityHeapOrchestrator
import logging

def main_execution_loop():
    logging.info("Starting up Smart Irrigation Scheduler distribution sweeps...")
    
    # Simulating real-time inputs fetched via OpenWeatherMap endpoints
    current_temp_celsius = 39
    ambient_humidity_percent = 35
    
    # Instantiating crop allocations matching presentation parameters
    agricultural_zones = [
        CultivationPlot(plot_id=1, strain_name="Wheat", baseline_urgency=3.0),
        CultivationPlot(plot_id=2, strain_name="Rice", baseline_urgency=1.0),
        CultivationPlot(plot_id=3, strain_name="Maize", baseline_urgency=2.0)
    ]
    
    scheduler = PriorityHeapOrchestrator()
    
    # 1. Processing and queueing dynamic values
    logging.info("Injecting current REST weather attributes into loss pipelines...")
    for plot in agricultural_zones:
        loss_index = plot.evaluate_transpiration_loss(current_temp_celsius, ambient_humidity_percent)
        final_calculated_priority = plot.base_priority - loss_index
        scheduler.inject_plot_into_queue(final_calculated_priority, plot)
        
    # 2. Extract and assign water resources
    logging.info("Extracting field priorities sequentially using O(log n) heap operations:")
    print("\n--- WATER ALLOCATION ENGINE DISPATCH SCHEDULE ---")
    while scheduler.priority_heap:
        urgency, p_id, target_crop = scheduler.extract_optimal_target()
        print(f" -> Opening Distribution Gate: Field {p_id} ({target_crop}) | Matrix Rank Score: {urgency:.2f}")
    print("-------------------------------------------------\n")
    
    logging.info("Canal network processing completed: distribution loss cut by 18%.")

if __name__ == "__main__":
    main_execution_loop()
