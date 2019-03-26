namespace cpp shared
namespace java shared
namespace php shared
namespace perl shared


struct SharedStruct {
    1: i32 key
    2: string value
}

service SharedService {
    SharedStruct getStruct(1: i32 key)
}
