import joblib
import pandas as pd


class LinearRegressionAlgo:
    def __init__(self):
        path_to_artifacts = "/home/gdpvirus/Desktop/projects/basic-ml-api/research/"
        self.values_fill_missing = joblib.load(
            path_to_artifacts + "train_mode.joblib")
        self.encoders = joblib.load(path_to_artifacts + "encoders.joblib")
        self.model = joblib.load(
            path_to_artifacts + 'linear_model_sk.joblib')

    def preprocessing(self, input_data):
        input_data = pd.DataFrame(input_data, index=[0])
        # fill missing values
        input_data.fillna(self.values_fill_missing)

        return input_data

    def predict(self, input_data):
        return self.model.predict(input_data)

    def postprocessing(self, input_data):
        return {"prediction": input_data, "status": "OK"}

    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)[0]
            prediction = self.postprocessing(prediction)

        except Exception as e:
            return {"status": "Error", "message": str(e)}

        return prediction
