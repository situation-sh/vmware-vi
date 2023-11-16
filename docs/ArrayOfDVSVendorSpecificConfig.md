# ArrayOfDVSVendorSpecificConfig

A boxed array of *DVSVendorSpecificConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSVendorSpecificConfig]**](DVSVendorSpecificConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_vendor_specific_config import ArrayOfDVSVendorSpecificConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSVendorSpecificConfig from a JSON string
array_of_dvs_vendor_specific_config_instance = ArrayOfDVSVendorSpecificConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSVendorSpecificConfig.to_json()

# convert the object into a dict
array_of_dvs_vendor_specific_config_dict = array_of_dvs_vendor_specific_config_instance.to_dict()
# create an instance of ArrayOfDVSVendorSpecificConfig from a dict
array_of_dvs_vendor_specific_config_form_dict = array_of_dvs_vendor_specific_config.from_dict(array_of_dvs_vendor_specific_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


