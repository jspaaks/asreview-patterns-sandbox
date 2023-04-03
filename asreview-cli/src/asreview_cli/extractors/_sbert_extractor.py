import click
from asreviewlib.extractors import SbertExtractor
from .._epilog import epilog


name = SbertExtractor.name


@click.command(name=f"e-{name}", help="Use SBERT extractor", epilog=epilog)
@click.option("--transformer_model", "transformer_model", default="all-mpnet-base-v2", type=click.STRING,
              help="hyperparameter 'transformer_model'.")
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the extractor configura" +
              "tion, even if that means overwriting a previous configuration.")
@click.pass_obj
def sbert_extractor(obj, transformer_model, force):
    if not force:
        assert obj.provided.extractor is False, "Attempted reassignment of extractor"
    obj.classifier.model = name
    obj.classifier.params = {
        "transformer_model": transformer_model
    }
    obj.provided.extractor = True