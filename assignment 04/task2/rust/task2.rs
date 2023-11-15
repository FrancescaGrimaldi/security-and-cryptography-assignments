// In Rust: write a function that takes a string as input and returns a new string that is equal to the 
// input but where &, < and > are replaced by &amp;, &lt; and &gt;

fn replace_char(s: &str) -> String {
    let mut result = String::new();
    for c in s.chars() {
        match c {
            '&' => result.push_str("&amp;"),
            '<' => result.push_str("&lt;"),
            '>' => result.push_str("&gt;"),
            _ => result.push(c),
        }
    }
    result
}

fn main() {
    let mut input = String::new();
    println!("Enter your string: ");
    std::io::stdin().read_line(&mut input).unwrap();
    
    println!("Output string: ");
    println!("{}", replace_char(&input));

}