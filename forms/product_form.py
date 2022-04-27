from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired
from data import db_session
from data.product_types import ProductType


class ProductForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        db_sess = db_session.create_session()
        product_types = db_sess.query(ProductType).all()
        self.type_id.choices = [(g.id, g.name) for g in product_types]
    type_id = SelectField('Вид', default=1)
    brand = StringField('Название', validators=[DataRequired()])
    product_date = DateField('Дата изготовления', validators=[DataRequired()])
    expiration_date = DateField('Срок годности', validators=[DataRequired()])
    amount_text = StringField('Количество(мл / г)', validators=[DataRequired()])
    submit = SubmitField('Добавить продукт')

