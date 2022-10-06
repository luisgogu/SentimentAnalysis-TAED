Create a virtual environment using conda for easier management of dependencies and packages. For installing conda, follow the instructions on the official conda website

`conda create --name codecarbon`

`conda activate codecarbon`

Installing Code Carbon: 

`pip install codecarbon`

### Command lines to insert in the code:

`from codecarbon import EmissionsTracker`

`{YOUR MODEL CODE}`

`tracker = EmissionsTracker()`


### Start the emissions tracker
`tracker.start()`

### Run yout model (GPU Intensive code goes here)
`model.fit(x_train, y_train, epochs=10)`

# End the emissions tracker
`emissions: float = tracker.stop()`

# Print your results regarding carbon emissions
`print(emissions)`

Installing Comet package:

`pip install comet_ml`

Note: the code carbon recommends to use the command: pip install comet_ml>=3.2.2
But specifying the version has led us to errors which blocked the execution of the code (version 3.2.2 not found)

Our Comet's API Key is: vW6un6ZBv0bp33xa8SpXzkfYs

The command lines that we have to insert into the code are:

`import tensorflow as tf`

`experiment = Experiment(api_key="YOUR API KEY")`

`{Here come your Data and your Model}`

`{Run your Model}`

`experiment.end()`
