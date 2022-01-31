from deep_daze import Imagine

imagine = Imagine(
    text="A dreamer",
    image_width=256,
    num_layers=32,
    batch_size=8,
    epochs=1,
    iterations=200,
    save_progress=True,
    open_folder=False,
    gradient_accumulate_every=2
)
imagine()
