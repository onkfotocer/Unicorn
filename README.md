# Unicorn

Modern computing platforms are highly-configurable with thousands of interacting configuration options. However, configuring these systems is challenging and misconfigurations can cause unexpected non-functional faults. This paper proposes CAUPER(short for CausalPerformance Debugging) that enables users to identify, explain, and fixthe root cause of non-functional faults earlyand in a principled fashion.CAUPER builds a causal model byobserving the performance of the system under different configurations. Then, it uses casual path extraction followed by counterfactual reasoning over the causal model to (a) identify the root causes of non-functional faults, (b) estimate the effects of various configuration options on the performance objective(s), and (c) prescribe candidate repairs to the relevant configuration options to fix the non-functional fault. We evaluated CAUPER on 5 highly-configurable systems by comparing with state-of-the-art configuration optimization and ML-based debugging approaches. The experimental results indicate that CAUPER can find effective repairs for faults in multiple non-functional properties with (atmost) 13% more accuracy, 32% higher gain, and 13×speed-up than other ML-based performance debugging methods. Compared to multi-objective optimization approaches, CAUPER can find fixes (atmost) 8× faster with comparable or better performance gain. Our study of non-functional faults reported in NVIDIA’s forum shows that CAUPER can find 14% better repairs than the experts’ advice in less than 30 minutes.

## Dependencies
* pandas    
* flask 
* Keras 
* PyTorch 
* Tensorflow
* numpy  
* json  
* causalgraphicalmodels 
* causalnex 
* graphviz 
* py-causal 
* causality  
* python 3.6
## Run instructions using Jetson faults dataset
To run experiments on NVIDIA Jetson TX1 or TX2 or Jetson Xavier devices please use the 
following command to launch a flask on localhost:
```python
command: python run_service.py softwaresystem
```
For example to initialize a flask app with image recogntion software system please use:
```python
command: python run_service.py Image
```

Once the flask app is running and modelserver is ready then please use the following command
to collect performance measurments for different configurations: 
```python
command: python run_params.py softwaresystem
```

To run causal models for a single-objective bug please run the following:
```python
command: python cauper.py  -o objective1  -s softwaresystem -k hardwaresystem
```
For example, to build causal models using fci with entropy for image recognition software 
system in TX1 with initial datafile irtx1.csv use the following for a latency (single objective) bug : 
```python
command: python cauper.py  -o inference_time  -s Image -k TX1
```

To run causal models for a multi-objective bug please run the following:
```python
command: python cauper.py  -o objective1 -o objective2 -s softwaresystem -k hardwaresystem
```
For example, to build causal models using fci with entropy for image recognition software 
system in TX1 with initial datafile irtx1.csv use the following for a latency and energy consumption (multi-ojective) bug : 
```python
command: python cauper.py  -o inference_time -o total_energy_consumption -s Image -k TX1
```
## Run instructions using a different dataset
If you want to run CAUPER on your own dataset you will only need cauper.py and src/causal_model.py.
To perform interventions using the recommended configuration by cauper.py you need to develop 
your own utilities (similar to run_params.py etc.). In addition to that, you need to
make some changes in the etc/config.yml file based on your need. The necessary steps are 
the following:

### Step 1:
Update init_dir variable in the config.yml file with the location of the initial data.

### Step 2:
Update bug_dir variable in the config.yml file with the location of the bug data.

### Step 3:
Update output_dir variable in the config.yml file where you want to save the output data.

### Step 4:
Update hardware_columns in the config.yml with the hardware configuration options you want to use.

### Step 5:
Update kernel_columns in the config.yml with the kernel configuration options you want to use.

### Step 6:
Update perf_columns in the config.yml with the events you want to track using perf use. If you use any other monitoring tool you need to update it accordingly.

### Step 7:
Update measurment_colums in the config.yml based on the performance objectives you want to use for bug resolve.

### Step 8:
Update is_intervenable variables in the config.yml with the configuration options you want to use and based on your application change their values to True or False. True indicates the configuration options can be intervened upon and vice-versa for False.

### Step 9: 
Update the option_values variables in the config.yml based on the allowable values your option can take. 

At this stage you can run cauper.py with your own specification. Please notice that you also need to update the directories according to your software and hardware name in data directory. 
If you change the name of the variables in the config file or use a new config fille you need to make changes accorsingly from line 49 - 58 in cauper.py.
If you use your own intervention uitility you need to update line 6 and line 126 of cauper.py.




## 📘&nbsp; License
CAUPER is released under the under terms of the [MIT License](LICENSE).
