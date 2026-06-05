import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CultivationPlot:
    """Data object encapsulating crop priorities and telemetry records."""
    def __init__(self, plot_id, strain_name, baseline_urgency):
        self.id = plot_id
        self.crop = strain_name
        self.base_priority = baseline_urgency  # Lower values dictate primary allocation targets
        logging.debug(f"Registered crop profile: Plot {self.id} with {self.crop}.")

    def evaluate_transpiration_loss(self, temperature_value, humidity_value) -> float:
        """Applies empirical loss factors to scale priorities dynamically."""
        try:
            # High temperatures or dry air increase water loss
            environmental_loss = (temperature_value * 0.12) - (humidity_value * 0.04)
            return float(environmental_loss)
        except ZeroDivisionError:
            logging.error("Exception handled: invalid environmental inputs calculated.")
            return 1.0
