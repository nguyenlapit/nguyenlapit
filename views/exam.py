coo_author = fields.Many2many(string='Đồng tác giả', comodel_name='book.author')
price = fields.Integer(string='Giá gốc')
price_sale = fields.Float(string='Giá bán', compute='_compute_price')


@api.one
@api.depends('price')
def _compute_price(self):
    if self.price != 0
        print(self.price)
        self.price = self.price_sale * 1.5
        print(self.price)


@api.multi
@api.constrains('coo_author', 'page')
def _check_author(self):
    if self.author in self.coo_author:
        print('Main:', self.author)
        print('Coo:', self.coo_author)
        raise exceptions.ValidationError("Tác giả chính không được chọn là tác giả phụ")
    if self.page == 0:
        raise exceptions.ValidationError('Số trang sách phải lớn hơn 0!')