if __name__ == "__main__":
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    spacy.cli.download("en_core_web_trf")

    # Print out the models & their versions
    print("Installed models:")
    for model in spacy.util.get_installed_models():
        print(model, spacy.load(model).meta["version"])