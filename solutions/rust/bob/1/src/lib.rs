pub fn reply(message: &str) -> &str {
    let trimmed_message = message.trim_matches(|c| char::is_ascii_whitespace(&c));

    if trimmed_message.is_empty() {
        return "Fine. Be that way!";
    }

    let mut iter = trimmed_message.chars();
    let mut is_question = false;
    let mut has_letters = false;
    let mut all_capital = true;

    let mut c = iter.next_back().unwrap();
    if c == '?' {
        is_question = true;
    }
    
    loop {
        if c.is_alphabetic() {
            has_letters = true;
            
            if c.is_lowercase() {
                all_capital = false;
            }
        }

        let next = &iter.next();
        if next.is_none() {
            break;
        }
        c = next.unwrap();
    }

    
    if is_question {
        if has_letters && all_capital {
            return "Calm down, I know what I'm doing!";
        } else {
            return "Sure.";
        }
    }

    if has_letters && all_capital {
        return "Whoa, chill out!";
    }

    "Whatever."
}
