// Package weather: Provide weather forcast features.
package weather

var (
	// CurrentCondition of the weather.
    CurrentCondition string
    // CurrentLocation of the weather.
	CurrentLocation  string
)
 
// Forecast returns the forcasted weather.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
