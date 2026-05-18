import cv2
import os

# Configuración
VIDEOS_DIR = r"C:\Users\sgghu\OneDrive\Documents\GitHub\TFG\data\raw"
FRAMES_DIR = r"C:\Users\sgghu\OneDrive\Documents\GitHub\TFG\data\frames"
FRAME_INTERVAL = 0.5  # segundos entre frames extraídos

def extract_frames(video_path, output_dir, interval):
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    video_output_dir = os.path.join(output_dir, video_name)
    os.makedirs(video_output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_step = int(fps * interval)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_idx = 0
    saved = 0

    print(f"Procesando: {video_name} | FPS: {fps:.1f} | Frames totales: {total_frames}")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_idx % frame_step == 0:
            filename = f"{video_name}_frame{frame_idx:05d}.jpg"
            cv2.imwrite(os.path.join(video_output_dir, filename), frame)
            saved += 1
        frame_idx += 1

    cap.release()
    print(f"  → {saved} frames guardados en {video_output_dir}")
    return saved

def main():
    total = 0
    videos = [f for f in os.listdir(VIDEOS_DIR) if f.endswith(".mp4")]

    if not videos:
        print("No se encontraron vídeos en data/raw/")
        return

    print(f"Vídeos encontrados: {len(videos)}\n")

    for video_file in videos:
        video_path = os.path.join(VIDEOS_DIR, video_file)
        saved = extract_frames(video_path, FRAMES_DIR, FRAME_INTERVAL)
        total += saved

    print(f"\nTotal frames extraídos: {total}")

if __name__ == "__main__":
    main()