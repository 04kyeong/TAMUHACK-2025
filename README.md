# TAMUHACK-2025

# Smart Trash Bin System 
 ![Image](https://github.com/user-attachments/assets/2bc04c55-8c29-4b50-a8d6-410ab4ad515c)
Demo photo of actual trash bin with ststem.
![Image](https://github.com/user-attachments/assets/36a91aff-9ff6-4c8a-9f9f-62b3c7cae2f7)
Website showing the 5 recent data in chart and graph.

# Demo Video and Presentation Slides 
Video: https://youtu.be/Ypi7wZAzr6w?si=U3QxXhpTmEYR5fR9
Slides: https://docs.google.com/presentation/d/1Q1CUxJG032nCj6oHM8BnSUK4z6yS-Vd81TZxGpLFf4g/edit?usp=sharing

## Inspiration
The idea stemmed from a common issue in public spaces: overflowing trash bins that create unsanitary environments and inefficiency in waste management. We wanted to create a solution that not only notifies janitors when bins are full but also provides valuable data to improve cleaning schedules and resource allocation.

## What it does
The Smart Trash Bin System detects when a trash bin is full and lights up an LED as a notification for janitors. It also tracks the time it takes for the bin to go from empty to full, providing usage data. This data can be analyzed to identify high-traffic areas and optimize waste collection schedules.

## How we built it
We used an ultrasonic distance sensor to measure the fill level of the bin and an Arduino Uno to process the data. An LED indicates when the bin is full, and the time tracking is done through the Arduino's internal clock. The collected data is stored and can be exported for analysis.

## Challenges we ran into
One challenge was calibrating the distance sensor to accurately detect different trash levels in varying conditions, such as changes in lighting or bin shape. Additionally, ensuring the system's power efficiency while running continuously required careful circuit design.

## Accomplishments that we're proud of
We successfully built a functional prototype that integrates sensor data and provides actionable insights. We're proud of the system's potential to reduce waste overflow and improve resource efficiency in public spaces.

## What we learned
We learned the importance of balancing functionality and simplicity when building hardware prototypes. Additionally, we gained valuable insights into sensor calibration, data collection, and designing systems for real-world use cases.

## What's next for Smart Trash Bin System
The next step is to integrate a wireless communication module, such as Wi-Fi or Bluetooth, to send real-time data to a centralized dashboard for remote monitoring. We also aim to expand the system's capabilities by adding features like predictive analytics to anticipate when bins will likely be full based on historical trends.

## Resources
https://howtomechatronics.com/tutorials/arduino/ultrasonic-sensor-hc-sr04/
Used HC-SR04 sensor distance calculation formula from this website. 

## Contact
For inquiries or collaboration, please contact Kyeongseo Choi and Seongjun Cho at kyeongstudy@tamu.edu
