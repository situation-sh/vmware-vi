# OvfUnsupportedType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the element with the unsupported type  ***Since:*** vSphere API 4.0  | 
**instance_id** | **str** | The OVF RASD InstanceId for the hardware description  ***Since:*** vSphere API 4.0  | 
**device_type** | **int** | The device type that is unsupported  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_unsupported_type import OvfUnsupportedType

# TODO update the JSON string below
json = "{}"
# create an instance of OvfUnsupportedType from a JSON string
ovf_unsupported_type_instance = OvfUnsupportedType.from_json(json)
# print the JSON string representation of the object
print OvfUnsupportedType.to_json()

# convert the object into a dict
ovf_unsupported_type_dict = ovf_unsupported_type_instance.to_dict()
# create an instance of OvfUnsupportedType from a dict
ovf_unsupported_type_form_dict = ovf_unsupported_type.from_dict(ovf_unsupported_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


