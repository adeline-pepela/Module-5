#from services.ts_pipeline import AdvancedTimeSeriesForecaster
from app.services.ts_pipeline import AdvancedTimeSeriesForecaster


#create an instance of the time series forecaster

forecaster = AdvancedTimeSeriesForecaster()
data = forecaster.get_data('AAPL', '5y')

print(data.head())