use crate::Comparison::{Equal, Sublist, Superlist, Unequal};
use std::cmp::Ordering;

#[derive(Debug, PartialEq)]
pub enum Comparison {
    Equal,
    Sublist,
    Superlist,
    Unequal,
}

pub fn sublist<T: PartialEq>(first_list: &[T], second_list: &[T]) -> Comparison {
    let first_list_size = first_list.len();
    let second_list_size = second_list.len();

    match first_list_size.cmp(&second_list_size) {
        Ordering::Equal => {
            if first_list == second_list {
                return Equal;
            }
        }
        Ordering::Greater => {
            if second_list_size == 0 || first_list.windows(second_list_size).any(|w| w == second_list) {
                return Superlist;
            }
        }
        Ordering::Less => {
            if first_list_size == 0 || second_list.windows(first_list_size).any(|w| w == first_list) {
                return Sublist;
            }
        }
    }

    Unequal
}
