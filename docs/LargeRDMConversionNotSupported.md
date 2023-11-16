# LargeRDMConversionNotSupported

The virtual machine is using a 2TB+ RDM device and operation is unable to convert the disk to a different type.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The name of the disk device using the RDM.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.large_rdm_conversion_not_supported import LargeRDMConversionNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of LargeRDMConversionNotSupported from a JSON string
large_rdm_conversion_not_supported_instance = LargeRDMConversionNotSupported.from_json(json)
# print the JSON string representation of the object
print LargeRDMConversionNotSupported.to_json()

# convert the object into a dict
large_rdm_conversion_not_supported_dict = large_rdm_conversion_not_supported_instance.to_dict()
# create an instance of LargeRDMConversionNotSupported from a dict
large_rdm_conversion_not_supported_form_dict = large_rdm_conversion_not_supported.from_dict(large_rdm_conversion_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


