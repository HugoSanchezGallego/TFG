from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolov8s.pt')

    results = model.train(
        data=r'C:\Users\sgghu\OneDrive\Documents\GitHub\TFG\data\dataset\data.yaml',
        epochs=50,
        imgsz=640,
        batch=16,
        device=0,
        project='models',
        name='detector_v1',
        patience=15,
        save=True,
        plots=True,
        workers=0
    )

    print(f'Mejor modelo guardado en: {results.save_dir}')