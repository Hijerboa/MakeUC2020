# MakeUC2020

Uses COVID-19 business guidelines provided by the [Ohio Department of Health](coronavirus.ohio.gov) to allow users to provide reports how well businesses are following current COVID-19 regulations through a
web interface, as well as view reports on businesses in the user's area. 

## Guidelines
### Employees:
- Ensure minimum of six feet between employees, if not possible, utilize barriers.
- Businesses must require all employees to wear facial coverings.
- Limit number of employees allowed in break rooms
at the same time and practice social distancing.
Maximum to be current group size per state guidelines
(currently 10).
### Customers:
- Ensure a minimum of six feet between parties waiting and when dining.
- Customers and guests must wear face coverings at all times, except when dining.
- Post a list of COVID-19 symptoms in a conspicuous place.
### Physical Space:
- Establish and post maximum dining area capacity using
updated COVID-19 compliant floor plans.With
maximum party size per state guidelines (currently 10.)
- When appropriate, establish ordering areas and waiting
areas with clearly marked safe distancing and
separations per individual/social group for both
restaurant and bar service.
- Remove self-service, table, and common area items
(e.g. table tents, vases, lemons, straws, stir sticks,
condiments.)
- Private dining and bar seating areas within a
foodservice establishment must follow all approved safe
social distancing guidelines.

## Flags
These guidelines are considered in one of three possibilities: The guideline is being followed explicitly, the guideline is not being followed
explicitly, or it is unclear whether the guideline is being followed. Internally this is handled as a flag stored in the "reports" database for each report.

| Guideline | Type | Flag |
| --------- | ---- | ---- |
| Minimum of six feet between employees or utilize barriers. | Negative | flag1 |
| Require all employees to wear facial coverings. | Negative | flag2 |
| Limit number of employees allowed in break rooms. | Negative | flag3 |
| Minimum of six feet between parties waiting and when dining. | Negative | flag4 |
| Customers and guests must wear face coverings at all times, except when dining. | Negative | flag5 |
| list of COVID-19 symptoms in a conspicuous place. | Negative | flag6 |
| Establish and post maximum dining area capacity | Negative | flag7 |
| establish ordering areas and waiting areas with clearly marked safe distancing | Negative | flag8 |
| Remove self-service, table, and common area items | Negative | flag9 |
| Private dining and bar seating areas follow all approved safe social distancing guidelines. | Negative | flag10 |
| Minimum of six feet between employees or utilize barriers. | Positive | flag11 |
| Require all employees to wear facial coverings. | Positive | flag12 |
| Limit number of employees allowed in break rooms. | Positive | flag13 |
| Minimum of six feet between parties waiting and when dining. | Positive | flag14 |
| Customers and guests must wear face coverings at all times, except when dining. | Positive | flag15 |
| list of COVID-19 symptoms in a conspicuous place. | Positive | flag16 |
| Establish and post maximum dining area capacity | Positive | flag17 |
| establish ordering areas and waiting areas with clearly marked safe distancing | Positive | flag18 |
| Remove self-service, table, and common area items | Positive | flag19 |
| Private dining and bar seating areas follow all approved safe social distancing guidelines. | Positive | flag20 |


