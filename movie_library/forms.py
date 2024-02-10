from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,TextAreaField,URLField
from wtforms.validators import InputRequired,NumberRange

class MovieForm(FlaskForm):
    title = StringField("Title",validators=[InputRequired()])
    director = StringField("Director",validators=[InputRequired()])
    
    year = IntegerField("Year",
                        validators=[
                            InputRequired(),
                            NumberRange(min= 1878, message="Please enter a year in format yyyy")
                            ]
                        )

    submit = SubmitField("Add Movie")

class StringListField(TextAreaField):
    def _value(self):
        if self.data:
            return "\n".join(self.data)
        else:
            return ""

    def process_formdata(self, valuelist):
        # checks valuelist contains at least 1 element, and the first element isn't falsy (i.e. empty string)
        if valuelist and valuelist[0]:
            self.data = [line.strip() for line in valuelist[0].split("\n")]
        else:
            self.data = []


class ExtendedMovieForm(MovieForm):
    cast = StringListField("Cast")
    series = StringListField("Series")
    tags = StringListField("Tags")
    description = TextAreaField("Description")
    video_link = URLField("Video link")

    submit = SubmitField("Submit")

    <iframe width="560" height="315" 
    src="https://www.youtube.com/embed/lMiuUcgn9hg?si=eALM2bFcv2ktEmI-" 