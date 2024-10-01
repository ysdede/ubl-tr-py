# MIT License

# Copyright (c) 2023 Yunus S. Dede

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from lxml import etree
import os
from typing import Union, List, Any, Optional

module_path = os.path.dirname(__file__)
parent_path = os.path.dirname(module_path)
xsd_path = os.path.join(parent_path, "UBLTR_1.2.1_Paketi", "xsdrt", "maindoc", "UBL-Invoice-2.1.xsd")
schema_doc = etree.parse(xsd_path)
schema = etree.XMLSchema(schema_doc)


class Country:
    """
    Ülke bilgisi girilecektir.
    2.2.12 Country Ülke

    IdentificationCode  Seçimli(0..1):  Ülkeleri tanımlamak için kullanılan kodlu elemandır.
                                        Bu eleman değer kümesini ISO 3166-1-alpha-2 Ülke Kodları listesinden almalıdır. Bknz.Kod Listeleri
    Name                Zorunlu(1)   :  Ülkeleri tanımlamak için kullanılan metin elemanıdır.

    Örnek
    <cac:Country>
        <cbc:IdentificationCode>TR</cbc:IdentificationCode>
        <cbc:Name>Türkiye</cbc:Name>
    </cac:Country>
    """
    def __init__(self, Name: str, IdentificationCode: str = None):
        self.Name = Name
        self.IdentificationCode = IdentificationCode

class Address:
    """
    Bu eleman adres bilgilerinin tanımlanmasında kullanılacaktır.
    2.2.1 Adress Adres | UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 12/81

    Kullanım
    ID                      Seçimli(0..1) : Mahalle, meydan, bulvar, cadde, sokak ve küme evlere karşılık gelecek şekilde,
                                            standart sayısal eşdeğer olarak TÜİK tarafından verilmiş olan “sabit tanımlama numarası” girilebilecektir.
    Postbox                 Seçimli(0..1) : Posta Kutusu girilecektir.
    Room                    Seçimli(0..1) : İç kapı numarası girilecektir.
    StreetName              Seçimli(0..1) : Meydan/bulvar/cadde/sokak/küme evler/site adı bilgileri girilecektir.
    BlockName               Seçimli(0..1) : Blok adı girilebilecektir.
    BuildingName            Seçimli(0..1) : Bina girilebilecektir.
    BuildingNumber          Seçimli(0..n) : Bina veya bloğa ait dış kapı numarası girilecektir.
    CitySubdivisionName     Zorunlu(1)    : İlçe/semt adı bilgileri girilecektir.
    CityName                Zorunlu(1)    : İl adı girilecektir.
    PostalZone              Seçimli(0..1) : Posta kod numarası girilecektir.
    Region                  Seçimli(0..1) : Kasaba/köy/mezra/mevkii bilgileri girilecektir.
    District                Seçimli(0..1) : Mahalle adı girilecektir.
    Country                 Zorunlu(1)    : Bknz. Country

    Örnek
    <cac:PostalAddress>
        <cbc:ID>2806632739</cbc:ID>
        <cbc:StreetName> Selvi Caddesi Sedir Sokak</cbc:StreetName>
        <cbc:BuildingNumber>75/A</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Kızılay</cbc:CitySubdivisionName>
        <cbc:CityName>Ankara</cbc:CityName>
        <cbc:PostalZone>06100</cbc:PostalZone>
        <cbc:District>Ihlamur Mahallesi</cbc:District>
        <cac:Country>
            <cbc:Name>Türkiye</cbc:Name>
        </cac:Country>
    </cac:PostalAddress>
    """

    def __init__(self, id: str = None, postbox: str = None, room: str = None, street_name: str = None, block_name: str = None,
                building_name: str = None, building_number: Union[str, List[str]] = None, city_subdivision_name: str = None,
                city_name: str = None, postal_zone: str = None, region: str = None, district: str = None, country: Country = None):
        self.id = id
        self.postbox = postbox
        self.room = room
        self.street_name = street_name
        self.block_name = block_name
        self.building_name = building_name
        self.building_number = building_number
        self.city_subdivision_name = city_subdivision_name
        self.city_name = city_name
        self.postal_zone = postal_zone
        self.region = region
        self.district = district
        self.country = country

class Location:
    """
    2.2.35 Location Konum Mekan bilgisi girilir. | UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 46/81

    ID      Seçimli(0..1) : Mekanı tanımlamak için kullanılır (örneğin GLN numarası)
    Address Seçimli(0..1) : Addres bilgisini tutar. Bknz. Address.

    Örnek
    <cac:Location>
        <cbc:ID>2806632739</cbc:ID>
        <cac:Address>
            <cbc:ID>2806632739</cbc:ID>
            <cbc:StreetName>Papatya Caddesi Yasemin Sokak</cbc:StreetName>
            <cbc:BuildingNumber>21</cbc:BuildingNumber>
            <cbc:CitySubdivisionName>Beşiktaş</cbc:CitySubdivisionName>
            <cbc:CityName>İstanbul</cbc:CityName>
            <cbc:PostalZone>34100</cbc:PostalZone>
            <cac:Country>
                <cbc:Name>Türkiye</cbc:Name>
            </cac:Country>
        </cac:Address>
    </cac:Location>
    """

    def __init__(self, id: str = None, address: Address = None):
        self.id = id
        self.address = address

class PostalAddress:
    """
    Bu eleman adres bilgilerinin tanımlanmasında kullanılacaktır.

    2.2.1 Adress Adres
    Elemanlar ve Kullanım Kardinaliteleri
                                            Seçimli(0..1) : ID
                                            Seçimli(0..1) : Postbox
                                            Seçimli(0..1) : Room
                                            Seçimli(0..1) : StreetName
                                            Seçimli(0..1) : BlockName
                                            Seçimli(0..1) : BuildingName
                                            Seçimli(0..n) : BuildingNumber
                                            Zorunlu(1): CitySubdivisionName
                                            Zorunlu(1): CityName
                                            Seçimli(0..1) : PostalZone
                                            Seçimli(0..1) : Region
                                            Seçimli(0..1) : District
                                            Zorunlu(1): Country
    Kullanım
    ID: Mahalle, meydan, bulvar, cadde, sokak ve küme evlere karşılık gelecek şekilde,
            standart sayısal eşdeğer olarak TÜİK tarafından verilmiş olan “sabit tanımlama numarası” girilebilecektir.
    Postbox: Posta Kutusu girilecektir.
    Room: İç kapı numarası girilecektir.
    StreetName: Meydan/bulvar/cadde/sokak/küme evler/site adı bilgileri girilecektir.
    BlockName: Blok adı girilebilecektir.
    BuildingName: Bina girilebilecektir.
    BuildingNumber: Bina veya bloğa ait dış kapı numarası girilecektir.
    CitySubdivisionName: İlçe/semt adı bilgileri girilecektir.
    CityName: İl adı girilecektir.
    PostalZone: Posta kod numarası girilecektir.
    Region: Kasaba/köy/mezra/mevkii bilgileri girilecektir.
    District: Mahalle adı girilecektir.
    Country: Bknz. Country

    Örnek
        <cac:PostalAddress>
            <cbc:ID>2806632739</cbc:ID>
            <cbc:StreetName> Selvi Caddesi Sedir Sokak</cbc:StreetName>
            <cbc:BuildingNumber>75/A</cbc:BuildingNumber>
            <cbc:CitySubdivisionName>Kızılay</cbc:CitySubdivisionName>
            <cbc:CityName>Ankara</cbc:CityName>
            <cbc:PostalZone>06100</cbc:PostalZone>
            <cbc:District>Ihlamur Mahallesi</cbc:District>
            <cac:Country>
                <cbc:Name>Türkiye</cbc:Name>
            </cac:Country>
        </cac:PostalAddress>
    """
    def __init__(self, ID: str = None, Postbox: str = None, Room: str = None, StreetName: str = None,
                BlockName: str = None, BuildingName: str = None, BuildingNumber: str = None,
                CitySubdivisionName: str = None, CityName: str = None, PostalZone: str = None,
                Region: str = None, District: str = None, Country: Union[Country, str] = None):
        self.id = ID
        self.postbox = Postbox
        self.room = Room
        self.street_name = StreetName
        self.block_name = BlockName
        self.building_name = BuildingName
        self.building_number = BuildingNumber
        self.city_subdivision_name = CitySubdivisionName
        self.city_name = CityName
        self.postal_zone = PostalZone
        self.region = Region
        self.district = District
        self.country = Country

class TaxScheme:
    """
    Bu eleman aracılığıyla vergi dairesi ile ilgili bilgiler verilebileceği gibi vergi ile ilgili bilgiler de verilebilir.
    Bu elemanın farklı kullanımları için ilgili belge açıklamalarına bakınız.

    2.2.59 TaxScheme Vergi Bilgileri

    ID          Seçimli(0..1):  Vergilendirme şemasının ID bilgisi girilir.
    Name        Seçimli(0..1):  Bu eleman “Party” elemanı içerisinde kullanıldığında vergi dairesi adını içermektedir.
                                Diğer elemanlar içerisinde kullanımında Vergi Kod listesinde henüz yer almayan bir verginin
                                söz konusu olması durumunda verginin adı girilecektir. Kontrolü Schematron kuralları ile yapılacaktır.
    TaxTypeCode Seçimli(0..1):  Vergi Tipi Kodu girilecektir. Bknz. Kod listeleri.

    Örnek
            Örnek 1:
                <cac:TaxScheme>
                    <cbc:TaxTypeCode>0015</cbc:TaxTypeCode>
                </cac:TaxScheme>

            Örnek 2:
                <cac:TaxScheme>
                    <cbc:Name>[KOD LİSTESİ İÇİNDE OLMAYAN VERGİ ADI]</cbc:Name>
                </cac:TaxScheme>

            Örnek 3:
                <cac:TaxScheme>
                    <cbc:Name>[ VERGİ DAİRESİ ADI]</cbc:Name>
                </cac:TaxScheme>
    """

    def __init__(self, ID: str = None, Name: str = None, TaxTypeCode: str = None):
        self.ID = ID
        self.Name = Name
        self.TaxTypeCode = TaxTypeCode

class PartyTaxScheme:
    """
    Bu eleman aracılığıyla Tarafın (Party) vergi dairesi ile ilgili bilgiler verilir.

    2.2.43 PartyTaxScheme Taraf Mükellefiyet Bilgileri

    RegistrationName    Seçimli(0..1): İhracat faturasında ilgili ülkedeki kurumun resmi ünvanı yazılır.
    CompanyID           Seçimli(0..1): İhracat faturasında ilgili ülkedeki kurumun vergi kayıt kodu yazılır.
    TaxScheme/Name” elemanı (Zorunlu(1)): bu kullanım için zorunludur. Vergi Dairesi adı “TaxScheme/Name” içine
    metin olarak girilmesi gerekir. XSD’de “TaxScheme/Name” seçimli olarak tanımlanmasına rağmen bu
    zorunluluk kontrolü ikinci faz doğrulamada Schematron kuralları ile gerçekleştirilecektir. Bknz: TaxScheme

    Örnek
            <cac:PartyTaxScheme>
                <cac:TaxScheme>
                    <cbc:Name> Büyük Mükellefler Vergi Dairesi</cbc:Name>
                </cac:TaxScheme>
            </cac:PartyTaxScheme>

    """

    def __init__(self, RegistrationName: str = None, CompanyID: str = None, TaxScheme: Union[TaxScheme, str] = None):
        self.registration_name = RegistrationName
        self.company_id = CompanyID
        self.tax_scheme = TaxScheme

class Communication:
    """
    Her türlü alternatif iletişim kanalının tanımlanmasında kullanılacaktır.
    2.2.9 Communication İletişim

    ChannelCode Zorunlu(1)      : Bu eleman için UN/EDIFACT 3155 İletişim Numarası Kod Listesi kullanılmalıdır. Bknz. Kod Listeleri.
    Channel     Seçimli(0..1)   : Bu eleman metin olarak kanal adı için kullanılacaktır.
    Value       Zorunlu(1)      : Bu eleman iletişim adresini metin olarak tutar.

    Örnek
            <cac:OtherCommunication>
                <cbc:ChannelCode>TL</cbc:ChannelCode>
                <cbc:Channel>Telex</cbc:Channel>
                <cbc:Value>1234567</cbc:Value>
            </cac:OtherCommunication>
    """

    def __init__(self, ChannelCode: str, Channel: str = None, Value: str = None):
        self.channel_code = ChannelCode
        self.channel = Channel
        self.value = Value

class Contact:
    """
    Bu elemana irtibat bilgileri yazılabilecektir.
    2.2.10 Contact İrtibat

    ID                  Seçimli(0..1):  İrtibatın numara bilgisi yazılabilir.
    Name                Seçimli(0..1):  İrtibatın ismi metin olarak yazılabilir.
    Telephone           Seçimli(0..1):  Telefon numarası metin olarak girilecektir.
    Telefax             Seçimli(0..1):  Fax numarası metin olarak girilecektir.
    ElectronicMail      Seçimli(0..1):  Elektronik posta adresi metin olarak girilecektir.
    Note                Seçimli(0..1):  Serbest metin açıklama girilebilecektir.
    OtherCommunication  Seçimli(0..n):  Başka iletişim kanalı veya ilave telefon, fax ve elektronik posta
                                        kullanılıyor ise bu eleman kanalın tanımlanmasında kullanılacaktır. Bknz. Communication.

    Örnek
            <cac:Contact>
                <cbc:Telephone>(312) 621 11112</cbc:Telephone>
                <cbc:Telefax>(312) 621 10102</cbc:Telefax>
                <cbc:ElectronicMail>bb@bb.com.tr</cbc:ElectronicMail>
            </cac:Contact>
    """
    def __init__(self, ID: str = None, Name: str = None, Telephone: str = None, Telefax: str = None,
                    ElectronicMail: str = None, Note: str = None, OtherCommunication: List[Communication] = None):
        self.id = ID
        self.name = Name
        self.telephone = Telephone
        self.telefax = Telefax
        self.electronic_mail = ElectronicMail
        self.note = Note
        self.other_communication = OtherCommunication


class Party:
    """
    Tarafları (kurum ve şahıslar) tanımlamak için kullanılır.
    2.2.41 Party Taraf

    WebsiteURI                  Seçimli(0..1):  Tarafın web sayfası adresi metin olarak girilir.
    IndustryClassificationCode  Seçimli(0..1):  Tarafın ana faaliyet (NACE) kodu girilecektir.
    PartyIdentification         Zorunlu(1..n):  Tarafın vergi kimlik numarası veya TC kimlik numarası metin olarak girilir.
                                                UBL-TR’de “PartyIdentification/ID” elemanının “schemeID” attribute’u zorunludur.
                                                Bunun kontrolleri XSD şeması seviyesinde değil, ikinci aşama Schematron kural seviyesinde yapılacaktır.
                                                “schemeID” vergi kimlik numarası için “VKN” ve TC kimlik numarası için “TCKN” değerlerini alabilir. Bknz. Kod Listeleri.
    PartyName                   Seçimli(0..1):  Taraf eğer kurum ise kurum ismi bu elemana metin olarak girilir.
    PostalAddress               Zorunlu(1)   :  Tarafın adresi girilir. Bknz. Address.
    PhysicalLocation            Seçimli(0..1):  Tarafın var ise depo bilgileri girilir.
    PartyTaxScheme              Seçimli(0..1):  Tarafın vergi kimlik numarası girilmişse bu alana vergi dairesi adı girilir. Bknz. PartyTaxScheme.
    PartyLegalEntity            Seçimli(0..n):  Tarafın diğer kayıtlı olduğu yerlerin bilgileri ve kayıtlı olduğu yerlerdeki kayıt numaraları detaylı olarak girilecektir. Bknz. PartyLegalEntity.
    Contact                     Seçimli(0..1):  Tarafın iletişim bilgileri girilir. Bknz. Contact.
    Person                      Seçimli(0..1):  Taraf eğer şahıssa bu eleman kullanılır. Bknz. Person.
    AgentParty                  Seçimli(0..1):  Tarafın şubesine ait bilgiler bu elemana girilir. Departman bilgileri AgentParty’nin içindeki AgentParty’e yazılabilir.

    Olası parametreler:
        - PartyIdentification/ID schemeID: “PartyIdentification/ID” elemanının “schemeID” attribute’u zorunludur.


    Örnek
    <cac:Party>
        <cbc:WebsiteURI>http://www.aaa.com.tr/</cbc:WebsiteURI>
        <cac:PartyIdentification>
            <cbc:ID schemeID="VKN">1288331521</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
            <cbc:Name>AAA AnonimŞirketi</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
            <cbc:ID>1234567890</cbc:ID>
            <cbc:StreetName>Papatya Caddesi Yasemin Sokak</cbc:StreetName>
            <cbc:BuildingNumber>21</cbc:BuildingNumber>
            <cbc:CitySubdivisionName>Beşiktaş</cbc:CitySubdivisionName>
            <cbc:CityName>İstanbul</cbc:CityName>
            <cbc:PostalZone>34100</cbc:PostalZone>
            <cac:Country>
                <cbc:Name>Türkiye</cbc:Name>
            </cac:Country>
        </cac:PostalAddress>
        <cac:PhysicalLocation>
            <cbc:ID>Depo Şube</cbc:ID>
            <cac:Address>
                <cbc:ID>1234567895</cbc:ID>
                <cbc:StreetName>Ihlamur Mahallesi Selvi Caddesi Sedir Sokak</cbc:StreetName>
                <cbc:BuildingNumber>79/A</cbc:BuildingNumber>
                <cbc:CitySubdivisionName>Balgat</cbc:CitySubdivisionName>
                <cbc:CityName>Ankara</cbc:CityName>
                <cbc:PostalZone>06800</cbc:PostalZone>
                <cac:Country>
                    <cbc:Name>Türkiye</cbc:Name>
                </cac:Country>
            </cac:Address>
        </cac:PhysicalLocation>
        <cac:PartyTaxScheme>
            <cac:TaxScheme>
                <cbc:Name>Büyük Mükellefler</cbc:Name>
            </cac:TaxScheme>
        </cac:PartyTaxScheme>
        <cac:Contact>
            <cbc:Telephone>(212) 925 51515</cbc:Telephone>
            <cbc:Telefax>(212) 925505015</cbc:Telefax>
            <cbc:ElectronicMail>aa@aaa.com.tr</cbc:ElectronicMail>
        </cac:Contact>
        <cac:Person>
            <cbc:FirstName>Cemal</cbc:FirstName>
            <cbc:FamilyName>Temiz</cbc:FamilyName>
        </cac:Person>
    </cac:Party>

    """

    def __init__(self, party_identification_id, party_name, postal_address, physical_location, party_tax_scheme, party_legal_entity, contact, person, agent_party):
        self.party_identification_id = party_identification_id
        self.party_name = party_name
        self.postal_address = postal_address
        self.physical_location = physical_location
        self.party_tax_scheme = party_tax_scheme
        self.party_legal_entity = party_legal_entity
        self.contact = contact
        self.person = person
        self.agent_party = agent_party

class CorporateRegistrationScheme:
    """
    Kurumun kayıtlı olduğu organizasyon hakkında bilgileri tutar. Örneğin sanayi odası veya ticaret odası.
    2.2.11 CorporateRegistrationScheme Kurumsal Sicil Şeması @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 20/81

    ID                              Seçimli(0..1): Kayıt yeri numarası girilebilir.
    Name                            Seçimli(0..1): Kayıt yeri ismi girilebilir.
    CorporateRegistrationTypeCode   Seçimli(0..1): Kayıt yeri tipi girilebilir.
    JuridictionRegionAddress        Seçimli(0..n): Kayıt yeri adresi girilebilir. Bknz. Address

    Örnek
    <cac:CorporateRegistrationScheme>
        <cbc:Name>ANKARA TICARET ODASI</cbc:Name>
        <cac:JurisdictionRegionAddress>
            <cbc:ID>2806632739</cbc:ID>
            <cbc:CitySubdivisionName>Söğütözü</cbc:CitySubdivisionName>
            <cbc:CityName>Ankara</cbc:CityName>
            <cac:Country>
                <cbc:Name>Türkiye</cbc:Name>
            </cac:Country>
        </cac:JurisdictionRegionAddress>
    </cac:CorporateRegistrationScheme>
    """

    def __init__(self, id: str = None, name: str = None, corporateRegistrationTypeCode: str = None, juridictionRegionAddress: Address = None):
        self.id = id
        self.name = name
        self.corporateRegistrationTypeCode = corporateRegistrationTypeCode
        self.juridictionRegionAddress = juridictionRegionAddress

class PartyLegalEntity:
    """
    Tarafın sicil bilgilerini veya merkez bilgilerini içerir.
    2.2.42 PartyLegalEntity Taraf Sicil Bilgileri @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 54/81

    RegistrationName                Seçimli(0..1): Kayıt ismi girilir.
    CompanyID                       Seçimli(0..1): Kayıt numarası girilir.
    RegistrationDate                Seçimli(0..1): Kayıt tarihi girilir.
    SolePrioprietorshipIndicator    Seçimli(0..1): Tek bir kişiye ait olup olmadığını belirtir.
    CorporateStockAmount            Seçimli(0..1): Ödenmiş sermaye bilgisi girilir.
    FullyPaidSharesIndicator        Seçimli(0..1): Şirketin halka açık olup olmadığının göstergesi girilebilir.
    CorporateRegistrationScheme     Seçimli(0..1): Kayıtlı olduğu yerin bilgilerini içerir. Bknz. CorporateRegistrationScheme
    HeadOfficeParty                 Seçimli(0..1): Merkez bilgilerini içerir. Bknz. Party

    Örnek
    <cac:PartyLegalEntity>
    <cbc:CompanyID>111111</cbc:CompanyID>
    <cac:CorporateRegistrationScheme>
        <cbc:Name>ANKARA TICARET ODASI</cbc:Name>
        <cac:JurisdictionRegionAddress>
            <cbc:ID>2806632739</cbc:ID>
            <cbc:CitySubdivisionName>Söğütözü</cbc:CitySubdivisionName>
            <cbc:CityName>Ankara</cbc:CityName>
            <cac:Country>
                <cbc:Name>Türkiye</cbc:Name>
            </cac:Country>
        </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
    </cac:PartyLegalEntity>

    <cac:PartyLegalEntity>
        <cac:HeadOfficeParty>
        <cac:PartyIdentification>
        <cbc:ID schemeID="VKN">111111111</cbc:ID>
        </cac:PartyIdentification>
        <cac:PostalAddress>
        <cbc:ID>2806632739</cbc:ID>
        <cbc:StreetName>111 sk. </cbc:StreetName>
        <cbc:BuildingNumber>18</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Çiğli</cbc:CitySubdivisionName>
        <cbc:CityName>İzmir</cbc:CityName>
        <cac:Country>
        <cbc:Name>Türkiye</cbc:Name>
        </cac:Country>
        </cac:PostalAddress>
        </cac:HeadOfficeParty>
    </cac:PartyLegalEntity>
    """

    def __init__(self, registrationName: str = None, companyID: str = None, registrationDate: str = None,
                solePrioprietorshipIndicator: bool = None, corporateStockAmount: float = None,
                fullyPaidSharesIndicator: bool = None, corporateRegistrationScheme: CorporateRegistrationScheme = None,
                headOfficeParty: Party = None):

        self.registrationName = registrationName
        self.companyID = companyID
        self.registrationDate = registrationDate
        self.solePrioprietorshipIndicator = solePrioprietorshipIndicator
        self.corporateStockAmount = corporateStockAmount
        self.fullyPaidSharesIndicator = fullyPaidSharesIndicator
        self.corporateRegistrationScheme = corporateRegistrationScheme
        self.headOfficeParty = headOfficeParty

class PartyIdentification:
    """
    Tarafın vergi kimlik numarası veya TC kimlik numarası metin olarak girilir.
    UBL-TR’de “PartyIdentification/ID” elemanının “schemeID” attribute’u zorunludur.
    Bunun kontrolleri XSD şeması seviyesinde değil, ikinci aşama Schematron kural seviyesinde yapılacaktır.
    “schemeID” vergi kimlik numarası için “VKN” ve TC kimlik numarası için “TCKN” değerlerini alabilir.
    Bknz. Kod Listeleri.

    UBL TR Ortak Elemanlarda tanımlanmamış.
    """
    def __init__(self, schemeID: str = None, value: str = None):
        self.schemeID = schemeID
        self.value = value


class PartyData:
    WebsiteURI: str = None
    PartyIdentification: PartyIdentification
    PartyName: str = None
    PostalAddress: PostalAddress = None     # type: ignore
    PartyTaxScheme: PartyTaxScheme = None   # type: ignore
    Contact: Contact = None                 # type: ignore

class FinancialInstitution:
    """
    Banka bilgisi girilebilir.
    2.2.26 FinancialInstitution Finansal Kurum

    Name    Seçimli(0..1) : Banka ismi girilebilir.

    Örnek
                <cac:FinancialInstitution>
                    <cbc:Name>Ziraat Bankası</cbc:Name>
                </cac:FinancialInstitution>
    """

    def __init__(self, Name: str = None):
        self.Name = Name


class Branch:
    """
    Şube bilgisi girilir. (Banka)
    2.2.7 Branch Şube

    Name                    Seçimli(0..1): Şube adı girilir.
    FinancialInstitution    Seçimli(0..1): Banka bilgisi girilir. Bknz. FinancialInstitution

    Örnek
                <cac:FinancialInstitutionBranch>
                    <cbc:Name>ODTÜ Şubesi</cbc:Name>
                    <cac:FinancialInstitution>
                        <cbc:Name>Ziraat Bankası</cbc:Name>
                    </cac:FinancialInstitution>
                </cac:FinancialInstitutionBranch>
    """

    def __init__(self, Name: str = None, FinancialInstitution: FinancialInstitution = None):
        self.Name = Name
        self.FinancialInstitution = FinancialInstitution

class FinancialAccount:
    """
    Hesap bilgilerinin tutulduğu bölümdür.
    2.2.25 FinancialAccount Hesap Bilgisi

    ID                          Zorunlu(1)      : Hesap numarası metin olarak girilir.
    CurrencyCode                Seçimli(0..1)   : Hesabın para birimi kodu girilir. Bknz. Kod Listeleri.
    PaymentNote                 Seçimli(0..1)   : Ödeme ile ilgili açıklama serbest metin olarak girilir.
    FinancialInstitutionBranch  Seçimli(0..1)   : Hesabın bulunduğu banka ve şube bilgileri girilebilir. Bknz. Branch

    Örnek
                <cac:PayeeFinancialAccount>
                    <cbc:ID>12345567</cbc:ID>
                    <cbc:CurrencyCode>TRY</cbc:CurrencyCode>
                    <cbc:PaymentNote>[ÖDEMEAÇIKLAMASI]</cbc:PaymentNote>
                </cac:PayeeFinancialAccount>
    """

    def __init__(self, ID: str = None, CurrencyCode: str = None, PaymentNote: str = None,
                    FinancialInstitutionBranch: Branch = None):
        self.id = ID
        self.currency_code = CurrencyCode
        self.payment_note = PaymentNote
        self.financial_institution_branch = FinancialInstitutionBranch

class Period:
    """
    Belgelerde dönem kullanılması halinde dönem bu elemanda gösterilir.
    2.2.46 Period Periyod

    Seçimli (0..1): StartDate
    Seçimli (0..1): StartTime
    Seçimli (0..1): EndDate
    Seçimli (0..1): EndTime
    Seçimli (0..1): DurationMeasure
    Seçimli (0..1): Description

    Kullanım
        Dönemin belli bir tarih aralığı olarak belirlenmesi halinde “StartDate” ve “EndDate” elemanları kullanılacaktır,
        bunun dışında dönem, süre olarak belirtiliyorsa ölçüsü belirtilerek “DurationMeasure” elemanı kullanılacaktır.

        StartDate: Dönemin başladığı tarih
        StartTime: Dönemin başladığı zaman
        EndDate: Dönemin bittiği tarih
        EndTime: Dönemin bittiği zaman
        DurationMeasure: Dönem süresi numerik olarak, dönem aralığı tipi’de “unitCode” attribute değerine
                            yıl için “ANN”, ay için “MON”, gün için “DAY” ve saat için “HUR” girilmesi gerekmektedir.
        Description: Dönemin açıklaması serbest metin olarak girilecektir.

    Örnek 1:
        <cac:InvoicePeriod>
            <cbc:StartDate>2009-08-13</cbc:StartDate>
            <cbc:EndDate>2009-08-14</cbc:EndDate>
        </cac:InvoicePeriod>

    Örnek 2:
        <cac:InvoicePeriod>
            <cbc:DurationMeasure unitCode="DAY">1</cbc:DurationMeasure>
            <cbc:Description>Günlük</cbc:Description>
        </cac:InvoicePeriod>
    """

    def __init__(self, StartDate: str = None, StartTime: str = None, EndDate: str = None, EndTime: str = None,
                    DurationMeasure: str = None, Description: str = None):
        self.start_date = StartDate
        self.start_time = StartTime
        self.end_date = EndDate
        self.end_time = EndTime
        self.duration_measure = DurationMeasure
        self.description = Description

class ExternalReference:
    """
    Belgelerde ilişkilendirilmek istenen dokümanların referanslarının yer aldığı elemandır.

    2.2.24 ExternalReference Harici Referans @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 33/81

    URI    Zorunlu(1): İlişkilendirilmek istenen dokumanın URI formatında referansını tutar.

    Örnek
    <cac:ExternalReference>
        <cbc:URI>#12345</cbc:URI>
    </cac:ExternalReference>
    """

    def __init__(self, URI: str = None):
        self.uri = URI

class Attachment:
    """
    Belgelerde referans verilmek istenen referansların ya da belgelere eklenmek istenen dokümanların yer aldığı elemandır.
    2.2.4 Attachment Ekli Dosya, UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 14/81

    Seçimli (0..1): ExternalReference
    Seçimli (0..1): EmbeddedDocumentBinaryObject

    Kullanım, İki çeşit kullanımı mevcuttur:
        1. ExternalReference: İlişkilendirilmek istenen dokümanın URI formatında referansını tutar.
        Eğer Attachment elemanı, bir “DigitalSignatureAttachment” ise (diğer bir deyişle Signature Elemanının içerisinde
        yer alıyorsa) External Reference zorunlu bir elemandır. Bknz. ExternalReference

        2. EmbeddedDocumentBinaryObject: İlişiklendirilmiş dokümanı base64Encoded formatında tutar.

    Örnek
        <cac:Attachment>
            <cac:ExternalReference>
                <cbc:URI>#12345</cbc:URI>
            </cac:ExternalReference>
        </cac:Attachment>

        <cac:Attachment>
            <cbc:EmbeddedDocumentBinaryObject mimeCode="application/CSTAdata+xml">
            UjBsR09EbGhjZ0dTQUxNQUFBUUNBRU1tQ1p0dU1GUXhEUzhi
            </cbc:EmbeddedDocumentBinaryObject>
        </cac:Attachment>
    """

    def __init__(self, ExternalReference: str = None, EmbeddedDocumentBinaryObject: str = None):
        self.external_reference = ExternalReference
        self.embedded_document_binary_object = EmbeddedDocumentBinaryObject

class DocumentReference:
    """
    Referans verilen yada eklenen belgelere ilişkin bilgiler girilecektir.
    2.2.20 DocumentReference Doküman Bilgisi @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 29/81

    ID                  Zorunlu(1)    : Referans verilen veya eklenen belgenin sıra numarası girilecektir.
    IssueDate           Zorunlu(1)    : Belgenin düzenlenme tarihi girilecektir.
    DocumentTypeCode    Seçimli(0..1) : Bu eleman belge seviyesinde kullanılmayacaktır.
                                        Kullanım alanı sistem seviyesinde dönen uygulama yanıtı (ApplicationResponse) belgesinin içindedir.
    DocumentType        Seçimli(0..1) : Referans verilen veya eklenen belgenin tipi girilecektir.
                                        Örnek olarak “XSLT”, “REKLAM”, “PROFORMA”, “GÖRÜŞME DETAYI” ve benzeri değerler girilebilir.
    DocumentDesciption  Seçimli(0..n) : Referans verilen ya da eklenen belgelere ilişkin serbest metin açıklaması girilebilir.
    Attachment          Seçimli(0..1) : Bknz. Attachment
    ValidityPeriod      Seçimli(0..1) : Referans verilen ya da eklenen belgenin geçerlilik süresi girilebilir. Bknz. Period
    IssuerParty         Seçimli(0..1) : Referans verilen ya da eklenen belgeyi yayınlayan taraf bilgisi girilebilir. Bknz. Party

    Örnek
            <cac:AdditionalDocumentReference>
                <cbc:ID>F47AC10B-58CC-4372-A567-0E02B2C3D479</cbc:ID>
                <cbc:IssueDate>2009-01-05</cbc:IssueDate>
                <cbc:DocumentType>PROFORMA </cbc:DocumentType>
            </cac:AdditionalDocumentReference>
    """

    def __init(self, ID: str = None, IssueDate: str = None, DocumentTypeCode: str = None,
                DocumentType: str = None, DocumentDescription: str = None, Attachment: Attachment = None,
                ValidityPeriod: Period = None, IssuerParty: Party = None):
        self.id = ID
        self.issue_date = IssueDate
        self.document_type_code = DocumentTypeCode
        self.document_type = DocumentType
        self.document_description = DocumentDescription
        self.attachment = Attachment
        self.validity_period = ValidityPeriod
        self.issuer_party = IssuerParty


class Person:
    """
    Şahısla ilgili bilgiler girilecektir.
    2.2.47 Person Kişi

    FirstName                   Zorunlu(1)      : Şahsın ilk adı girilecektir.
    FamilyName                  Zorunlu(1)      : Şahsın soyadı girilecektir.
    Title                       Seçimli(0..1)   : Şahsın ünvanı girilecektir.
    MiddleName                  Seçimli(0..1)   : Şahsın diğer isimleri yazılacaktır.
    NameSuffix                  Seçimli(0..1)   : Şahsın adının ön eki varsa bu alana girilecektir.
    NationalityID               Seçimli(0..1)   : Şahsın milliyeti girilecektir.
    FinancialAccount            Seçimli(0..1)   : Şahsın hesap bilgileri girilecektir. Bknz. FinancialAccount
    IdentityDocumentReference   Seçimli(0..1)   : Şahsın kimlik dokümanına (Örneğin pasaport numarası buraya yazılacaktır)
                                                    referans girilebilecektir. Bknz. DocumentReference.
    Örnek
                <cac:Person>
                    <cbc:FirstName>Ali</cbc:FirstName>
                    <cbc:FamilyName>Kaya</cbc:FamilyName>
                    <cbc:Title>Dr.</cbc:Title>
                    <cbc:MiddleName>Mehmet</cbc:MiddleName>
                    <cbc:NameSuffix>PhD.</cbc:NameSuffix>
                </cac:Person>
    """
    def __init__(self, FirstName: str = None, FamilyName: str = None, Title: str = None, MiddleName: str = None,
                NameSuffix: str = None, NationalityID: str = None, FinancialAccount: FinancialAccount = None,
                IdentityDocumentReference: DocumentReference = None):
        self.first_name = FirstName
        self.family_name = FamilyName
        self.title = Title
        self.middle_name = MiddleName
        self.name_suffix = NameSuffix
        self.nationality_id = NationalityID
        self.financial_account = FinancialAccount
        self.identity_document_reference = IdentityDocumentReference

class CustomerParty:
    """
    Alıcı tarafın bilgilerini tutan elemandır.
    2.2.13 CustomerParty Alıcı

    Party           Zorunlu(1): Alıcı tarafı tanımlar ve aşağıdaki kısıtlar mevcuttur:
                                “Party/PartyIdentification”:
                                    Alıcının kurum olması durumunda vergi kimlik numarası girilmesi zorunludur.
                                    Alıcının şahıs olması durumunda TC kimlik numarası girilmesi zorunludur.
                                    Tarafın vergi kimlik numarası girilmişse bu alana vergi dairesi adı girilir. Bknz. PartyTaxScheme.

                                “Party/Person”:
                                    Tarafın şahıs olması durumunda bu eleman zorunludur. Bknz. Party

    DeliveryContact Seçimli(0..1): ReceiptAdvice içerisinde kullanımında teslim alan bilgisi girilebilir. Bknz. Contact

    Örnek
            <cac:AccountingCustomerParty>
                <cac:Party>
                    <cbc:WebsiteURI>http://www.aaa.com.tr/</cbc:WebsiteURI>
                    <cac:PartyIdentification>
                        <cbc:ID schemeID="VKN">1288331521</cbc:ID>
                    </cac:PartyIdentification>
                    <cac:PartyName>
                        <cbc:Name>AAA Anonim Şirketi</cbc:Name>
                    </cac:PartyName>
                    <cac:PostalAddress>
                        <cbc:ID>2806632739</cbc:ID>
                        <cbc:StreetName>Papatya Caddesi Yasemin Sokak</cbc:StreetName>
                        <cbc:BuildingNumber>21</cbc:BuildingNumber>
                        <cbc:CitySubdivisionName>Beşiktaş</cbc:CitySubdivisionName>
                        <cbc:CityName>İstanbul</cbc:CityName>
                        <cbc:PostalZone>34100</cbc:PostalZone>
                        <cac:Country>
                            <cbc:Name>Türkiye</cbc:Name>
                        </cac:Country>
                    </cac:PostalAddress>
                    <cac:PartyTaxScheme>
                        <cac:TaxScheme>
                            <cbc:Name> Büyük Mükellefler</cbc:Name>
                        </cac:TaxScheme>
                    </cac:PartyTaxScheme>
                    <cac:Contact>
                        <cbc:Telephone>(212) 925 51515</cbc:Telephone>
                        <cbc:Telefax>(212) 925505015</cbc:Telefax>
                        <cbc:ElectronicMail>aa@aaa.com.tr</cbc:ElectronicMail>
                    </cac:Contact>
                </cac:Party>
            </cac:AccountingCustomerParty>
    """

    def __init__(self, Party: Party = None, DeliveryContact: Contact = None):
        self.party = Party
        self.delivery_contact = DeliveryContact

class SignatoryParty:
    """
    Template for SignatoryParty, inherit for specific signatory parties.
    2.3.27 Signature
    Signature Mali Mühür/İmza
    Kardinalite Zorunlu (1…n)
    Açıklama Bu elemanda faturada kullanılan mali mühür ve/veya elektronik
    imza ile sertifikalara ilişkin bilgilere yer verilecektir.
    Kullanım Bknz. Ortak Sınıflar: Signature
    """
    VKN_TCKN = None
    VKN = None
    ROOM = None
    STREET_NAME = None
    BUILDING_NAME = None
    BUILDING_NUMBER = None
    CITY_SUBDIVISION_NAME = None
    CITY_NAME = None
    POSTAL_ZONE = None
    COUNTRY_NAME = None
    URI = None


class KolaysoftSignature(SignatoryParty):
    """
    Example signatory party: Kolaysoft Signature
    """
    VKN_TCKN = "5750464002"
    VKN = "5750464002"
    ROOM = "201-204"
    STREET_NAME = "A.T.G.B. Üniversiteler Mah. 1605. Cad."
    BUILDING_NAME = "Cyberpark Vakıf Binası"
    BUILDING_NUMBER = "3"
    CITY_SUBDIVISION_NAME = "Çankaya"
    CITY_NAME = "Ankara"
    POSTAL_ZONE = "06800"
    COUNTRY_NAME = "Türkiye"
    URI = "#Signature_cf981f3d-3be5-4b9d-8b6d-7f5e18175a2f"


class PayeeFinancialAccount:
    """
    Alacaklı hesap bilgileri.

    <cac:PayeeFinancialAccount>
        <cbc:ID>IBANTR12345567</cbc:ID>
        <cbc:CurrencyCode>TRY</cbc:CurrencyCode>
        <cbc:PaymentNote>[ÖDEMEAÇIKLAMASI]</cbc:PaymentNote>
    </cac:PayeeFinancialAccount>
    """

    def __init__(self, ID: str = None, CurrencyCode: str = None, PaymentNote: str = None):
        self.ID = ID
        self.CurrencyCode = CurrencyCode
        self.PaymentNote = PaymentNote


class PaymentMeans:
    """
    2.3.34 PaymentMeans: Ödeme Şekli Ödeme Şekline İlişkin Bilgiler
    Kardinalite: Seçimli(0..n)
    Açıklama: Bu elemana ödeme şekli ile ilgili bilgiler yazılabilecektir.
    Kullanım: Bknz. Ortak Sınıflar: PaymentMeans
    Örnek:  <cac:PaymentMeans>
                <cbc:PaymentMeansCode>42</cbc:PaymentMeansCode>
                <cbc:PaymentDueDate>2009-01-13</cbc:PaymentDueDate>
                <cbc:PaymentChannelCode>1234</cbc:PaymentChannelCode>
                <cbc:InstructionNote>[AÇIKLAMA]</cbc:InstructionNote>
                <cac:PayeeFinancialAccount>
                    <cbc:ID>IBANTR12345567</cbc:ID>
                    <cbc:CurrencyCode>TRY</cbc:CurrencyCode>
                    <cbc:PaymentNote>[ÖDEMEAÇIKLAMASI]</cbc:PaymentNote>
                </cac:PayeeFinancialAccount>
            </cac:PaymentMeans>

    Ortak Sınıf:
    Açıklama Ödeme şeklinin girildiği elemandır.
    2.2.44 PaymentMeans Ödeme Şekli
    Elemanlar ve Kullanım Kardinaliteleri
                                Zorunlu(1): PaymentMeansCode
                                Seçimli(0..1): PaymentDueDate
                                Seçimli(0..1): PaymentChannelCode
                                Seçimli(0..1): InstructionNote
                                Seçimli(0..1): PayerFinancialAccount
                                Seçimli(0..1): PayeeFinancialAccount

    Kullanım PaymentMeansCode: Ödeme şeklinin kodu girilir.
    Bu eleman için UN/EDIFACT 4461 Ödeme Çeşitleri Kod Listesi kullanılacaktır. Bknz. Kod listeleri.
    PaymentDueDate: Son ödeme günü yıl-ay-gün formatında girilir.
    PaymentChannelCode: Ödeme kanalı kodu girilir.
    InstructionNote: Ödeme ile ilgili açıklamalar serbest metin olarak girilir.
    PayerFinancialAccout: Ödeme yapan tarafın hesap bilgileri girilir. Bknz. FinancialAccount.
    PayeeFinancialAccount: Ödeme yapılacak hesap girilir. Bknz. FinancialAccount.

    Örnek
    <cac:PaymentMeans>
        <cbc:PaymentMeansCode>42</cbc:PaymentMeansCode>
        <cbc:PaymentDueDate>2009-01-13</cbc:PaymentDueDate>
        <cbc:PaymentChannelCode>1234</cbc:PaymentChannelCode>
        <cbc:InstructionNote>[AÇIKLAMA]</cbc:InstructionNote>
        <cac:PayeeFinancialAccount>
            <cbc:ID>1012212345567</cbc:ID>
            <cbc:CurrencyCode>TRY</cbc:CurrencyCode>
            <cbc:PaymentNote>[ÖDEMEAÇIKLAMASI]</cbc:PaymentNote>
        </cac:PayeeFinancialAccount>
    </cac:PaymentMeans>
    """

    def __init__(self, PaymentMeansCode: str = None, PaymentDueDate: str = None, PaymentChannelCode: str = None,
                InstructionNote: str = None, PayeeFinancialAccount: PayeeFinancialAccount = None):
        self.PaymentMeansCode = PaymentMeansCode
        self.PaymentDueDate = PaymentDueDate
        self.PaymentChannelCode = PaymentChannelCode
        self.InstructionNote = InstructionNote
        self.PayeeFinancialAccount = PayeeFinancialAccount


class PaymentTerms:
    """
    Bu elemana ödeme koşulları ve ödemenin yapılmaması halinde uygulanacak müeyyideler yazılabilecektir.
    2.3.35 PaymentTerms Ödeme Koşulları
    Kardinalite Seçimli (0..1)
    Kullanım Bknz. Ortak Sınıflar: PaymentTerms
    Örnek
            <cac:PaymentTerms>
                <cbc:Note>[AÇIKLAMA]</cbc:Note>
                <cbc:PenaltySurchargePercent>20.0</cbc:PenaltySurchargePercent>
                <cbc:PaymentDueDate>2009-01-13</cbc:PaymentDueDate>
                <cbc:Amount currencyID="TRY">100.0</cbc:Amount>
            </cac:PaymentTerms>


    Ortak Sınıflar: 2.2.45 PaymentTerms Ödeme Koşulları
    Elemanlar ve Kullanım
                        Seçimli(0..1): Note
                        Seçimli(0..1): PenaltySurchargePercent
                        Kardinaliteleri Seçimli(0..1): Amount
                        Seçimli(0..1): PenaltyAmount
                        Seçimli(0..1): PaymentDueDate
                        Seçimli(0..1): SettlementPeriod

    Note: Ödeme koşulları ile ilgili açıklama serbest metin olarak girilir.
    PenaltySurchargePercent: Ödemenin gecikmesi durumunda uygulanacak ceza oranı numerik olarak girilir.
    Amount: Ödeme tutarı numerik olarak girilebilir.
    PenaltyAmount: Ödemenin gecikmesi durumunda uygulanacak ceza tutarı numerik olarak girilir.
    PaymentDueDate: Son ödeme günü yıl-ay-gün formatında girilir.
    SettlementPeriod: Ödeme dönemi girilir. Bknz. Period

    Örnek
                        <cac:PaymentTerms>
                            <cbc:Note>[AÇIKLAMA]</cbc:Note>
                            <cbc:PenaltySurchargePercent>20.0</cbc:PenaltySurchargePercent>
                            <cbc:Amount currencyID="TRY">100.0</cbc:Amount>
                        </cac:PaymentTerms>

                        <cac:PaymentTerms>
                            <cbc:Note>[AÇIKLAMA]</cbc:Note>
                            <cbc:PenaltySurchargePercent>20.0</cbc:PenaltySurchargePercent>
                            <cbc:PaymentDueDate>2009-01-13</cbc:PaymentDueDate>
                            <cbc:Amount currencyID="TRY">100.0</cbc:Amount>
                        </cac:PaymentTerms>
    """

    def __init__(self, Note: str = None, PenaltySurchargePercent: str = None, PaymentDueDate: str = None,
                Amount: str = None, CurrencyID: str = None):
        self.Note = Note
        self.PenaltySurchargePercent = PenaltySurchargePercent
        self.PaymentDueDate = PaymentDueDate
        self.Amount = Amount
        self.CurrencyID = CurrencyID


class TaxCategory:
    """
    2.2.58 TaxCategory TaxCategory Vergi Türü
    Belge üzerinde yer alan vergi türü, muafiyet ve istisnalara ilişkin bilgiler girilir.

    Name                    Seçimli(0..1)   : Vergi türü ismi girilecektir.
    TaxExemptionReasonCode  Seçimli(0..1)   : Vergi muafiyet, istisna sebepleri bu alana kodlu olarak girilecektir. Bknz. Kod listeleri.
    TaxExemptionReason      Seçimli(0..1)   : Vergi muafiyet, istisna sebepleri bu alana serbest metin olarak girilecektir.
    TaxScheme               Zorunlu(1)      : TaxScheme Uygulanan vergi türü hakkında bilgiler girilir. Bknz. TaxScheme

    Örnek
        <cac:TaxCategory>
            <cbc:TaxExemptionReasonCode>301</cbc:TaxExemptionReasonCode>
            <cac:TaxScheme>
                <cbc:Name>Katma Değer Vergisi</cbc:Name>
                <cbc:TaxTypeCode>0015</cbc:TaxTypeCode>
            </cac:TaxScheme>
        </cac:TaxCategory>

        <cac:TaxCategory>
            <cac:TaxScheme>
                <cbc:Name>Katma Değer Vergisi</cbc:Name>
                <cbc:TaxTypeCode>0015</cbc:TaxTypeCode>
            </cac:TaxScheme>
        </cac:TaxCategory>
    """

    def __init__(self, Name: str = None, TaxExemptionReasonCode: str = None, TaxExemptionReason: str = None,
                TaxScheme: TaxScheme = None):
        self.Name = Name
        self.TaxExemptionReasonCode = TaxExemptionReasonCode
        self.TaxExemptionReason = TaxExemptionReason
        self.TaxScheme = TaxScheme


class TaxSubtotal:
    """
    Vergi ve diğer yasal yükümlülüklerin hesaplaması ile ilgili bilgilere yer verilecektir.
    2.2.60 TaxSubtotal Vergi Ara Toplamı

    TaxableAmount                   Seçimli(0..1)   :   Verginin üzerinden hesaplandığı tutar (matrah) bilgisi girilecektir.
    TaxAmount                       Zorunlu(1)      :   Hesaplanan Vergi Tutarıdır.
    CalculationSequenceNumeric      Seçimli(0..1)   :   Vergi hesaplamasında belli bir sıra izlenmesi veya birden fazla vergi hesaplaması
                                                        yapılması halinde ilgili sıra numarası girilecektir.
    TransactionCurrencyTaxAmount    Seçimli(0..1)   :   Belge para birimi cinsinden toplam vergi tutarıdır.
    Percent                         Seçimli(0..1)   :   Vergi oranı girilebilecektir.
    BaseUnitMeasure                 Seçimli(0..1)   :   Vergileme ölçüsü olarak miktar(kilogram, metre vb.) kullanılması halinde ilgili tarife bilgileri bu elemana girilecektir.
    PerUnitAmount                   Seçimli(0..1)   :   Vergileme ölçüsü olarak tutar(perakende satış fiyatı gibi.) kullanılması halinde ilgili tarife bilgileri bu elemana girilecektir.
    TaxCategory                     Zorunlu(1)      :   Verginin türü ile ilgili bilgiler girilecektir. Bknz: TaxCategory

    Örnek
        <cac:TaxSubtotal>
            <cbc:TaxableAmount currencyID="TRY">19.17</cbc:TaxableAmount>
            <cbc:TaxAmount currencyID="TRY">3.45</cbc:TaxAmount>
            <cbc:CalculationSequenceNumeric>1</cbc:CalculationSequenceNumeric>
            <cbc:Percent>18.0</cbc:Percent>
            <cac:TaxCategory>
                <cac:TaxScheme>
                    <cbc:Name>Katma Değer Vergisi</cbc:Name>
                    <cbc:TaxTypeCode> 0015</cbc:TaxTypeCode>
                </cac:TaxScheme>
            </cac:TaxCategory>
        </cac:TaxSubtotal>
    """

    def __init__(self, TaxableAmount: str = None, TaxAmount: str = None, CalculationSequenceNumeric: str = None,
                    TransactionCurrencyTaxAmount: str = None, Percent: str = None, BaseUnitMeasure: str = None,
                    PerUnitAmount: str = None, TaxCategory: TaxCategory = None):
        self.TaxableAmount = TaxableAmount
        self.TaxAmount = TaxAmount
        self.CalculationSequenceNumeric = CalculationSequenceNumeric
        self.TransactionCurrencyTaxAmount = TransactionCurrencyTaxAmount
        self.Percent = Percent
        self.BaseUnitMeasure = BaseUnitMeasure
        self.PerUnitAmount = PerUnitAmount
        self.TaxCategory = TaxCategory

class TaxTotal:
    """
    Vergi ve diğer yasal yükümlülüklerin hesaplaması ile ilgili bilgiler ile belge üzerinde hesaplanan toplam vergi ve yasal yükümlülük tutarı girilecektir.
    2.2.61 TaxTotal Vergi Toplamı

    TaxAmount   Zorunlu(1)      :   Toplam Vergi Tutarıdır.
    TaxSubtotal Zorunlu(1..n)   :   Vergi hesaplaması ile ilgili bilgilere yer verilir. Birden fazla vergi türü veya aynı vergi türü içerisinde farklı oranlarda
                                    yapılan hesaplamalarla ilgili bilgilere de bu alanda yer verilecektir. Bknz. TaxSubtotal.

    Üç çeşit kullanımı mevcuttur:

    1. “Invoice/TaxTotal”: Hesaplanan vergilerin toplam tutarı girilir. Bu alan zorunludur.
     TaxAmount: Toplam vergi tutarı girilir.
     TaxSubtotal: Vergi hesaplaması ile ilgili bilgilere yer verilir. Birden fazla vergi türü veya aynı vergi türü
    içerisinde farklı oranlarda yapılan hesaplamalarla ilgili bilgilere de bu alanda yer verilecektir. Bknz. TaxSubtotal.

    2. “Invoice/InvoiceLine/TaxTotal”: Hesaplanan vergilerin kalem bazlı hesaplanması durumunda bu alan kullanılır. Bu alan seçimlidir.
     TaxAmount: Kalem için hesaplanan toplam vergi tutarı girilir.
     TaxSubtotal: Kalem bazında vergi hesaplaması söz konusu olması halinde ilgili bilgilere yer verilebilecektir. Bknz. TaxSubtotal.

    3. “WithholdingTaxTotal”: Tevkifatlı faturalarda, uygulanan tevkifat miktarları, oranları ve diğer bilgileri girilir.
     TaxAmount: Toplam tevkifat tutarı girilir.
     TaxSubtotal: Tevkifat kodu ve oranı bilgisi girilir.
    Ek parametreler:
        - currencyID: Vergi tutarının para birimi bilgisi girilecektir. Varsayılan değer: “TRY”.

    Örnek
    <cac:TaxTotal>
        <cbc:TaxAmount currencyID="TRY">123.93</cbc:TaxAmount>
        <cac:TaxSubtotal>
            <cbc:TaxableAmount currencyID="TRY">688.50</cbc:TaxableAmount>
            <cbc:TaxAmount currencyID="TRY">123.93</cbc:TaxAmount>
            <cbc:CalculationSequenceNumeric>1.0</cbc:CalculationSequenceNumeric>
            <cbc:Percent>18.0</cbc:Percent>
            <cac:TaxCategory>
                <cac:TaxScheme>
                    <cbc:Name>Katma Değer Vergisi</cbc:Name>
                    <cbc:TaxTypeCode>0015</cbc:TaxTypeCode>
                </cac:TaxScheme>
            </cac:TaxCategory>
        </cac:TaxSubtotal>
    </cac:TaxTotal>

    <cac:WithholdingTaxTotal>
        <cbc:TaxAmount currencyID="TRY">3240</cbc:TaxAmount>
        <cac:TaxSubtotal>
            <cbc:TaxAmount currencyID="TRY">3240</cbc:TaxAmount>
            <cbc:Percent>90</cbc:Percent>
            <cac:TaxCategory>
                <cac:TaxScheme>
                    <cbc:TaxTypeCode>606</cbc:TaxTypeCode>
                </cac:TaxScheme>
            </cac:TaxCategory>
        </cac:TaxSubtotal>
    </cac:WithholdingTaxTotal>

    <cac:TaxTotal>
		<cbc:TaxAmount currencyID="TRY">4538.97</cbc:TaxAmount>
		<cac:TaxSubtotal>
			<cbc:TaxableAmount currencyID="TRY">25216.50</cbc:TaxableAmount>
			<cbc:TaxAmount currencyID="TRY">4538.97</cbc:TaxAmount>
			<cbc:CalculationSequenceNumeric>1.0</cbc:CalculationSequenceNumeric>
			<cbc:Percent>18</cbc:Percent>
			<cac:TaxCategory>
				<cac:TaxScheme>
					<cbc:Name>Katma Değer Vergisi</cbc:Name>
					<cbc:TaxTypeCode>0015</cbc:TaxTypeCode>
				</cac:TaxScheme>
			</cac:TaxCategory>
		</cac:TaxSubtotal>
	</cac:TaxTotal>
    """

    def __init__(self, TaxAmount: str = None, TaxSubtotal: Union[TaxSubtotal, List[TaxSubtotal]] = None, CurrencyID: str = "TRY"):
        self.TaxAmount = TaxAmount
        self.TaxSubtotal = TaxSubtotal
        self.CurrencyID = CurrencyID

class MonetaryTotal:
    """
            <cac:LegalMonetaryTotal>
                <cbc:LineExtensionAmount
                currencyID="TRY">90</cbc:LineExtensionAmount>
                <cbc:TaxExclusiveAmount currencyID="TRY">80</cbc:TaxExclusiveAmount>
                <cbc:TaxInclusiveAmount currencyID="TRY">94</cbc:TaxInclusiveAmount>
                <cbc:AllowanceTotal currencyID="TRY">10</cbc:AllowanceTotal >
                <cbc:PayableRoundingAmount currencyID="TRY">0.4</cbc:PayableRoundingAmount>
                <cbc:PayableAmount currencyID="TRY">94.4</cbc:PayableAmount>
            </cac:LegalMonetaryTotal>
    """

    def __init__(self, LineExtensionAmount: str = None, TaxExclusiveAmount: str = None, TaxInclusiveAmount: str = None,
                AllowanceTotalAmount: str = None, ChargeTotalAmount: str = None, PayableRoundingAmount: str = None,
                PayableAmount: str = None,
                CurrencyID: str = 'TRY'):
        self.LineExtensionAmount = LineExtensionAmount
        self.TaxExclusiveAmount = TaxExclusiveAmount
        self.TaxInclusiveAmount = TaxInclusiveAmount
        self.AllowanceTotalAmount = AllowanceTotalAmount
        self.ChargeTotalAmount = ChargeTotalAmount
        self.PayableRoundingAmount = PayableRoundingAmount
        self.PayableAmount = PayableAmount
        self.CurrencyID = CurrencyID


class InvoicedQuantity:
    """
    1.5 InvoicedQuantity, UBL-TR Kod Listeleri Ocak 2023 Versiyon: 1.31 8/20
    Bu elemanın “unitCode” attribute’unun değer kümesi öncelikle aşağıdaki listeden alınmalıdır
    (Her türlü unitCode attribute’unun değeri bu listeden alınacaktır).
    Bu listede bulunmayan birim kodları ise “UN/ECE Unit Codes4” listesinden alınmalıdır.

    http://www.unece.org/uncefact/codelist/standard/ISO_ISO3AlphaCurrencyCode_20100407.xsd
    http://www.iso.org/iso/english_country_names_and_code_elements
    http://www.unece.org/trade/untdid/d00a/tred/tred3155.htm
    https://www.unece.org/fileadmin/DAM/cefact/recommendations/rec20/rec20_Rev11e_2015.xls

    KOD     ADI
    B32     KG-METRE KARE
    C62     ADET(UNIT)
    CCT     TON BAŞINA TAŞIMA KAPASİTESİ
    PR      ÇİFT
    D30     BRÜT KALORİ DEĞERİ
    D40     BİN LİTRE
    GFI     FISSILE İZOTOP GRAMI
    GRM     GRAM
    GT      GROSS TON
    CEN     YÜZ ADET
    KPO     KİLOGRAM POTASYUM OKSİT
    MND     KURUTULMUŞ NET AĞIRLIKLI KİLOGRAMI
    3I      KİLOGRAM-ADET
    KFO     DİFOSFOR PENTAOKSİT KİLOGRAMI
    KGM     KİLOGRAM
    KHY     HİDROJEN PEROKSİT KİLOGRAMI
    KMA     METİL AMİNLERİN KİLOGRAMI
    KNI     AZOTUN KİLOGRAMI
    KPH     KİLOGRAM POTASYUM HİDROKSİT
    KSD     %90 KURU ÜRÜN KİLOGRAMI
    KSH     SODYUM HİDROKSİT KİLOGRAMI
    KUR     URANYUM KİLOGRAMI
    D32     TERAWATT SAAT
    GWH     GİGAWATT SAAT
    MWH     MEGAWATT SAAT (1000 kW.h)
    KWH     KİLOWATT SAAT
    KWT     KİLOWATT
    LPA     SAF ALKOL LİTRESİ
    LTR     LİTRE
    MTK     METRE KARE
    DMK     DESİMETRE KARE
    MTQ     METRE KÜP
    MTR     METRE
    NCL     HÜCRE ADEDİ
    CTM     KARAT
    SM3     STANDART METREKÜP
    R9      BİN METRE KÜP
    SET     SET
    T3      BİN ADET

    <cbc:InvoicedQuantity unitCode="C62">1.0</cbc:InvoicedQuantity>
    """

    def __init__(self, UnitCode: str = None, Qty: str = None):
        self.UnitCode = UnitCode
        self.Qty = Qty


class AllowanceCharge:
    """
    Iskonto veya artırımların tanımlandığı elemandır.
    2.2.3 AllowanceCharge Iskonto/Artırım @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 13/81

    ChargeIndicator         Zorunlu(1)   : Iskonto ise “false”, artırım ise “true” değerini alır
    AllowanceChargeReason   Seçimli(0..1): Iskonto/ Artırım Nedeni. Iskonto veya artırımın sebebi serbest metin olarak girilir.
    MultiplierFactorNumeric Seçimli(0..1): Iskonto/ Artırım Oranı. Iskonto veya artırım oranı numerik olarak girilir.
    SequenceNumeric         Seçimli(0..1): Sıra Numarası. Birden fazla iskonto veya fiyat artırımı kullanılması durumunda sıra numarası girilir.
    Amount                  Zorunlu(1)   : Iskonto/ Artırım Tutarı. Iskonto veya artırım miktarı numerik girilir.
    BaseAmount              Seçimli(0..1): İskonto veya artırımın uygulandığı tutar. Iskonto veya artırım oranının uygulandığı tutar girilir.
    PerUnitAmount           Seçimli(0..1): Ürün adetine göre iskonto veya artırımın uygulandığı durumlarda uygulanan ürün miktarını gösterir

    Örnek:
    <cac:AllowanceCharge>
        <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReason>Müşteri İndirimi</cbc:AllowanceChargeReason>
        <cbc:MultiplierFactorNumeric>0.1</cbc:MultiplierFactorNumeric>
        <cbc:Amount currencyID="TRY">20</cbc:Amount>
        <cbc:BaseAmountcurrencyID="TRY">200</cbc:BaseAmount>
    </cac:AllowanceCharge>

    """

    def __init__(self, ChargeIndicator: str, Amount: str, AllowanceChargeReason: str = None,
                MultiplierFactorNumeric: str = None,
                SequenceNumeric: str = None, BaseAmount: str = None, PerUnitAmount: str = None,
                CurrencyID: str = 'TRY'):
        self.ChargeIndicator = ChargeIndicator
        self.AllowanceChargeReason = AllowanceChargeReason
        self.MultiplierFactorNumeric = MultiplierFactorNumeric
        self.SequenceNumeric = SequenceNumeric
        self.Amount = Amount
        self.BaseAmount = BaseAmount
        self.PerUnitAmount = PerUnitAmount
        self.CurrencyID = CurrencyID

class ItemIdentification:
    """
    Ürün numaralandırlması için kullanılır. Her türlü numaralandırılma için kullanılabilir.
    Örneğin, ilaç sektöründe PluKod’u veya otomotiv sektöründe aracın motor numarası gibi.

    2.2.31 ItemIdentification Kalem Kimliği @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 43/81

    ID  Zorunlu(1): Ürün numarası girilir.

    Örnek
    <cac:ManufacturersItemIdentification>
        <cbc:ID>1387</cbc:ID>
    </cac:ManufacturersItemIdentification>
    """

    def __init__(self, ID: str = None):
        self.ID = ID

class CommodityClassification:
    """
    Ürün hakkında uluslararası standart veya ulusal kodlar (örneğin, Sağlık Uygulama Tebliği) tabanlı sınıflandırma bilgisi vermek istenmesi durumunda girilir.

    2.2.8 CommodityClassification Ürün Sınıflandırılması (Standart) @UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 17/81

    ItemClassificationCode  Zorunlu(1): Kod bilgisi girilir. Bknz. ItemClassificationCode  # TODO: UBL TR'de bilgi yok!
    # https://docs.peppol.eu/poacc/billing/3.0/syntax/ubl-invoice/cac-InvoiceLine/cac-Item/cac-CommodityClassification/cbc-ItemClassificationCode/

    Örnek
    <cac:CommodityClassification>
        <cbc:ItemClassificationCode listAgencyID="113" listID="UNSPSC">12344321</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    """

    def __init__(self, ItemClassificationCode: str = None, listAgencyID: str = None, listID: str = None):
        self.ItemClassificationCode = ItemClassificationCode
        self.listAgencyID = listAgencyID
        self.listID = listID



class Item:
    """
    Mal/Hizmet bilgilerinin girildiği bölümdür.
    2.2.30 Item Kalem @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 41/81

    Description                     Seçimli(0..1): Mal/Hizmet hakkında açıklama serbest metin olarak girilir.
    Name                            Zorunlu(1)   : Mal/hizmet adı serbest metin olarak girilir.
    Keyword                         Seçimli(0..1): Mal/hizmet ile ilgili anahtar kelimeler veya fatura satır tipi bilgileri girilebilir.
    BrandName                       Seçimli(0..1): Mal/hizmet marka adı serbest metin olarak girilir.
    ModelName                       Seçimli(0..1): Mal/hizmet model adı serbest metin olarak girilir.
    BuyersItemIdentification        Seçimli(0..1): Alıcının mal/hizmete verdiği tanımlama bilgisi girilir. Bknz. ItemIdentification
    SellersItemIdentification       Seçimli(0..1): Satıcının mal/hizmete verdiği tanımlama bilgisi girilir. Bknz. ItemIdentification
    ManufacturersItemIdentification Seçimli(0..1): Üreticinin mal/hizmete verdiği tanımlama bilgisi girilir.
                                                    Araç Tescil Faturalarında Şasi Numarası bu elemana girilecektir. Bknz. ItemIdentification
    AdditionalItemIdentification    Seçimli(0..n): Mal/hizmet için diğer kullanılabilecek sınıflandırma bilgileri girilebilir. Bknz. ItemIdentification
    OriginCountry                   Seçimli(0..1): Menşei bilgisi girilebilir. Bknz. Country
    CommodityClassification         Seçimli(0..n): Emtia sınıflandırma bilgisi girilir. Bknz. CommodityClassification
    ItemInstance                    Seçimli(0..n): Parti lot bilgisi, ürün takip numarası, üretim zamanı, seri numarası ve kayıt numarası gibi bilgiler girilebilir.

    Örnek
    <cac:Item>
        <cbc:Description>[ÜRÜN AÇIKLAMASI]</cbc:Description>
        <cbc:Name>[ÜRÜN ADI]</cbc:Name>
        <cbc:BrandName>[MARKA ADI]</cbc:BrandName>
        <cbc:ModelName>[MODEL ADI]</cbc:ModelName>
        <cac:BuyersItemIdentification>
            <cbc:ID>123445</cbc:ID>
        </cac:BuyersItemIdentification>
        <cac:SellersItemIdentification>
            <cbc:ID>12354</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:ManufacturersItemIdentification>
            <cbc:ID>1387</cbc:ID>
        </cac:ManufacturersItemIdentification>
        <cac:CommodityClassification>
            <cbc:ItemClassificationCode>U12.23</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
    </cac:Item>
    """

    def __init__(self, Name: str, Description: str = None, Keyword: str = None, BrandName: str = None, ModelName: str = None,
                    BuyersItemIdentification: ItemIdentification = None, SellersItemIdentification: ItemIdentification = None,
                    ManufacturersItemIdentification: ItemIdentification = None, AdditionalItemIdentification: list = None,
                    OriginCountry: Country = None, CommodityClassification: list = None, ItemInstance: list = None):
        self.Description = Description
        self.Name = Name
        self.Keyword = Keyword
        self.BrandName = BrandName
        self.ModelName = ModelName
        self.BuyersItemIdentification = BuyersItemIdentification
        self.SellersItemIdentification = SellersItemIdentification
        self.ManufacturersItemIdentification = ManufacturersItemIdentification
        self.AdditionalItemIdentification = AdditionalItemIdentification
        self.OriginCountry = OriginCountry
        self.CommodityClassification = CommodityClassification
        self.ItemInstance = ItemInstance

class OrderReference:
    """
    Siparişe ait bilgiler girilecektir.
    2.2.39 OrderReference Sipariş Bilgisi, UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 49/81

    ID                  Zorunlu(1)      : Sipariş numarası girilecektir.
    SalesOrderID        Seçimli(0..1)   : Satıcının verdiği sipariş numarası girilecektir.
    IssueDate           Zorunlu(1)      : Sipariş tarihi girilecektir.
    OrderTypeCode       Seçimli(0..1)   : Sipariş tipi girilecektir.
    DocumentReference   Seçimli(0..n)   : Bknz. DocumentReference

    <cac:OrderReference>
        <cbc:ID>12345</cbc:ID>
        <cbc:IssueDate>2009-04-13</cbc:IssueDate>
    </cac:OrderReference>

    """

    def __init__(self, ID: str = None, SalesOrderID: str = None, IssueDate: str = None, OrderTypeCode: str = None, DocumentReference: list = None):
        self.ID = ID
        self.SalesOrderID = SalesOrderID
        self.IssueDate = IssueDate
        self.OrderTypeCode = OrderTypeCode
        self.DocumentReference = DocumentReference

class OrderLineReference:
    """
    Siparişin kalemlerine referans atmak için kullanılır.
    2.2.38 OrderLineReference Sipariş Kalemi Referansı, UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 48/81

    LineID              Zorunlu(1)      : Kalem numarası girilir.
    SalesOrderLineID    Seçimli(0..1)   : Alıcının verdiği kalem numarası verilir.
    UUID                Seçimli(0..1)   : Sipariş Kaleminin tekil numarası girilir.
    LineStatusCode      Seçimli(0..1)   : Kalemin durumu girilir.
    OrderReference      Seçimli(0..1)   : İlgili sipariş belgesine referans verilir. Bknz. OrderReference

    Örnek
    <cac:OrderLineReference>
        <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    """

    def __init__(self, LineID: str = None, SalesOrderLineID: str = None, UUID: str = None, LineStatusCode: str = None, OrderReference: OrderReference = None):
        self.LineID = LineID
        self.SalesOrderLineID = SalesOrderLineID
        self.UUID = UUID
        self.LineStatusCode = LineStatusCode
        self.OrderReference = OrderReference

class LineReference:
    """
    Kalem ile ilgili tanımlayıcı bilgilere bu elemanda yer verilecektir.
    2.2.33 LineReference Referans Satır, UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 43/81

    LineID              Zorunlu(1)   : Kalem Numarası. Kalemin sıra numarası girilecektir.
    LineStatusCode      Seçimli(0..1): Kalemin durum bilgisi girilebilecektir.
    DocumentReference   Seçimli(0..1): Referans Belge Bknz. DocumentReference

    <cac:LineReference>
        <cbc:LineID>3</cbc:LineID>
    </cac:LineReference>
    """

    def __init__(self, LineID: str = None, LineStatusCode: str = None, DocumentReference: DocumentReference = None):
        self.LineID = LineID
        self.LineStatusCode = LineStatusCode
        self.DocumentReference = DocumentReference

class Despatch:
    """
    Malların alıcıya gönderimlesi için satıcıdan teslim alınması kapsamında zaman ve mekan bilgileri girilir.
    2.2.17 Despatch İrsaliye Bilgisi @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 25/81

    ID                      Seçimli(0..1): İlgili gönderimi belge içerisinde tekil olarak tanımlar.
    ActualDespatchDate      Seçimli(0..1): Gerçekleşen gönderim tarihi girilir. (Fiili Sevk Tarihi)
    ActualDespatchTime      Seçimli(0..1): Gerçekleşen gönderim zamanı girilir. (Fiili Sevk Zamanı)
    Instructions            Seçimli(0..1): Serbest metin olarak gönderime yönelik açıklamalar girilir.
    DespatchAddress         Seçimli(0..1): Malların gönderim için alınacağı adres girilir. Bknz. Address
    DespatchParty           Seçimli(0..1): Malları satıcıdan teslim alacak taraf bilgileri girilir. Bknz. Party
    Contact                 Seçimli(0..1): Malları satıcıdan teslim alacak tarafın iletişim bilgileri girilir. Bknz. Contact
    EstimatedDespatchPeriod Seçimli(0..1): Tahmini teslim alış dönemi girilir. Bknz. Period

    Örnek
    <cac:Despatch>
        <cbc:ActualDespatchDate>2005-06-25</cbc:ActualDespatchDate>
        <cbc:ActualDespatchTime>11:35:00</cbc:ActualDespatchTime>
        <cac:DespatchParty>
        <cac:PartyIdentification>
        <cbc:ID/>
        </cac:PartyIdentification>
        <cac:PartyName>
        <cbc:Name>AAA Kargo</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
        <cbc:ID/>
        <cbc:CitySubdivisionName/>
        <cbc:CityName/>
        <cac:Country>
        <cbc:Name>Türkiye</cbc:Name>
        </cac:Country>
        </cac:PostalAddress>
        </cac:DespatchParty>
        <cac:Contact>
        <cbc:Telephone>312 1111111</cbc:Telephone>
        <cbc:Telefax>312 1111111</cbc:Telefax>
        <cbc:ElectronicMail>aaa@aaa.com.tr</cbc:ElectronicMail>
        </cac:Contact>
    </cac:Despatch>
    """

    def __init__(self, ID: str = None, ActualDespatchDate: str = None, ActualDespatchTime: str = None,
                Instructions: str = None, DespatchAddress: Address = None, DespatchParty: Party = None, Contact: Contact = None,
                EstimatedDespatchPeriod: Period = None):

        self.ID = ID
        self.ActualDespatchDate = ActualDespatchDate
        self.ActualDespatchTime = ActualDespatchTime
        self.Instructions = Instructions
        self.DespatchAddress = DespatchAddress
        self.DespatchParty = DespatchParty
        self.Contact = Contact
        self.EstimatedDespatchPeriod = EstimatedDespatchPeriod


class DeliveryTerms:
    """
    Teslimat koşulları girilir.
    2.2.16 DeliveryTerms Teslimat Koşulları @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 24/81

    ID              Seçimli(0..1): Teslim koşulları girilir (örneğin CIF, FOB).
    SpecialTerms    Seçimli(0..1): Teslimat koşulları serbest metin olarak girilir.
    Amount          Seçimli(0..1): Teslimat koşullarının kapsadığı tutar girilebilir.

    Örnek
    <cac:DeliveryTerms>
        <cbc:ID>CIF</cbc:ID>
    </cac:DeliveryTerms>
    """

    def __init__(self, ID: str = None, SpecialTerms: str = None, Amount: str = None):
        self.ID_schemeID = 'INCOTERMS'
        self.ID = ID
        self.SpecialTerms = SpecialTerms
        self.Amount = Amount

class Temperature:
    """
    Sıcaklık bilgisi girilir.
    2.2.62 Temperature Sıcaklık @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 75/81

    AttributeID         Zorunlu(1)   : Sıcaklık nitelik numarası girilir.
    Measure             Zorunlu(1)   : Ölçüm girilir.
    Description         Seçimli(0..n): Açıklama girilir.

    Örnek
    <cac:MaximumTemperature>
        <cbc:AttributeID>SICAKLIK</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">10.0</cbc:Measure>
    </cac:MaximumTemperature>
    """

    def __init__(self, AttributeID: str, Measure: str, unitCode: str = 'CEL', Description: str = None):
        self.AttributeID = AttributeID
        self.Measure = Measure
        self.Description = Description
        self.unitCode = unitCode

class Dimension:
    """
    Boyut bilgileri girilir.
    2.2.19 Dimension Boyut

    AttributeID     Zorunlu(1)      : Hangi özelliğin ölçüldüğü girilir.
    Measure         Seçimli(0..1)   : Ölçüm girilir.
    Description     Seçimli(0..n)   : Açıklama girilir.
    MinimumMeasure  Seçimli(0..1)   : Minimum ölçüm girilir.
    MaximumMeasure  Seçimli(0..1)   : Maximum ölçüm girilir.

    Örnek
    <cac:MeasurementDimension>
        <cbc:AttributeID>Uzunluk</cbc:AttributeID>
        <cbc:Measure unitCode="MTR">6.1</cbc:Measure>
    </cac:MeasurementDimension>

    <cac:MeasurementDimension>
        <cbc:AttributeID>Boy</cbc:AttributeID>
        <cbc:Measure unitCode="MTR">2.6</cbc:Measure>
    </cac:MeasurementDimension>

    <cac:MeasurementDimension>
        <cbc:AttributeID>Genişlik</cbc:AttributeID>
        <cbc:Measure unitCode="MTR">2.44</cbc:Measure>
    </cac:MeasurementDimension>
    """

    def __init__(self, AttributeID: str, unitCode: str, Measure: str = None, Description: list = None,
                MinimumMeasure: str = None, MaximumMeasure: str = None):
        self.AttributeID = AttributeID
        self.Measure = Measure
        self.Description = Description
        self.MinimumMeasure = MinimumMeasure
        self.MaximumMeasure = MaximumMeasure
        self.unitCode = unitCode


class GoodsItem:
    """
    Taşıması gerçekleşen mallar hakkındaki bilgileri içerir.
    2.2.27 GoodsItem Taşınan Mal @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 35/81

    ID                                  Seçimli(0..1): İlgili ürünü belge içinde tekil olarak tanımlar.
    Description                         Seçimli(0..n): Serbet metin olarak açıklama girilebilir.
    HazardousRiskIndicator              Seçimli(0..1): Ürün tehlikeli madde kategorisinde sayılıp sayılamayacağını gösteren bilgi.
    DeclaredCustomsValueAmount          Seçimli(0..1): Gümrük değeri tutarı girilir.
    DeclaredForCarriageValueAmount      Seçimli(0..1): Nakliye tutarı (navlun) girilir.
    DeclaredStatisticsValueAmount       Seçimli(0..1): Ürünün GTIP kıymet değeri girilir.
    FreeOnBoardValueAmount              Seçimli(0..1): FOB tutarı girilir.
    InsuranceValueAmount                Seçimli(0..1): Sigorta tutarı girilir.
    ValueAmount                         Seçimli(0..1): Ürünün değeri girilir. Ana seviyedeki Shipment'ın altında kullanımında toplam tutar bilgisi girilebilir.
    GrossWeightMeasure                  Seçimli(0..1): Brüt ağırlığı girilir.
    NetWeightMeasure                    Seçimli(0..1): Net ağırlığı girilir.
    ChargableWeightMeasure              Seçimli(0..1): Belli bir ücretin uygulanabileceği brüt ağırlığı girilir.
    GrossVolumeMeasure                  Seçimli(0..1): Brüt hacim girilir.
    NetVolumeMeasure                    Seçimli(0..1): Net hacim girilir.
    Quantity                            Seçimli(0..1): Miktar girilir.
    RequiredCustomsID                   Seçimli(0..1): Ürünün veya malın GTIP numarası girilir.
    CustomsStatusCode                   Seçimli(0..1): Gümrük durum kodu girilir.
    CustomsTariffQuantity               Seçimli(0..1): İstatistiksel, tarife veya mali amaçlı gümrük mal miktarı girilir.
    CustomsImportClassifiedIndicator    Seçimli(0..1): Malların gümrükte ithalat için sınıflandırılmış olup olmadığını belirtir.
    ChargeableQuantity                  Seçimli(0..1): Belli bir ücretin uygulanabileceği miktar girilir.
    ReturnableQuantity                  Seçimli(0..1): Malların ne kadarının geri gelebileceği girilir.
    TraceID                             Seçimli(0..1): Takip numarası girilir.
    Item                                Seçimli(0..n): Malların fatura kalemleriyle olan ilişkileri girilir. Bknz. Item
    FreightAllowanceCharge              Seçimli(0..n): Taşıma bedelinde indirim/fiyat artırımı var ise girilir. Bknz. AllowanceCharge
    InvoiceLine                         Seçimli(0..n): Birim fiyat ve kalem toplam fiyat bilgileri girilir.
    Temperature                         Seçimli(0..n): Sevkiyattaki mallar ile ilgili her türlü sıcaklık bilgisi girilebilir. Bknz. Temperature
    OriginAddress                       Seçimli(0..1): Ürünlerin üretildiği adres girilir. Bknz. Address
    MeasurementDimension                Seçimli(0..n): Ürünlerin diğer ölçümleri girilir. Bknz. Dimension

    Örnek
    <cac:GoodsItem>
    <cbc:ID>1</cbc:ID>
    <cbc:Description>Buzdolabı</cbc:Description>
    <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
    <cbc:DeclaredCustomsValueAmount
        currencyID="GBP">524.80</cbc:DeclaredCustomsValueAmount>
    <cbc:DeclaredStatisticsValueAmount
        currencyID="USD">1000.00</cbc:DeclaredStatisticsValueAmount>
    <cbc:FreeOnBoardValueAmount
        currencyID="USD">1241.30</cbc:FreeOnBoardValueAmount>
    <cbc:InsuranceValueAmount
        currencyID="USD">1241.30</cbc:InsuranceValueAmount>
    <cbc:ValueAmount
        currencyID="USD">1000.00</cbc:ValueAmount>
    <cbc:GrossWeightMeasure
        unitCode="KGM">130</cbc:GrossWeightMeasure>
    <cbc:NetWeightMeasure
        unitCode="KGM">110</cbc:NetWeightMeasure>
    <cbc:GrossVolumeMeasure
        unitCode="MTQ">2</cbc:GrossVolumeMeasure>
    <cbc:NetVolumeMeasure
        unitCode="MTQ">2.235</cbc:NetVolumeMeasure>
    <cbc:Quantity>10</cbc:Quantity>
    <cbc:RequiredCustomsID>ECN12344566</cbc:RequiredCustomsID>
    <cbc:CustomsStatusCode>Cleared</cbc:CustomsStatusCode>
    <cbc:CustomsTariffQuantity>100</cbc:CustomsTariffQuantity>
</cac:GoodsItem>
    """

    def __init__(self, ID: str = None, Description: Union[str, list] = None, HazardousRiskIndicator: bool = None,
                    DeclaredCustomsValueAmount: str = None, DeclaredStatisticsValueAmount: str = None,
                    FreeOnBoardValueAmount: str = None, InsuranceValueAmount: str = None, ValueAmount: str = None,
                    GrossWeightMeasure: str = None, NetWeightMeasure: str = None, GrossVolumeMeasure: str = None,
                    NetVolumeMeasure: str = None, Quantity: str = None, RequiredCustomsID: str = None,
                    CustomsStatusCode: str = None, CustomsTariffQuantity: str = None, CustomsImportClassifiedIndicator: str = None,
                    ChargeableQuantity: str = None, ReturnableQuantity: str = None, TraceID: str = None, Item: Union[Item, list] = None,
                    FreightAllowanceCharge: Union[AllowanceCharge, list] = None, InvoiceLine: list = None,  # TODO: InvoiceLine, Gerçek InvoiceLine nesnesi kullanılırsa kendisine referans vererek döngüye girebilir?
                    Temperature: Union[Temperature, list] = None, OriginAddress: Address = None, MeasurementDimension: Union[Dimension, list] = None):

        self.ID = ID
        self.Description = Description
        self.HazardousRiskIndicator = HazardousRiskIndicator
        self.DeclaredCustomsValueAmount = DeclaredCustomsValueAmount
        self.DeclaredStatisticsValueAmount = DeclaredStatisticsValueAmount
        self.FreeOnBoardValueAmount = FreeOnBoardValueAmount
        self.InsuranceValueAmount = InsuranceValueAmount
        self.ValueAmount = ValueAmount
        self.GrossWeightMeasure = GrossWeightMeasure
        self.NetWeightMeasure = NetWeightMeasure
        self.GrossVolumeMeasure = GrossVolumeMeasure
        self.NetVolumeMeasure = NetVolumeMeasure
        self.Quantity = Quantity
        self.RequiredCustomsID = RequiredCustomsID
        self.CustomsStatusCode = CustomsStatusCode
        self.CustomsTariffQuantity = CustomsTariffQuantity
        self.CustomsImportClassifiedIndicator = CustomsImportClassifiedIndicator
        self.ChargeableQuantity = ChargeableQuantity
        self.ReturnableQuantity = ReturnableQuantity
        self.TraceID = TraceID
        self.Item = Item
        self.FreightAllowanceCharge = FreightAllowanceCharge
        self.InvoiceLine = InvoiceLine
        self.Temperature = Temperature
        self.OriginAddress = OriginAddress
        self.MeasurementDimension = MeasurementDimension


class Package:
    """
    Taşıma sırasındaki paket bilgisi girilir.
    2.2.40 Package Paket @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 50/81

    ID                          Seçimli(0..1): Paket numarası girilir.
    Quantity                    Seçimli(0..1): Paket adedi girilir.
    ReturnableMaterialIndicator Seçimli(0..1): Paket materyali geri dönüşümlü olup olmadığını belirtir.
    PackageLevelCode            Seçimli(0..1): Paketleme seviyesini belirtir.
    PackagingTypeCode           Seçimli(0..1): Paketleme tipini belirtir.
    PackagingMaterial           Seçimli(0..n): Paketleme materyalini belirtir.
    ContainedPackage            Seçimli(0..n): İçerdiği diğer paketler girilir. Bknz. Package
    GoodsItem                   Seçimli(0..n): İçerdiği ürünler girilir. Bknz. GoodsItem
    MeasurementDimension        Seçimli(0..n): Paket boyutları girilir. Bknz. Dimension

    Örnek
    <cac:Package>
        <cbc:ID>CON_P_1</cbc:ID>
        <cbc:Quantity>10</cbc:Quantity>
        <cbc:PackagingTypeCode>PL</cbc:PackagingTypeCode>
        <cac:GoodsItem>
            <cac:Item>
                <cac:CommodityClassification>
                <cbc:CargoTypeCode>12</cbc:CargoTypeCode>
                </cac:CommodityClassification>
            </cac:Item>
        </cac:GoodsItem>
    </cac:Package>
    """

    def __init__(self, ID: str = None, Quantity: str = None, ReturnableMaterialIndicator: str = None,
                    PackageLevelCode: str = None, PackagingTypeCode: str = None, PackagingMaterial: Union[str, list] = None,
                    ContainedPackage: Any = None, GoodsItem: Union[GoodsItem, list] = None,  # TODO: ContainedPackage list[Package], kendisine referans. Hata alırsak ContainedPackage: list = None yap
                    MeasurementDimension: Optional[List[Dimension]] = None):

        self.ID = ID
        self.Quantity = Quantity
        self.ReturnableMaterialIndicator = ReturnableMaterialIndicator
        self.PackageLevelCode = PackageLevelCode
        self.PackagingTypeCode = PackagingTypeCode
        self.PackagingMaterial = PackagingMaterial
        self.ContainedPackage = ContainedPackage
        self.GoodsItem = GoodsItem
        self.MeasurementDimension = MeasurementDimension

class Stowage:
    """
    İstif yeri bilgisi girilir.
    2.2.56 Stowage İstif Yeri @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 69/81

    LocationID              Seçimli(0..1): İstif yeri mekan numarası girilir.
    Location                Seçimli(0..n): Mekan bilgisi detaylı olarak girilir.
    MeasurementDimension    Seçimli(0..n): İstif yeri ölçüleri girilir. Bknz. Dimension

    Örnek
    <cac:Stowage>
        <cbc:LocationID>111111</cbc:LocationID>
        <cac:MeasurementDimension>
            <cbc:AttributeID>Uzunluk</cbc:AttributeID>
            <cbc:Measure unitCode="MTR">6.1</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
            <cbc:AttributeID>Boy</cbc:AttributeID>
            <cbc:Measure unitCode="MTR">2.6</cbc:Measure>
        </cac:MeasurementDimension>
        <cac:MeasurementDimension>
            <cbc:AttributeID>Genişlik</cbc:AttributeID>
            <cbc:Measure unitCode="MTR">2.44</cbc:Measure>
        </cac:MeasurementDimension>
    </cac:Stowage>
    """

    def __init__(self, LocationID: str = None, Location: Optional[List[Location]] = None, MeasurementDimension: Optional[List[Dimension]] = None):

            self.LocationID = LocationID
            self.Location = Location
            self.MeasurementDimension = MeasurementDimension

class AirTransport:
    """
    Hava taşımacılığında kullanılan hava aracının numarasını tanımlamak için kullanılır.
    2.2.2 AirTransport Hava Taşımacılığı @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 13/81

    AircraftID  Zorunlu(1): Kullanılan hava aracının numarasını tanımlamak için kullanılır.

    Örnek
    <cac:AirTransport>
        <cbc:AircraftID>AB12345</cbc:AircraftID>
    </cac:AirTransport>

    """

    def __init__(self, AircraftID: str):

        self.AircraftID = AircraftID

class RoadTransport:
    """
    Karayolu taşımacılığında kullanılan araç bilgisini içerir.
    2.2.52 RoadTransport Karayolu Taşımacılığı @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 63/81

    LicensePlateID  Zorunlu(1): Plaka numarası girilir.

    Örnek
    <cac:RoadTransport>
        <cbc:LicensePlateID>12345678911</cbc:LicensePlateID>
    </cac:RoadTransport>
    """

    def __init__(self, LicensePlateID: str):

            self.LicensePlateID = LicensePlateID

class RailTransport:
    """
    Tren bilgisini içerir.
    2.2.49 RailTransport Demiryolu Taşımacılığı @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 60/81

    TrainID     Zorunlu(1)      : Tren numarası girilir.
    RailCarID   Seçimli(0..1)   : Vagon numarası girilir.

    Örnek
    <cac:RailTransport>
        <cbc:TrainID>TR111111</cbc:TrainID>
        <cbc:RailCarID>23</cbc:RailCarID>
    </cac:RailTransport >
    """

    def __init__(self, TrainID: str, RailCarID: str = None):

        self.TrainID = TrainID
        self.RailCarID = RailCarID

class MaritimeTransport:
    """
    Deniz taşımacılığındaki gemi bilgileri girilir.
    2.2.36 MaritimeTransport Deniz Taşımacılığı @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 47/81

    VesselID                                Seçimli(0..1): Geminin varsa IMO ve MMSI numarası girilir.
    VesselName                              Seçimli(0..1): Geminin adı girilir.
    RadioCallSignID                         Seçimli(0..1): Geminin radyo çağrı adı girilir.
    ShipsRequirements                       Seçimli(0..n): Geminin ihtiyaçları bu elemana girilir.
    GrossTonnageMeasure                     Seçimli(0..1): Geminin brüt ağırlığı girilir.
    NetTonnageMeasure                       Seçimli(0..1): Geminin net ağırlığı girilir.
    RegistryCertificateDocumentReference    Seçimli(0..1): Geminin kayıt dokümanı referansı girilir. Bknz. DocumentReference
    RegistryPortLocation                    Seçimli(0..1): Geminin kayıt limanı bilgisi girilir. Bknz. Location

    Örnek
    <cac:MaritimeTransport>
        <cbc:VesselID>SomeIMONr</cbc:VesselID>
        <cbc:VesselName>SomeVesselName</cbc:VesselName>
    </cac:MaritimeTransport>
    """

    def __init__(self, VesselID: str = None, VesselName: str = None, RadioCallSignID: str = None,
                ShipsRequirements: Optional[List[str]] = None, GrossTonnageMeasure: str = None,
                NetTonnageMeasure: str = None, RegistryCertificateDocumentReference: DocumentReference = None,
                RegistryPortLocation: Location = None):

        self.VesselID = VesselID
        self.VesselName = VesselName
        self.RadioCallSignID = RadioCallSignID
        self.ShipsRequirements = ShipsRequirements
        self.GrossTonnageMeasure = GrossTonnageMeasure
        self.NetTonnageMeasure = NetTonnageMeasure
        self.RegistryCertificateDocumentReference = RegistryCertificateDocumentReference
        self.RegistryPortLocation = RegistryPortLocation

class TransportMeans:
    """
    Taşıma şekli bilgileri girilir.
    2.2.65 TransportMeans Taşıma Şekli @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 79/81

    JourneyID                   Seçimli(0..1): Seyahat/Sefer numarası girilir.
    RegistrationNationalityID   Seçimli(0..1): Kayıtlı olduğu ülke kodlu olarak girilir.
    RegistrationNationality     Seçimli(0..n): Kayıtlı olduğu ülke serbest metin olarak girilir.
    DirectionCode               Seçimli(0..1): Yön bilgisi kodlu olarak girilir.
    TransportMeansTypeCode      Seçimli(0..1): Taşıma şekli kodlu olarak girilir.
    TradeServiceCode            Seçimli(0..1): Ticaret servisi kodlu olarak girilir.
    Stowage                     Seçimli(0..1): İstifleme bilgisi kodlu olarak girilir. Bknz. Stowage
    AirTransport                Seçimli(0..1): Hava taşımacılığı bilgisi girilir. Bknz. AirTransport
    RoadTransport               Seçimli(0..1): Karayolu taşımacılığı bilgisi girilir. Bknz. RoadTransport
    RailTransport               Seçimli(0..1): Demiryolu taşımacılığı bilgisi girilir. Bknz. RailTransport
    MaritimeTransport           Seçimli(0..1): Deniz taşımacılığı bilgisi girilir. Bknz. MaritimeTransport
    OwnerParty                  Seçimli(0..1): Bu araca sahip olan taraf bilgisi girilir. Bknz. Party
    MeasurementDimension        Seçimli(0..n): Ölçüm bilgileri girilir. Bknz. Dimension

    Örnek
    <cac:TransportMeans>
        <cbc:JourneyID>M22</cbc:JourneyID>
        <cbc:RegistrationNationalityID>DK</cbc:RegistrationNationalityID>
        <cbc:RegistrationNationality>Danimarka</cbc:RegistrationNationality>
        <cbc:TransportMeansTypeCode>83</cbc:TransportMeansTypeCode>
        <cac:MaritimeTransport>
            <cbc:VesselID>1111111</cbc:VesselID>
            <cbc:VesselName>Gemi adı</cbc:VesselName>
        </cac:MaritimeTransport>
    </cac:TransportMeans>

    """

    def __init__(self, JourneyID: str = None, RegistrationNationalityID: str = None,
                RegistrationNationality: Optional[List[str]] = None, DirectionCode: str = None,
                TransportMeansTypeCode: str = None, TradeServiceCode: str = None, Stowage: Stowage = None,
                AirTransport: AirTransport = None, RoadTransport: RoadTransport = None,
                RailTransport: RailTransport = None, MaritimeTransport: MaritimeTransport = None,
                OwnerParty: Party = None, MeasurementDimension: Optional[List[Dimension]] = None):

        self.JourneyID = JourneyID
        self.RegistrationNationalityID = RegistrationNationalityID
        self.RegistrationNationality = RegistrationNationality
        self.DirectionCode = DirectionCode
        self.TransportMeansTypeCode = TransportMeansTypeCode
        self.TradeServiceCode = TradeServiceCode
        self.Stowage = Stowage
        self.AirTransport = AirTransport
        self.RoadTransport = RoadTransport
        self.RailTransport = RailTransport
        self.MaritimeTransport = MaritimeTransport
        self.OwnerParty = OwnerParty
        self.MeasurementDimension = MeasurementDimension

class TransportEquipment:
    """
    Taşıma ekipmanı bilgileri girilir.
    2.2.63 TransportEquipment Taşıma Ekipmanı

    ID                          Seçimli(0..1): Tekil numarası girilir. Örneğin Dorse Plaka numarası.
    TransportEquipmentTypeCode  Seçimli(0..1): Ekipman tipi kodu girilir.
    Description                 Seçimli(0..1): Serbest metin açıklama girilir.

    Örnek
    <cac:TransportEquipment>
        <cbc:ID schemeID="DORSEPLAKA">06DR4049</cbc:ID>
        <cbc:TransportEquipmentTypeCode>BPO</cbc:TransportEquipmentTypeCode>
    </cac:TransportEquipment>

    Ek parametre: ID schemeID
    """

    def __init__(self, ID: str = None, TransportEquipmentTypeCode: str = None, Description: str = None, ID_schemeID: str = None):
        self.ID = ID
        self.TransportEquipmentTypeCode = TransportEquipmentTypeCode
        self.Description = Description
        self.ID_schemeID = ID_schemeID

class HazardousGoodsTransit:
    """
    Taşıma sırasındaki tehlikeli malları anlatır.
    2.2.28 HazardousGoodsTransit Tehlikeli Mal @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 37/81

    TransportEmergencyCardCode  Seçimli(0..1): Taşıma sırasında her hangi bir tehlikeli durum olması durumunda nasıl müdahale edileceğini anlatan kod girilebilir.
    PackagingCriteriaCode       Seçimli(0..1): Paketleme kriterleri kodu girilir.
    HazardousRegulationCode     Seçimli(0..1): Ürünün taşımasına yönelik kanun ve kuralları belirten kod girilir.
    InhalationToxicityZoneCode  Seçimli(0..1): ABD Ulaştırma Bakanlığı tarafından belirlenen Tehlikeli Maddeler için Soluma Toksisitesi Tehlike Bölgesini belirten kod girilir.
    TransportAuthorizationCode  Seçimli(0..1): Tehlikeli kargonun taşınmasının yetki kodu girilir.
    MaximumTemperature          Seçimli(0..1): Ürünü güvenle taşınması için gerekli maximum sıcaklık girilir. Bknz. Temperature
    MinimumTemperature          Seçimli(0..1): Ürünü güvenle taşınması için gerekli minimum sıcaklık girilir. Bknz. Temperature

    Örnek
    <cac:HazardousGoodsTransit>
        <cbc:TransportEmergencyCardCode>[CODE]</cbc:TransportEmergencyCardCode>
        <cbc:PackingCriteriaCode>[CODE]</cbc:PackingCriteriaCode>
        <cbc:HazardousRegulationCode>[CODE]</cbc:HazardousRegulationCode>
        <cbc:InhalationToxicityZoneCode>[CODE]</cbc:InhalationToxicityZoneCode>
        <cbc:TransportAuthorizationCode>[CODE]</cbc:TransportAuthorizationCode>
        <cac:MaximumTemperature>
            <cbc:AttributeID>SICAKLIK</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">100.0</cbc:Measure>
        </cac:MaximumTemperature>
        <cac:MinimumTemperature>
            <cbc:AttributeID>SICAKLIK </cbc:AttributeID>
            <cbc:Measure unitCode="CEL">10.0</cbc:Measure>
        </cac:MinimumTemperature>
    </cac:HazardousGoodsTransit>
    """

    def __init__(self, TransportEmergencyCardCode: str = None, PackagingCriteriaCode: str = None,
                    HazardousRegulationCode: str = None, InhalationToxicityZoneCode: str = None,
                    TransportAuthorizationCode: str = None, MaximumTemperature: Temperature = None,
                    MinimumTemperature: Temperature = None):

        self.TransportEmergencyCardCode = TransportEmergencyCardCode
        self.PackagingCriteriaCode = PackagingCriteriaCode
        self.HazardousRegulationCode = HazardousRegulationCode
        self.InhalationToxicityZoneCode = InhalationToxicityZoneCode
        self.TransportAuthorizationCode = TransportAuthorizationCode
        self.MaximumTemperature = MaximumTemperature
        self.MinimumTemperature = MinimumTemperature

class CustomsDeclaration:
    """
    Ürün hakkında gümrük numaralandırma bilgisi girilir.
    2.2.14 CustomsDeclaration Gümrük Kimliği @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 22/81

    ID              Zorunlu(1)      : Ürünün ilgili gümrük numarası girilir.
    IssuerParty     Seçimli(0..1)   : Numaralandırmayı yapan kurum bilgisi girilir.

    Örnek
    <cac:CustomsIdentification>
        <cbc:ID>1288331</cbc:ID>
    </cac:CustomsIdentification>
    """

    def __init__(self, ID: str, IssuerParty: Party = None):
        self.ID = ID
        self.IssuerParty = IssuerParty  # TODO: Tip Party mi serbest metin mi?

class TransportHandlingUnit:
    """
    Taşıma ünitesi hakkında detaylı bilgi girilir.
    2.2.64 TransportHandlingUnit Taşıma Yükleme-Boşaltma Üniteleri @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 76/81

    ID                              Seçimli(0..1): Taşıma ünitesi numarası girilir.
    TransportHandlingUnitTypeCode   Seçimli(0..1): Taşıma ünitesi tipi kodlu olarak girilir.
    HandlingCode                    Seçimli(0..1): Nasıl paketlenip taşınacağı kodlu olarak tanımlar.
    HandlingInstructions            Seçimli(0..1): Nasıl paketlenip taşınacağıserbest metin olarak tanımlar.
    HazardousRiskIndicator          Seçimli(0..1): Tehlikeli madde içerip içermediğini belirtir.
    TotalGoodsItemQuantity          Seçimli(0..1): Toplam ürün miktarı girilir.
    TotalPackageQuantity            Seçimli(0..1): Toplam paket miktarı girilir.
    DamageRemarks                   Seçimli(0..n): Zarar bilgisi girilir.
    TraceID                         Seçimli(0..1): Takip numarası girilir.
    ActualPackage                   Seçimli(0..n): İçerdiği paket bilgileri girilir. Bknz. Package
    TransportEquipment              Seçimli(0..n): Ekipman bilgisi girilir. Bknz. TransportEquipment
    TransportMeans                  Seçimli(0..n): Taşıma şekli bilgisi girilir. Bknz. TransportMeans.
    HazardousGoodsTransit           Seçimli(0..n): Taşıma sırasındaki tehlikeli malların bilgisi girilir. Bknz. HazardousGoodsTransit
    MeasurementDimension            Seçimli(0..n): Taşıma ünitesi ölçüleri girilir. Bknz. Dimension
    MinimumTemperature              Seçimli(0..1): Taşıma ünitesi için maksimum sıcaklık girilir. Bknz.Temperature
    MaximumTemperature              Seçimli(0..1): Taşıma ünitesi için minimum sıcaklık girilir. Bknz.Temperature
    FloorSpaceMeasurementDimension  Seçimli(0..1): Yerde kapladığı alan bilgisi girilir. Bknz. Dimension
    PalletSpaceMeasurementDimension Seçimli(0..1): Palette kapladığı alan blgisi girilir. Bknz. Dimension
    ShipmentDocumentReference       Seçimli(0..n): İlgili gönderi belgesine referans girilir. Bknz. DocumentReference
    CustomsDeclaration              Seçimli(0..n): Gümrük numaralandırma bilgisi girilir. Bknz. CustomsDeclaration

    Örnek
    <cac:TransportHandlingUnit>
        <cbc:ID>CON_THU_2</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode>4</cbc:TransportHandlingUnitTypeCode>
        <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
        <cbc:TotalGoodsItemQuantity>500</cbc:TotalGoodsItemQuantity>
        <cbc:TotalPackageQuantity>10</cbc:TotalPackageQuantity>
        <cbc:ShippingMarks>Genel kargo</cbc:ShippingMarks>
        <cac:TransportEquipment>
        <cbc:ID>CON_TE_2</cbc:ID>
        <cbc:TransportEquipmentTypeCode>CN</cbc:TransportEquipmentTypeCode>
        </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
    """

    def __init__(self, ID: str = None, TransportHandlingUnitTypeCode: str = None, HandlingCode: str = None,
                HandlingInstructions: str = None, HazardousRiskIndicator: bool = None, TotalGoodsItemQuantity: int = None,
                TotalPackageQuantity: int = None, DamageRemarks: str = None, TraceID: str = None, ActualPackage: Package = None,
                TransportEquipment: TransportEquipment = None, TransportMeans: TransportMeans = None,
                HazardousGoodsTransit: HazardousGoodsTransit = None, MeasurementDimension: Dimension = None,
                MinimumTemperature: Temperature = None, MaximumTemperature: Temperature = None,
                FloorSpaceMeasurementDimension: Dimension = None, PalletSpaceMeasurementDimension: Dimension = None,
                ShipmentDocumentReference: DocumentReference = None, CustomsDeclaration: CustomsDeclaration = None):
        self.ID = ID
        self.TransportHandlingUnitTypeCode = TransportHandlingUnitTypeCode
        self.HandlingCode = HandlingCode
        self.HandlingInstructions = HandlingInstructions
        self.HazardousRiskIndicator = HazardousRiskIndicator
        self.TotalGoodsItemQuantity = TotalGoodsItemQuantity
        self.TotalPackageQuantity = TotalPackageQuantity
        self.DamageRemarks = DamageRemarks
        self.TraceID = TraceID
        self.ActualPackage = ActualPackage
        self.TransportEquipment = TransportEquipment
        self.TransportMeans = TransportMeans
        self.HazardousGoodsTransit = HazardousGoodsTransit
        self.MeasurementDimension = MeasurementDimension
        self.MinimumTemperature = MinimumTemperature
        self.MaximumTemperature = MaximumTemperature
        self.FloorSpaceMeasurementDimension = FloorSpaceMeasurementDimension
        self.PalletSpaceMeasurementDimension = PalletSpaceMeasurementDimension
        self.ShipmentDocumentReference = ShipmentDocumentReference
        self.CustomsDeclaration = CustomsDeclaration

class Shipment:
    """
    Gönderi (Kargo) bilgileri girilir.
    2.2.53 Shipment Gönderi @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 64/81


    ID                                  Zorunlu(1)   : Kargo numarası girilir.
    HandlingCode                        Seçimli(0..1): Kargonun nasıl paketlenip taşınacağı kodlu olarak tanımlar (örneğin kırılacak mal).
    HandlingInstructions                Seçimli(0..1): Kargonun nasıl paketlenip taşınacağı serbest metin olarak tanımlar.
    GrossWeightMeasure                  Seçimli(0..1): Brüt ağırlık girilir.
    NetWeightMeasure                    Seçimli(0..1): Net ağırlık girilir.
    GrossVolumeMeasure                  Seçimli(0..1): Brüt hacim girilir.
    NetVolumeMeasure                    Seçimli(0..1): Net hacim girilir.
    TotalGoodsItemQuantity              Seçimli(0..1): Toplam mal miktarı girilir.
    TotalTransportHandlingUnitQuantity  Seçimli(0..1): Toplam taşıma ünitesi miktarı girilir.
    InsuranceValueAmount                Seçimli(0..1): Sigorta tutarı girilir.
    DeclaredCustomsValueAmount          Seçimli(0..1): Beyan edilen gümrük değeri tutarı girilir.
    DeclaredForCarriageValueAmount      Seçimli(0..1): Beyan edilen taşıma ücreti (navlun) girilir.
    DeclaredStatisticsValueAmount       Seçimli(0..1): Ürünün GTIP kıymet değeri girilir.
    FreeOnBoardValueAmount              Seçimli(0..1): FOB değeri girilir.
    SpecialInstructions                 Seçimli(0..n): Özel talimatlar serbest metin olarak girilir.
    GoodsItem                           Seçimli(0..n): DespatchLine/Shipment elemanı içerisinde kullanımında fiyat bilgileri girilir.
    ShipmentStage                       Seçimli(0..n): Gönderinin hangi aşamada olduğu bilgisi girilir. Ayrıca taşıyıcı (plaka, şoför) gibi detay bilgiler girilir.
                                                        (TransportModeCode elemanı havayolu, karayolu gibi, gönderinin hangi modda gönderildiği bilgisini içerir)
    Delivery                            Seçimli(0..1): DespatchAdvice dokümanı içerisinde kullanımında taşıyıcı firma, fiili sevk tarihi ve asıl teslim tarihi bilgileri girilir.
    TransportHandlingUnit               Seçimli(0..n): Taşıma üniteleri bilgisi girilir. Bknz. TransportHandlingUnit
    ReturnAddress                       Seçimli(0..1): Ürünlerin geri iade edileceği adres girilir. Bknz. Address
    FirstArrivalPortLocation            Seçimli(0..1): İlk ulaşım limanı girilir. Bknz. Location
    LastExitPortLocation                Seçimli(0..1): Son çıkış limanı girilir. Bknz. Location

    Örnek
    <cac:Shipment>
        <cbc:ID/>
        <cbc:GrossWeightMeasure unitCode="KGM">14444</cbc:GrossWeightMeasure>
        <cbc:NetWeightMeasure unitCode="KGM">14414</cbc:NetWeightMeasure>
        <cbc:TotalTransportHandlingUnitQuantity>21</cbc:TotalTransportHandlingUnitQuantity>
        <cbc:InsuranceValueAmount currencyID="USD">150</cbc:InsuranceValueAmount>
        <cbc:DeclaredForCarriageValueAmount currencyID="USD">3900</cbc:DeclaredForCarriageValueAmount>
    </cac:Shipment>
    """

    def __init__(self, ID: str, HandlingCode: str = None, HandlingInstructions: str = None, GrossWeightMeasure: str = None,
                    NetWeightMeasure: str = None, GrossVolumeMeasure: str = None, NetVolumeMeasure: str = None,
                    TotalGoodsItemQuantity: str = None, TotalTransportHandlingUnitQuantity: str = None,
                    InsuranceValueAmount: str = None, DeclaredCustomsValueAmount: str = None,
                    DeclaredForCarriageValueAmount: str = None, DeclaredStatisticsValueAmount: str = None,
                    FreeOnBoardValueAmount: str = None, SpecialInstructions: list = None, GoodsItem: list = None,
                    ShipmentStage: list = None, Delivery: any = None, TransportHandlingUnit: list = None,
                    ReturnAddress: Address = None, FirstArrivalPortLocation: Location = None, LastExitPortLocation: Location = None):
        self.ID = ID
        self.HandlingCode = HandlingCode
        self.HandlingInstructions = HandlingInstructions
        self.GrossWeightMeasure = GrossWeightMeasure
        self.NetWeightMeasure = NetWeightMeasure
        self.GrossVolumeMeasure = GrossVolumeMeasure
        self.NetVolumeMeasure = NetVolumeMeasure
        self.TotalGoodsItemQuantity = TotalGoodsItemQuantity
        self.TotalTransportHandlingUnitQuantity = TotalTransportHandlingUnitQuantity
        self.InsuranceValueAmount = InsuranceValueAmount
        self.DeclaredCustomsValueAmount = DeclaredCustomsValueAmount
        self.DeclaredForCarriageValueAmount = DeclaredForCarriageValueAmount
        self.DeclaredStatisticsValueAmount = DeclaredStatisticsValueAmount
        self.FreeOnBoardValueAmount = FreeOnBoardValueAmount
        self.SpecialInstructions = SpecialInstructions
        self.GoodsItem = GoodsItem
        self.ShipmentStage = ShipmentStage
        self.Delivery = Delivery
        self.TransportHandlingUnit = TransportHandlingUnit
        self.ReturnAddress = ReturnAddress
        self.FirstArrivalPortLocation = FirstArrivalPortLocation
        self.LastExitPortLocation = LastExitPortLocation


class Delivery:
    """
    Ürün tesliman bilgileri detaylı olarak girilir.
    2.2.15 Delivery Gönderim, Taşıma, Sevkiyat Bilgileri @ UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 23/81

    ID                          Seçimli(0..1): Teslimatı belge içerisinde tekil olarak tanımlar.
    Quantity                    Seçimli(0..1): Ürün miktarı girilir.
    ActualDeliveryDate          Seçimli(0..1): Gerçekleşen teslim tarihi yazılır.
    ActualDeliveryTime          Seçimli(0..1): Gerçekleşen teslim zamanı yazılır.
    LatestDeliveryDate          Seçimli(0..1): Son teslim tarihi girilir.
    LatestDeliveryTime          Seçimli(0..1): Son teslim zamanı girilir.
    TrackingID                  Seçimli(0..1): Takip numarası girilir.
    DeliveryAddress             Seçimli(0..1): Teslimat adresi girilir. Bknz. Address.
    AlternativeDeliveryLocation Seçimli(0..1): Alternatif teslim yeri girilir. Bknz. Location.
    EstimatedDeliveryPeriod     Seçimli(0..1): Tahmini teslim dönemi girilir. Bknz. Period
    CarrierParty                Seçimli(0..1): Taşıyıcı taraf girilir. Bknz. Party
    DeliveryParty               Seçimli(0..1): Teslimat yapılacak (ürünleri teslim alacak) taraf girilir. Bknz. Party
    Despatch                    Seçimli(0..1): Gönderi bilgisi girilir. Bknz. Despatch
    DeliveryTerms               Seçimli(0..n): Teslimat şartları girilir. Bknz. DeliveryTerms
    Shipment                    Seçimli(0..1): Yük/kargo bilgileri girilir. Bknz. Shipment

    Örnek
    <cac:Delivery>
        <cac:DeliveryAddress>
            <cbc:ID/>
            <cbc:CitySubdivisionName/>
            <cbc:CityName>Bakü</cbc:CityName>
            <cac:Country>
                <cbc:Name>Azerbaycan</cbc:Name>
            </cac:Country>
        </cac:DeliveryAddress>
        <cac:CarrierParty>
            <cac:PartyIdentification>
                <cbc:ID/>
            </cac:PartyIdentification>
            <cac:PartyName>
            <cbc:Name>AAA Nakliyat</cbc:Name>
            </cac:PartyName>
            <cac:PostalAddress>
            <cbc:ID/>
            <cbc:CitySubdivisionName/>
            <cbc:CityName/>
            <cac:Country>
            <cbc:Name>Türkiye</cbc:Name>
            </cac:Country>
            </cac:PostalAddress>
        </cac:CarrierParty>
        <cac:DeliveryTerms>
        <cbc:ID>CIF</cbc:ID>
        </cac:DeliveryTerms>
        <cac:Shipment>
        <cbc:ID/>
        <cbc:GrossWeightMeasure unitCode="KGM">14444</cbc:GrossWeightMeasure>
        <cbc:NetWeightMeasure unitCode="KGM">14414</cbc:NetWeightMeasure>
        <cbc:TotalTransportHandlingUnitQuantity>21</cbc:TotalTransportHandlingUnitQuantity>
        <cbc:InsuranceValueAmount currencyID="USD">150</cbc:InsuranceValueAmount>
        <cbc:DeclaredForCarriageValueAmount currencyID="USD">3900</cbc:DeclaredForCarriageValueAmount>
        </cac:Shipment>
    </cac:Delivery>
    """

    def __init__(self, ID: str = None, Quantity: str = None, ActualDeliveryDate: str = None, ActualDeliveryTime: str = None,
                LatestDeliveryDate: str = None, LatestDeliveryTime: str = None, TrackingID: str = None, DeliveryAddress: Address = None,
                AlternativeDeliveryLocation: Location = None, EstimatedDeliveryPeriod: Period = None, CarrierParty: Party = None,
                DeliveryParty: Party = None, Despatch: Despatch = None, DeliveryTerms: DeliveryTerms = None, Shipment: Shipment = None):
        self.ID = ID
        self.Quantity = Quantity
        self.ActualDeliveryDate = ActualDeliveryDate
        self.ActualDeliveryTime = ActualDeliveryTime
        self.LatestDeliveryDate = LatestDeliveryDate
        self.LatestDeliveryTime = LatestDeliveryTime
        self.TrackingID = TrackingID
        self.DeliveryAddress = DeliveryAddress
        self.AlternativeDeliveryLocation = AlternativeDeliveryLocation
        self.EstimatedDeliveryPeriod = EstimatedDeliveryPeriod
        self.CarrierParty = CarrierParty
        self.DeliveryParty = DeliveryParty
        self.Despatch = Despatch
        self.DeliveryTerms = DeliveryTerms
        self.Shipment = Shipment

class Price:
    """
    Mal/hizmetin birim fiyatı girilir.
    2.2.48 Price Fiyat

    PriceAmount Zorunlu(1): Mal/hizmetin birim fiyatı nümerik olarak girilir.

    Örnek
    <cac:Price>
        <cbc:PriceAmount currencyID="TRY">60</cbc:PriceAmount>
    </cac:Price>
    """

    def __init__(self, PriceAmount: str = None, currencyID: str = "TRY"):
        self.PriceAmount = PriceAmount
        self.currencyID = currencyID

class InvoiceLine:
    """
    Belgede geçen mal/hizmete ilişkin bilgilerin girildiği elemandır.

    Ortak Sınıflar 2.2.29 InvoiceLine Mal/Hizmet Kalemleri, UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 41/81

    ID                      Zorunlu(1)      : Kalem sıra numarası girilir.
    Note                    Seçimli(0..1)   : Kalem hakkında açıklama serbest metin olarak girilir.
    InvoicedQuantity        Zorunlu(1)      : Mal/hizmet miktarı birimi ile birlikte girilir. Bknz. Kod Listeleri.
    LineExtensionAmount     Zorunlu(1)      : Mal/hizmet miktarı ile Mal/hizmet birim fiyatının çarpımı ile bulunan tutardır (varsa iskonto düşülür).
    OrderLineReference      Seçimli(0..n)   : Fatura ile ilişkili sipariş dokümanının kalemlerine referans atmak için kullanılır. Bknz. OrderLineReference
    DespatchLineReference   Seçimli(0..n)   : Fatura ile ilişkili irsaliye dokümanının kalemlerine referans atmak için kullanılır. Bknz. LineReference
    ReceiptLineReference    Seçimli(0..n)   : Fatura ile ilişkili alındı dokümanının kalemlerine referans atmak için kullanılır. Bknz. LineReference
    Delivery                Seçimli(0..n)   : Kalem bazlı teslimat olması durumunda bu eleman doldurulur. Bknz. Delivery
    AllowanceCharge         Seçimli(0..n)   : Kalem bazlı ıskonto/artırım tutarıdır. Bknz. AllowanceCharge.
    TaxTotal                Seçimli(0..1)   : Kalem bazlı vergi bilgilerinin girildiği elemandır. Bknz. TaxTotal.
    WithholdingTaxTotal     Seçimli(0..n)   : Kalem bazlı tevkifat uygulanması durumunda bu eleman kullanılır. Bknz. TaxTotal
    Item                    Zorunlu(1)      : Mal/hizmet hakkında bilgiler buraya girilir. Bknz. Item.
    Price                   Zorunlu(1)      : Mal/hizmet birim fiyatı hakkında bilgiler buraya girilir. Bknz. Price.
    SubInvoiceLine          Seçimli(0..n)   : Eğer ürün için ek bir birim kodu kullanılması gerekiyorsa bu elemanın içindeki
                                                InvoicedQuantity elemanı (diğer opsiyonel elemanlar boş bırakılarak) kullanılabilir. Bknz. InvoiceLine

    Olası ek parametreler:
        - InvoicedQuantity unitCode
        - * currencyID

    <cac:InvoiceLine>
        <cbc:ID>1</cbc:ID>
        <cbc:InvoicedQuantity unitCode=”BX”>30</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="TRY">1800</cbc:LineExtensionAmount>
            <cac:Item>
            <cbc:Name>Notebook Çantası</cbc:Name>
                <cac:SellersItemIdentification>
                    <cbc:ID>1234567</cbc:ID>
                </cac:SellersItemIdentification>
            </cac:Item>
        <cac:Price>
            <cbc:PriceAmount currencyID="TRY">60</cbc:PriceAmount>
        </cac:Price>
    </cac:InvoiceLine>

    <cac:InvoiceLine>
        <cbc:ID>1</cbc:ID>
        <cbc:InvoicedQuantity unitCode="C62">1</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="TRY">19999</cbc:LineExtensionAmount>
        <cac:TaxTotal>
            <cbc:TaxAmount currencyID="TRY">3599.82</cbc:TaxAmount>
            <cac:TaxSubtotal>
                <cbc:TaxableAmount currencyID="TRY">19999</cbc:TaxableAmount>
                <cbc:TaxAmount currencyID="TRY">3599.82</cbc:TaxAmount>
                <cbc:Percent>18</cbc:Percent>
                <cac:TaxCategory>
                    <cac:TaxScheme>
                        <cbc:Name>GERÇEK USULDE KATMA DEĞER VERGİSİ</cbc:Name>
                        <cbc:TaxTypeCode>0015</cbc:TaxTypeCode>
                    </cac:TaxScheme>
                </cac:TaxCategory>
            </cac:TaxSubtotal>
        </cac:TaxTotal>
        <cac:Item>
            <cbc:Name>Philips EP5443/70 Lattego Tam Otomatik Kahve ve Espresso Makinesi</cbc:Name>
            <cac:SellersItemIdentification>
                <cbc:ID>HBCV00000PN2T3</cbc:ID>
            </cac:SellersItemIdentification>
        </cac:Item>
        <cac:Price>
            <cbc:PriceAmount currencyID="TRY">19999</cbc:PriceAmount>
        </cac:Price>
    </cac:InvoiceLine>
    """

    def __init__(self, ID: str, InvoicedQuantity: str, InvoicedQuantity_unitCode: str, LineExtensionAmount: str, Item: Item,
                Price: Price, Note: str = None, OrderLineReference: list = None, DespatchLineReference: list = None,
                ReceiptLineReference: list = None, Delivery: list = None, AllowanceCharge: Union[AllowanceCharge, list] = None, TaxTotal: TaxTotal = None,
                WithholdingTaxTotal: list = None, SubInvoiceLine: list = None, currencyID: str = "TRY"):  # TODO: Default döküman currencyID'si kullanılabilir.
        self.ID = ID
        self.InvoicedQuantity = InvoicedQuantity
        self.InvoicedQuantity_unitCode = InvoicedQuantity_unitCode
        self.LineExtensionAmount = LineExtensionAmount
        self.Note = Note
        self.OrderLineReference = OrderLineReference
        self.DespatchLineReference = DespatchLineReference
        self.ReceiptLineReference = ReceiptLineReference
        self.Delivery = Delivery
        self.AllowanceCharge = AllowanceCharge
        self.TaxTotal = TaxTotal
        self.WithholdingTaxTotal = WithholdingTaxTotal
        self.Item = Item
        self.Price = Price
        self.SubInvoiceLine = SubInvoiceLine
        self.currencyID = currencyID

class UBLInvoice:
    def __init__(self):
        self.root = etree.Element("Invoice", nsmap={
            None: "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2",
            "xsd": "http://www.w3.org/2001/XMLSchema",
            "ext": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
            "cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "cac": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
        })

        # InputDocument nesnesine eklenmesi gereken alanlar.
        # Bazıları Xml'e eklenmiyor.

        self.id = None
        self.uuid = None
        self.issue_date = None
        self.issue_time = None
        self.local_id = None        # XML'e eklenmiyor.
        self.sourceUrn = None       # XML'e eklenmiyor.
        self.destinationUrn = None  # XML'e eklenmiyor.
        # -------------------------
        self.profile_id = None
        self.copy_indicator = None
        self.invoice_type_code = None
        self.note = None
        self.document_currency_code = None
        self.line_count_numeric = None
        self.despatch_document_reference = None

    def xml(self):
        return etree.tostring(self.root, pretty_print=True, encoding='unicode')

    def add_ubl_extension(self):
        """
        2.3.1 UBLExtensions
        UBLExtensions       : UBL Genişletme Alanı
        Diyagram            : ext:UBLExtensions
        Kardinalite         : Zorunlu(1..n)
        Açıklama            : Bu alana XAdES formatında mali mühür/ elektronik imza bilgileri yazılacaktır.
        Kullanım            : Bknz. Ortak Sınıflar: UBLExtension

        :return:
        """
        ubl_extensions = etree.SubElement(
            self.root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}UBLExtensions"
        )
        ubl_extension = etree.SubElement(
            ubl_extensions, "{urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}UBLExtension"
        )
        extension_content = etree.SubElement(
            ubl_extension, "{urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2}ExtensionContent"
        )
        auto_generated_wildcard = etree.SubElement(extension_content, "auto-generated-wildcard")

    def add_ubl_version_id(self, version_id_str: str = "2.1"):
        """
        2.3.2 UBLVersionID
        UBLVersionID        : UBL Versiyon Numarası
        Diyagram            : cbc:UBLVersionID
        Kardinalite         : Zorunlu (1)
        Açıklama            : XSD dokümanının UBL versiyonu yazılacaktır.
        Kullanım            : Bu değer için “2.1” kullanılacaktır.
        Örnek <cbc:UBLVersionID>2.1</cbc:UBLVersionID>

        :param version_id_str:
        :return:
        """

        ubl_version_id = etree.SubElement(
            self.root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}UBLVersionID"
        )
        ubl_version_id.text = version_id_str

    def add_customisation_id(self, customisation_id_text: str = "TR1.2"):
        """
        2.3.3 CustomizationID
        CustomizationID     : Özelleştirme Numarası
        Diyagram            : cbc:CustomizationID
        Kardinalite         : Zorunlu (1)
        Açıklama            : UBL’in özelleştirme numarasıdır.
        Kullanım:           : Bu değer için “TR1.2” kullanılacaktır.
        Örnek               : <cbc:CustomizationID>TR1.2</cbc:CustomizationID>

        :param customisation_id_text:
        :return:
        """
        customization_id = etree.SubElement(
            self.root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CustomizationID"
        )
        customization_id.text = customisation_id_text

    def add_profile_id(self, profile_id_text: str = "TEMELFATURA"):
        """
        2.3.4 ProfileID
        ProfileID       : Senaryo
        Diyagram        : cbc:ProfileID
        Kardinalite     : Zorunlu (1)
        Açıklama        : Kullanılan senaryodur.
        Kullanım:       : Bknz. Kod Listeleri
        Örnek           :
        <cbc:ProfileID>TEMELFATURA</cbc: ProfileID>

        Dokümanın ait olduğu süreci tanımlamak için “/Invoice/ProfileID” elemanı kullanılmaktadır.
        “ProfileID” elemanı aşağıdaki tabloda yer alan değerleri alabilir.

        Senaryo Adı             Açıklama
        ----------------------  ------------------------------------------------------------
        TEMELFATURA             Temel Fatura sürecini belirtir.
        TICARIFATURA            Ticari Fatura sürecini belirtir.
        YOLCUBERABERFATURA      Yolcu Beraber Eşya Fatura sürecini belirtir.
        EARSIVFATURA            e-Arşiv Fatura sürecini belirtir.
        IHRACAT                 İhracat Fatura sürecini belirtir.

        :param profile_id_text:
        :return:

        """
        profile_id = etree.SubElement(
            self.root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ProfileID"
        )
        profile_id.text = profile_id_text

    def add_id(self, id_text: str):
        """"
        2.3.5 ID
        ID              :   Fatura Numarası
        Diyagram        :   cbc:ID
        Kardinalite     :   Zorunlu (1)
        Açıklama        :   Üç haneli alfanumerik birim kod ile 13 haneli müteselsil numaranın birleşiminden
                            meydana gelen Fatura Numarası bu elemana yazılacaktır. Müteselsil numaranın ilk dört hanesi
                            faturanın düzenlendiği yılı kalan dokuz hane ise müteselsil numarayı ifade etmektedir.
                            Fatura düzenleyen bünyesinde aynı fatura numarası birden fazla kullanılamaz.
        Kullanım        :   Alfanumerik
        Örnek           :   <cbc:ID>GIB2009000000001</cbc:ID>

        Atamadan önce kontrolden geçirelim, en azından fatura yılı ile başlamalı.

        :param id_text: Invoice number, eg. GIB20230105103023
        :return: None
        """
        # Create the ID element
        id = etree.SubElement(self.root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID")
        id.text = id_text

        self.id = id_text

    def add_copy_indicator(self, copy_indicator_text: str = "false"):
        """
        2.3.6 CopyIndicator
        CopyIndicator   : Asıl/Suret
        Diyagram        : cbc:CopyIndicator
        Kardinalite     : Zorunlu (1)
        Açıklama        : Bu elemanda düzenlenen faturanın asıl veya suret olduğu gösterilecektir.
        Kullanım        : Asıl ise “false”, suret ise “true”
        Örnek           : <cbc:CopyIndicator>true</cbc:CopyIndicator>

        :param copy_indicator_text:
        :return:
        """
        # Create the CopyIndicator element
        copy_indicator = etree.SubElement(
            self.root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CopyIndicator"
        )
        copy_indicator.text = copy_indicator_text

    def add_uuid(self, uuid_text: str = None):
        """
        2.3.7 UUID
        UUID            :   Evrensel Tekil Tanımlama Numarası
        Diyagram        :   cbc:UUID
        Kardinalite     :   Zorunlu (1)
        Açıklama        :   Evrensel Tekil Tanımlama Numarası (ETTN), düzenlenen faturanın evrensel eşsizliğini sağlayan
                            numaradır. Bu numara fatura düzenleyen tarafından standartlara uygun olarak üretilip
                            faturalarda kullanılacaktır.
        Kullanım        :   GUID formatı
        Örnek           :   <cbc:UUID>e093a490-dd99-11dd-ad8b-0800200c9a66</cbc:UUID>

        TODO: UUID testinden geçir.
        :param uuid_text:
        :return:
        """
        if not uuid_text:
            from uuid import uuid4
            uuid_text = str(uuid4())

        uuid = etree.SubElement(
            self.root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}UUID"
        )
        uuid.text = uuid_text

        self.uuid = uuid_text

    def add_issue_date(self, issue_date_text: str):
        """
        2.3.8 IssueDate
        IssueDate       : Düzenleme Tarihi
        Diyagram        : cbc:IssueDate
        Kardinalite     : Zorunlu (1)
        Açıklama        : Bu elemana faturanın düzenleme tarihi yazılacaktır.
        Kullanım        : Yıl-Ay-Gün (YYYY-AA-GG)
        Örnek           : <cbc:IssueDate>2009-01-01</cbc:IssueDate>

        ISO 8601 formatında olmalı. Kontrolden geçir yada dönüştür.
        :param issue_date_text: ISO 8601 format, eg. 2021-01-01
        :return:
        """

        issue_date = etree.SubElement(
            self.root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IssueDate"
        )
        issue_date.text = issue_date_text

        self.issue_date = issue_date_text

    def add_issue_time(self, issue_time_text: str):
        """
        2.3.9 IssueTime
        IssueTime       : Düzenleme Zamanı
        Diyagram        : cbc:IssueTime
        Kardinalite     : Seçimli (0…1)
        Açıklama        : Bu elemana faturanın düzenleme saati yazılabilecektir.
        Kullanım        : Saat:Dakika:Saniye
        Örnek           : <cbc:IssueTime>14:50:00</cbc:IssueTime>

        Not: 24 saat formatında.
        :param issue_time_text:
        :return:
        """

        issue_time = etree.SubElement(
            self.root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IssueTime"
        )
        issue_time.text = issue_time_text

    #
    def add_invoice_type_code(self, invoice_type_code_text: str):
        """
        2.3.10 InvoiceTypeCode
        InvoiceTypeCode     : Fatura Tip Kodu
        Diyagram            : cbc:InvoiceTypeCode
        Kardinalite         : Zorunlu (1)
        Açıklama            : Bu elemanda UBL-TR içerisinde yer alan fatura tiplerine ait kodlar yazılacaktır.
        Kullanım            : Bknz. Kod Listeleri
        Örnek               : <cbc:InvoiceTypeCode>SATIS</cbc:InvoiceTypeCode>

        ../UBLTR_1.2.1_Kılavuzlar/KOD LİSTELERİ/UBL-TR Kod Listeleri-V 1.31.pdf sayfa 7

        Faturalar düzenleme amaçlarına göre beş tipte tanımlanmıştır.
        Her türlü mal ve hizmet satışı ile ilgili düzenlenen faturalar için “SATIS” değerini;
        bir malın iadesi amacıyla alıcı tarafından düzenlenen faturalar ise “IADE” değerini;
        tevkifat içeren faturalar için “TEVKIFAT” değerini;
        vergi istisnası içeren faturalar için “ISTISNA” değerini ve
        özel matrah faturaları için “OZELMATRAH” değerini;
        ihraç kayıtlı satışlar ile DİİB ve geçici kabul rejimi kapsamındaki satışlar için düzenlenen faturalarda
        “IHRACKAYITLI” değerini alacaktır.

        TODO: Enum tanımla.

        :param invoice_type_code_text:
        :return:
        """

        invoice_type_code = etree.SubElement(
            self.root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}InvoiceTypeCode"
        )
        invoice_type_code.text = invoice_type_code_text

    def add_note(self, note_text: str = None):
        """
        2.3.11 Note
        Note            :   Not
        Diyagram        :   cbc:Note
        Kardinalite     :   Seçimli (0…n)
        Açıklama        :   Faturada yer verilmek istenen genel açıklamalar için bu
                            eleman kullanılacaktır. Birden fazla açıklama yapılmak
                            istenmesi halinde elemanın tekrar kullanımı mümkündür.
        Kullanım        :   Serbest Metin
        Örnek           :   <cbc:Note>İş bu fatura muhteviyatına 7 gün içerisinde itiraz edilmediği
                            taktirde aynen kabul edilmiş sayılır.</cbc:Note>

        TODO: xml attack kontrolü yapılabilir.
        :param note_text:
        :return:
        """
        note = etree.SubElement(
            self.root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Note"
        )
        note.text = note_text

    def add_document_currency_code(self, document_currency_code_text: str = 'TRY'):
        """
        2.3.12 DocumentCurrencyCode
        DocumentCurrency Code   : Belge Para Birim Kodu
        Diyagram                : cbc:DocumentCurrencyCode
        Kardinalite             : Zorunlu (1)
        Açıklama                : Bu elemana faturanın düzenlendiği paranın birim kodu yazılacaktır.
        Kullanım                : Bknz. Kod Listeleri
        Örnek                   : <cbc:DocumentCurrencyCode>TRY</cbc:DocumentCurrencyCode>

        ISO 4217 Para Birimi Kodlarından (alfanumerik) alınmalıdır.
        :param document_currency_code_text:
        :return:
        """

        document_currency_code = etree.SubElement(
            self.root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}DocumentCurrencyCode"
        )
        document_currency_code.text = document_currency_code_text

    def add_tax_currency_code(self, tax_currency_code_text: str):
        """
        2.3.13 TaxCurrencyCode
        TaxCurrencyCode         :   Vergi Para Birimi Kodu
        Diyagram                :   cbc:TaxCurrencyCode
        Kardinalite             :   Seçimli (0…1)
        Açıklama                :   Fatura üzerinde gösterilen vergilerin “Belge Para Birim Kodu”
                                    dışında başka bir para birimi ile gösterilmesi gerekiyorsa bu
                                    para biriminin kodu yazılabilecektir.
        Kullanım                :   Bknz. Kod Listeleri
        Örnek                   :   <cbc:TaxCurrencyCode>USD</cbc:TaxCurrencyCode>
        TODO: Şart değil.
        :param tax_currency_code_text:
        :return:
        """

    def pricing_currency_code(self, pricing_currency_code_text: str):
        """
        2.3.14 PricingCurrencyCode
        PricingCurrencyCode         :   Fiyatlandırma Para Birim Kodu
        Diyagram
        Kardinalite                 :   Seçimli (0…1)
        Açıklama                    :   Mal veya hizmet bedellerinin “Belge Para Birim Kodu” dışında
                                        bir para birimi ile gösterilmesi gerekiyorsa sözkonusu para
                                        birimi bu elemana kodlanabilecektir.
        Kullanım                    :   Bknz. Kod Listeleri
        Örnek                       :   <cbc:PricingCurrencyCode>USD</cbc:PricingCurrencyCode>
        TODO: şart değil, örnek xmllerde verilmemiş.
        :return:
        """

    def add_line_count_numeric(self, line_count_numeric_text: str):
        """
        2.3.18 LineCountNumeric
        LineCountNumeric        :   Kalem Sayısı
        Diyagram                :   cbc:LineCountNumeric
        Kardinalite             :   Zorunlu (1)
        Açıklama                :   Bu elemana fatura üzerinde yer alan kalem sayısı yazılacaktır. Malın adedi
                                    birden fazla olsa dahi bu mal grubu tek bir kalem olarak gösterilecektir.
        Kullanım                :   Numerik
        Örnek                   :   <cbc:LineCountNumeric>2</cbc:LineCountNumeric>

        TODO: Line sayısını otomatik hesapla.
        :param line_count_numeric_text:
        :return:
        """
        # Create the LineCountNumeric element
        line_count_numeric = etree.SubElement(
            self.root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}LineCountNumeric"
        )
        line_count_numeric.text = line_count_numeric_text

    def add_despatch_document_reference(self, ID: str, IssueDate: str):
        """
        İrsaliye bilgileri için bu eleman kullanılabilecektir. Birden fazla irsaliyeye ait bilgilerin
        girilmesi ve irsaliye belgesinin faturaya eklenmesinde bu eleman kullanılabilecektir.

        :param ID: irsaliye numarası
        :param IssueDate: irsaliye tarihi (YYYY-MM-DD) ISO 8601 formatında
        :return: None

        2.3.22 DespatchDocumentReference İrsaliye Bilgileri
        Kardinalite                 : Seçimli (0…n)

        Kullanım                    : Bknz. Ortak Sınıflar: DocumentReference

        Örnek                       :   <cac:DespatchDocumentReference>
                                            <cbc:ID>123456</cbc:ID>
                                            <cbc:IssueDate>2009-04-13</cbc:IssueDate>
                                        </cac:DespatchDocumentReference>

        """
        DespatchDocumentReference = etree.SubElement(
            self.root,
            "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}DespatchDocumentReference"
        )

        DespatchDocumentReference_ID = etree.SubElement(
            DespatchDocumentReference, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID"
        )

        DespatchDocumentReference_ID.text = ID

        DespatchDocumentReference_IssueDate = etree.SubElement(
            DespatchDocumentReference, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IssueDate"
        )

        DespatchDocumentReference_IssueDate.text = IssueDate

    def add_signature(self, signatory: SignatoryParty):
        """
        2.3.27 Signature
        Signature       : Mali Mühür/İmza
        Diyagram
        Kardinalite     : Zorunlu (1…n)
        Açıklama        : Bu elemanda faturada kullanılan mali mühür ve/veya elektronik imza ile sertifikalara ilişkin bilgilere yer verilecektir.
        Kullanım        : Bknz. Ortak Sınıflar: Signature
        Örnek           : <cac:Signature> ...

        Entegratör firma bilgileri. Girilmesi zorunlu.
        TODO: External reference URI'de bir UUID var.
        TODO: UUID sabit yada rastgele olabilir. Test et.
        TODO: Örnek, <cbc:URI>#Signature_cf981f3d-3be5-4b9d-8b6d-7f5e18175a2f</cbc:URI>
        :param signatory: SignatoryParty Sınıfı, imzalayan (entegratör) bilgileri
        :return:
        """
        # Create the Signature element
        signature = etree.SubElement(
            self.root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Signature"
        )
        # Create the ID element with schemeID attribute
        signature_ID = etree.SubElement(signature,
                                        "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID"
                                        )
        signature_ID.set("schemeID", "VKN_TCKN")  # TODO: Değişken olabilir?
        signature_ID.text = signatory.VKN_TCKN
        # Create the SignatoryParty element
        signatory_party = etree.SubElement(
            signature, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}SignatoryParty"
        )
        # Create the PartyIdentification element
        party_identification = etree.SubElement(
            signatory_party,
            "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyIdentification"
        )
        # Create the ID element with schemeID attribute
        party_identification_ID = etree.SubElement(
            party_identification, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID"
        )
        party_identification_ID.set("schemeID", "VKN")
        party_identification_ID.text = signatory.VKN

        # PostalAddress
        postal_address = etree.SubElement(
            signatory_party, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PostalAddress"
        )

        # Create the StreetName element
        street_name = etree.SubElement(
            postal_address, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}StreetName"
        )
        street_name.text = signatory.STREET_NAME
        # Create the BuildingNumber element
        building_number = etree.SubElement(
            postal_address, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}BuildingNumber"
        )
        building_number.text = signatory.BUILDING_NUMBER
        # CitySubdivisionName
        CitySubdivisionName = etree.SubElement(
            postal_address, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CitySubdivisionName"
        )
        CitySubdivisionName.text = signatory.CITY_SUBDIVISION_NAME
        CityName = etree.SubElement(
            postal_address, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CityName"
        )
        CityName.text = signatory.CITY_NAME
        PostalZone = etree.SubElement(
            postal_address, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PostalZone"
        )
        PostalZone.text = signatory.POSTAL_ZONE

        # Create the Country element
        country = etree.SubElement(postal_address, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Country")
        # add country name
        country_name = etree.SubElement(country,
                                        "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Name"
                                        )
        country_name.text = signatory.COUNTRY_NAME

        # Create the DigitalSignatureAttachment element
        digital_signature_attachment = etree.SubElement(
            signature,
            "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}DigitalSignatureAttachment"
        )
        # Create the ExternalReference element
        external_reference = etree.SubElement(
            digital_signature_attachment,
            "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}ExternalReference"
        )
        # Create the URI element
        external_reference_URI = etree.SubElement(
            external_reference, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}URI"
        )
        external_reference_URI.text = signatory.URI  # TODO: Dinamik?

    def add_accounting_supplier_party(self, supplier_party: PartyData):
        """
        AccountingSupplier Party: Satıcı
        Kardinalite             : Zorunlu (1)
        Açıklama                : Bu elemanda faturayı düzenleyen tarafın bilgileri yer alacaktır.
        Kullanım                : Bknz. Ortak Sınıflar: SupplierParty
        Örnek

        :param supplier_party:
        :return:
        """
        # add accounting supplier party
        accounting_supplier_party = etree.SubElement(self.root,
                                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}AccountingSupplierParty"
                                                    )
        # Create the Party element
        party = etree.SubElement(accounting_supplier_party,
                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Party"
                                )
        # Create the PartyIdentification element
        party_identification = etree.SubElement(
            party, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyIdentification"
        )
        # Create the ID element with schemeID attribute
        party_identification_ID = etree.SubElement(
            party_identification, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID"
        )
        party_identification_ID.set("schemeID", supplier_party.PartyIdentification.schemeID)
        party_identification_ID.text = supplier_party.PartyIdentification.value
        # Create the PartyName element
        party_name = etree.SubElement(
            party, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyName"
        )
        # Create the Name element
        party_name_Name = etree.SubElement(
            party_name, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Name"
        )
        party_name_Name.text = supplier_party.PartyName
        # Create the PostalAddress element
        postal_address = etree.SubElement(
            party, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PostalAddress"
        )
        # Create the CitySubdivisionName element
        city_subdivision_name = etree.SubElement(
            postal_address, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CitySubdivisionName"
        )
        city_subdivision_name.text = supplier_party.PostalAddress.city_subdivision_name
        # Create the CityName element
        city_name = etree.SubElement(
            postal_address, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CityName"
        )
        city_name.text = supplier_party.PostalAddress.city_name
        # Create the Country element
        country = etree.SubElement(postal_address,
                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Country"
                                )
        # Create the Name element
        country_name = etree.SubElement(country,
                                        "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Name"
                                        )
        country_name.text = supplier_party.PostalAddress.country

    def add_accounting_customer_party(self, customer_party: PartyData):
        """
        2.3.29 AccountingCustomerParty
        AccountingCustomer Party: Alıcı
        Kardinalite             : Zorunlu (1)
        Açıklama                : Bu elemanda faturayı alan tarafın bilgileri yer alacaktır.
        Kullanım                : Bknz. Ortak Sınıflar: CustomerParty
        Örnek                   : Bknz. 2.3.29 AccountingCustomerParty

        :param customer_party:
        :return:
        """
        # add accounting customer party
        accounting_customer_party = etree.SubElement(
            self.root,
            "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}AccountingCustomerParty"
        )
        # Create the Party element
        party = etree.SubElement(accounting_customer_party,
                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Party"
                                )
        if customer_party.WebsiteURI:
            website_uri = etree.SubElement(
                party, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}WebsiteURI"
            )
            website_uri.text = customer_party.WebsiteURI

        # Create the PartyIdentification element
        party_identification = etree.SubElement(
            party, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyIdentification"
        )
        # Create the ID element with schemeID attribute
        party_identification_ID = etree.SubElement(
            party_identification, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID"
        )
        party_identification_ID.set("schemeID", customer_party.PartyIdentification.schemeID)
        party_identification_ID.text = customer_party.PartyIdentification.value
        # Create the PartyName element
        party_name = etree.SubElement(
            party, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyName"
        )
        # Create the Name element
        party_name_Name = etree.SubElement(
            party_name, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Name"
        )
        party_name_Name.text = customer_party.PartyName
        # Create the PostalAddress element
        postal_address = etree.SubElement(
            party, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PostalAddress"
        )

        if customer_party.PostalAddress.id:
            id = etree.SubElement(postal_address,
                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID"
                                )
            id.text = customer_party.PostalAddress.id

        if customer_party.PostalAddress.street_name:
            street_name = etree.SubElement(
                postal_address, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}StreetName"
            )
            street_name.text = customer_party.PostalAddress.street_name

        if customer_party.PostalAddress.building_number:
            building_number = etree.SubElement(
                postal_address, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}BuildingNumber")
            building_number.text = customer_party.PostalAddress.building_number

        # Create the CitySubdivisionName element
        city_subdivision_name = etree.SubElement(
            postal_address, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CitySubdivisionName"
        )
        # TODO: Boş ise hata veriyor.
        city_subdivision_name.text = customer_party.PostalAddress.city_subdivision_name

        city_name = etree.SubElement(
            postal_address, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CityName"
        )
        city_name.text = customer_party.PostalAddress.city_name

        if customer_party.PostalAddress.postal_zone:
            postal_zone = etree.SubElement(
                postal_address, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PostalZone"
            )
            postal_zone.text = customer_party.PostalAddress.postal_zone

        if customer_party.PostalAddress.country:
            country = etree.SubElement(
                postal_address, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Country"
            )
            # Create the Name element
            country_name = etree.SubElement(
                country, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Name"
            )
            country_name.text = customer_party.PostalAddress.country

    def add_paymentmeans(self, pmeans: PaymentMeans):
        """
        2.3.34 Payment Means
        PaymentMeans        : Ödeme Şekli
        Diyagram
        Kardinalite         : Seçimli(0..n)
        Açıklama            : Bu elemana ödeme şekli ile ilgili bilgiler yazılabilecektir.
        Kullanım            : Bknz. Ortak Sınıflar: PaymentMeans
        Örnek               : Bknz. 2.3.34 Payment Means Örnek

        :param payment_means:
        :return:
        """
        if not pmeans:
            return

        payment_means = etree.SubElement(self.root,
                                        "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PaymentMeans")
        if pmeans.PaymentMeansCode:
            # Create the PaymentMeansCode element
            payment_means_code = etree.SubElement(payment_means,
                                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PaymentMeansCode")
            payment_means_code.text = pmeans.PaymentMeansCode

        # Create the PayeeFinancialAccount element
        payee_financial_account = etree.SubElement(payment_means,
                                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PayeeFinancialAccount")
        # Create the ID element
        id = etree.SubElement(payee_financial_account,
                            "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID")
        id.text = pmeans.PayeeFinancialAccount.ID
        # Create the CurrencyCode element
        currency_code = etree.SubElement(payee_financial_account,
                                        "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CurrencyCode")
        currency_code.text = pmeans.PayeeFinancialAccount.CurrencyCode
        # Create the PaymentNote element
        payment_note = etree.SubElement(payee_financial_account,
                                        "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PaymentNote")
        payment_note.text = pmeans.PayeeFinancialAccount.PaymentNote

    def add_paymentterms(self, pterms: PaymentTerms):
        """
        2.3.35 PaymentTerms
        PaymentTerms        :   Ödeme Koşulları
        Diyagram
        Kardinalite         :   Seçimli (0..1)
        Açıklama            :   Bu elemana ödeme koşulları ve ödemenin yapılmaması halinde
                                uygulanacak müeyyideler yazılabilecektir.
        Kullanım            :   Bknz. Ortak Sınıflar: PaymentTerms
        Örnek               :   <cac:PaymentTerms>
                                    <cbc:Note>[AÇIKLAMA]</cbc:Note>
                                    <cbc:PenaltySurchargePercent>20.0</cbc:PenaltySurchargePercent>
                                    <cbc:PaymentDueDate>2009-01-13</cbc:PaymentDueDate>
                                    <cbc:Amount currencyID="TRY">100.0</cbc:Amount>
                                </cac:PaymentTerms>

        :param payment_terms:
        :return:
        """
        if not pterms:
            return

        payment_terms = etree.SubElement(
            self.root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PaymentTerms"
        )
        if pterms.Note:
            # Create the Note element
            note = etree.SubElement(payment_terms,
                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Note"
                                    )
            note.text = pterms.Note

        if pterms.PenaltySurchargePercent:
            penalty_surcharge_percent = etree.SubElement(
                payment_terms,
                "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PenaltySurchargePercent"
            )
            penalty_surcharge_percent.text = pterms.PenaltySurchargePercent

        if pterms.PaymentDueDate:
            payment_due_date = etree.SubElement(
                payment_terms, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PaymentDueDate"
            )
            payment_due_date.text = pterms.PaymentDueDate
        if pterms.Amount and pterms.CurrencyID:
            amount = etree.SubElement(payment_terms,
                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Amount"
                                    )
            amount.text = pterms.Amount
            amount.set("currencyID", pterms.CurrencyID)

    def add_taxtotal(self, taxt: TaxTotal):
        """
        2.3.41 TaxTotal
        TaxTotal        :   Toplam Vergi
        Diyagram
        Kardinalite     :   Zorunlu (1…n)
        Açıklama        :   Bu elemana faturada yer alan vergi ve diğer yasal
                            yükümlülükler ile ilgili bilgiler yazılacaktır.
        Kullanım        :   Bknz. Ortak Sınıflar: TaxTotal

        Ayrıca bkz. class TaxTypeCode
        :param taxt: TaxTotal
        """
        tax_total = etree.SubElement(self.root,
                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxTotal")
        # Create the TaxAmount element
        tax_amount = etree.SubElement(tax_total,
                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxAmount")
        tax_amount.set("currencyID", taxt.CurrencyID)
        tax_amount.text = taxt.TaxAmount
        # Create the TaxSubtotal element
        tax_subtotal = etree.SubElement(tax_total,
                                        "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxSubtotal")
        # TODO: İlk elementi alıyoruz. Daha sonra düzenlenecek.
        # TODO: Vergi girilmediyse hata veriyor.

        print(taxt.TaxSubtotal, type(taxt.TaxSubtotal))
        from pprint import pprint
        pprint(taxt.__dict__)

        if taxt.TaxSubtotal and isinstance(taxt.TaxSubtotal, list):
            taxt.TaxSubtotal = taxt.TaxSubtotal[0]

        # Create the TaxableAmount element
        taxable_amount = etree.SubElement(tax_subtotal,
                                        "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxableAmount")
        taxable_amount.set("currencyID", taxt.CurrencyID)
        taxable_amount.text = taxt.TaxSubtotal.TaxableAmount
        # Create the TaxAmount element
        tax_amount = etree.SubElement(tax_subtotal,
                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxAmount")
        tax_amount.set("currencyID", taxt.CurrencyID)
        tax_amount.text = taxt.TaxSubtotal.TaxAmount

        # # Create the CalculationSequenceNumeric element
        # calculation_sequence_numeric = etree.SubElement(
        #     tax_subtotal,
        #     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CalculationSequenceNumeric"
        # )
        # calculation_sequence_numeric.text = taxt.TaxSubtotal.CalculationSequenceNumeric
        # Create the Percent element
        percent = etree.SubElement(tax_subtotal,
                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Percent")
        percent.text = taxt.TaxSubtotal.Percent
        # Create the TaxCategory element
        tax_category = etree.SubElement(tax_subtotal,
                                        "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxCategory")
        # Create the TaxScheme element
        """
        lxml.etree.DocumentInvalid: Element '{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxScheme', attribute 'schemeID': The attribute 'schemeID' is not allowed., line 102
        """
        tax_scheme = etree.SubElement(tax_category,
                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxScheme")  # , schemeID='UN/ECE 5153', schemeAgencyID='6')
        # Create the Name element
        name = etree.SubElement(tax_scheme,
                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Name")
        name.text = taxt.TaxSubtotal.TaxCategory.Name
        # Create the TaxTypeCode element
        """
        lxml.etree.DocumentInvalid: Element '{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxTypeCode', attribute 'schemeID': The attribute 'schemeID' is not allowed., line 104
        """
        tax_type_code = etree.SubElement(tax_scheme, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxTypeCode")  # , schemeID='UN/ECE 5305', schemeAgencyID='6')
        tax_type_code.text = taxt.TaxSubtotal.TaxCategory.TaxScheme.TaxTypeCode

    def add_withholdingtaxtotal(self):
        """
        2.3.42 WithholdingTaxTotal
        WithholdingTaxTotal     :   Tevkifat Bilgileri
        Diyagram
        Kardinalite             :   Seçimli (0…n)
        Açıklama                :   Bu elemana tevkifatlı faturalarda yer alan tevkifat ile ilgili
                                    bilgiler yazılacaktır.
        Kullanım                :   Bknz. Ortak Sınıflar: TaxTotal
        Örnek                   :   <cac:WithholdingTaxTotal>
                                        <cbc:TaxAmount currencyID="TRY">3240</cbc:TaxAmount>
                                        <cac:TaxSubtotal>
                                            <cbc:TaxAmount currencyID="TRY">3240</cbc:TaxAmount>
                                            <cbc:Percent>90</cbc:Percent>
                                            <cac:TaxCategory>
                                                <cac:TaxScheme>
                                                    <cbc:TaxTypeCode>606</cbc:TaxTypeCode>
                                                </cac:TaxScheme>
                                            </cac:TaxCategory>
                                        </cac:TaxSubtotal>
                                    </cac:WithholdingTaxTotal>

        Elemanın kullanımı zorunlu değildir. Fatura üzerinde kesinti yapılmışsa bu eleman kullanılacaktır.

        Ayrıca bkz. class TaxTypeCode
        :param tax_total:
        :return:
        """
        withholding_tax_total = etree.SubElement(
            self.root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}WithholdingTaxTotal"
        )
        # Create the TaxAmount element
        tax_amount = etree.SubElement(
            withholding_tax_total,
            "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxAmount"
        )
        tax_amount.set("currencyID", "TRY")
        tax_amount.text = "3240"
        # Create the TaxSubtotal element
        tax_subtotal = etree.SubElement(
            withholding_tax_total,
            "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxSubtotal"
        )
        # Create the TaxAmount element
        tax_amount = etree.SubElement(
            tax_subtotal, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxAmount"
        )
        tax_amount.set("currencyID", "TRY")
        tax_amount.text = "3240"
        # Create the Percent element
        percent = etree.SubElement(tax_subtotal,
                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Percent"
                                )
        percent.text = "90"
        # Create the TaxCategory element
        tax_category = etree.SubElement(
            tax_subtotal, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxCategory"
        )
        # Create the TaxScheme element
        tax_scheme = etree.SubElement(
            tax_category, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxScheme")  # , schemeID='UN/ECE 5153', schemeAgencyID='6')
        # Create the TaxTypeCode element
        tax_type_code = etree.SubElement(
            tax_scheme, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxTypeCode"
        )
        tax_type_code.text = "606"

    def add_legalmonetarytotal(self, monetary_total: MonetaryTotal):
        """
        2.3.43 LegalMonetaryTotal
        LegalMonetaryTotal      : Parasal Toplamlar
        Diyagram
        Kardinalite             : Zorunlu (1)
        Açıklama                : Bu elemanda faturadaki çeşitli tutarların toplamları yer alacaktır.

        UBL-TR Ortak Elemanlar - V 0.7.pdf 2.2.37 MonetaryTotal

        Elemanlar ve Kullanım Kardinaliteleri
        Zorunlu(1): LineExtensionAmount
        Zorunlu(1): TaxExclusiveAmount
        Zorunlu(1): TaxInclusiveAmount
        Seçimli(0..1): AllowanceTotalAmount
        Seçimli(0..1): ChargeTotalAmount
        Seçimli(0..1): PayableRoundingAmount
        Zorunlu(1): PayableAmount

        Kullanım:
        LineExtensionAmount: Mal/hizmet miktarı ile Mal/hizmet birim fiyatının çarpımı ile bulunan tutardır.
        TaxExclusiveAmount: Vergiler hariç, ıskonto veya artırım dahil toplam tutar girilir.(Vergi Matrahı).
        TaxInclusiveAmount: Vergiler, ıskonto ve artırım dahil toplam tutar girilir.
        AllowanceTotalAmount: Toplam ıskonto tutarı girilir.
        ChargeTotalAmount: Toplam fiyat artırımı tutarı girilir.
        PayableRoundingAmount: Yuvarlama tutarı girilir.
        PayableAmount: Ödenecek tutar girilir.

        Örnek   <cac:LegalMonetaryTotal>
                    <cbc:LineExtensionAmount
                    currencyID="TRY">90</cbc:LineExtensionAmount>
                    <cbc:TaxExclusiveAmount currencyID="TRY">80</cbc:TaxExclusiveAmount>
                    <cbc:TaxInclusiveAmount currencyID="TRY">94</cbc:TaxInclusiveAmount>
                    <cbc:AllowanceTotal currencyID="TRY">10</cbc:AllowanceTotal >
                    <cbc:PayableRoundingAmount currencyID="TRY">0.4</cbc:PayableRoundingAmount>
                    <cbc:PayableAmount currencyID="TRY">94.4</cbc:PayableAmount>
                </cac:LegalMonetaryTotal>

        :return:
        """

        legal_monetary_total = etree.SubElement(self.root,
                                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}LegalMonetaryTotal")
        # Create the LineExtensionAmount element
        line_extension_amount = etree.SubElement(legal_monetary_total,
                                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}LineExtensionAmount")
        line_extension_amount.set("currencyID", monetary_total.CurrencyID)
        line_extension_amount.text = monetary_total.LineExtensionAmount
        # Create the TaxExclusiveAmount element
        tax_exclusive_amount = etree.SubElement(legal_monetary_total,
                                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxExclusiveAmount")
        tax_exclusive_amount.set("currencyID", monetary_total.CurrencyID)
        tax_exclusive_amount.text = monetary_total.TaxExclusiveAmount
        # Create the TaxInclusiveAmount element
        tax_inclusive_amount = etree.SubElement(legal_monetary_total,
                                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxInclusiveAmount")
        tax_inclusive_amount.set("currencyID", monetary_total.CurrencyID)
        tax_inclusive_amount.text = monetary_total.TaxInclusiveAmount

        if monetary_total.AllowanceTotalAmount:
            allowance_total_amount = etree.SubElement(legal_monetary_total,
                                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}AllowanceTotalAmount")
            allowance_total_amount.set("currencyID", monetary_total.CurrencyID)
            allowance_total_amount.text = monetary_total.AllowanceTotalAmount

        if monetary_total.ChargeTotalAmount:
            charge_total_amount = etree.SubElement(legal_monetary_total,
                                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ChargeTotalAmount")
            charge_total_amount.set("currencyID", monetary_total.CurrencyID)
            charge_total_amount.text = monetary_total.ChargeTotalAmount

        if monetary_total.PayableRoundingAmount:
            payable_rounding_amount = etree.SubElement(legal_monetary_total,
                                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PayableRoundingAmount")
            payable_rounding_amount.set("currencyID", monetary_total.CurrencyID)
            payable_rounding_amount.text = monetary_total.PayableRoundingAmount

        payable_amount = etree.SubElement(legal_monetary_total,
                                        "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PayableAmount")
        payable_amount.set("currencyID", monetary_total.CurrencyID)
        payable_amount.text = monetary_total.PayableAmount

    def add_invoice_line(self, invoice_line: Union[InvoiceLine, List[InvoiceLine]]):
        """
        Belgede geçen mal/hizmete ilişkin bilgilerin girildiği elemandır.
        InvoiceLine  : Mal/Hizmet Kalemleri
        Kardinalite  : Zorunlu (1…n)
        Açıklama     : Bu elemanda faturada yer alan mal ve/veya hizmetlere ait bilgiler yer alacaktır.
        Kullanım     : Bknz. Ortak Sınıflar: InvoiceLine
        Örnek        :
        <cac:InvoiceLine>
            <cbc:ID>1</cbc:ID>
            <cbc:InvoicedQuantity unitCode=”BX”>30</cbc:InvoicedQuantity>
            <cbc:LineExtensionAmount currencyID="TRY">1800</cbc:LineExtensionAmount>
            <cac:Item>
                <cbc:Name>URUN ADI</cbc:Name>
                <cac:SellersItemIdentification>
                    <cbc:ID>1234567</cbc:ID>
                </cac:SellersItemIdentification>
            </cac:Item>
            <cac:Price>
                <cbc:PriceAmount currencyID="TRY">60</cbc:PriceAmount>
            </cac:Price>
        </cac:InvoiceLine>

        :param invoice_line:
        :return:

        Ortak Sınıflar 2.2.29 InvoiceLine Mal/Hizmet Kalemleri, UBL-TR Ortak Elemanlar Nisan 2017 Versiyon : 0.7 41/81

        Elemanlar ve Kullanım Kardinaliteleri
                                            Zorunlu(1): ID
                                            Seçimli(0..1): Note
                                            Zorunlu(1): InvoicedQuantity
                                            Zorunlu(1): LineExtensionAmount
                                            Seçimli(0..n): OrderLineReference
                                            Seçimli(0..n): DespatchLineReference
                                            Seçimli(0..n): ReceiptLineReference
                                            Seçimli(0..n): Delivery
                                            Seçimli(0..n): AllowanceCharge
                                            Seçimli(0..1): TaxTotal
                                            Seçimli(0..n): WithholdingTaxTotal
                                            Zorunlu(1): Item
                                            Zorunlu(1): Price
                                            Seçimli(0..n): SubInvoiceLine

        Kullanım
        ID                      Zorunlu(1)      : Kalem sıra numarası girilir.
        Note                    Seçimli(0..1)   : Kalem hakkında açıklama serbest metin olarak girilir.
        InvoicedQuantity        Zorunlu(1)      : Mal/hizmet miktarı birimi ile birlikte girilir. Bknz. Kod Listeleri.
        OrderLineReference      :   Fatura ile ilişkili sipariş dokümanının kalemlerine referans atmak için kullanılır.
                                    Bknz. OrderLineReference
        DespatchLineReference   :   Fatura ile ilişkili irsaliye dokümanının kalemlerine referans atmak için kullanılır.
                                    Bknz. LineReference
        ReceiptLineReference    :   Fatura ile ilişkili alındı dokümanının kalemlerine referans atmak için kullanılır.
                                    Bknz. LineReference
        Delivery                :   Kalem bazlı teslimat olması durumunda bu eleman doldurulur. Bknz. Delivery
        LineExtensionAmount     :   Mal/hizmet miktarı ile Mal/hizmet birim fiyatının çarpımı ile bulunan tutardır
                                    (varsa iskonto düşülür).
        AllowanceCharge         :   Kalem bazlı ıskonto/artırım tutarıdır. Bknz. AllowanceCharge.
        TaxTotal                :   Kalem bazlı vergi bilgilerinin girildiği elemandır. Bknz. TaxTotal.
        WithholdingTaxTotal     :   Kalem bazlı tevkifat uygulanması durumunda bu eleman kullanılır. Bknz. TaxTotal
        Item                    :   Mal/hizmet hakkında bilgiler buraya girilir. Bknz. Item.
        Price                   :   Mal/hizmet birim fiyatı hakkında bilgiler buraya girilir. Bknz. Price.
        SubInvoiceLine          :   Eğer ürün için ek bir birim kodu kullanılması gerekiyorsa bu elemanın içindeki
                                    InvoicedQuantity elemanı (diğer opsiyonel elemanlar boş bırakılarak) kullanılabilir.
                                    Bknz. InvoiceLine

        Örnek
        <cac:InvoiceLine>
            <cbc:ID>1</cbc:ID>
            <cbc:InvoicedQuantity unitCode=”BX”>30</cbc:InvoicedQuantity>
            <cbc:LineExtensionAmount currencyID="TRY">1800</cbc:LineExtensionAmount>
                <cac:Item>
                <cbc:Name>Notebook Çantası</cbc:Name>
                    <cac:SellersItemIdentification>
                        <cbc:ID>1234567</cbc:ID>
                    </cac:SellersItemIdentification>
                </cac:Item>
            <cac:Price>
                <cbc:PriceAmount currencyID="TRY">60</cbc:PriceAmount>
            </cac:Price>
        </cac:InvoiceLine>
        """
        # ID, InvoicedQuantity, LineExtensionAmount, Name, SellersItemIdentification, PriceAmount

        # TODO: Tekrarlayan elemanlar için fonksiyon yazılacak.
        # if not all(isinstance(line, InvoiceLine) for line in invoice_line):
        #     raise ValueError("All elements of invoice_lines must be of type InvoiceLine")

        # check if invoice_line is a InvoiceLine object from the same module, Unresolved reference 'InvoiceLine'
        # if not isinstance(invoice_line, InvoiceLine):
        #     raise ValueError("invoice_line must be of type InvoiceLine")

        if not isinstance(invoice_line, List):
            invoice_line = [invoice_line]

        for InvoiceLine in invoice_line:
            # InvoiceLine root element
            invoice_line = etree.SubElement(self.root,
                                            "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}InvoiceLine")

            # Zorunlu(1): ID Kalem sıra numarası
            id = etree.SubElement(invoice_line, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID")
            id.text = InvoiceLine.ID

            invoiced_quantity = etree.SubElement(invoice_line,
                                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}InvoicedQuantity")
            invoiced_quantity.set("unitCode", InvoiceLine.InvoicedQuantity_unitCode)
            invoiced_quantity.text = InvoiceLine.InvoicedQuantity
            line_extension_amount = etree.SubElement(invoice_line,
                                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}LineExtensionAmount")
            line_extension_amount.set("currencyID", InvoiceLine.currencyID)
            line_extension_amount.text = InvoiceLine.LineExtensionAmount

            if InvoiceLine.TaxTotal:
                tax_total = etree.SubElement(invoice_line,
                                            "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxTotal")
                tax_amount = etree.SubElement(tax_total,
                                            "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxAmount")
                tax_amount.set("currencyID", InvoiceLine.currencyID)
                tax_amount.text = InvoiceLine.TaxTotal.TaxAmount
                tax_subtotal = etree.SubElement(tax_total,
                                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxSubtotal")
                taxable_amount = etree.SubElement(tax_subtotal,
                                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxableAmount")
                taxable_amount.set("currencyID", InvoiceLine.currencyID)

                if not isinstance(InvoiceLine.TaxTotal.TaxSubtotal, list):
                    InvoiceLine.TaxTotal.TaxSubtotal = [InvoiceLine.TaxTotal.TaxSubtotal]

                for subtotal in InvoiceLine.TaxTotal.TaxSubtotal:
                    taxable_amount.text = subtotal.TaxableAmount
                    # Create the TaxAmount element
                    tax_amount = etree.SubElement(tax_subtotal,
                                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxAmount")
                    tax_amount.set("currencyID", InvoiceLine.currencyID)
                    tax_amount.text = subtotal.TaxAmount
                    # Create the Percent element
                    percent = etree.SubElement(tax_subtotal,
                                            "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Percent")
                    percent.text = subtotal.Percent
                    # Create the TaxCategory element
                    tax_category = etree.SubElement(tax_subtotal,
                                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxCategory")

                    # Create the TaxScheme element
                    tax_scheme = etree.SubElement(tax_category,
                                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxScheme")  # , schemeID='UN/ECE 5153', schemeAgencyID='6')
                    # Create the Name element
                    name = etree.SubElement(tax_scheme,
                                            "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Name")
                    name.text =subtotal.TaxCategory.TaxScheme.Name  # "GERÇEK USULDE KATMA DEĞER VERGİSİ"
                    # Create the TaxTypeCode element
                    tax_type_code = etree.SubElement(tax_scheme,
                                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxTypeCode")
                    tax_type_code.text = subtotal.TaxCategory.TaxScheme.TaxTypeCode  # "0015"

            # Create the Item element
            item = etree.SubElement(invoice_line,
                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Item")
            # Create the Name element
            name = etree.SubElement(item, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Name")
            name.text = InvoiceLine.Item.Name

            if InvoiceLine.Item.SellersItemIdentification:
                # Create the SellersItemIdentification element
                sellers_item_identification = etree.SubElement(item,
                                                            "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}SellersItemIdentification")
                # Create the ID element
                id = etree.SubElement(sellers_item_identification,
                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID")
                id.text = InvoiceLine.Item.SellersItemIdentification.ID

            # Create the Price element
            price = etree.SubElement(invoice_line,
                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Price")
            # Create the PriceAmount element
            price_amount = etree.SubElement(price,
                                            "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PriceAmount")
            price_amount.set("currencyID", InvoiceLine.currencyID)
            price_amount.text = InvoiceLine.Price.PriceAmount



    def add_ContractDocumentReference(self, cdr: DocumentReference):
        """
        2.3.25 ContractDocumentReference
        ContractDocumentReference Kontrat Dokümanı Bilgileri
        UBL-TR Fatura Aralık 2017
        Versiyon : 1.0 21/37
        Diyagram
        Kardinalite Seçimli (0…n)
        Açıklama Fatura ile ilgili kontrat dokümanın bilgilerinin gösterilmesinde
        bu eleman kullanılabilecektir.
        Kullanım Bknz. Ortak Sınıflar: DocumentReference
        Örnek
        <cac:ContractDocumentReference>
            <cbc:ID>123456</cbc:ID>
            <cbc:IssueDate>2009-04-13</cbc:IssueDate>
        </cac:ContractDocumentReference>

        :param cdr:
        :return:
        """


    def dump_xml(self):  # TODO: Move to utils.py
        with open("invoice-dump.xml", "w") as f:
            f.write(etree.tostring(self.root, pretty_print=True, xml_declaration=True, encoding="UTF-8").decode("UTF-8"))




class TaxTypeCode:
    """
    1.9 TaxTypeCode
    Bu eleman TaxTotal elemanı altında bulunması durumunda “VERGİ KODLARI
    LİSTESİ”nde yer alan kodları alabilir. Vergi Kodları Listesi “Kod Listeleri” dizini altında
    yer almaktadır. Bu listede daha sonradan yapılacak ilave ve değişiklikler
    www.efatura.gov.tr internet adresinden ayrıca duyurulacaktır.
    UBLTR_1.2.1_Kilavuzlar/KOD LİSTELERİ/UBL-TR Kod Listeleri-V 1.31.pdf Versiyon: 1.31 13/20
    """

    def __init__(self):
        self.tax_type_codes = {
            "0003": ("GELİR VERGİSİ STOPAJI", "GV STOPAJI"),
            "0011": ("KURUMLAR VERGİSİ STOPAJI", "KV STOPAJI"),
            "0015": ("GERÇEK USULDE KATMA DEĞER VERGİSİ", "KDV GERCEK"),
            "0021": ("BANKA MUAMELELERİ VERGİSİ", "BMV"),
            "0022": ("SİGORTA MUAMELELERİ VERGİSİ", "SMV"),
            "0059": ("KONAKLAMA VERGİSİ", "KONAKLAMA VERGİSİ"),
            "0061": ("KAYNAK KULLANIMI DESTEKLEME FONU KESİNTİSİ", "KKDF KESİNTİ"),
            "0071": ("PETROL VE DOĞALGAZ ÜRÜNLERİNE İLİŞKİN ÖZEL TÜKETİM VERGİSİ", "ÖTV 1.LİSTE"),
            "0073": ("KOLALI GAZOZ, ALKOLLÜ İÇEÇEKLER VE TÜTÜN MAMÜLLERİNE İLİŞKİN ÖZEL TÜKETİM VERGİSİ", "ÖTV 3.LİSTE"),
            "0074": ("DAYANIKLI TÜKETİM VE DİĞER MALLARA İLİŞKİN ÖZEL TÜKETİM VERGİSİ", "ÖTV 4.LİSTE"),
            "0075": ("ALKOLLÜ İÇEÇEKLERE İLİŞKİN ÖZEL TÜKETİM VERGİSİ", "ÖTV 3A LİSTE"),
            "0076": ("TÜTÜN MAMÜLLERİNE İLİŞKİN ÖZEL TÜKETİM VERGİSİ", "ÖTV 3B LİSTE"),
            "0077": ("KOLALI GAZOZLARA İLİŞKİN ÖZEL TÜKETİM VERGİSİ", "ÖTV 3C LİSTE"),
            "1047": ("DAMGA VERGİSİ", "DAMGA V"),
            "1048": ("5035 SAYILI KANUNA GÖRE DAMGA VERGİSİ", "5035SKDAMGAV"),
            "4071": ("ELEKTRİK VE HAVALI GAZ TÜKETİM VERGİSİ", "ELK.HAVAGAZ.TÜK.VER."),
            "4080": ("ÖZEL İLETİŞİM VERGİSİ", "Ö.İLETİŞİM V"),
            "4081": ("5035 SAYILI KAUNA GÖRE ÖZEL İLETİŞİM VERGİSİ", "5035ÖZİLETV."),
            "4171": ("PETROL VE DOĞALGAZ ÜRÜNLERİNE İLİŞKİN ÖTV TEVKİFATI", "PTR-DGZ ÖTV TEVKİFAT"),
            "8001": ("BORSA TESCİL ÜCRETİ", "BORSA TES.ÜC."),
            "8002": ("ENERJİ FONU", "ENERJİ FONU"),
            "8004": ("TRT PAYI", "TRT PAYI"),
            "8005": ("ELEKTRİK TÜKETİM VERGİSİ", "ELK.TÜK.VER."),
            "8006": ("TELSİZ KULLANI ÜCRETİ", "TK KULLANIM"),
            "8007": ("TELSİZ RUHSAT ÜCRETİ", "TK RUHSAT"),
            "8008": ("ÇEVRE TEMİZLİK VERGİSİ", "ÇEV. TEM .VER."),
            "9021": ("4961 BANKA SİGORTA MUAMELELERİ VERGİSİ", "4961BANKASMV"),
            "9040": ("MERA FONU", "MERA FONU"),
            "9077": ("MOTORLU TAŞIT ARAÇLARINA İLİŞKİN ÖZEL TÜKETİM VERGİSİ (TESCİLE TABİ OLANLAR)", "ÖTV 2.LİSTE"),
            "9944": ("BELEDİYELERE ÖDENEN HAL RÜSUMU", "BEL.ÖD.HAL RÜSUM"),
        }

