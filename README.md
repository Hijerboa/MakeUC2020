# MakeUC2020

Uses COVID-19 business guidelines provided by the [Ohio Department of Health](https://coronavirus.ohio.gov) to allow users to provide reports how well businesses are following current COVID-19 regulations through a
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
| Minimum of six feet between employees or utilize barriers. | Negative | 0x80000000 |
| Require all employees to wear facial coverings. | Negative | 0x40000000 |
| Limit number of employees allowed in break rooms. | Negative | 0x20000000 |
| Minimum of six feet between parties waiting and when dining. | Negative | 0x10000000 |
| Customers and guests must wear face coverings at all times, except when dining. | Negative | 0x8000000 |
| list of COVID-19 symptoms in a conspicuous place. | Negative | 0x4000000 |
| Establish and post maximum dining area capacity | Negative | 0x2000000 |
| establish ordering areas and waiting areas with clearly marked safe distancing | Negative | 0x1000000 |
| Remove self-service, table, and common area items | Negative | 0x800000 |
| Private dining and bar seating areas follow all approved safe social distancing guidelines. | Negative | 0x400000 |
| Minimum of six feet between employees or utilize barriers. | Positive | 0x8000 |
| Require all employees to wear facial coverings. | Positive | 0x4000 |
| Limit number of employees allowed in break rooms. | Positive | 0x2000 |
| Minimum of six feet between parties waiting and when dining. | Positive | 0x1000 |
| Customers and guests must wear face coverings at all times, except when dining. | Positive | 0x800 |
| list of COVID-19 symptoms in a conspicuous place. | Positive | 0x400 |
| Establish and post maximum dining area capacity | Positive | 0x200 |
| establish ordering areas and waiting areas with clearly marked safe distancing | Positive | 0x100 |
| Remove self-service, table, and common area items | Positive | 0x80 |
| Private dining and bar seating areas follow all approved safe social distancing guidelines. | Positive | 0x40 |

Neutral reports are indicated by the lack of a flag in a guideline (positive or negative).