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

def draw_line_n(n, bin_count, bin_for_q1, bin_for_q2, bin_for_q3):
    print(Fore.blue, Style.bold, end="")
    print("       ", end="")
    zone = 0
    for i in range(bin_count):
        if i == 0:
            print(legend[n][0], end="")
            continue
        if i == bin_count-1:
            print(legend[n][-1], end="")
            continue

        if i==bin_for_q1:
            print(legend[n][2], end="")
            zone = 1
            continue

        if i==bin_for_q2:
            print(legend[n][4], end="")
            zone = 2
            continue

        if i == bin_for_q3:
            print(legend[n][5], end="")
            zone = 3
            continue
        if zone == 0 or zone == 3:
            print(legend[n][1], end="")
            continue
        if zone == 1 or zone == 2:
            print(legend[n][3], end="")
            continue
    print(Style.reset)

def draw_legends(bin_count, min_v, max_v, q1_v, q2_v, q3_v, bin_for_q1, bin_for_q2, bin_for_q3):
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
    input_data = sys.stdin.read().strip('\n')
    input_list = input_data.split('\n')

    # Convert input to floats
    try:
        input_list = list(map(float,input_list))
    except:
        raise SystemError("Failed to convert input to float")

    # print("Input data: ", input_list)

    q1_v = percentile(input_list,25)
    q2_v = percentile(input_list,50)
    q3_v = percentile(input_list,75)
    min_v = min(input_list)
    max_v = max(input_list)
    iqr_v = q3_v - q1_v

    # print(q1_v, q2_v, q3_v, min_v, max_v, iqr_v)

    bins = 50
    bin_width = (max_v - min_v) / bins
    bin_for_q1 = int((q1_v - min_v) / bin_width)
    bin_for_q2 = int((q2_v - min_v) / bin_width)
    bin_for_q3 = int((q3_v - min_v) / bin_width)

    # print(bin_for_q1, bin_for_q2, bin_for_q3)

    print("\n")
    draw_line_n(1, bins, bin_for_q1, bin_for_q2, bin_for_q3)
    draw_legends(bins, min_v, max_v, q1_v, q2_v, q3_v, bin_for_q1, bin_for_q2, bin_for_q3)


    



if __name__ == "__main__":
    main()
