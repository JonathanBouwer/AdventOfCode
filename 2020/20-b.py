from time import perf_counter
from math import sqrt
t0 = perf_counter()

a = [
"Tile 3583:",
".##..#..#.",
"....##....",
"##..#..#..",
".....#....",
".#..#.....",
"#.#.......",
"#.....#..#",
"....#....#",
"...#.##.#.",
".#....##.#",
"",
"Tile 3967:",
"..###..#..",
"#.........",
".........#",
"#...#....#",
"....#....#",
"#...#....#",
"#..#...#.#",
"##....##..",
"#....#....",
"##.###.#..",
"",
"Tile 3307:",
".#.#...#..",
"......#..#",
".........#",
"##.....##.",
"..#.....#.",
".#...####.",
"#....#.#.#",
"......##.#",
"#.##.#..##",
".....#.##.",
"",
"Tile 1741:",
".##..#.#..",
"#..##.#...",
".#.....#..",
"...####.##",
"#.#..###..",
"####.#....",
"..#.##.#..",
"#.....#.#.",
"#.###.....",
"####...###",
"",
"Tile 3821:",
".#######.#",
"...#......",
"#.##.#...#",
".#...#####",
"....#.##..",
"#.#.#.....",
"##......##",
"#..#.....#",
"##..#..#.#",
"###..#.#..",
"",
"Tile 1787:",
"..##.#.###",
"...##..#.#",
"#..#.###.#",
"..#.##..#.",
"#.#.....##",
"...#...#.#",
"#..##..#.#",
"##.#.##..#",
"...#..#...",
"..#..##...",
"",
"Tile 2281:",
"..#.#.##.#",
".......##.",
"..#..#..#.",
"....#.#..#",
"#...#.##.#",
"#..#.##.#.",
"#.#....#.#",
"#....##...",
".....#..##",
"...#.#...#",
"",
"Tile 3593:",
"...#..#..#",
".........#",
".........#",
"#.#..#...#",
"##......##",
"##........",
"...#.#...#",
"#...#...##",
"...#.#.#..",
"#..#......",
"",
"Tile 3259:",
".####.....",
"....#.#.##",
"#....#..##",
"#........#",
".....#....",
".#.....#.#",
"...##....#",
"#.....#.#.",
"#.#..#....",
"#.#..##.#.",
"",
"Tile 2663:",
".####..###",
"#.#..##...",
"#..#...#..",
"#..#....#.",
"..#.##...#",
".#....#.#.",
"#..#....#.",
"#.#.......",
".#.#......",
"..#..#####",
"",
"Tile 3833:",
"####....#.",
".......#.#",
".#........",
"#...#.##.#",
"#.##.#.#.#",
"...#.....#",
"##...#...#",
"#.#.##...#",
"##.#.#.##.",
".##.###.##",
"",
"Tile 3373:",
"#.....##.#",
"#...###..#",
"..#.#..#..",
"####..#.##",
"#...#.##.#",
"#..##.#...",
"#..##...##",
"#.####....",
"##..#...#.",
"##.##.#.##",
"",
"Tile 1511:",
".#.###...#",
"#....#...#",
".##.#.....",
"...##.###.",
"#.##.##..#",
"####.#..##",
"#..#.#....",
"#.......#.",
"#......#.#",
"###...#...",
"",
"Tile 1723:",
"...##..#.#",
"..#..#...#",
".##.....#.",
"#..#......",
".#..#.#..#",
".#........",
"...#.#..##",
"##.......#",
"..#..###..",
"#####...##",
"",
"Tile 1543:",
"#..#.##.##",
"#.....#..#",
".....#.#.#",
"###.......",
"...##....#",
"..#..#...#",
"#.....##.#",
"#.#..##.##",
"...###....",
"###.#...#.",
"",
"Tile 1433:",
"##.##..##.",
"###....#.#",
"..#.....##",
".#.##..#..",
".#.#...###",
"#.#.....#.",
"..##.....#",
"#....#....",
"..#.#...#.",
".#...#####",
"",
"Tile 1949:",
"#.#..##..#",
".........#",
".#.......#",
"#..##..###",
"........##",
"#........#",
".....#...#",
"...####.#.",
".#...##...",
"###.#.#..#",
"",
"Tile 3889:",
"###...####",
"#....##..#",
".#.###...#",
"##..#.....",
".....#....",
"....#.#.#.",
".........#",
"#....##..#",
"##.##..##.",
"#.###.####",
"",
"Tile 2477:",
".....#..##",
"#.##.###..",
"###..#...#",
".#....#.#.",
"#..#......",
"...#.....#",
"##.....#..",
"..##.....#",
".##.#....#",
"#####.####",
"",
"Tile 2137:",
"..########",
"#..#......",
"...#.##..#",
"#.#..#...#",
".#..#...##",
"##.....#.#",
".#....##..",
".##.......",
".#..####..",
"#..###...#",
"",
"Tile 3313:",
"..####.#.#",
"#..#.....#",
"#....#....",
"..##..##..",
"#....##...",
"..........",
"#.........",
".......###",
"##........",
".###...###",
"",
"Tile 1493:",
"#..####.##",
"##.#..#...",
"#.#.....##",
".##......#",
".##...#..#",
"#..##....#",
"#.#.#.#.#.",
"#.#...#..#",
"#.#.#....#",
"#.####...#",
"",
"Tile 1579:",
".##..##.##",
"#.#.......",
".......#..",
"..#...##..",
"#..####...",
".#.#.##.##",
"###.#.....",
"#....##.##",
"....#...##",
"##....#.#.",
"",
"Tile 2221:",
".#.#......",
".......##.",
"#..#.#...#",
"..###.###.",
"....#...##",
"##.#..##..",
"..##.#.#..",
"......####",
"..##.#.#..",
".###..#.##",
"",
"Tile 3643:",
"..###...#.",
"#..#..#..#",
".##.......",
"#..###....",
"##...##.##",
"#...#...#.",
"###......#",
"....#..#.#",
".#.#.....#",
"..#..#.#..",
"",
"Tile 3881:",
"###.##.##.",
".####..###",
"#.###..##.",
"....#...#.",
"##...#..#.",
"#........#",
"....#...#.",
"...#.....#",
".#.....##.",
".####..#.#",
"",
"Tile 3823:",
"..#.##..##",
"#...#....#",
"..#...#...",
"#.#.##...#",
".####....#",
".#...#...#",
"..........",
".........#",
"...#..#...",
"....#..#.#",
"",
"Tile 3181:",
"####..##.#",
"#.....##.#",
"#.......##",
".......#.#",
"..#..##.#.",
"##..#..#..",
"...##.....",
".........#",
"....#.##..",
".##.###.#.",
"",
"Tile 2837:",
".###.#.###",
"#.##..#.##",
".....##...",
"###......#",
"##.......#",
"........##",
"##.##..#..",
"....###...",
"..........",
"#......#.#",
"",
"Tile 2063:",
"..#####...",
"..........",
"........#.",
"..##.....#",
"###...#.#.",
"#.#.....#.",
".....#..##",
"#.......#.",
"##....##..",
"#.##.###.#",
"",
"Tile 1187:",
"#...##..##",
"#........#",
"#.#.......",
"...#.#....",
".....#.#.#",
"#....#....",
"..###.....",
".#........",
"..#...###.",
"####.#.#.#",
"",
"Tile 3137:",
"...###..#.",
"#.##.....#",
"..#...#..#",
"#..#.....#",
"......#...",
"#.....##.#",
"...#......",
"#.#.#.####",
"..#....#..",
".#..#.#.##",
"",
"Tile 2411:",
"#.....##..",
".......#.#",
".....##...",
"#.#.......",
"#..##....#",
".##.##....",
".##...##..",
"#.#.......",
"##.....#.#",
".##.###...",
"",
"Tile 2713:",
"..#.#.####",
"...####.#.",
"##..#...#.",
"#..##.....",
"#...#.....",
".#...#.###",
"..........",
"#.#.##..#.",
"#.#..#..#.",
".#..##.#.#",
"",
"Tile 1103:",
"##.#...##.",
"#.....##..",
"...###..#.",
"..##.....#",
".####..#..",
"..#.###.#.",
"##.....#..",
".#..#....#",
"#........#",
"####...##.",
"",
"Tile 3943:",
".###......",
"#...#.#...",
"..##..#..#",
".##..#.#.#",
"..........",
"##...#....",
"#..#...#..",
"#..###...#",
"###....###",
"#.#....###",
"",
"Tile 1871:",
"##.#...##.",
"#......#..",
".#.##.....",
".#####.#..",
"#.#....#..",
"#..#....##",
"#..####.#.",
"#....#....",
"...#.....#",
"...#.##.#.",
"",
"Tile 3407:",
"#.#.#####.",
"##.#..#..#",
".###.#.#.#",
"..#.......",
"##.###.#..",
".....#.###",
"#.#.......",
"##..#.#..#",
"#.#.##.#.#",
"#..#..###.",
"",
"Tile 2441:",
"#####.#..#",
"...#.#....",
"..#...#..#",
".##....#..",
"#.##..#...",
".##.#..#.#",
"##.......#",
".##..#....",
".......#..",
".#..#.###.",
"",
"Tile 3637:",
".#..##.#.#",
"...##..#..",
"#.#.###...",
"#....#...#",
"..#.....##",
"#....#...#",
"#..#.#.#..",
"....#..#.#",
"....#.#..#",
".#.###.##.",
"",
"Tile 1549:",
"....##.##.",
".#....#...",
"..####.#..",
"....#.#..#",
"#........#",
"..#.......",
".#.#....##",
"...######.",
"#...##....",
".#...##...",
"",
"Tile 1481:",
"...##.##..",
"#...#.##..",
"#..#..#.#.",
"#.#.#...#.",
"#...#.##..",
".##....#..",
"#........#",
"....#.#...",
"#.#.....##",
"#.....####",
"",
"Tile 1559:",
"#..#....#.",
"..#.##.#.#",
"#.....#.##",
".###.#...#",
"..####..##",
"#..#.#..#.",
"#.#...###.",
"#.....#.#.",
".#.....#..",
"#..####.#.",
"",
"Tile 2251:",
"#..#.....#",
".#..#.....",
"#.#....#..",
"#....##..#",
"##....#..#",
"..#..#....",
"#.#.#.#...",
"#...#....#",
"###..#.##.",
"##..#.####",
"",
"Tile 2897:",
"...###....",
"##..#....#",
".........#",
".#.......#",
"...#.....#",
"..#..#...#",
".#...#...#",
"#....#....",
".#......##",
"..##...##.",
"",
"Tile 2239:",
"#..###..#.",
".#.......#",
".#..#..#..",
"#.##....##",
"#....#.#.#",
"##..#.....",
"#........#",
"...##.#..#",
"#...###..#",
"...#.#.###",
"",
"Tile 2593:",
".#....##.#",
"##......##",
"..#..##...",
".#..#.....",
"...#.#...#",
"#.#..#.#..",
"......#.#.",
"#...##...#",
"###..##..#",
"#.#####.##",
"",
"Tile 3697:",
"##.######.",
"###....#..",
"#.....##.#",
"##...#..##",
"#.....#..#",
".#.#..#...",
"#......##.",
"#.#.#.#.#.",
".........#",
"....####..",
"",
"Tile 3739:",
"##.#......",
".#.....#.#",
"..#.....##",
"#....##...",
"##.#...#..",
"###.#...##",
".#...#.###",
".#..#.##.#",
"..#..#..#.",
"...#.##...",
"",
"Tile 2459:",
".#.####...",
"#..#...#..",
".....#.##.",
"..#....##.",
"#......##.",
"##...#..##",
"#....#....",
"###...#..#",
"###.##.###",
".....##...",
"",
"Tile 2939:",
"##.#.#....",
"#..#.#####",
"#...###.#.",
"..#...#.##",
".#.....##.",
"###....#..",
".##...#..#",
".....#.#..",
"..#..#....",
"..##..#.##",
"",
"Tile 2347:",
".###..#..#",
"##......#.",
"#......#..",
"#...#....#",
"#......#..",
"##.......#",
"..#.......",
"#.##..#...",
"#..#..###.",
"#....##..#",
"",
"Tile 2381:",
"######....",
"##.......#",
".#....###.",
"#.##.##.#.",
"#.#..#....",
".........#",
"....#..#.#",
"#####.....",
"..##....##",
"#..###...#",
"",
"Tile 2503:",
"#.#...###.",
"#...#..#..",
".##.#.#.##",
".#.....#..",
"#...##....",
"##.#.....#",
"...#..#..#",
"..#.##...#",
"......#...",
"##..#..##.",
"",
"Tile 3023:",
".#...#....",
"#.##...#..",
"##....#...",
".#..#.....",
".#.#.....#",
"#.#.......",
"##..#.#.#.",
"#...#.#...",
"...#..#.##",
"#...##.###",
"",
"Tile 3851:",
"#..##.#.#.",
"#...#....#",
"###..#....",
"#.#.#...##",
"..#.#..#.#",
"#.......#.",
"..#.....##",
"..........",
"#.#.#.#..#",
"..#.##..#.",
"",
"Tile 1009:",
".####.##..",
"#.........",
".#.#......",
"..#.#.....",
"#......##.",
"###.......",
"#.#.......",
".......#.#",
".#....#.##",
"#.####.#.#",
"",
"Tile 1151:",
".#.##..#..",
"..#......#",
"##....##.#",
"#......###",
"##.....#..",
"##..#.#..#",
"...#......",
".##...##..",
"##..###..#",
"######.###",
"",
"Tile 2683:",
"#..#.#..##",
".#....#.#.",
"#...##....",
"....###...",
"...#..#...",
"..#.......",
"...#...#..",
"....#.#...",
"..#..#...#",
"..#.#.##..",
"",
"Tile 3323:",
"#.#..##.##",
"#.#....###",
"#.##.###.#",
"##....#...",
"##..#.....",
"###.#.#.##",
"#......#.#",
"..#....##.",
"#......#.#",
".##...#..#",
"",
"Tile 2333:",
"##.#..#..#",
"#..##.....",
".........#",
".#.#.#....",
"#...##...#",
"#.#.#....#",
"..#.###..#",
"....###.#.",
"#...#....#",
"..#.....#.",
"",
"Tile 2543:",
"#..###.#..",
"....#..#.#",
"..#...#.#.",
"#...##...#",
".#.....###",
"..........",
"#..#....#.",
"#....#..#.",
"#.#..##..#",
"##...#..##",
"",
"Tile 1483:",
"###..##..#",
".#......#.",
".......#.#",
"#........#",
"...#...#.#",
"#.#.#.....",
"#......#.#",
"#...#.#...",
"#...####..",
"#.##..#..#",
"",
"Tile 2027:",
".#..#....#",
"....##....",
"....#...##",
"#.#..#....",
"#.#.....##",
".......#.#",
"#...#.....",
".##....#.#",
"###.#.##.#",
".###.#.###",
"",
"Tile 1699:",
"#.###..##.",
"..#.###...",
".........#",
".#.#..#..#",
"...##.##..",
"#........#",
".......#.#",
"##..#...##",
".....#....",
"#########.",
"",
"Tile 2843:",
"#...#.####",
"....#.##..",
"...#....#.",
".....#....",
"#..##.....",
".....#....",
"###.#.....",
"......#..#",
"#.#.#...##",
"#...##.##.",
"",
"Tile 1597:",
"#..#######",
"..........",
".#........",
"#..##.#...",
"##.....#..",
"##.###...#",
".....###.#",
"...##.#..#",
"#....#...#",
"##.#.#####",
"",
"Tile 2311:",
".#.#.#.###",
".#.......#",
"..#...#.##",
"#..#....##",
"#...#.....",
".........#",
".#.#...##.",
".#.##....#",
"..#..#...#",
"...##.#.#.",
"",
"Tile 1889:",
"#.###.###.",
".#...#...#",
"#........#",
"#......#.#",
"..#......#",
"#......###",
".....#.##.",
"#.....#..#",
"........##",
"####...#.#",
"",
"Tile 3581:",
"........##",
".#...#...#",
"###.....#.",
"..........",
"#.#......#",
"......#..#",
"##........",
"..#...####",
"#..#......",
".##.###.##",
"",
"Tile 1499:",
"##.#.#....",
".##...##..",
"##.....##.",
"###.#...##",
"..##....#.",
".#....#...",
"#..#...##.",
"..#....##.",
".#.....#..",
"..#.####.#",
"",
"Tile 2999:",
".#.###..#.",
"#.#...#...",
"##.#......",
"...#..#...",
"..###..###",
"...#.#..#.",
"#..##.#..#",
".........#",
"..#....##.",
"..#.###.#.",
"",
"Tile 1487:",
"#....#....",
".#.....#..",
".#.#.....#",
"#.#......#",
"#.#.##....",
"#.....#...",
".....#....",
"##........",
"##..##...#",
"#.#..#...#",
"",
"Tile 2969:",
"#..#.#..##",
"###..#...#",
".#..#.....",
"...####.#.",
"#.#.##..#.",
"...###...#",
"#...#.....",
"..#...##..",
"##..#.#..#",
"#..#.###.#",
"",
"Tile 1873:",
"..###.#.#.",
"..#.###.#.",
"#.#.##...#",
".#...#...#",
"....#.....",
"##.....##.",
".....#.#..",
"..#..#..#.",
"..##..#..#",
"##...#....",
"",
"Tile 2029:",
"#.#...####",
"#....##...",
".#.#...##.",
"#####.#.#.",
"#..#......",
"#...#..#..",
"#.#.#..#.#",
"#......#.#",
"...####.#.",
"..##.#.###",
"",
"Tile 3517:",
".##...##..",
".#......#.",
"....##....",
"#.##..#..#",
".......##.",
"#..#......",
"...##...#.",
"........##",
"#...#....#",
"..######.#",
"",
"Tile 2803:",
"#.##.###..",
".#..##...#",
"...##.....",
".#.#.#.#..",
"#.......#.",
".##.#.#..#",
".#.###.#..",
".#..#...##",
"#...###...",
".###..#.##",
"",
"Tile 1237:",
".######.##",
"#.#.......",
"....#....#",
".....#...#",
"#.###.#.##",
"#...####..",
"#.#......#",
"#.#.##.#.#",
"#..#..#...",
".#..#....#",
"",
"Tile 3877:",
"..#.#.#.##",
"..##...#..",
"#..#...#..",
"#.......#.",
"#.......#.",
"#...#.##..",
".#.......#",
"....#..###",
"##.......#",
".#.##.#.#.",
"",
"Tile 2081:",
"####.#####",
"....#..##.",
"........##",
"....#..##.",
"#..#....#.",
".##...##..",
"......#...",
".#....#..#",
"#.#.#...##",
".##...##.#",
"",
"Tile 2789:",
".#.##..#.#",
".......#..",
"##.......#",
"..#..#..##",
"..#.......",
".#........",
"#..##.#.#.",
"###.#..###",
"##..#...##",
"..#..#....",
"",
"Tile 3989:",
"##.##...##",
"#....#..#.",
".#....#.##",
"#......#.#",
"#.#..#....",
"#....#.#.#",
"...#...#..",
"#........#",
".......#.#",
"##.##.##..",
"",
"Tile 1933:",
".....###.#",
"#...#.#..#",
".#....#..#",
".#........",
"#####.##..",
"#..#.#...#",
"#..#.#...#",
"....##....",
"#....#..#.",
"##..#..##.",
"",
"Tile 1601:",
"##.#..##..",
".#.###.#.#",
"..#.###..#",
"##.#.#....",
".....###.#",
"##.##.####",
"#.#...#..#",
"#...##....",
"...#......",
".####..###",
"",
"Tile 1117:",
"#..##..##.",
"......##.#",
"....##.#..",
"#....#....",
".#.#.....#",
".....#.##.",
"#....##...",
"#.....#...",
"..#..##.#.",
".#.###.#..",
"",
"Tile 1409:",
"#...###...",
"#......#..",
"........#.",
".#........",
"##....#...",
"#.......##",
"#......#..",
"......##.#",
"#..###.#..",
".####.##..",
"",
"Tile 3359:",
"##.##....#",
"#..#...#.#",
"#....#####",
"...##..#..",
"..#..#...#",
"........##",
"...#...#.#",
".........#",
"...#.#.#.#",
"##.#....##",
"",
"Tile 2539:",
"...##.##.#",
"#.##.#...#",
"...##.#...",
"..#.#..#..",
"#.#..#.###",
"......##.#",
"#.......#.",
".#.......#",
"#...####..",
"..#...###.",
"",
"Tile 1607:",
"##..###.#.",
"#...#....#",
"#.#.#..#..",
"#..#....##",
"#.#......#",
"....##....",
"#..###...#",
"..#.##..##",
"##....##.#",
"...##..###",
"",
"Tile 2971:",
"#....#..##",
".##......#",
"#..##.....",
"#...##.##.",
"#...#.##..",
"....##...#",
"..#.###...",
"##.#.#..##",
"#..#..###.",
"#...###.##",
"",
"Tile 2447:",
"#..#..##.#",
"#....##..#",
".....##...",
"..#.###..#",
"#..#.##...",
"#.#.#...##",
"#.#..###.#",
"####..#...",
"#.#...###.",
"#..###..##",
"",
"Tile 1709:",
".....#..##",
"##....#...",
".........#",
"...###..#.",
"###......#",
"..#..#...#",
"#.###.#..#",
"###....##.",
"...#..##.#",
"##.#...#..",
"",
"Tile 3109:",
".#..###.##",
"....#.#.##",
"..#...#..#",
"#...#.....",
"####.#....",
".#.#...###",
"###....#..",
"#..###....",
"..........",
"##.##...##",
"",
"Tile 2089:",
"..####..#.",
".###.....#",
"....#..###",
".#.......#",
"..##.....#",
"#.###....#",
"#.#.##.#.#",
"#.......#.",
"...#.##.#.",
"...#..#.##",
"",
"Tile 1619:",
"#...#.#.#.",
"#.........",
"#....##.##",
"##....#...",
"#####.....",
"##.#..#..#",
"###...#..#",
"...#......",
"##..#....#",
".##.##...#",
"",
"Tile 3319:",
"###.#.#.#.",
".#....#..#",
"#.#.#...##",
"...#.....#",
"..........",
"........#.",
"..........",
"...#.##..#",
"#.#.#....#",
"##......#.",
"",
"Tile 1621:",
"#.###.###.",
".#...#...#",
"#.#......#",
"#....#....",
"#..#.....#",
"##..#..#..",
".###..#.#.",
"#.#.#.####",
"#.......##",
"##.##...#.",
"",
"Tile 2857:",
"##.#.#.#..",
"...#...##.",
"#......#..",
"......#...",
".#.#..#...",
".##..#...#",
"..###....#",
"#.##......",
"#.###...##",
"..#..##.#.",
"",
"Tile 2143:",
"#.#.......",
"#...#.##..",
"#..#.....#",
"...#.....#",
"#...#....#",
"........##",
"##....#.##",
"##..##..#.",
"#..#.....#",
"#..##....#",
"",
"Tile 3037:",
"........##",
"#....#..#.",
"......#...",
"....#.#...",
"...###.###",
"...###...#",
"..........",
"#.....#..#",
"##..#.....",
"#....#....",
"",
"Tile 1733:",
"#.#..#.#..",
".#....##..",
"#..#.#...#",
"........#.",
".........#",
"##....#...",
"#.....#..#",
"#..####.#.",
"#...##....",
"..#....##.",
"",
"Tile 2657:",
".##...#..#",
"#...#.##..",
"##........",
".##......#",
".#...#...#",
"..##...#..",
".........#",
"....#...#.",
"..#.##...#",
"#..######.",
"",
"Tile 1451:",
"#.....#..#",
".....#.##.",
"......##..",
"..#.......",
"..........",
"#..##....#",
"###......#",
"##.#.....#",
"#...##.###",
"###.#.....",
"",
"Tile 3191:",
"####.#.#.#",
".........#",
"###.#####.",
"#.....##..",
"...#....#.",
"##..#....#",
".#..#.#..#",
"#........#",
"######..#.",
".####.####",
"",
"Tile 3163:",
".#.##.#..#",
"##.##.#.#.",
"##..#....#",
".#....#.#.",
"##.#.....#",
".#........",
"#.#......#",
"#.......##",
"#........#",
"###...###.",
"",
"Tile 3067:",
".#...##...",
"..###.....",
"##.#..#..#",
"##.##..#..",
".......#..",
"#...##.#..",
"####....#.",
"#.#....#..",
"........#.",
".##.#....#",
"",
"Tile 3203:",
"##...#.#.#",
".##..#####",
"#.......##",
".#....#...",
".#....#..#",
"..#.#....#",
"#....#.#..",
"#....#####",
"#...####..",
"....##.###",
"",
"Tile 3229:",
"...#......",
"#...#.....",
"..##.#.##.",
"#.#...#...",
"#.##.#..##",
"##....##..",
"..#.###..#",
".....#...#",
"...#.....#",
"..#.#.....",
"",
"Tile 2083:",
"....#.###.",
"..........",
".........#",
"...##..#.#",
".##..#....",
"#..#..#...",
"......#.#.",
"#........#",
"#.##......",
"###..#.###",
"",
"Tile 3253:",
".##..#.#..",
".#.#...#.#",
"#.#....#..",
"...#.....#",
"#.........",
"#.........",
".##......#",
"......###.",
"#.........",
".....#...#",
"",
"Tile 1381:",
"###...##.#",
"#.#####.#.",
"###..#..##",
"#.........",
"..#..#...#",
"..#.#...##",
".#.#.....#",
"..#...##.#",
"##.#..#..#",
"######....",
"",
"Tile 2113:",
".....##..#",
".....###..",
"...#.....#",
"##.#..#...",
"....#.....",
"...#......",
"#..###.#.#",
"..........",
"#.#.......",
"..#..#.#..",
"",
"Tile 1087:",
"###..#.##.",
"#....#....",
"..#......#",
"###.#....#",
".#.......#",
"..#....##.",
"#...#....#",
"....#...##",
"....#.#.#.",
"#.#..#.###",
"",
"Tile 2833:",
".....#...#",
"#...#.#.#.",
"#.......#.",
"#......#.#",
".#.##.#...",
"........##",
"....#.#.##",
"........##",
"......#.#.",
"######.#..",
"",
"Tile 1063:",
".....###.#",
"#####.#..#",
"..###....#",
"...#.##...",
"###....#.#",
".....##...",
"####.....#",
"..##.#....",
"#...#...#.",
"...##.###.",
"",
"Tile 3049:",
"#.#.#..###",
"...##....#",
"#..#..#.#.",
"##.##..#..",
"###.....##",
"#.#..#.#..",
"#..##....#",
"#.#...#..#",
"##..#..#.#",
"....#####.",
"",
"Tile 1657:",
"#..####...",
"........##",
".........#",
"#...#.#...",
"#.#......#",
".#.#....#.",
"#....###.#",
"#..####.#.",
"#..#..####",
"...###..#.",
"",
"Tile 3863:",
"##.#######",
"..#.#.#...",
"#....#..#.",
"........##",
"#.##......",
"....#.....",
"#.#..##...",
"#.#......#",
"..#..#.#..",
"##.####..#",
"",
"Tile 3083:",
"##.#...###",
".#..#..#..",
"#.#####...",
"#..#.#....",
"##.....#..",
"#..##..###",
".#.#.....#",
"#.#..#..##",
".#.#..#.##",
"...#......",
"",
"Tile 3853:",
"#.###..###",
"##..#..##.",
".....##.##",
"......#..#",
"...#.#..#.",
"###....#..",
"##.....#..",
"##........",
"...#..#..#",
"###.###..#",
"",
"Tile 2129:",
"..#....#.#",
"#...#.....",
"##...##..#",
"#.#.......",
"....#.....",
"##......##",
"#..#......",
"#..#..#...",
"..........",
"...#.#.#..",
"",
"Tile 1759:",
"..##..###.",
".......#..",
".#.#.....#",
".....#....",
"#......#.#",
"#.#......#",
"#..#.#.#.#",
"#..#.#...#",
"#.#...#..#",
".##....#.#",
"",
"Tile 3617:",
"..#.#..###",
"..###....#",
"##.#.....#",
"#.##....##",
".....#..#.",
".........#",
"..........",
".####..#.#",
"#.#...#.#.",
"....##.##.",
"",
"Tile 2017:",
"..#.##.#.#",
"....#...##",
"..........",
".#........",
"#.....#...",
"#.....#...",
"#.........",
"....#.#.#.",
"..#.......",
"..#...#.##",
"",
"Tile 1277:",
"..##...#.#",
".##..#..#.",
".#....##.#",
"#....##...",
"#..#.##..#",
"###..##..#",
".........#",
".##.#.....",
"..#.......",
"##.###.#..",
"",
"Tile 2617:",
"###.......",
"......#...",
"##.##..#..",
"#.#....#..",
".###....##",
"..###..#.#",
"##...##..#",
"#..#......",
"#..#..####",
"#.##..#...",
"",
"Tile 2719:",
"..#.#.##.#",
"........##",
"...#.#....",
"...##....#",
".#.##.#...",
"..#.##.###",
"##.#.....#",
".........#",
"..#.#...##",
"###.#..###",
"",
"Tile 3671:",
"#..##..###",
"#...#...##",
"..........",
"...##.....",
".#..#.#..#",
"#.#..#....",
"#..###.###",
"..##..####",
"#.........",
".#..#.#..#",
"",
"Tile 3389:",
".#....#.##",
".#..##.#.#",
"#...##....",
"##....#..#",
"##......##",
".#...#....",
"..#....#..",
"....##....",
"#.#...#.#.",
"#.#.#..###",
"",
"Tile 3457:",
".#########",
"#..#......",
"..##......",
"#.........",
".#...#....",
".###.....#",
".......#.#",
".........#",
"###....#..",
"#.......##",
"",
"Tile 1777:",
"###.#.####",
"#..#...###",
".#.#..#..#",
".......#..",
"#.#..##.##",
"..###.....",
"###......#",
".#........",
"#.####....",
"##..######",
"",
"Tile 3613:",
"####.#...#",
"##.......#",
".......##.",
"#....#...#",
"......##.#",
"...#.#..##",
"#......#..",
"...#...#..",
".##..##...",
".#...#..#.",
"",
"Tile 3529:",
".#.##.#...",
"##.....#.#",
"#...#..#..",
"......##.#",
"##..#.##.#",
"##........",
"#.....#...",
"...#...#..",
"...##.#...",
"..###.....",
"",
"Tile 1153:",
"##.##.##..",
"..#####..#",
"##...#..#.",
".......###",
".#.......#",
"..#.#.....",
".......#.#",
"#...#..###",
".....#.#..",
".#.##....#",
"",
"Tile 2467:",
"####....##",
"#..###...#",
"#####....#",
".#......#.",
"###.......",
"##.......#",
".##.#.#..#",
"....#.#...",
"#........#",
".#..#.####",
"",
"Tile 3947:",
"#.##.##.#.",
"##.......#",
"......#..#",
"#...#..###",
".....#.###",
"##..#..#..",
"...#.#...#",
"#...#....#",
".......#.#",
"#...#..#.#",
"",
"Tile 1399:",
".##.#..###",
"#.......#.",
"#.......#.",
".....#..#.",
"#........#",
"##..#..#.#",
".##..##..#",
"#..#......",
"#.....#..#",
"#.##..##..",
"",
"Tile 2879:",
"....###..#",
"..#.......",
"#...#.....",
"...#.#....",
".........#",
".##..#.##.",
".#...###.#",
".#.....#.#",
"..##.....#",
"##...#.#..",
"",
"Tile 1039:",
"#......#.#",
"##.##.###.",
".....##..#",
"#........#",
"..#.......",
"#.........",
".#..#.#.#.",
".....###..",
"#....#####",
".#.....###",
"",
"Tile 2777:",
"#..##...#.",
"....#....#",
"........#.",
"##.#....#.",
"..#.##...#",
".#....#.#.",
"#....#....",
"#..#.#...#",
"#...##.#.#",
"#.......#.",
"",
"Tile 1097:",
"##...###..",
"..#..####.",
"##....#.##",
"#.....##..",
"...#....##",
".##..#....",
"#.##..###.",
"##...#....",
"#.###....#",
".#.#.###..",
"",
"Tile 3793:",
"####.....#",
"..........",
".#.##.#...",
"....#....#",
"#.....#...",
"..###..##.",
"##..#.#...",
"##........",
"#........#",
".###......",
"",
"Tile 2689:",
"####...#..",
"..##....##",
"#.#....#.#",
".....##..#",
"#.......##",
"#.........",
"#.....#..#",
"##........",
".......#.#",
"#.###..#.#",
"",
]

a_small = [
"Tile 2311:",
"..##.#..#.",
"##..#.....",
"#...##..#.",
"####.#...#",
"##.##.###.",
"##...#.###",
".#.#.#..##",
"..#....#..",
"###...#.#.",
"..###..###",
"",
"Tile 1951:",
"#.##...##.",
"#.####...#",
".....#..##",
"#...######",
".##.#....#",
".###.#####",
"###.##.##.",
".###....#.",
"..#.#..#.#",
"#...##.#..",
"",
"Tile 1171:",
"####...##.",
"#..##.#..#",
"##.#..#.#.",
".###.####.",
"..###.####",
".##....##.",
".#...####.",
"#.##.####.",
"####..#...",
".....##...",
"",
"Tile 1427:",
"###.##.#..",
".#..#.##..",
".#.##.#..#",
"#.#.#.##.#",
"....#...##",
"...##..##.",
"...#.#####",
".#.####.#.",
"..#..###.#",
"..##.#..#.",
"",
"Tile 1489:",
"##.#.#....",
"..##...#..",
".##..##...",
"..#...#...",
"#####...#.",
"#..#.#.#.#",
"...#.#.#..",
"##.#...##.",
"..##.##.##",
"###.##.#..",
"",
"Tile 2473:",
"#....####.",
"#..#.##...",
"#.##..#...",
"######.#.#",
".#...#.#.#",
".#########",
".###.#..#.",
"########.#",
"##...##.#.",
"..###.#.#.",
"",
"Tile 2971:",
"..#.#....#",
"#...###...",
"#.#.###...",
"##.##..#..",
".#####..##",
".#..####.#",
"#..#.#..#.",
"..####.###",
"..#.#.###.",
"...#.#.#.#",
"",
"Tile 2729:",
"...#.#.#.#",
"####.#....",
"..#.#.....",
"....#..#.#",
".##..##.#.",
".#.####...",
"####.#.#..",
"##.####...",
"##..#.##..",
"#.##...##.",
"",
"Tile 3079:",
"#.#.#####.",
".#..######",
"..#.......",
"######....",
"####.#..#.",
".#...#.##.",
"#.#####.##",
"..#.###...",
"..#.......",
"..#.###...",
""
]

tiles = {}
cur_id = ""
cur_tile = []
for l in a:
    if l == "":
        tiles[cur_id] = cur_tile
        cur_id = ""
        cur_tile = []
    elif "Tile" in l:
        cur_id = l.split(" ")[1][:-1]
    else:
        cur_tile.append(l)
        
        
borders = {}

def add_border(border, id):
    if border not in borders:
        borders[border] = []
    borders[border].append(id)

for k, v in tiles.items():
    border_1 = (v[0], "T")
    border_2 = (v[-1], "B")
    border_3 = ("".join([l[0] for l in v]), "L")
    border_4 = ("".join([l[-1] for l in v]), "R")
    bs = [border_1, border_2, border_3, border_4]
    for b, b_id in bs:
        add_border(b, (k, b_id))
        add_border(b[::-1], (k, "F" + b_id))
    
adjacents = {}
def add_adjacent(adjacent, id):
    if adjacent not in adjacents:
        adjacents[adjacent] = set()
    adjacents[adjacent].add(id)
    
for k, vs in borders.items():
    for v1, v1_id in vs:
        for v2, v2_id in vs:
            if v1 == v2:
                continue
            add_adjacent(v1, v2)

start_corner = ""
for k, v in adjacents.items():
    if len(v) == 2:
        start_corner = k
        break
        
        
dim = int(sqrt(len(adjacents.keys())))
sea_map_sets = [[set() for i in range(dim)] for j in range(dim)]
sea_map_sets[0][0] = {start_corner}
seen = {start_corner}

for total in range(dim * dim):
    for subtract in range(total + 1):
        if total == 0:
            continue
            
        x = (total - subtract - 1 + (total + 1)) % (total + 1)
        y = (subtract + 1) % (total + 1)
        if x >= dim or y >= dim:
            continue
        
        above = set()
        if y > 0:
            above = set.union(*[set(adj for adj in adjacents[ad]) for ad in sea_map_sets[y - 1][x]])
        left = set()
        if x > 0:
            left = set.union(*[set(adj for adj in adjacents[ad]) for ad in sea_map_sets[y][x - 1]])
            
        if len(above) == 0 or len(left) == 0:
            possible_values = above.union(left)
        else:
            possible_values = above.intersection(left)
        possible_values -= seen

        if len(possible_values) > 2 or len(possible_values) == 0:
            raise Exception("Welp")

        if len(possible_values) == 1:
            sea_map_sets[y][x] = possible_values
            seen = seen.union(possible_values)
        elif y > x:
            sea_map_sets[y][x] = {[i for i in possible_values][0]}
            seen = seen.union(sea_map_sets[y][x])
        else:
            sea_map_sets[y][x] = {[i for i in possible_values][1]}
            seen = seen.union(sea_map_sets[y][x])

sea_map = [[ [x for x in sea_map_sets[j][i]][0] for i in range(dim)] for j in range(dim)]

def rotate_cw(tile_id):
    tiles[tile_id] = ["".join([tiles[tile_id][9 - x][y] for x in range(10)]) for y in range(10)]

def flip_x(tile_id):
    tiles[tile_id] = ["".join(tiles[tile_id][y][::-1]) for y in range(10)]

def flip_y(tile_id):
    tiles[tile_id] = tiles[tile_id][::-1]

# since input is predefined do predefined flip, idk this is annoying code to do searches for
if sea_map[0][1] < sea_map[1][0]:
    sea_map = [[sea_map[x][y] for x in range(len(sea_map[0]))] for y in range(len(sea_map))]
rotate_cw(sea_map[0][0])
flip_y(sea_map[0][0]) # if using small_a comment this line

for y in range(dim):
    for x in range(dim):
        tile_id = sea_map[y][x]
        if y == 0:
            if x == 0:
                continue
            side_to_move = ""
            # Rotate to match right border of left tile
            right_border = "".join([l[-1] for l in tiles[sea_map[y][x - 1]]]) 
            for b in borders[right_border]:
                if b[0] == tile_id:
                    side_to_move = b[1]
            if side_to_move == "L":
                pass
            elif side_to_move == "B":
                rotate_cw(tile_id)
            elif side_to_move == "R":
                flip_x(tile_id)
            elif side_to_move == "T":
                rotate_cw(tile_id)
                flip_x(tile_id)
            elif side_to_move == "FL":
                flip_y(tile_id)
            elif side_to_move == "FB":
                rotate_cw(tile_id)
                flip_y(tile_id)
            elif side_to_move == "FR":
                flip_x(tile_id)
                flip_y(tile_id)
            elif side_to_move == "FT":
                rotate_cw(tile_id)
                flip_x(tile_id)
                flip_y(tile_id)
        else:
            # Rotate to match bottom border of above
            bottom_border = tiles[sea_map[y - 1][x]][-1]
            side_to_move = ""
            for b in borders[bottom_border]:
                if b[0] == tile_id:
                    side_to_move = b[1]
            if side_to_move == "T":
                pass
            elif side_to_move == "L":
                rotate_cw(tile_id)
                flip_x(tile_id)
            elif side_to_move == "B":
                flip_y(tile_id)
            elif side_to_move == "R":
                rotate_cw(tile_id)
                flip_x(tile_id)
                flip_y(tile_id)
            elif side_to_move == "FT":
                flip_x(tile_id)
            elif side_to_move == "FL":
                rotate_cw(tile_id)
            elif side_to_move == "FB":
                flip_x(tile_id)
                flip_y(tile_id)
            elif side_to_move == "FR":
                rotate_cw(tile_id)
                flip_y(tile_id)

full_map = []
for tile_y in range(dim):
    for y in range(1, len(tiles[sea_map[0][0]]) - 1):
        full_map_row = []
        for tile_x in range(dim):
            full_map_row.append(tiles[sea_map[tile_y][tile_x]][y][1:-1])
        full_map.append("".join(full_map_row))
       

sea_monster = [
"                  # ",
"#    ##    ##    ###",
" #  #  #  #  #  #   "
]
sea_monster_length = len(sea_monster[0])   
sea_monster_height = len(sea_monster)  

def find_sea_monsters(map_rotation):
    sea_monster_positions = []
    for y in range(len(full_map) - sea_monster_height + 1):
        for x in range(len(full_map[y]) - sea_monster_length + 1):
            invalid_seamonster = False
            for sy in range(sea_monster_height):
                for sx in range(sea_monster_length):
                    if sea_monster[sy][sx] == " ":
                        continue
                    if map_rotation[y + sy][x + sx] != "#":
                        invalid_seamonster = True
                        break

                if invalid_seamonster:
                    break

            if not invalid_seamonster:
                # print(f"FOUND SEA MONSTER AT {x} {y}")
                sea_monster_positions.append((x, y))
    return sea_monster_positions

len_row_full_map = len(full_map[0])
result = []
for i in range(4):
    full_map = ["".join([full_map[len_row_full_map - 1 - x][y] for x in range(len_row_full_map)]) for y in range(len_row_full_map)]
    result = find_sea_monsters(full_map)
    if len(result) > 0:
        # print(f"FOUND AFTER {i} ROTATIONS")
        break

for sea_moster_pos in result:
    x, y = sea_moster_pos
    for sy in range(sea_monster_height):
        new_line = [c for c in full_map[y + sy]]
        for sx in range(sea_monster_length): 
            if sea_monster[sy][sx] == "#":
                new_line[x + sx] = "X"
        full_map[y + sy] = "".join(new_line)

count = 0
for row in full_map:
    for c in row:
        if c == "#":
            count += 1
print(count)

# Fuck this, 4hrs 23m
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')