// 
// Usefull Functions
//

pub fn get_magnitude(from: &str, to: &str, classification: Vec<&str>, magnitudes: Vec<&f64>) -> f64 {
    // Index distance is the distance (in integer) from (From) to (To) values inside the ORDER list
    let index_distance = [index_of(classification.as_slice(), &from), index_of(classification.as_slice(), &to)];

    let mut magnitude: f64 = 1.0;

    for &value_magnitude in &magnitudes[(index_distance[0].unwrap() as usize)..(index_distance[1].unwrap() as usize)] {
        magnitude *= value_magnitude;
    }

    return magnitude
}


pub fn index_of<T: PartialEq>(vector: &[T], item: &T) -> Option<usize> {
    return vector.iter().position(|x| x == item)
}

pub fn multiply_by_magnitude(order: Vec<&str>, magnitudes: Vec<&f64>, value: f64, from: &str, to: &str) -> f64 {
    // Check if the user is trying to convert a large unit to a small unit or vice versa
    let startindex = index_of(&order, &from).unwrap();
    let endindex = index_of(&order, &to).unwrap();
    let direction = endindex as i32 - startindex as i32;

    if direction == 0 {
        // User is trying to convert the same unit, so value doesn't change
        return value;
    } else if direction < 0 {
        let magnitude = get_magnitude(to, from, order, magnitudes);
        return value * magnitude;
    } else {
        let magnitude = get_magnitude(from, to, order, magnitudes);
        return value / magnitude;
    }
}

pub fn check_for_invalid_parameters(order: &[&str], from: &str, to: &str) {
    if !order.contains(&from) { panic!("Invalid unit of measurement: {}", from); }
    if !order.contains(&to) { panic!("Invalid unit of measurement: {}", to); }
}

