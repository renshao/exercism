use std::collections::HashSet;

fn sort_chars(word: &str) -> String {
    let mut word_chars : Vec<char> = word.to_lowercase().chars().collect();
    word_chars.sort_unstable();
    word_chars.into_iter().collect()
}

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &[&'a str]) -> HashSet<&'a str> {
    let word_lowercase = word.to_lowercase();
    let word_sorted = sort_chars(word);

    let mut results = vec![];
    for possible_anagram in possible_anagrams {
        if possible_anagram.to_lowercase().eq(&word_lowercase) {
            continue;
        }

        let sorted = sort_chars(possible_anagram);
        if sorted.eq(&word_sorted) {
            results.push(*possible_anagram);
        }
    }

    return results.into_iter().collect();
}
