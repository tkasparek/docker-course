#![feature(proc_macro_hygiene, decl_macro)]

#[macro_use] extern crate rocket;

#[get("/<name>")]
fn hello(name: String) -> String {
    format!("Hello, {}!", name)
}

fn main() {
    rocket::ignite().mount("/hello", routes![hello]).launch();
}
