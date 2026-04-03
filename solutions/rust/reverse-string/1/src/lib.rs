pub fn reverse(input: &str) -> String {
    let mut s = String::with_capacity(input.len());
    for c in input.chars() {
        s.insert(0, c);
    }

    return s;
}
