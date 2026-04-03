use std::fmt;
use std::fmt::Formatter;

#[derive(Debug, PartialEq)]
pub struct Clock {
    minutes: i32,
    hours: i32,
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        Clock::minutes_to_clock(hours * 60 + minutes)
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        Clock::minutes_to_clock(self.hours * 60 + self.minutes + minutes)
    }

    fn minutes_to_clock(minutes: i32) -> Clock {
        let mut minutes = minutes;
        if minutes < 0 {
            minutes = minutes % (60 * 24) + 60 * 24;
        }

        let hours = minutes / 60 % 24;
        minutes %= 60;
        Clock {
            minutes,
            hours,
        }
    }
}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        write!(f, "{:02}:{:02}", self.hours, self.minutes)
    }
}
