# DesiredSoftwareSpec

Desired Software Spec is defined as combination of base-image and add-on component which user wants to install on ESX host or cluster.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_image_spec** | [**DesiredSoftwareSpecBaseImageSpec**](DesiredSoftwareSpecBaseImageSpec.md) |  | 
**vendor_add_on_spec** | [**DesiredSoftwareSpecVendorAddOnSpec**](DesiredSoftwareSpecVendorAddOnSpec.md) |  | [optional] 
**components** | [**List[DesiredSoftwareSpecComponentSpec]**](DesiredSoftwareSpecComponentSpec.md) | Additional components which should be part of the desired software spec.  These components would override the components present in *DesiredSoftwareSpec.vendorAddOnSpec* and *DesiredSoftwareSpec.baseImageSpec*.  ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.desired_software_spec import DesiredSoftwareSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DesiredSoftwareSpec from a JSON string
desired_software_spec_instance = DesiredSoftwareSpec.from_json(json)
# print the JSON string representation of the object
print DesiredSoftwareSpec.to_json()

# convert the object into a dict
desired_software_spec_dict = desired_software_spec_instance.to_dict()
# create an instance of DesiredSoftwareSpec from a dict
desired_software_spec_form_dict = desired_software_spec.from_dict(desired_software_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


