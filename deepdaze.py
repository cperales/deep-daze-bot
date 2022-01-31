from deep_daze import Imagine

imagine = Imagine(
    text='a blue orb',
    lr=1e-4,
    image_width=256,
    num_layers=12,
    batch_size=2,
    epochs=1,
    iterations=800,
    save_progress=False,
    open_folder=False,
    gradient_accumulate_every=2
)

imagine()
