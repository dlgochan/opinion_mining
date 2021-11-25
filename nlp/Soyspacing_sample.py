from soyspacing.countbase import CountSpace

corpus_fname = "demo_model.txt"
model = CountSpace()
model.train(corpus_fname)

model_fname = 'twitter_model'
model.save_model(model_fname, json_format=False)

model12 = CountSpace()
model12.load_model(model_fname, json_format=False)

verbose=False
mc = 10  # min_count
ft = 0.3 # force_abs_threshold
nt =-0.3 # nonspace_threshold
st = 0.3 # space_threshold

sent = '이건진짜좋은영화 라라랜드진짜좋은영화'

# with parameters
sent_corrected, tags = model.correct(
    doc=sent,
    verbose=verbose,
    force_abs_threshold=ft,
    nonspace_threshold=nt,
    space_threshold=st,
    min_count=mc)

# without parameters
sent_corrected, tags = model.correct(sent)

print(sent_corrected)
