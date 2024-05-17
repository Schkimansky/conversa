mod usefull_functions;
use usefull_functions::{get_magnitude, multiply_by_magnitude, check_for_invalid_parameters};
use std::ffi::CStr;
use std::os::raw::c_char;

fn process_string(input: *const c_char) -> &'static str {
    unsafe {
        println!("Unsafe code: c_str");
        let c_str = unsafe { CStr::from_ptr(input) };
        println!("Unsafe code: str_slice");
        let str_slice = c_str.to_str().unwrap();
        println!("Unsafe code: println received");
        println!("Received string from Python: {}", str_slice);
        println!("Unsafe code: return");
        return str_slice
    }
}



#[no_mangle]
pub extern "C" fn time(value: f64, from: *const c_char, to: *const c_char) -> f64 {
    println!("Starting");
    let from_str = process_string(from);
    let to_str = process_string(to);
    println!("Passed unsafe code.");

    let order = vec!["milliseconds", "seconds", "minutes", "hours", "days", "years", "decades", "centuries"];
    let magnitudes = vec![&1000.0, &60.0, &60.0, &24.0, &365.0, &10.0, &10.0];

    return multiply_by_magnitude(order, magnitudes, value, from_str, to_str)
}