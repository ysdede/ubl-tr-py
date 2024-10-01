# UBL-TR-PY: Python için UBL e-Fatura Oluşturucu

UBL-TR-PY, Türkiye UBL (Universal Business Language) e-fatura standartlarına uygun SOAP/XML belgeleri oluşturmayı kolaylaştıran bir Python modülüdür.  
Bu kütüphane, XML öğelerini Python nesneleri olarak tanımlayarak karmaşık XML işlemlerini izole eder ve uyumlu e-faturaların daha kolay oluşturulmasını sağlar.

## Özellikler

- Python nesneleri kullanarak UBL e-faturaları oluşturma
- Gelir İdaresi Başkanlığı (GİB) e-fatura entegrasyon dokümanları ve XML şemalarına uyumlu
- Tedarikçi/müşteri bilgileri, ödeme koşulları, vergi toplamları ve fatura kalemleri gibi çeşitli fatura bileşenlerini destekler


# UBL-TR-PY: Turkish UBL e-Invoice Generator for Python

UBL-TR-PY is a Python module that simplifies the creation of SOAP/XML documents compatible with Turkish UBL (Universal Business Language) e-invoice standards. This library helps isolate complex XML processing by defining XML elements as Python objects, making it easier to generate compliant e-invoices.

## Features

- Create UBL e-invoices using Python objects
- Compliant with Turkish Revenue Administration (GİB) e-invoice integration documents and XML schemas
- Supports various invoice components such as supplier/customer information, payment terms, tax totals, and invoice lines


## Örnek kullanım


```python
from rs_ubl_tr.UBLInvoice import (
    UBLInvoice,
    ItemIdentification,
    Price,
    PartyData,
    PartyIdentification,
    PostalAddress,
    PartyTaxScheme,
    Contact,
    PayeeFinancialAccount,
    PaymentMeans,
    PaymentTerms,
    TaxTotal,
    TaxSubtotal,
    TaxCategory,
    MonetaryTotal,
    InvoicedQuantity,
    Item,
    InvoiceLine,
    TaxScheme
)

# Boş bir fatura oluştur
ubl_doc = UBLInvoice()

# Zorunlu alanlar (versiyon bilgisi vb. sabit veriler)
ubl_doc.add_ubl_extension()
ubl_doc.add_ubl_version_id()
ubl_doc.add_customisation_id()

print(type(ubl_doc))

ubl_doc.add_profile_id('TEMELFATURA')
ubl_doc.add_id('INV2024050512346')          # Invoice number, Üç haneli alfanumerik birim kod ile 13 haneli müteselsil numara
ubl_doc.add_copy_indicator('false')         # Kopya (nüsha) fatura mı?
ubl_doc.add_uuid()
ubl_doc.add_issue_date('2024-05-05')        # Fatura tarihi
ubl_doc.add_issue_time('12:34:56')          # Fatura saati
ubl_doc.add_invoice_type_code('SATIS')      # Fatura tipi
ubl_doc.add_note('Fatura notu')             # Fatura notu
ubl_doc.add_document_currency_code('TRY')   # Fatura döviz cinsi
ubl_doc.add_line_count_numeric('1')         # Fatura satır sayısı (invoice line), otomatik olarak sayabilir ve doldurabiliriz.
ubl_doc.add_despatch_document_reference('IRS2024050510346', '2024-05-05') # İrsaliye numarası, irsaliye tarihi, seçimli.
```

İmzalayan entegratör bilgisi. Diğer entegratörler eklenebilir.
```python
from rs_ubl_tr.UBLInvoice import KolaysoftSignature
kolaysoft_party_info = KolaysoftSignature()
ubl_doc.add_signature(signatory=kolaysoft_party_info)
```

Partydata faturayı kesen ve alan için aynı sınıfı kullanır.

Satıcı (fatura oluşturan) bilgileri:
```python
AccountingSupplierParty = PartyData()
AccountingSupplierParty.PartyIdentification = PartyIdentification(schemeID='VKN', value='12345678900')
AccountingSupplierParty.PartyName = 'GÖTÜR LTD. ŞTİ.'

AccountingSupplierParty.PostalAddress = PostalAddress(ID='1234567890', StreetName='Papatya Caddesi Yasemin Sokak',
                                                      BuildingNumber='21', CitySubdivisionName='Beşiktaş',
                                                      CityName='İstanbul', PostalZone='34100', Country='Türkiye')

# We can modify PostalAddress after initialization:
AccountingSupplierParty.PostalAddress.PostalZone = '34400'

AccountingSupplierParty.PartyTaxScheme = PartyTaxScheme(Name='Büyük Mükellefler')
AccountingSupplierParty.Contact = Contact(ElectronicMail='info@gtr.mv', Telephone='555555555', Telefax='666666666')

ubl_doc.add_accounting_supplier_party(AccountingSupplierParty)
```

Müşteri (alıcı) bilgileri:
```python
AccountingCustomerParty = PartyData()
AccountingCustomerParty.PartyIdentification = PartyIdentification(schemeID='VKN', value='0000510000')
AccountingCustomerParty.PartyName = 'SAGATGRUP YAZILIM VE BİLİŞİM TEKNOLOJİLERİ TİCARET LİMİTED ŞİRKETİ'
AccountingCustomerParty.PostalAddress = PostalAddress(CitySubdivisionName='Çankaya', CityName='Ankara',
                                                      Country='Türkiye')
AccountingCustomerParty.PartyTaxScheme = PartyTaxScheme(TaxScheme=TaxScheme(Name='DOĞANBEY VERGİ DAİRESİ MÜD.'))
AccountingCustomerParty.Contact = None  # Default None, belirtilmese de olur.

ubl_doc.add_accounting_customer_party(AccountingCustomerParty)
```

```python
paymentmeans = PaymentMeans(PaymentMeansCode='1', PaymentDueDate='2024-05-25',
                            PaymentChannelCode='1',
                            PayeeFinancialAccount=PayeeFinancialAccount(ID='1',
                                                                        CurrencyCode='TRY',
                                                                        PaymentNote='İST Bank Şişli Şubesi'))
ubl_doc.add_paymentmeans(paymentmeans)

p_terms = PaymentTerms(Note='Fatura düzenlenme tarihinden itibaren 20 gün içerisinde ödenecektir.',
                       PaymentDueDate='2024-02-25')
ubl_doc.add_paymentterms(p_terms)

inv_tax_scheme = TaxScheme(Name='GERÇEK USULDE KATMA DEĞER VERGİSİ', TaxTypeCode='0015')
inv_tax_category = TaxCategory(Name='GERÇEK USULDE KATMA DEĞER VERGİSİ', TaxScheme=inv_tax_scheme)
inv_tax_total_tax_subtotal = TaxSubtotal(TaxableAmount='1', TaxAmount='0.18', CalculationSequenceNumeric='1', Percent='18',
                                         TaxCategory=inv_tax_category)
tax_total = TaxTotal(TaxAmount='0.18', TaxSubtotal=inv_tax_total_tax_subtotal)
ubl_doc.add_taxtotal(tax_total)

monetary_total = MonetaryTotal(LineExtensionAmount='1.00', TaxExclusiveAmount='1.00',
                               TaxInclusiveAmount='1.18', AllowanceTotalAmount='0.00', PayableAmount='1.18')

ubl_doc.add_legalmonetarytotal(monetary_total)

line_1_tax_scheme = TaxScheme(Name='GERÇEK USULDE KATMA DEĞER VERGİSİ', TaxTypeCode='0015')
line_1_tax_cat = TaxCategory(TaxScheme=line_1_tax_scheme)
line_1_taxsub = TaxSubtotal(TaxableAmount='1', TaxAmount='0.18', CalculationSequenceNumeric='1', Percent='18',
                            TaxCategory=line_1_tax_cat)
line_1_sellers_item_id = ItemIdentification(ID='STK000006DMDE')

line_1_item = Item(Name='Mal ya da hizmetin adı', SellersItemIdentification=line_1_sellers_item_id)

line_1_taxtotal = TaxTotal(TaxAmount='0.18', TaxSubtotal=line_1_taxsub)
line_1_inv_qty = InvoicedQuantity(UnitCode='C62', Qty='1')

line_1_price = Price(PriceAmount='1.00')
# ID                      Zorunlu(1)      : Kalem sıra numarası girilir.
# Item                    Zorunlu(1)      : Mal/hizmet hakkında bilgiler buraya girilir. Bknz. Item.
# Price                   Zorunlu(1)      : Mal/hizmet birim fiyatı hakkında bilgiler buraya girilir. Bknz. Price.
# InvoicedQuantity        Zorunlu(1)      : Mal/hizmet miktarı birimi ile birlikte girilir. Bknz. Kod Listeleri.
# LineExtensionAmount     Zorunlu(1)      : Mal/hizmet miktarı ile Mal/hizmet birim fiyatının çarpımı ile bulunan tutardır (varsa iskonto düşülür).
inv_line_1 = InvoiceLine(ID='1', Item=line_1_item, Price=line_1_price, InvoicedQuantity=line_1_inv_qty, LineExtensionAmount='1.00',
                         TaxTotal=line_1_taxtotal)

ubl_doc.add_invoice_line(inv_line_1)
```

Üretilen xml içeriğini inceleyebiliriz:
```python
# print(ubl_doc.xml())
# or:
with open('test.xml', 'w') as f:
    f.write(ubl_doc.xml())
```

Entegratöre iletebilirsiniz (sendInvoice metodu temsili gösterilmiştir):
```python
response = sendInvoice(username, password, xmlContent=ubl_doc.xml(), sourceUrn=sourceUrn, destinationUrn=destinationUrn,
documentDate=ubl_doc.issue_date, documentId=ubl_doc.id, documentUUID=ubl_doc.uuid)
```

## Documentation

For detailed usage instructions and API reference, please visit our [documentation](https://github.com/ysdede/ubl-tr-py/docs).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Gelir İdaresi Başkanlığı (GİB) belgelerine ulaşmak için: https://ebelge.gib.gov.tr/efaturamevzuat.html
