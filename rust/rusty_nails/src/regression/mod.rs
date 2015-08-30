
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
pub extern "C" fn init_regression(input: u32, name: &str) -> LinearRegression {
    println!("func input: {}", input);
    LinearRegression::new(name.to_string(), input)
}

#[no_mangle]
pub extern "C" fn process_regression(linear_regression: &mut LinearRegression) -> u32 {
    linear_regression.process();
    linear_regression.get_output()
}
