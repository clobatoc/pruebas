from odoo import api,models,fields

class ExampleModel(models.Model):
    #nombre del modelo; se utilizan . y no _ por problemas con base de datos:
    _name='example.model'
    #The char not have max size
    name=fields.Char(
        required=True,
        # Solo lectura por interfaz, OJO, por código se puede escribir
        #readonly=True,
        #Limit of size:
        #size=X;
    )
    number_integer=fields.Integer(
        string=u'Integer Field',
        index=True,
    )
    #coma flotante
    number_float=fields.Float()
    is_record=fields.Boolean()
    #Fecha
    field_date=fields.Date()
    #Fecha y hora string
    field_datetime=fields.Datetime()


    """
    Campos relacionales
    ===================
    
    Many2one: de muchos me cojo uno
    One2many: 
    Many2many: de muchos a muchos
    """
    user_id=fields.Many2one(
        comodel_name="res.users",
    )



