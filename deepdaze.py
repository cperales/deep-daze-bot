from deep_daze import Imagine

imagine = Imagine(
    text='a dog eating on the lawn',
    image_width=256,
    num_layers=24,
    batch_size=4,
    epochs=3,
    iterations=800,
    save_progress=True,
    open_folder=False,
    gradient_accumulate_every=1
)

imagine()
