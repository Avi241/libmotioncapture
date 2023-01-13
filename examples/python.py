import motioncapture
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("type")
    parser.add_argument("hostname")
    args = parser.parse_args()

    mc = motioncapture.connect(args.type, {"hostname": args.hostname})
    print("hii")
    while True:
        mc.waitForNextFrame()
        print("hii")
        print(mc.pointCloud)
