from google.cloud import aiplatform

def initialize_google_ai(project_id, location):
    aiplatform.init(project=project_id, location=location)

def predict_with_model(model_name, instances):
    endpoint = aiplatform.Endpoint(endpoint_name=model_name)
    response = endpoint.predict(instances=instances)
    return response
