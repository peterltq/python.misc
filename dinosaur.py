from pathlib import Path
import math


# file1 = None
name_map: dict[str, list] = {}

print(f"current file:{__file__}")

with open(Path(__file__).resolve().parent / "file1.csv", encoding="UTF-8") as file1:
    lines1 = file1.read()
    for i, line in enumerate(lines1.split("\n")):
        if i==0: 
            continue
        if len(line) == 0:
            break;
        name, leg_len, diet = line.split(',')
        name_map.setdefault(name, [(None, None), (None, None), None])
        name_map[name][0] = (leg_len, diet)

with open(Path(__file__).resolve().parent / "file2.csv", encoding="UTF-8") as file2:
    lines2 = file2.read()
    for i, line in enumerate(lines2.split("\n")):
        if i==0 or len(line) == 0:
            continue;
        name, stride_len, stance = line.split(",")
        name_map.setdefault(name, [(None, None), (None, None), None])
        
        name_map[name][1] = (stride_len, stance)

# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
for name, tuples in name_map.items():
    leg_len, diet = tuples[0]
    stride_len, stance = tuples[1] if len(tuples) >= 2 else (None, None)

    if ( leg_len is not None and diet is not None and 
        stride_len is not None and stance is not None):
        speed = (float(stride_len) / float(leg_len)) * math.sqrt(float(leg_len) * 9.8)
        tuples[2] = speed


output_map = dict(
    sorted(name_map.items(), key=lambda entry: -entry[1][2] if entry[1][2] is not None else float("inf") ))

output = [(k, 
           v[2] , # score
           v[1][1] # stance
           ) for k, v in output_map.items() if v[1][1] == "bipedal" and v[2] is not None]

print(f"{output=}")


print("End")

