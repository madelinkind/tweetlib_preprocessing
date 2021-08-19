from tweetlib.definitions import TypeTask
from tweetlib.classification.classification import Classification


dict_task = {
    TypeTask.VALIDATE_MODEL: Classification.validation_method,
    TypeTask.PREDICTION: Classification.predict_method,
    TypeTask.MODEL_STORAGE: Classification.model_storage
}