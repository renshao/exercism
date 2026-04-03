use crate::Comparison::{Superlist, Equal, Sublist, Unequal};

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

    if first_list_size == second_list_size {
        if first_list == second_list {
            return Equal;
        }
    } else if first_list_size > second_list_size {
        if second_list_size == 0 {
            return Superlist;
        }
        for window in first_list.windows(second_list_size) {
            if window == second_list {
                return Superlist;
            }
        }
    } else {
        if first_list_size == 0 {
            return Sublist;
        }
        for window in second_list.windows(first_list_size) {
            if window == first_list {
                return Sublist;
            }
        }
    }

    Unequal
}
