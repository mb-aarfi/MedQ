# MedQ - Revolutionizing Healthcare with Real-Time Data

## Idea & Approach

**MedQ** is a hospital-based app designed to bring healthcare services directly to users’ fingertips. Despite the presence of OPD registration platforms, they often lack real-time data integration, providing limited insights into bed availability and using inefficient queuing models.

The MedQ app addresses these challenges by:
- Implementing a priority-based queue system, prioritizing patients based on the severity of their conditions.
- Providing real-time availability of OPD beds and timely updates, allowing users to choose hospitals based on bed count, distance, cost, and more.
- Gathering real-time data from hospitals and updating it in the database, making this information easily accessible to users.

### Key Features:
1. **Priority-Based Queuing System** - Prioritizes patients based on their medical condition's urgency.
2. **Real-Time Bed Availability** - Allows users to see current bed counts and book accordingly.
3. **User-Centric Filters** - Search by bed count, distance, hospital cost, and more.

## Architecture Diagram
![Architecture diagram](https://github.com/user-attachments/assets/37999e4a-13f5-4104-aa12-757ee540cc85)

## Dependencies
- **Flutter Framework**: Cross-platform front-end development.
- **MERN Stack**: Backend development for hospitals' real-time data.
- **Firebase**: Storage for real-time data.

## Tech Stack
**Frontend:**
- HTML5, CSS, React JS

**Backend:**
- JavaScript, Node JS, Flask, Python, Flutter

**Database:**
- Firebase, Firestore

**Authentication:**
- Firebase

**UI Design:**
- Figma, Visily, Whimsical, Lucid

**APIs:**
- Google Maps API, TomTom API

## Feasibility Analysis

We conducted a survey across hospitals and gained insights from staff, revealing these crucial statistics:

- **94%** of respondents prefer an app that provides faster OPD registration, reducing inline waiting time.
- **76%** believe in a priority-based registration system.
- **82%** support real-time bed and doctor availability information.

### Survey Questions:
1. Will you use an app that minimizes waiting time for OPD registration?
2. Should OPD slots be registered based on patient priority or FCFS (First-Come-First-Serve)?
3. Would real-time information on beds and doctors improve your hospital experience?
4. Have you seen an app providing real-time bed/doctor availability and patient priority slot booking?

## Challenges and Solutions

**Challenge**: Understanding the real problems faced by hospitals  
**Solution**: Hospital visits provided key insights into actual pain points.

**Challenge**: Designing a Queuing Model  
**Solution**: Integrating priorities with FCFS created an optimal dynamic queuing system.

**Challenge**: ML Model Integration  
**Solution**: Flask provided an effective way to overcome integration issues.

## Viability Analysis

### Target Market Size:
- **Population**: Our app targets 33 million people in Delhi.
- **Patient Segment**: 50,000 daily OPD registrations in government hospitals.
- **Hospital Segment**: Targeting 180 hospitals (148 private, 32 government).

### Revenue Model:
1. Subscription fees from hospitals.
2. Advertisements.
3. **MedCoin**: A reward system providing additional benefits like discounted services.

## Top Selling Points:
1. **Reduction in Pre-Admit Struggle**: Seamless bed and doctor availability.
2. **Asset to Life-Saving**: Speedy admission through real-time updates.
3. **By 2030**, we aim to reduce patient waiting times by 30%.

## Research and References

- **"The Role of Real-Time Data in Healthcare"**  
Journal: Healthcare Informatics Research  
[Link](https://link.springer.com/journal/41666)

- **"Queueing Models for Healthcare Operations"**  
International Series in Operations Research & Management Science, Volume 184  
[Link](https://link.springer.com/chapter/10.1007/978-1-4614-5885-2_2)

- **"Predictive Analytics in Hospital Management"**  
Author: Gopalakrishna Palem  
[Link](https://www.researchgate.net/publication/236336250_The_Practice_of_Predictive_Analytics_in_Healthcare)

- **"Impact of Bed Availability on Patient Care"**  
Source: National Library of Medicine  
[Link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1089232/)
