"""LivePortrait without InsightFace (commercial-safe variant).
Replaces LivePortrait's FaceAnalysisDIY (InsightFace det_10g + 2d106det, non-commercial weights)
with MediaPipe FaceMesh (Apache-2.0, model bundled in the pip wheel). We emit 68 iBUG-style points;
LivePortrait's crop code accepts 68-pt input (parse_pt2_from_pt68) and its own MIT landmark.onnx
refines them to 203 points. No InsightFace weights are downloaded or loaded.
Usage (from the LivePortrait checkout): python lp_mediapipe.py <inference.py args...>"""
import os, runpy, sys
import numpy as np
import mediapipe as mp

# MediaPipe 468-mesh -> 68 iBUG landmarks (widely used mapping)
MP68 = [162, 234, 93, 58, 172, 136, 149, 148, 152, 377, 378, 365, 397, 288, 323, 454, 389,  # jaw 0-16
        71, 63, 105, 66, 107, 336, 296, 334, 293, 301,  # brows 17-26
        168, 197, 5, 4, 75, 97, 2, 326, 305,  # nose 27-35
        33, 160, 158, 133, 153, 144, 362, 385, 387, 263, 373, 380,  # eyes 36-47
        61, 39, 37, 0, 267, 269, 291, 405, 314, 17, 84, 181,  # outer lips 48-59
        78, 82, 13, 312, 308, 317, 14, 87]  # inner lips 60-67
assert len(MP68) == 68


class _Face:
    def __init__(self, bbox, lmk):
        self.bbox, self.landmark_2d_106, self.det_score = bbox, lmk, 1.0


class MediaPipeFaceAnalysis:
    def __init__(self, *a, **k):
        self.mesh = mp.solutions.face_mesh.FaceMesh(static_image_mode=True, max_num_faces=4, refine_landmarks=False)

    def prepare(self, *a, **k):
        pass

    def warmup(self):
        pass

    def get(self, img_bgr, **kw):
        h, w = img_bgr.shape[:2]
        res = self.mesh.process(img_bgr[:, :, ::-1].copy())
        faces = []
        for fl in (res.multi_face_landmarks or []):
            pts = np.array([[p.x * w, p.y * h] for p in fl.landmark], dtype=np.float32)
            lmk = pts[MP68]
            x0, y0 = pts.min(0); x1, y1 = pts.max(0)
            faces.append(_Face(np.array([x0, y0, x1, y1], np.float32), lmk))
        faces.sort(key=lambda f: -(f.bbox[2] - f.bbox[0]) * (f.bbox[3] - f.bbox[1]))  # largest first
        mx = kw.get("max_face_num", 0)
        return faces[:mx] if mx else faces


sys.path.insert(0, os.getcwd())
import src.utils.cropper as _cropper  # noqa: E402
_cropper.FaceAnalysisDIY = MediaPipeFaceAnalysis
sys.argv = ["inference.py"] + sys.argv[1:]
runpy.run_path("inference.py", run_name="__main__")
