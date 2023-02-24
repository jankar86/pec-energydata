# pec-energydata
Simple docker container that utilizes python and selenium to export energy usage data from PEC 

Add how to use this thing once its done....


## Pull repo build/run locally:

# Pre-Reqs:
- Docker installed on system you are testing with
 
```

git clone git@github.com:jankar86/pec-energydata.git
cd pec-energydata
docker run -it -w /app/src -v $(pwd):/app/src jankar86/pec-energydata:latest bash

```
