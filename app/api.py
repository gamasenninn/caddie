from app import app
from models import *
from flask import jsonify, request
import json
from datetime import date


@app.route('/')
def index():
    return 'HelloWorld!'


# -----ユーザー(Users)-----
@app.route('/users', methods=['GET'])
def user_index():
    users = User.query.all()
    return jsonify(UserSchema(many=True).dump(users))


@app.route('/user/<id>', methods=['GET'])
def user_show(id):
    userCount = User.query.filter(User.id == id).count()
    if userCount:
        user = User.query.filter(User.id == id).first()
        return jsonify(UserSchema().dump(user))
    else:
        return jsonify([])


@app.route('/user', methods=['POST'])
def user_create():
    data = request.json
    newUser = User(
        name=data['name'],
        password=data['password'],
        group=data['group'],
        role=data['role'],
    )
    db.session.add(newUser)
    db.session.commit()
    id = newUser.id
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/user/<id>', methods=['PUT'])
def user_update(id):
    data = request.json
    user = User.query.filter(User.id == id).one()

    user.name = data['name']
    user.password = data['password']
    user.group = data['group']
    user.role = data['role']

    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/user/<id>', methods=['DELETE'])
def user_destroy(id):
    user = User.query.filter(User.id == id).delete()
    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": ''})


# -----得意先(Customers)-----
@app.route('/customers', methods=['GET'])
def customer_index():
    customers = Customer.query.all()
    return jsonify(CustomerSchema(many=True).dump(customers))


@app.route('/customer/<id>', methods=['GET'])
def customer_show(id):
    customerCount = Customer.query.filter(Customer.id == id).count()
    if customerCount:
        customer = Customer.query.filter(Customer.id == id).first()
        return jsonify(CustomerSchema().dump(customer))
    else:
        return jsonify([])


@app.route('/customer', methods=['POST'])
def customer_create():
    data = request.json
    newCustomer = Customer(
        customerName=data.get('customerName'),
        honorificTitle=data.get('honorificTitle'),
        postNumber=data.get('postNumber'),
        address=data.get('address'),
        telNumber=data.get('telNumber'),
        faxNumber=data.get('faxNumber'),
        url=data.get('url'),
        email=data.get('email'),
        manager=data.get('manager'),
        representative=data.get('representative'),
        memo=data.get('memo'),
    )
    db.session.add(newCustomer)
    db.session.commit()
    id = newCustomer.id
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/customer/<id>', methods=['PUT'])
def customer_update(id):
    data = request.json
    customer = Customer.query.filter(Customer.id == id).one()

    customer.customerName = data.get('customerName')
    customer.honorificTitle = data.get('honorificTitle')
    customer.postNumber = data.get('postNumber')
    customer.address = data.get('address')
    customer.telNumber = data.get('telNumber')
    customer.faxNumber = data.get('faxNumber')
    customer.url = data.get('url')
    customer.email = data.get('email')
    customer.manager = data.get('manager')
    customer.representative = data.get('representative')
    customer.memo = data.get('memo')

    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/customer/<id>', methods=['DELETE'])
def customer_destroy(id):
    customer = Customer.query.filter(Customer.id == id).delete()
    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": ''})


# -----商品(Items)-----
@app.route('/items', methods=['GET'])
def item_index():
    items = Item.query.all()
    return jsonify(ItemSchema(many=True).dump(items))


@app.route('/item/<id>', methods=['GET'])
def item_show(id):
    itemCount = Item.query.filter(Item.id == id).count()
    if itemCount:
        item = Item.query.filter(Item.id == id).first()
        return jsonify(ItemSchema().dump(item))
    else:
        return jsonify([])


@app.route('/item', methods=['POST'])
def item_create():
    data = request.json
    newItem = Item(
        itemName=data.get('itemName'),
        unit=data.get('unit'),
        basePrice=data.get('basePrice'),
        cost=data.get('cost'),
        memo=data.get('memo'),
    )
    db.session.add(newItem)
    db.session.commit()
    id = newItem.id
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/item/<id>', methods=['PUT'])
def item_update(id):
    data = request.json
    item = Item.query.filter(Item.id == id).one()

    item.itemName = data.get('itemName')
    item.unit = data.get('unit')
    item.basePrice = data.get('basePrice')
    item.cost = data.get('cost')
    item.memo = data.get('memo')

    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/item/<id>', methods=['DELETE'])
def item_destroy(id):
    item = Item.query.filter(Item.id == id).delete()
    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": ''})


# -----請求書(Invoices)-----
@app.route('/invoices', methods=['GET'])
def invoice_index():
    invoices = Invoice.query.all()
    return jsonify(InvoiceSchema(many=True).dump(invoices))


@app.route('/invoice/<id>', methods=['GET'])
def invoice_show(id):
    invoiceCount = Invoice.query.filter(Invoice.id == id).count()
    if invoiceCount:
        invoice = Invoice.query.filter(Invoice.id == id).first()
        return jsonify(InvoiceSchema().dump(invoice))
    else:
        return jsonify([])


@app.route('/invoice', methods=['POST'])
def invoice_create():
    data = request.json
    newInvoice = Invoice(
        customerId=data.get('customerId'),
        applyNumber=data.get('applyNumber'),
        applyDate=data.get('applyDate'),
        expiry=data.get('expiry'),
        title=data.get('title'),
        memo=data.get('memo'),
        remarks=data.get('remarks'),
        isTaxExp=data.get('isTaxExp'),
    )
    db.session.add(newInvoice)
    db.session.commit()
    id = newInvoice.id
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/invoice/<id>', methods=['PUT'])
def invoice_update(id):
    data = request.json
    invoice = Invoice.query.filter(Invoice.id == id).one()
    invoice.customerId = data.get('customerId')
    invoice.applyNumber = data.get('applyNumber')
    invoice.applyDate = data.get('applyDate')
    invoice.expiry = data.get('expiry')
    invoice.title = data.get('title')
    invoice.memo = data.get('memo')
    invoice.remarks = data.get('remarks')
    invoice.isTaxExp = data.get('isTaxExp')
    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/invoice/<id>', methods=['DELETE'])
def invoice_destroy(id):
    invoice = Invoice.query.filter(Invoice.id == id).delete()
    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": ''})


# 請求書＿商品(Invoice_Items)
@app.route('/invoice_items', methods=['GET'])
def invoice_item_index():
    invoiceItems = Invoice_Item.query.all()
    return jsonify(Invoice_ItemSchema(many=True).dump(invoiceItems))


@app.route('/invoice_item/<id>', methods=['GET'])
def invoice_item_show(id):
    invoiceItemCount = Invoice_Item.query.filter(Invoice_Item.id == id).count()
    if invoiceItemCount:
        invoiceItem = Invoice_Item.query.filter(Invoice_Item.id == id).first()
        return jsonify(Invoice_ItemSchema().dump(invoiceItem))
    else:
        return jsonify([])


@app.route('/invoice_item', methods=['POST'])
def invoice_item_create():
    data = request.json
    newInvoiceItem = Invoice_Item(
        invoiceId=data.get('invoiceId'),
        itemId=data.get('itemId'),
        price=data.get('price'),
        count=data.get('count'),
    )
    db.session.add(newInvoiceItem)
    db.session.commit()
    id = newInvoiceItem.id
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/invoice_item/<id>', methods=['PUT'])
def invoice_item_update(id):
    data = request.json
    invoiceItem = Invoice_Item.query.filter(Invoice_Item.id == id).one()
    invoiceItem.invoiceId = data.get('invoiceId')
    invoiceItem.itemId = data.get('itemId')
    invoiceItem.price = data.get('price')
    invoiceItem.count = data.get('count')
    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/invoice_item/<id>', methods=['DELETE'])
def invoice_item_destroy(id):
    invoiceItem = Invoice_Item.query.filter(Invoice_Item.id == id).delete()
    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": ''})


# 見積書(Quotations)
@app.route('/quotations', methods=['GET'])
def quotation_index():
    quotations = Quotation.query.all()
    return jsonify(QuotationSchema(many=True).dump(quotations))


@app.route('/quotation/<id>', methods=['GET'])
def quotation_show(id):
    quotationCount = Quotation.query.filter(Quotation.id == id).count()
    if quotationCount:
        quotation = Quotation.query.filter(Quotation.id == id).first()
        return jsonify(QuotationSchema().dump(quotation))
    else:
        return jsonify([])


@app.route('/quotation', methods=['POST'])
def quotation_create():
    data = request.json
    newQuotation = Quotation(
        customerId=data.get('customerId'),
        applyNumber=data.get('applyNumber'),
        applyDate=data.get('applyDate'),
        expiry=data.get('expiry'),
        title=data.get('title'),
        memo=data.get('memo'),
        remarks=data.get('remarks'),
        isTaxExp=data.get('isTaxExp'),
    )
    db.session.add(newQuotation)
    db.session.commit()
    id = newQuotation.id
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/quotation/<id>', methods=['PUT'])
def quotation_update(id):
    data = request.json
    quotation = Quotation.query.filter(Quotation.id == id).one()
    quotation.customerId = data.get('customerId')
    quotation.applyNumber = data.get('applyNumber')
    quotation.applyDate = data.get('applyDate')
    quotation.expiry = data.get('expiry')
    quotation.title = data.get('title')
    quotation.memo = data.get('memo')
    quotation.remarks = data.get('remarks')
    quotation.isTaxExp = data.get('isTaxExp')
    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/quotation/<id>', methods=['DELETE'])
def quotation_destroy(id):
    quotation = Quotation.query.filter(Quotation.id == id).delete()
    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": ''})


# 見積書＿商品(Quotation_Items)
@app.route('/quotation_items', methods=['GET'])
def quotation_item_index():
    quotationItems = Quotation_Item.query.all()
    return jsonify(Quotation_ItemSchema(many=True).dump(quotationItems))


@app.route('/quotation_item/<id>', methods=['GET'])
def quotation_item_show(id):
    quotationItemCount = Quotation_Item.query.filter(
        Quotation_Item.id == id).count()
    if quotationItemCount:
        quotationItem = Quotation_Item.query.filter(
            Quotation_Item.id == id).first()
        return jsonify(Quotation_ItemSchema().dump(quotationItem))
    else:
        return jsonify([])


@app.route('/quotation_item', methods=['POST'])
def quotation_item_create():
    data = request.json
    newQuotationItem = Quotation_Item(
        quotationId=data.get('quotationId'),
        itemId=data.get('itemId'),
        price=data.get('price'),
        count=data.get('count'),
    )
    db.session.add(newQuotationItem)
    db.session.commit()
    id = newQuotationItem.id
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/quotation_item/<id>', methods=['PUT'])
def quotation_item_update(id):
    data = request.json
    quotationItem = Quotation_Item.query.filter(Quotation_Item.id == id).one()
    quotationItem.quotationId = data.get('quotationId')
    quotationItem.itemId = data.get('itemId')
    quotationItem.price = data.get('price')
    quotationItem.count = data.get('count')
    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/quotation_item/<id>', methods=['DELETE'])
def quotation_item_destroy(id):
    quotationItem = Quotation_Item.query.filter(
        Quotation_Item.id == id).delete()
    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": ''})


# メモ(Memos)
@app.route('/memos', methods=['GET'])
def memo_index():
    memos = Memo.query.all()
    return jsonify(MemoSchema(many=True).dump(memos))


@app.route('/memo/<id>', methods=['GET'])
def memo_show(id):
    memoCount = Memo.query.filter(Memo.id == id).count()
    if memoCount:
        memo = Memo.query.filter(Memo.id == id).first()
        return jsonify(MemoSchema().dump(memo))
    else:
        return jsonify([])


@app.route('/memo', methods=['POST'])
def memo_create():
    data = request.json
    newMemo = Memo(
        title=data.get('title'),
        content=data.get('content'),
    )
    db.session.add(newMemo)
    db.session.commit()
    id = newMemo.id
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/memo/<id>', methods=['PUT'])
def memo_update(id):
    data = request.json
    memo = Memo.query.filter(Memo.id == id).one()

    memo.title = data.get('title')
    memo.content = data.get('content')

    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/memo/<id>', methods=['DELETE'])
def memo_destroy(id):
    memo = Memo.query.filter(Memo.id == id).delete()
    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": ''})


# 単位(Units)
@app.route('/units', methods=['GET'])
def unit_index():
    units = Unit.query.all()
    return jsonify(UnitSchema(many=True).dump(units))


@app.route('/unit/<id>', methods=['GET'])
def unit_show(id):
    unitCount = Unit.query.filter(Unit.id == id).count()
    if unitCount:
        unit = Unit.query.filter(Unit.id == id).first()
        return jsonify(UnitSchema().dump(unit))
    else:
        return jsonify([])


@app.route('/unit', methods=['POST'])
def unit_create():
    data = request.json
    newUnit = Unit(
        unitName=data.get('unitName'),
    )
    db.session.add(newUnit)
    db.session.commit()
    id = newUnit.id
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/unit/<id>', methods=['PUT'])
def unit_update(id):
    data = request.json
    unit = Unit.query.filter(Unit.id == id).one()

    unit.unitName = data.get('unitName')

    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": data})


@app.route('/unit/<id>', methods=['DELETE'])
def unit_destroy(id):
    unit = Unit.query.filter(Unit.id == id).delete()
    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": ''})


# 設定(Setting)
@app.route('/setting', methods=['GET'])
def setting_index():
    setting = Setting.query.all()
    return jsonify(SettingSchema(many=True).dump(setting))


@app.route('/setting', methods=['PUT'])
def setting_update():
    data = request.json
    setting = Setting.query.filter(Setting.id == 1).one()

    setting.companyName = data.get('companyName')
    setting.representative = data.get('representative')
    setting.postNumber = data.get('postNumber')
    setting.address = data.get('address')
    setting.telNumber = data.get('telNumber')
    setting.faxNumber = data.get('faxNumber')
    setting.url = data.get('url')
    setting.email = data.get('email')
    setting.logoFilePath = data.get('logoFilePath')
    setting.stampFilePath = data.get('stampFilePath')
    setting.isDisplayQuotationLogo = data.get('isDisplayQuotationLogo')
    setting.isDisplayInvoiceLogo = data.get('isDisplayInvoiceLogo')
    setting.isDisplayDeliveryLogo = data.get('isDisplayDeliveryLogo')
    setting.isDisplayQuotationStamp = data.get('isDisplayQuotationStamp')
    setting.isDisplayInvoiceStamp = data.get('isDisplayInvoiceStamp')
    setting.isDisplayDeliveryStamp = data.get('isDisplayDeliveryStamp')

    db.session.commit()
    return jsonify({"result": "OK", "id": id, "data": data})


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5010)