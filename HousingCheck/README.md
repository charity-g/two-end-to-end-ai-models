# HOUSING CHECK PLAN

## Installing

- `conda env create -f environment.yaml`

## Deinstalling
- `conda remove --name housing --all`

## Setting the scenario up

0) [DONE] Getting data for your region 
    - doesn't matter what columns you have as long as target column ($ sell price of house) is present
1) Creating the model
2) Loading up the Flask app
    - I use this hosting service: `https://www.pythonanywhere.com/` 
3) Play with the app to run predictsion
4) Repeats step 1-4 as you add new data