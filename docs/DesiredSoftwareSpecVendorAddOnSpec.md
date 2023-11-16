# DesiredSoftwareSpecVendorAddOnSpec

Vendor specific add-on info for ESX host.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Vendor add-on name.  ***Since:*** vSphere API 7.0  | 
**version** | **str** | Vendor add-on version.  ***Since:*** vSphere API 7.0  | 

## Example

```python
from vmware_vi.models.desired_software_spec_vendor_add_on_spec import DesiredSoftwareSpecVendorAddOnSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DesiredSoftwareSpecVendorAddOnSpec from a JSON string
desired_software_spec_vendor_add_on_spec_instance = DesiredSoftwareSpecVendorAddOnSpec.from_json(json)
# print the JSON string representation of the object
print DesiredSoftwareSpecVendorAddOnSpec.to_json()

# convert the object into a dict
desired_software_spec_vendor_add_on_spec_dict = desired_software_spec_vendor_add_on_spec_instance.to_dict()
# create an instance of DesiredSoftwareSpecVendorAddOnSpec from a dict
desired_software_spec_vendor_add_on_spec_form_dict = desired_software_spec_vendor_add_on_spec.from_dict(desired_software_spec_vendor_add_on_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


