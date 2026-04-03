// The code below is a stub. Just enough to satisfy the compiler.
// In order to pass the tests you can add-to or change any of this code.

#[derive(Debug)]
pub struct Duration {
    seconds: u64,
}

#[macro_export]
macro_rules! impl_planet {
    ($t:ty, earth_years => $x:expr) => {
        impl Planet for $t {
            fn years_during(d: &Duration) -> f64 {
                d.seconds as f64 / 31557600.0 / $x
            }
        }
    };
}

impl From<u64> for Duration {
    fn from(s: u64) -> Self {
        Duration { seconds: s }
    }
}

pub trait Planet {
    fn years_during(d: &Duration) -> f64;
}

pub struct Mercury;
pub struct Venus;
pub struct Earth;
pub struct Mars;
pub struct Jupiter;
pub struct Saturn;
pub struct Uranus;
pub struct Neptune;

impl_planet!(Mercury, earth_years => 0.2408467 );
impl_planet!(Venus, earth_years => 0.61519726);
impl_planet!(Earth, earth_years => 1.0);
impl_planet!(Mars, earth_years => 1.8808158);
impl_planet!(Jupiter, earth_years => 11.862615);
impl_planet!(Saturn, earth_years => 29.447498);
impl_planet!(Uranus, earth_years => 84.016846);
impl_planet!(Neptune, earth_years => 164.79132);
