from deep_daze import Imagine

imagine = Imagine(
    text="a house in the trees",
    image_width=256,
    num_layers=6,
    batch_size=1,
    save_progress=True,
    open_folder=False,
    gradient_accumulate_every=16 # Increase gradient_accumulate_every to correct for loss in low batch sizes
)

imagine()