from odoo import fields, models,api,exceptions,date
class BookList(models.Model):
    _name = 'book.list'

    name = fields.Char(size=100, string='Tên sách')
    page = fields.Integer(size=10,string="Số trang")
    nxb = fields.Many2one(comodel_name="book.public.company", string="Nhà xuất bản", required=False, )
    ngxb = fields.Date(string="Ngày xuất bản",requited=True)
    category = fields.Many2one(comodel_name="book.category", string="Danh mục sách", required=True )
    author = fields.Many2one(comodel_name="book.author", string="Tác giả", required=False )
    description = fields.Html('Mô tả')
    thumb = fields.Binary(string="Hình ảnh", attachment=True)
    language = fields.Selection(string="Ngôn ngữ", selection=[('0', 'Tiếng Việt'), ('1', 'Tiếng Anh'), ('2', 'Tiếng Pháp')], required=True )
    coo_author = fields.Many2many(string='Đồng tác giả', comodel_name='book.author')
    price = fields.Integer(string='Giá gốc')
    price_sale = fields.Float(string='Giá bán', compute='_compute_price')
    sl_nhap = fields.Integer(string='Số lượng nhập', size=20)
    ngay_nhap = fields.Date(string='Ngày nhập',default='date.today')
    sl_con = fields.Integer(string = 'Số lượng còn lại',compute = '')

    @api.one
    @api.depends('price')
    def _compute_price(self):
        if self.price != 0:
            print(self.price)
            self.price = self.price_sale * 1.5
            print(self.price)
            print(self.price)

    @api.multi
    @api.constrains('coo_author', 'page')
    def _check_author(self):
        if self.author is not None:
            if self.author in self.coo_author:
                print('Main:', self.author)
                print('Coo:', self.coo_author)
                raise exceptions.ValidationError("Tác giả chính không được chọn là tác giả phụ")
            if self.page == 0:
                raise exceptions.ValidationError('Số trang sách phải lớn hơn 0!')


class BookAuthor(models.Model):
    _name = 'book.author'

    name = fields.Char(size=100,string='Tên tác giả',required=True)
    birthday = fields.Date(string='Ngày sinh',required = True)
    gender = fields.Selection(string="Giới tính", selection=[('0', 'Nam'), ('1', 'Nữ'),('2', 'Giới tính thứ 3'), ], required=True )
    image = fields.Binary(string="Avatar", attachments = True )


class BookCategory(models.Model):
    _name = 'book.category'

    name = fields.Char(size=100, string='Tên thể loại')
    description = fields.Text(string='Ghi chú')

class PublishingCompany(models.Model):
    _name = 'book.public.company'

    name = fields.Char(size=500)
    description = fields.Html('Giới thiệu')

class Phieumuon(models.Model):
    _name = 'book.phieumuon'
    _rec_name = 'tennguoimuon'

    tennguoimuon=fields.Char(string='Tên sách',comodel_name = 'hr.employee')
    price = fields.Integer(string='Giá gốc')
    sl_nhap = fields.Integer(string='Số lượng nhập',required = True)



