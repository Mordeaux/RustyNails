extern crate libc;

use std::str;
use std::ffi::CStr;
use self::libc::c_char;

#[repr(C)]
pub struct LinearRegression {
    input: u32,
    name: String,
    output: Option<u32>,
}

impl LinearRegression {
    fn new(name: String, input: u32) -> LinearRegression {
        println!("constructor input: {}", name);
        println!("constructor input: {}", input);
        LinearRegression{
            name: name,
            input: input,
            output: None,
        }
    }
    fn process(&mut self) {
        let output = self.input + 1;
        self.output = Some(output);
    }
    fn get_output(&mut self) -> u32 {
        match self.output {
            Some(i) => i,
            None => 0
        }
    }
}

#[no_mangle]
pub extern "C" fn init_regression(input: u32, name: *const c_char) -> LinearRegression {
    println!("func input: {}", input);
    let name_cstring = unsafe {
        CStr::from_ptr(name)
    };
    let name_bytes = name_cstring.to_bytes();
    match str::from_utf8(name_bytes) {
        Ok(s) => LinearRegression::new(s.to_string(), input),
        Err(_) => LinearRegression::new("failed".to_string(), 0u32)
    }
}

#[no_mangle]
pub extern "C" fn process_regression(linear_regression: &mut LinearRegression) -> u32 {
    linear_regression.process();
    linear_regression.get_output()
}
