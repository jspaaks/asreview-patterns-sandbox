import click
from asreviewlib.classifiers import LstmBaseClassifier
from .._epilog import epilog


name = LstmBaseClassifier.name


@click.command(name=f"c-{name}", help="Use LSTM Base classifier", epilog=epilog)
@click.argument("feature_matrix_file", type=click.Path(exists=True, readable=True))
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the classifier configura" +
              "tion, even if that means overwriting a previous configuration.")
@click.pass_obj
def lstm_base_classifier(obj, feature_matrix_file, force):
    if not force:
        assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.model = name
    obj.classifier.params = {}
    obj.provided.classifier = True