num=3
func=lambda :[lambda x: i*x for i in range(num)]
xxx=''.join(map(str,(f(num) for f in func())))
print(xxx)

