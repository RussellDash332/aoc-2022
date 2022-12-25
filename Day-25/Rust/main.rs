fn get_input() -> String {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).expect("Failed");
    buffer
}

fn main() {
    let mut n:i64 = 0;
    let mut t:i64 = 0;
    use std::collections::HashMap;
    
    let mut h = HashMap::new();
    h.insert('0', 0);
    h.insert('1', 1);
    h.insert('2', 2);
    h.insert('-', -1);
    h.insert('=', -2);

    let mut r = HashMap::new();
    for (key, val) in h.iter() {
        r.insert(val, key);
    }

    loop {
        let target = get_input();
        if target.trim().chars().count() == 0 {break;}
        for c in target.trim().chars() { 
            t = 5*t + h.get(&c).unwrap_or(&0);
        }
        n += t;
        t = 0;
    }
    let mut stack = Vec::new();
    while n > 0 {
        stack.push(r.get(&(n%5 - 5*(if n%5>2 {1} else {0}))));
        n = n/5 + (if n%5>2 {1} else {0});
    }
    let mut ans: String = "".to_string();
    while stack.len() != 0 {
        ans.push(**stack.pop().unwrap().unwrap());
    }
    println!("Part 1: {}", ans);
    println!("Part 2: THE END!");
}