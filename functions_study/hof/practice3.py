def philosophy(statement):
    def thought():
        return statement
    return thought


question = philosophy('To B, or not to B. It depends where the bomb is.')
print(question())
