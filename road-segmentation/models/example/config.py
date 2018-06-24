from core.abstract_config import AbstractConfig

class Config(AbstractConfig):

    def __init__(self, model_name: str):
        super().__init__(model_name)


    # Overwrite any Configurations from Abstract Config
    N_EPOCHS = 8
    N_BATCHES_PER_EPOCH = 2
    SUMMARY_IMAGE_EVERY_STEP = 4

    # Define new Configurations for your Model
