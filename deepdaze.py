from deep_daze import Imagine

imagine = Imagine(
    text="A dreamer",
    image_width=256,
    num_layers=6,
    batch_size=1,
    epochs=10,
    iterations=1000,
    save_progress=False,
    open_folder=False,
    gradient_accumulate_every=16
)
imagine()