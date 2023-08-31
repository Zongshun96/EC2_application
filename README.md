# Overview
This repo has the dummy example application for paper LIBRA([DOI](https://doi.ieeecomputersociety.org/10.1109/IC2E52221.2021.00028), [Code](https://github.com/Zongshun96/LIBRA)).

# Application Detail
Load and rotate a local image, disregarding the input.

### in `simple_python_MT_server/`
The EC2 implementation with a python server is in `simple_python_MT_server/`. 
Please see [launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html) for making a VM image for AWS autoscaling. Especially, we can add a bash script in `user data` section of a template ([tutotial](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#advanced-settings-for-your-launch-template)) to launch the python server when a new instance is started.
For example, with amazon linux, in `simple_python_MT_server/server_launch.sh`
```
#!/bin/bash
python3 '/home/ec2-user/EC2_application/simple_python_MT_server/server.py'
```

### in `lambda_ImgLoad1Sec/`
The Lambda version is in `lambda_ImgLoad1Sec/`. [Here](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html) is a tutorial to deploy.