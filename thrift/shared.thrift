namespace cl shared
namespace cpp shared
namespace d shared
namespace dart shared
namespace java shared
namespace php shared
namespace perl shared
namespace haxe shared
namespace netcore shared
namespace netstd shared


struct SharedStruct {
    1: i32 key
    2: string value
}

service SharedService {
    SharedStruct getStruct(1: i32 key)
}
