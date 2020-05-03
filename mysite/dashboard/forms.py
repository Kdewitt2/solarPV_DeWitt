from django import forms

class ClientForm(forms.Form):
    clientCode = forms.CharField(label='Client Code', max_length=8, required=True)
    clientName = forms.CharField(label='Client Name', max_length=50, required=True)
    clientType = forms.CharField(label='Client Type', max_length=25)

class LocationForm(forms.Form):
    clientCode = forms.CharField(label='Client Code', max_length=8, required=True)
    address1 = forms.CharField(label='Address', max_length=50)
    address2 = forms.CharField(label='Address2', max_length=50)
    city = forms.CharField(label='City', max_length=25)
    state = forms.CharField(label='State (Abbr)', max_length=2)
    postalCode = forms.CharField(label='Postal Code', max_length=5)
    country = forms.CharField(label='Country', max_length=25)
    phoneNumber = forms.CharField(label='Phone Number', max_length=15)
    faxNumber = forms.CharField(label='Fax Number', max_length=15)


class ProductForm(forms.Form):
    prodName = forms.CharField(label="Product Name", max_length=25, required=True)
    cellTech = forms.CharField(label="Cell Technology", max_length=50)
    cellManuf = forms.CharField(label="Cell Manufacturer", max_length=50)
    numCells = forms.CharField(label="Number of Cells", max_length=4)
    numCellsSeries = forms.CharField(label="Number of Cells in Series", max_length=4)
    numSeriesStrings = forms.CharField(label="Number of Series Strings", max_length=4)
    numDiodes = forms.CharField(label="Number of Diodes", max_length=4)
    prodLength = forms.CharField(label="Product Length", max_length=10)
    prodWidth = forms.CharField(label="Product Width", max_length=10)
    superstrateType = forms.CharField(label="Superstrate Type", max_length=50)
    superstrateManuf = forms.CharField(label="Superstrate Manufacturer", max_length=50)
    substrateType = forms.CharField(label="Substrate Type", max_length=50)
    substrateManuf = forms.CharField(label="Substrate Manufacturer", max_length=50)
    frameType = forms.CharField(label="Frame Type", max_length=50)
    frameAdhesive = forms.CharField(label="Frame Adhesive", max_length=50)
    encapsulantType = forms.CharField(label="Encapsulant Type", max_length=50)
    encapsulantManuf = forms.CharField(label="Encapsulant Manufacturer", max_length=50)
    junctionBoxType = forms.CharField(label="Junction Box Type", max_length=50)
    junctionBoxManuf = forms.CharField(label="Junction box Manufacturer", max_length=50)

class TestStandardForm(forms.Form):
    testStandName = forms.CharField(label="Test Standard Name", max_length=50, required=True)
    testStandDesc = forms.CharField(label="Description", max_length=200, required=True)
    testStandPubDate = forms.CharField(label="Test Standard Publish Date", max_length=10, required=True)    

class CertificateForm(forms.Form):
    certID = forms.CharField(label="Certificate ID", max_length=8, required=True)
    certNumber = forms.CharField(label="Certificate Number", max_length=8, required=True)
    location = forms.CharField(label='Location Address', max_length=50, required=True)
    reportNum = forms.CharField(label="Report Number", max_length=8, required=True)
    contact = forms.CharField(label="Contact", max_length=8, required=True)
    testStand = forms.CharField(label='Test Standard', max_length=8, required=True)
    modelNum = forms.CharField(label='Model Number', max_length=8, required=True)
    certIssueDate = forms.CharField(label="Certificate Issue Date", max_length=10, required=True)
    