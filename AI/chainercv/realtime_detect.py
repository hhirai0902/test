import argparse
import chainer
import cv2
from timeit import default_timer as timer

from chainercv.links import SSD300
#from chainercv.datasets import voc_detection_label_names, voc_semantic_segmentation_label_colors
from chainercv.datasets import voc_bbox_label_names, voc_semantic_segmentation_label_colors


def main():
    chainer.config.train = False

    parser = argparse.ArgumentParser()
    parser.add_argument('--gpu', type=int, default=-1)
    parser.add_argument('video')
    parser.add_argument("--start_frame",default=0)
    args = parser.parse_args()

#    label_names = voc_detection_label_names
    label_names = voc_bbox_label_names

    model = SSD300(
        n_fg_class=20,
        pretrained_model="voc0712")

    if args.gpu >= 0:
        chainer.cuda.get_device_from_id(args.gpu).use()
        model.to_gpu()

    vid = cv2.VideoCapture(args.video)
    if not vid.isOpened():
        raise ImportError(("Couldn't open video file or webcam. If you're "
                           "trying to open a webcam, make sure you video_path is an integer!"))

    # Skip frames until reaching start_frame
    if args.start_frame > 0:
        vid.set(cv2.cv.CV_CAP_PROP_POS_MSEC, args.start_frame)

    # Compute aspect ratio of video
    vidw = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    vidh = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    vidar = vidw / vidh

    accum_time = 0
    curr_fps = 0
    fps = "FPS: ??"
    prev_time = timer()

    while True:
        retval, ori_img = vid.read()
        if not retval:
            print("Done!")
            return
        im_size = (300, 300)
        resized = cv2.resize(ori_img, im_size)
        rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

        # Reshape to original aspect ratio for later visualization
        # The resized version is used,to visualize what kind of resolution
        # the network has to work with.
        to_draw = cv2.resize(resized, (int(300 * vidar),int(300 * vidar)))

        # transpose (H, W, C) -> (C, H, W)
        image = rgb.transpose((2, 0, 1))

        # Use model to predict
        bboxes, labels, scores = model.predict([image])
        bbox, label, score = bboxes[0], labels[0], scores[0]

        if len(bbox) != 0:
            for i, bb in enumerate(bbox):
                # Interpret output, only one frame is used
                print(i)
                lb = label[i]
                conf = score[i].tolist()
                ymin = int(bb[0] * vidar)
                xmin = int(bb[1] * vidar)
                ymax = int(bb[2] * vidar)
                xmax = int(bb[3] * vidar)

                # Draw the box on top of the to_draw image
                class_num = int(lb)
                cv2.rectangle(to_draw, (xmin, ymin), (xmax, ymax),
                voc_semantic_segmentation_label_colors[class_num], 2)
                text = label_names[class_num] + " " + ('%.2f' % conf)
                print(text)

                text_top = (xmin, ymin - 10)
                text_bot = (xmin + 80, ymin + 5)
                text_pos = (xmin + 5, ymin)
                cv2.rectangle(to_draw, text_top, text_bot,
                voc_semantic_segmentation_label_colors[class_num],
                 -1)
                cv2.putText(to_draw, text, text_pos,
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 0), 1)

        # Calculate FPS
        # This computes FPS for everything,  not just the model's execution
        # which may or may not be what you want
        curr_time = timer()
        exec_time = curr_time - prev_time
        prev_time = curr_time
        accum_time = accum_time + exec_time
        curr_fps = curr_fps + 1
        if accum_time > 1:
            accum_time = accum_time - 1
            fps = "FPS: " + str(curr_fps)
            curr_fps = 0
        # Draw FPS in top left corner
        cv2.rectangle(to_draw, (0, 0), (50, 17), (255, 255, 255), -1)
        cv2.putText(to_draw, fps, (3, 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 0), 1)
        cv2.imshow("SSD result", to_draw)
        cv2.waitKey(10)


if __name__ == '__main__':
    main()