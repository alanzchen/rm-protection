class Config():
    def __init__(self):
        self.suffix = ".rm-protection"
        self.invalid = ['.', '..', './', '../']
        self.protect_prefix = 'protect: '
        self.rm_prefix = 'rm-p: '