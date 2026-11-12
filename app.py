import argparse


def greet(name):
    return f"Hello from receiver, {name}!"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="输出一条问候语")
    parser.add_argument("--name", default="Git learner", help="要问候的名字")
    args = parser.parse_args()
    print(greet(args.name))
