import argparse
import sys
from numpy import percentile
from colored import Fore, Style

def parse_args():
    parser = argparse.ArgumentParser(description='draw a histogram from stdin', add_help=False)
    parser.add_argument('-b', '--bins', type=int, help='the number of bins (default=60)', default=60)
    parser.add_argument('-h', '--height', type=int, help='the height of the plot (default=10)', default=10)
    parser.add_argument('-?', '--help', action='help', help='show this help and exit')
    return parser.parse_args(sys.argv[1:])


legend = [
    "╷ ┌─┰┐╷",
    "├─┤ ┃├┤",
    "╵ └─┸┘╵"
]

legend = [
    "       ",
    "┠─┨░┃┠┨",
    "       "
]

def draw_line_n(n, bin_count, bin_for_min, bin_for_max, bin_for_q1, bin_for_q2, bin_for_q3):
    print(Fore.blue, Style.bold, end="")
    print("       ", end="")
    zone = 0
    for i in range(bin_count):
        if i == bin_for_min:
            zone = 1
            print(legend[n][0], end="")
            continue

        if zone == 0:
            print(" ", end="")
            continue
        if i == bin_for_max-1:
            print(legend[n][-1], end="")
            break

        if i==bin_for_q1:
            print(legend[n][2], end="")
            zone = 2
            continue

        if i==bin_for_q2:
            print(legend[n][4], end="")
            zone = 3
            continue

        if i == bin_for_q3:
            print(legend[n][5], end="")
            zone = 4
            continue
        if zone == 0 or zone == 1 or zone == 4:
            print(legend[n][1], end="")
            continue
        if zone == 2 or zone == 3:
            print(legend[n][3], end="")
            continue
    print(Style.reset)

def draw_legends(bin_count, min_v, max_v, q1_v, q2_v, q3_v, bin_for_min, bin_for_max, bin_for_q1, bin_for_q2, bin_for_q3):
    padding = "        "
    line = f"{Style.bold}Min:{Style.reset}{min_v}"
    line += " " * (bin_count - len(line))
    print(padding + line)
    
    line = " "*bin_for_q1 + f"{Style.bold}Q1:{Style.reset}{q1_v}"
    line += " " * (bin_count - len(line))
    print(padding+line)

    line = " "*bin_for_q2 + f"{Style.bold}Q2:{Style.reset}{q2_v}"
    line += " " * (bin_count - len(line))
    print(padding+line)

    line = " "*bin_for_q3 + f"{Style.bold}Q3:{Style.reset}{q3_v}"
    line += " " * (bin_count - len(line))
    print(padding+line)
    
    line = " "*bin_count + f"{Style.bold}Max:{Style.reset}{max_v}"
    line += " " * (bin_count - len(line))
    print(padding+line)


def main():

    args = parse_args()
    bins = args.bins
    input_data = sys.stdin.read().strip('\n')
    input_list = input_data.split('\n')

    # Convert input to floats
    input_lines = {}
    try:
        for line in input_list:
            line = line.split()
            line = list(map(float, line))
            for n, val in enumerate(line):
                if n not in input_lines:
                    input_lines[n] = []
                input_lines[n].append(round(val, 2))
        print(input_lines)


    except:
        raise SystemError("Failed to convert input to float")

    # print("Input data: ", input_list)

    absolute_min = min(map(min, input_lines.values()))
    absolute_max = max(map(max, input_lines.values()))
    print(absolute_min, absolute_max)

    for n in range(len(input_lines)):
        input_list = input_lines[n]
        q1_v = round(percentile(input_list,25), 2)
        q2_v = round(percentile(input_list,50), 2)
        q3_v = round(percentile(input_list,75), 2)
        min_v = min(input_list)
        max_v = max(input_list)
        iqr_v = q3_v - q1_v

        # print(q1_v, q2_v, q3_v, min_v, max_v, iqr_v)

        bin_width = (absolute_max - absolute_min) / bins
        bin_for_q1 = int((q1_v - absolute_min) / bin_width)
        bin_for_q2 = int((q2_v - absolute_min) / bin_width)
        bin_for_q3 = int((q3_v - absolute_min) / bin_width)
        bin_for_min = int((min_v - absolute_min) / bin_width)
        bin_for_max = int((max_v - absolute_min) / bin_width)

        # print(bin_for_q1, bin_for_q2, bin_for_q3)

        print("\n")
        draw_line_n(1, bins, bin_for_min, bin_for_max, bin_for_q1, bin_for_q2, bin_for_q3)
        draw_legends(bins, min_v, max_v, q1_v, q2_v, q3_v, bin_for_min, bin_for_max, bin_for_q1, bin_for_q2, bin_for_q3)

    # q1_v = percentile(input_list,25)
    # q2_v = percentile(input_list,50)
    # q3_v = percentile(input_list,75)
    # min_v = min(input_list)
    # max_v = max(input_list)
    # iqr_v = q3_v - q1_v

    # print(q1_v, q2_v, q3_v, min_v, max_v, iqr_v)

    # bins = 50
    # bin_width = (max_v - min_v) / bins
    # bin_for_q1 = int((q1_v - min_v) / bin_width)
    # bin_for_q2 = int((q2_v - min_v) / bin_width)
    # bin_for_q3 = int((q3_v - min_v) / bin_width)

    # # print(bin_for_q1, bin_for_q2, bin_for_q3)

    # print("\n")
    # draw_line_n(1, bins, bin_for_q1, bin_for_q2, bin_for_q3)
    # draw_legends(bins, min_v, max_v, q1_v, q2_v, q3_v, bin_for_q1, bin_for_q2, bin_for_q3)


    



if __name__ == "__main__":
    main()
