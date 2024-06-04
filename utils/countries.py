import plotly as px
from typing import Dict, Set

regions =  {
    "South America" : ['Colombia', 'Venezuela', 'Suriname', 'French Guiana', 'Guyana', 'Ecuador', 'Peru', 'Bolivia', 'Chile', 'Paraguay', 'Brazil', 'Uruguay', 'Argentina'],
    
    "Asia" : [
        'Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia',
        'China', 'Cyprus', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan',
        'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar',
        'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Russia', 'Saudi Arabia',
        'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor',
        'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen', 'Macao', 'Christmas Island', 'Hong Kong'],
    
    "Europe" : [
        'Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia',
        'Cyprus', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary',
        'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta',
        'Moldova', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal',
        'Romania', 'Russia', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland',
        'Ukraine', 'United Kingdom', 'Faeroe Islands', 'Greenland', 'Sint Maarten (Dutch part)', 'Martinique', 'Bermuda', 'Aruba'
    ],
    
    "Africa" : [
        'Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cape Verde', 'Cameroon',
        'Central African Republic', 'Chad', 'Comoros', 'Democratic Republic of Congo', 'Congo',
        'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana',
        'Guinea', 'Guinea-Bissau', "Cote d'Ivoire", 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi',
        'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda',
        'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan',
        'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe', 'Mayotte', 'Saint Helena', 'Reunion'
    ],
    
    "North America" : [
        'Antigua and Barbuda', 'Bahamas', 'Barbados', 'Belize', 'Canada', 'Costa Rica', 'Cuba', 'Dominica',
        'Dominican Republic', 'El Salvador', 'Grenada', 'Guatemala', 'Haiti', 'Honduras', 'Jamaica', 'Mexico',
        'Nicaragua', 'Panama', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines',
        'Trinidad and Tobago', 'United States', 'Montserrat', 'Anguilla', 'Bermuda', 'Aruba', 'Turks and Caicos Islands', 'Guadeloupe', 'Saint Pierre and Miquelon', 'Puerto Rico', 'Curacao'
    ],
    
    "Oceania" : [
        'Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia', 'Nauru', 'New Zealand', 'Palau', 'Papua New Guinea',
        'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu', 'New Caledonia', 'Wallis and Futuna', 'French Polynesia', 'Niue', 'Cook Islands'
    ]
}

def find_countries_by_region(countries: Set[str], region_dict: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
  """
  Finds countries belonging to each region in the provided dictionary.

  Args:
      countries: A set of country names.
      region_dict: A dictionary mapping region names to sets of countries in that region.

  Returns:
      A dictionary where keys are region names and values are sets of countries belonging to that region.
  """

  # Initialize a dictionary to store results
  countries_by_region = {region: set() for region in region_dict.keys()}

  # Find intersection of countries and each region's countries
  for country in countries:
    for region, region_countries in region_dict.items():
      if country in region_countries:
        countries_by_region[region].add(country)

  # Return the dictionary with countries grouped by region
  return countries_by_region