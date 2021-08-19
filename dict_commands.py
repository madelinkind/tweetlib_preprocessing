from tweetlib.definitions import TypeTask

dict_commands = {
    'create-model': TypeTask.MODEL_STORAGE,
    'update-model': TypeTask.MODEL_STORAGE,
    'find-author': TypeTask.PREDICTION,
    'validate-new-model': TypeTask.VALIDATE_MODEL,
    'validate-existing-model': TypeTask.VALIDATE_MODEL
}