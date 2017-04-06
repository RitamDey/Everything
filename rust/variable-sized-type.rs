fn main() {
    let another: i64 = std::i64::MAX;
    let another2: u64 = std::u64::MAX;

    /**
    * isize is a type with the size of the maximum size of a pointer in the machine
    * on x86_64 machine it means that it will have the size and MAX same as i64
    **/
    let unknown_size: usize = std::usize::MAX;
    let z: isize = std::isize::MAX;

    println!("MAX size of the isize {:?}", z);
    println!("MAX size of the u32   {:?}", another);
    println!("MAX size of the usize {:?}", unknown_size);
    println!("MAX size of the u64   {:?}", another2);
}