use std::thread;

mod regression;

#[no_mangle]
pub extern fn process() {
    let handles: Vec<_> = (0..10).map(|_| {
        thread::spawn(|| {
            let mut x = 0;
            for _ in (0..5_000_000) {
                x += 1
            }
        x
        })
    }).collect();

    for h in handles {
        println!("Thread finished at count={}",
        h.join().map_err(|_| "Could not join a thread!").unwrap());
    }
    println!("Rust is done!");
}

#[no_mangle]
pub extern fn linear_regression() {
    regression::linear_regression();
}
