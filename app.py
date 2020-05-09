import conway, argparse, sys

def main():
    parser = argparse.ArgumentParser(description="Conways game of life")
    parser.add_argument("-g",
                        "--gridsize",
                        nargs = "+",
                        type = int,
                        dest = "grid",
                        help = "define the desired size of your game of Life",
                        required = False)
    parser.add_argument("--glider",
                        nargs = "+",
                        type = int,
                        dest = "glider",
                        help = "place a Glider at (i,j)",
                        required = False)
    parser.add_argument("-i",
                        "--interval",
                        type = int,
                        dest = "interval",
                        help = "Refresh rate in ms",
                        required = False)
    parser.add_argument("--zeros",
                        action = "store_true",
                        help = "Initializes the board as all dead cells. Useful if you just want to see how a special shape works (like a glider)")
    args = parser.parse_args()

    updateInt = 50
    if args.interval:
        updateInt = args.interval

    M = 100
    N = 100
    if args.grid and (args.grid[0] > 8 and args.grid[1] > 8):
        M = args.grid[0]
        N = args.grid[1]

    if args.zeros:
        grid = conway.zeros(M, N)
    else:
        grid = conway.createGrid(M, N)

    if args.glider:
        place = tuple(args.glider)
        grid = conway.addGlider(place[0],
                                place[1],
                                grid)

    conway.animate_matplot(N, grid, updateInt)

if __name__ == '__main__':
    main()

