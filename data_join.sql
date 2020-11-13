SELECT "Country","Population","Death","death/population","Health_Spending",
"Hospital_bed","Hospital_stay","Life_expectancy","Unemployment_rate",
"Obesity_rate",	"transporation","poverty_rate",	"science_score"
FROM country_name 
inner join covid_data
on country_name.index = covid_data.country_id
inner join health_spending
on country_name.index = health_spending.country_id
inner join hospital_bed
on country_name.index = hospital_bed.country_id
inner join hospital_stay
on country_name.index = hospital_stay.country_id
inner join life_expectancy
on country_name.index = life_expectancy.country_id
inner join unemployment
on country_name.index = unemployment.country_id
inner join obesity
on country_name.index = obesity.country_id
inner join transporation
on country_name.index = transporation.country_id
inner join poverty
on country_name.index = poverty.country_id
inner join "Science_score"
on country_name.index = "Science_score".country_id