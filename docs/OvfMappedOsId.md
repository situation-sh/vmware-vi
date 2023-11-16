# OvfMappedOsId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ovf_id** | **int** | The operating system id specified in the OVF descriptor.  ***Since:*** vSphere API 4.0  | 
**ovf_description** | **str** | The OS description specified in the OVF descriptor.  ***Since:*** vSphere API 4.0  | 
**target_description** | **str** | The display name of the target OS  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_mapped_os_id import OvfMappedOsId

# TODO update the JSON string below
json = "{}"
# create an instance of OvfMappedOsId from a JSON string
ovf_mapped_os_id_instance = OvfMappedOsId.from_json(json)
# print the JSON string representation of the object
print OvfMappedOsId.to_json()

# convert the object into a dict
ovf_mapped_os_id_dict = ovf_mapped_os_id_instance.to_dict()
# create an instance of OvfMappedOsId from a dict
ovf_mapped_os_id_form_dict = ovf_mapped_os_id.from_dict(ovf_mapped_os_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


