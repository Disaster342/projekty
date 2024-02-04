v1 = 1  # int
v2 = 1.0
v3 = "Hello world"
v4 = []
v5 = ()
v6 = {}
v7 = {}


def func1(param1, param2, param3, param4, param5, param6=None, *args, **kwargs):
    print(param1)
    return "srt"


func1(
    v1,
    "argument2",
    "argument3",
    "argument4",
    "argument5",
    "something ",
    data={"something": "else"},
)
# [[1,1], 2, 3, 4, 5]
# for x, y in container:


def func2(param1, param2):
    return param1 * param2


print(func2(v1, v2))
