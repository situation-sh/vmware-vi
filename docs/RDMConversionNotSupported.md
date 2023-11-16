# RDMConversionNotSupported

The virtual machine is using an RDM device with compatibility mode set to 'physicalMode' and operation is unable to convert the disk to a different type.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The name of the disk device using the RDM.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.rdm_conversion_not_supported import RDMConversionNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of RDMConversionNotSupported from a JSON string
rdm_conversion_not_supported_instance = RDMConversionNotSupported.from_json(json)
# print the JSON string representation of the object
print RDMConversionNotSupported.to_json()

# convert the object into a dict
rdm_conversion_not_supported_dict = rdm_conversion_not_supported_instance.to_dict()
# create an instance of RDMConversionNotSupported from a dict
rdm_conversion_not_supported_form_dict = rdm_conversion_not_supported.from_dict(rdm_conversion_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


